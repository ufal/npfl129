# NPFL129 (Machine Learning for Greenhorns) Slides

The NPFL129 (Machine Learning for Greenhorns) slides can be viewed in any modern browser (with Chrome and Firefox tested). The slides can be printed into PDF in Chrome and Firefox (but in Firefox you need to manually specify page size as 297mm and 167mm).

Several key shortcuts are available:
- `h` toggles handout mode, where only complete slides are kept;
- `b` toggles background visiblity.

You can see the slides either [on-line at ÚFAL](https://ufal.mff.cuni.cz/courses/npfl129), or locally – in that case:
1. Make sure the `slimd` submodule is updated by running:
   ```
   git submodule update --init
   ```
1. Start a simple local webserver which is required for the AJAX requests and SVGZ images to work:
   ```
   python3 server.py [port]
   ```
1. Navigate to `http://localhost:8000`
