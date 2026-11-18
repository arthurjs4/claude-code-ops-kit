# Rules for `data/`

- CSV/JSON files here are the source of truth for the workflow (items, status, dates).
- Edit them only through the provided scripts or by exact, minimal edits; never rewrite a whole file.
- Dates are ISO (YYYY-MM-DD). Status values: `new`, `drafted`, `sent`, `replied`, `closed`.
- Never store real personal data in the example files; use placeholders like `Example Co`.
