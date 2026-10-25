// Maintainer utility: export the editable SVG with a browser's SVG renderer.
// Requires Playwright and its Chromium browser; not part of skill installation.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(root, 'docs/assets/job-search-workflow.svg');
const output = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.join(root, 'docs/assets/job-search-workflow.png');
const svg = await fs.readFile(source, 'utf8');
const browser = await chromium.launch({
  headless: true,
  ...(process.env.WORKFLOW_BROWSER_CHANNEL
    ? { channel: process.env.WORKFLOW_BROWSER_CHANNEL }
    : {}),
});

try {
  const page = await browser.newPage({
    viewport: { width: 1200, height: 1840 },
    deviceScaleFactor: 2,
  });
  await page.route('**/*', route => route.abort());
  await page.setContent(`<style>html,body{margin:0}svg{display:block}</style>${svg}`);
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => {
    const diagram = document.querySelector('svg');
    const { width, height } = diagram.viewBox.baseVal;
    const issues = [];
    const labels = [...diagram.querySelectorAll('text')];
    for (const label of labels) {
      const r = label.getBBox();
      if (r.width > Number(label.dataset.maxWidth) + 0.5 ||
          r.x < 30 || r.x + r.width > width - 30 ||
          r.y < 0 || r.y + r.height > height) {
        issues.push(`Text outside its allotted bounds: ${label.textContent}`);
      }
      if (label.dataset.box) {
        const box = document.getElementById(label.dataset.box).getBBox();
        if (r.x < box.x + 8 || r.x + r.width > box.x + box.width - 8 ||
            r.y < box.y || r.y + r.height > box.y + box.height) {
          issues.push(`Text outside its shape: ${label.textContent}`);
        }
      }
    }
    const nodes = [...diagram.querySelectorAll('[data-kind]')]
      .filter(node => node.dataset.kind !== 'panel');
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i].getBBox(), b = nodes[j].getBBox();
        if (a.x < b.x + b.width && a.x + a.width > b.x &&
            a.y < b.y + b.height && a.y + a.height > b.y) {
          issues.push(`Overlapping shapes: ${nodes[i].id}, ${nodes[j].id}`);
        }
      }
    }
    return { width, height, labels: labels.length, issues };
  });
  if (report.issues.length) throw new Error(report.issues.join('\n'));
  await page.locator('svg').screenshot({ path: output });
  console.log(`Rendered ${report.width * 2}×${report.height * 2} PNG; ` +
    `${report.labels} labels checked for width and containment; no overlapping shapes.`);
} finally {
  await browser.close();
}
