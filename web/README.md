# Data Analytics and Databases — browser edition

Buildless local browser workbench and project documentation.

Run from repository root: `python -m http.server 8000`, then open `http://localhost:8000/web/`.

Sites deployment is pending. Original Python notebooks + SQLite source remains separate.

The browser workbench filters eight invented rows and reports their arithmetic mean. It is a transparent SQL-style illustration, not a query against the repository database or evidence of forecast accuracy.

The source passes JavaScript syntax checks and deterministic calculation checks recorded in the task verification report; full browser/layout and original-application validation require a browser and the original runtime.

See [reproducible verification](VERIFICATION.md) and run `node web/verify.cjs`.
