# Workflow diagram

[job-search-workflow.svg](job-search-workflow.svg) is the editable source. It uses native SVG text, shapes and icons, with no embedded raster images or external assets. [job-search-workflow.png](job-search-workflow.png) is the 2400×3680 export used in the main README.

Edit the SVG, then render from the repository root with Node.js, Playwright and its Chromium browser available:

```sh
node scripts/render-workflow.mjs
```

To use an installed Chrome browser, set `WORKFLOW_BROWSER_CHANNEL=chrome`. An optional first argument selects a different output path.

The renderer checks label widths, shape containment and overlapping nodes before exporting at 2× resolution. Visually review the result, then update the approved PNG digest in [check_package.py](../../scripts/check_package.py). Run the package checks before publishing.

This is a maintainer utility; users do not need it to install or use the skills.
