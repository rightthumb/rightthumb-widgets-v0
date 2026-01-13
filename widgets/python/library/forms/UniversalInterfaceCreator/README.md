# UniversalInterfaceCreator (UIC)

> **Web • GUI • Terminal — Built for my resume**
>
> Generate the *same* data-collection workflow across **Web (HTML)**, **Desktop GUI (Tkinter)**, and **Terminal/TTY** from a single JSON-like form spec. UIC auto-selects the best interface at runtime, validates inputs, and can submit results to an HTTP endpoint, SQLite (SmartTables), or local files.

---

## What it is

UniversalInterfaceCreator converts a structured **form definition** (a Python dict/JSON) into a working UI:

* **Web**: launches a local HTTP server and renders a form (auto-opens browser).
* **GUI**: builds a native **Tkinter** dialog with labels, entries, dropdowns, radio and checkbox groups.
* **Terminal**: falls back to an interactive, prompt-driven CLI if no GUI is available or `terminal` is forced.
* **Prompt‑Toolkit (planned)**: advanced full-screen TUI scaffolding exists; final polish TBD.

The library also ships a thin data layer (**SmartTablesSQLite**) and a **DataManager** to persist form results in SQLite without pre-defining schemas (columns added on demand).

> Aliases for quick use: `SmartTables`, `SmartTable`, `UI`, `UIC`, `uic`, `ui` → all map to `genForm()`.

---

## Key features

* **Single spec → 3 UIs** (Web / Tkinter / Terminal) with auto-detection & overrides.
* **Field types**: `text`, `password`, `text_area`, `radio`, `dropdown`, `checkbox`.
* **Validation**: `required`, `length.min/max`, `regex`, **remote** validation via `validation.url` POST.
* **Styling (Tkinter)**: font & color at global or field level; per-field widths & column spans.
* **Security niceties**: optional `md5` hashing for fields; passwords redacted in output (`ab...`).
* **Submission routes** (pick any per form):

  * `Config.post` → HTTP POST (sends `{ package: <json> }`).
  * `Config.sqlite` → SQLite via SmartTables (auto‑creates table/columns).
  * `Config.save` → Save to local JSON (path).
  * `Config.table` → Save to a named table via RightThumb `saveTable`.
  * `Config.print` → Print to stdout (debug/dev).
* **Record hydration**: `getRecord` + `Table` + `record` can fetch a record first, then render.
* **Config inheritance** when passing a **list** of form specs: later specs inherit prior `Config`.

---

## Runtime selection (how UI is chosen)

1. If `Config.advanced` and `prompt_toolkit` is present → **advanced TUI** (WIP UI).
2. Else, if Tkinter available:

   * If `Config.html` → start **Web** server.
   * Else if `Config.terminal` → force **Terminal**.
   * Else → **Tkinter GUI**.
3. If Tkinter not available → **Terminal**.

---

## Config schema (common options)

```jsonc
{
  "Config": {
    // Routing
    "post": "https://example.com/api/submit",   // HTTP endpoint (optional)
    "sqlite": "inventory",                      // SQLite DB/table name (optional)
    "save": "./out.json",                       // Save record to a JSON file (optional)
    "table": "MyRightThumbTable",               // Save via RightThumb saveTable (optional)
    "print": true,                                // Print package to stdout (debug)

    // UI selection
    "html": false,                                // true = web server UI
    "terminal": false,                            // force terminal prompts
    "advanced": false,                            // try prompt_toolkit flow (experimental)

    // UI/Style defaults (Tkinter)
    "title": "Dynamic Form",                     // window/page title
    "description": "Demo form",                  // top heading / page description
    "font": { "type": "Arial", "size": 12 },  // default font
    "color": { "text": "#111", "bg": "#fff" },
    "field": { "width": 24 },                    // default entry width

    // SmartTables/Record bootstrapping
    "getRecord": "https://api.example.com/get", // optional bootstrap
    "sqlite_mode": "smart"                       // reserved / future options
  }
}
```

### Field object

```jsonc
{
  "label": "Your Name",          // required, unique key for the field
  "type": "text",                // one of: text, password, text_area, radio, dropdown, checkbox
  "value": "",                   // default value (string or list for checkbox)
  "options": ["A", "B"],          // for radio/dropdown/checkbox
  "md5": false,                   // if true, hashes this field's value (server-side)
  "disabled": false,              // disables input (GUI/Web)
  "col_span": 2,                  // GUI layout hint
  "config": {                     // per-field UI overrides
    "width": 32,
    "font": {"type": "Arial", "size": 12},
    "color": {"text": "#222", "bg": "#fff"}
  },
  "validation": {
    "required": true,             // if true, must be present/non-empty
    "length": { "min": 2, "max": 64 },
    "regex": "^[A-Za-z .-]+$",   // python re
    "url": "https://example.com/validate" // POSTs {value:<>, ...}; truthy means ok
  }
}
```

---

## Minimal form (Terminal/Tkinter/Web — auto)

```python
form = {
  "Config": {"title": "Hello", "description": "Minimal demo"},
  "User": [
    {"label": "Name", "type": "text", "validation": {"required": true}},
    {"label": "Email", "type": "text"}
  ]
}
result = UIC(form)  # or SmartTables(form)
print(result)
```

**What happens**

* Picks UI based on environment.
* Validates `Name`.
* Returns a dict of `{label: value}` with passwords redacted in memory printouts.

---

## Web-first form (auto-launches localhost server)

```python
form = {
  "Config": {
    "title": "Web Intake",
    "description": "Submit from your browser",
    "html": true
  },
  "Profile": [
    {"label": "Full Name", "type": "text", "validation": {"required": true}},
    {"label": "Bio", "type": "text_area", "value": "Tell us a bit…"},
    {"label": "Role", "type": "dropdown", "options": ["Engineer","PM","Designer"]},
    {"label": "Track", "type": "radio", "options": ["Frontend","Backend","Data"]},
    {"label": "Skills", "type": "checkbox", "options": ["Python","JS","SQL"], "value": ["JS"]}
  ]
}
UIC(form)
```

* Starts a local server on `localhost:8xxx` and opens your browser.
* On submit, the page shows the JSON result. The process exits automatically.

---

## GUI example with styling & validation

```python
form = {
  "Config": {
    "title": "Signup",
    "description": "Create your account",
    "field": {"width": 28},
    "font": {"type": "Segoe UI", "size": 11},
    "color": {"text": "#111", "bg": "#fafafa"}
  },
  "Account": [
    {"label": "Username", "type": "text", "validation": {"required": true, "length": {"min": 3}}},
    {"label": "Password", "type": "password", "validation": {"required": true, "length": {"min": 8}}},
    {"label": "Newsletter", "type": "checkbox", "options": ["Product","Engineering","Jobs"], "value": ["Product"]}
  ]
}
UIC(form)
```

---

## Terminal-only example (force TTY)

```python
form = {
  "Config": {"terminal": true, "title": "CLI Wizard"},
  "Steps": [
    {"label": "Project Name", "type": "text", "validation": {"required": true}},
    {"label": "Environment", "type": "dropdown", "options": ["dev","staging","prod"], "value": "dev"}
  ]
}
UIC(form)
```

---

## Submitting to SQLite (SmartTables)

```python
form = {
  "Config": {"sqlite": "inventory", "title": "Add Asset"},
  "Asset": [
    {"label": "sku", "type": "text", "validation": {"required": true}},
    {"label": "brand", "type": "text"},
    {"label": "price", "type": "text"}
  ]
}
out = UIC(form)
print(out)
# → {"sku": "A-100", "brand": "Acme", "price": "79.99"}
# UIC auto-creates SQLite DB `{tt}/db/inventory.db`, ensures columns, inserts a row, and returns last_insert_id in the response if using `submit()` routing.
```

> **How it works**: `DataManager` parses your spec, ensures the table exists via `SmartTablesSQLite`, adds missing columns based on your record’s types, then inserts.

---

## Posting to a remote API

```python
form = {
  "Config": {
    "post": "https://example.com/api/ingest",
    "title": "Remote Submit"
  },
  "Payload": [
    {"label": "email", "type": "text", "validation": {"required": true, "regex": "^.+@.+$"}},
    {"label": "note", "type": "text_area"}
  ]
}
UIC(form)
```

The payload is sent as:

```json
{ "package": { "action": "add", "structure": {…}, "record": {…} } }
```

For **remote validation**, set `validation.url` on a field; UIC POSTs `{value: "…"}` and treats a truthy/JSON response as valid.

---

## Passwords & hashing

* Fields with `type: "password"` are **redacted** to the first 2 chars when echoed (`ab...  <--(Redacted)`).
* Any field can add `"md5": true` to store the MD5 hash of the value instead of the raw input.

---

## Disabling fields / setting defaults

```python
{
  "Config": {"title": "Review"},
  "Meta": [
    {"label": "ID", "type": "text", "value": "123", "disabled": true},
    {"label": "Owner", "type": "text", "value": "scott"}
  ]
}
```

---

## Checkboxes — single vs. multiple

```python
{
  "Config": {"title": "Tags"},
  "Tags": [
    {"label": "Labels", "type": "checkbox", "options": ["alpha","beta","prod"], "value": ["alpha","beta"]}
  ]
}
```

Returned value is a **list of selected options**.

---

## Using a list of forms (inherit Config)

```python
forms = [
  {"Config": {"title": "Wizard", "sqlite": "wizard"}},
  {"Step 1": [{"label": "Name", "type": "text"}]},
  {"Step 2": [{"label": "Goal", "type": "text_area"}]}
]
UIC(forms)
```

Later specs inherit the first `Config`, so you don’t repeat routing & style.

---

## Hydrating a record before render

```python
form = {
  "Config": {"title": "Edit Record"},
  "Table": "customers",
  "record": 42,
  "getRecord": "https://api.example.com/customers/get",
  "Fields": {
    "Main": [
      {"label": "Name", "type": "text"},
      {"label": "Email", "type": "text"}
    ]
  }
}
UIC(form)
```

UIC calls `getRecord` to retrieve and prefill fields before rendering.

---

## Programmatic API

```python
from yourmodule import genForm as UIC

# Build & run
result = UIC(form_spec)
# → returns dict of {label: value} or server response from chosen submission route
```

**Core objects inside**

* `UniversalInterfaceCreator(form_spec)` — orchestrates UI route, render, validate, submit.
* `SmartTablesSQLite(db_name)` — SQLite driver with auto‑schema (`table_create`, `record_add`, etc.).
* `DataManager(json_or_dict)` — parses `{ package: { action, structure, record } }` and performs persistence.

---

## Notes & limits

* **Prompt‑Toolkit** advanced TUI is scaffolded; production focus is Terminal/Tkinter/Web.
* Web UI uses a simple local `http.server` with plain HTML; CSS can be injected via your own stylesheet.
* For security, prefer server-side validation/endpoints for sensitive flows.

---

## One‑pager snippet (for resume bullets)

* Single form spec → **Web/Tk/CLI** UIs
* **Validation**: required, length, regex, remote URL
* **Destinations**: HTTP, SQLite (auto schema), local JSON, RightThumb table
* **Fields**: text, password (redacted), textarea, radio, dropdown, checkbox
* **Styling**: fonts, colors, widths, per-field overrides
* **Aliases**: `SmartTables`, `SmartTable`, `UI`, `UIC`, `uic`, `ui`

---

## Quick copy: End‑to‑end demo

```python
form = {
  "Config": {
    "title": "Asset Intake",
    "description": "Quick demo",
    "sqlite": "assets",   // persist automatically
    "html": false          // flip to true to collect via browser
  },
  "Asset": [
    {"label": "SKU", "type": "text", "validation": {"required": true}},
    {"label": "Brand", "type": "text"},
    {"label": "Price", "type": "text"},
    {"label": "Features", "type": "checkbox", "options": ["WiFi","BT","USB-C"]}
  ]
}
print(UIC(form))
```

---

*Built on RightThumb primitives; productionized for repeatable, environment‑agnostic data capture.*
