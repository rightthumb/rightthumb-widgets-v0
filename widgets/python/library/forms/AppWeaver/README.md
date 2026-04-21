# AppWeaver Forms TUI (prompt_toolkit)

This app renders an interactive **terminal form** from a JSON schema (the same structure you use in your web auto‑form apps). It supports **Tab / Shift+Tab** field navigation, collapsible sections, and exports values as JSON.

---

## Features

* **Tab / Shift+Tab** to move between inputs (with initial focus set automatically).
* **Collapsible sections** for `fieldset`, `group`, and `section` blocks; only the first opens by default.
* **F6 / F7** to switch to next/previous section; **Enter** toggles a section header.
* **Ctrl+S** prints JSON to screen and `stdout`.
* **Esc / Ctrl+Q / Ctrl+C / q** to exit.
* **Datalists → autocomplete** via `WordCompleter`.
* **Select/Radio** rendered as `RadioList`.
* **Hidden fields** included in output but not shown.
* Minimal dependencies: just `prompt_toolkit`.

---

## Install & Run

```bash
pip install prompt_toolkit

# Run with built-in demo schema
python form.py

# Or run with your schema
python form.py path/to/schema.json
```

**Windows note:** If Shift+Fn keys aren’t recognized, use **F6/F7** for section navigation.

---

## JSON Schema (overview)

Top-level keys:

* `title` *(str)* — shown at the top.
* `fields` *(array)* — ordered list of elements below.
* `datalists` *(array)* — optional autocompletion sources.

### Field objects

Common keys (per field):

* `type` — see **Supported field types** below.
* `db` *(str)* — key used in the output JSON.
* `label` *(str)* — caption shown on the left.
* `value` — initial value.
* `attributes` *(dict)* — extra hints (e.g., `{"min":0,"max":100}` for `range`).
* `list` *(str)* — datalist `id` for autocompletion.
* `options` *(array)* — for `radio`/`select` options.
* `multiple` *(bool)* — for `file` inputs to accept CSV of paths.
* `is` *(str)* — special handling; currently `"tags"` converts CSV → array in output.

### Container elements

* `fieldsetStart` / `fieldsetEnd`
* `groupStart` / `groupEnd`
* `sectionStart` / `sectionEnd`

Containers may include:

* `label` — header text.
* `showToggle` *(bool)* — if true, rendered as collapsible (default used here).

### Datalists

```json
{
  "datalists": [
    { "id": "langList", "options": ["javascript", "python", "php"] }
  ]
}
```

Refer to them from a field via `"list": "langList"`.

---

## Supported field types & mappings

| Schema `type`                                                            | Terminal widget / behaviour                         |
| ------------------------------------------------------------------------ | --------------------------------------------------- |
| `hidden`                                                                 | Not displayed; value included in JSON               |
| `labelOnly`                                                              | Static label row                                    |
| `text`, `email`, `url`, `tel`, `date`, `time`, `datetime-local`, `color` | Single‑line `TextArea`                              |
| `password`                                                               | Single‑line `TextArea` (masked)                     |
| `textarea`                                                               | Multi‑line `TextArea`                               |
| `number`                                                                 | Single‑line `TextArea` (no coercion yet)            |
| `range`                                                                  | Single‑line `TextArea` with `(min/max)` hint        |
| `radio`                                                                  | `RadioList` of options                              |
| `select`                                                                 | `RadioList` (terminal-friendly select)              |
| `checkbox`/`switch`                                                      | `Checkbox`                                          |
| `file`                                                                   | Path input; if `multiple: true`, CSV parsed → array |

> **Tags**: If a field has `"is": "tags"`, the UI stays CSV, but on save the value becomes an array of strings.

---

## Keyboard shortcuts

* **Tab / Shift+Tab** — next/previous focus
* **Enter** (on a section header) — toggle open/closed
* **F6 / F7** — next/previous section
* **F2** — toggle all sections
* **Ctrl+S** — save (emit JSON)
* **Esc / Ctrl+Q / Ctrl+C / q** — exit

---

## Output

* Press **Ctrl+S** to serialize the current values.
* Output appears in the bottom pane **and** is printed to `stdout` (so you can pipe it):

```bash
python form.py schema.json > result.json
```

**Conversions performed on save**

* `hidden` → raw stored value.
* `tags` (`is: "tags"`) → CSV → `list[str]`.
* `file` with `multiple: true` → CSV → `list[str]`.

All other fields are returned as strings.

---

## Example schema snippet

```json
{
  "title": "Full Field Type Coverage",
  "fields": [
    { "db": "_id", "type": "hidden", "value": "_id" },
    { "type": "labelOnly", "label": "🔐 Identification" },

    { "type": "fieldsetStart", "label": "Default", "showToggle": true },
    { "db": "one", "label": "One", "type": "text" },
    { "db": "two", "label": "Two", "type": "text" },
    { "type": "fieldsetEnd" }
  ],
  "datalists": [
    { "id": "langList", "options": ["javascript", "python"] }
  ]
}
```

---

## Troubleshooting

**Nothing navigates when I press Tab.**
Make sure a field has focus. Click one, or press **F6** to open a section. We also bind `Shift+Tab` as `s-tab` (some terminals don’t support `backtab`).

**I get “Window too small”.**
The app opens only the first section by default to keep height low. If your terminal is still small, enlarge it or collapse more sections (Enter on the headers).

**Shift+Fn keys don’t work.**
Use **F6/F7** for section navigation.

**Version differences**

* Older `prompt_toolkit` builds don’t accept `RadioList(current_value=...)` — this app sets it after construction.
* Private widget attributes (like `Button._label`) are **not** used here; this avoids `AttributeError` across versions.
* Some builds don’t know `backtab`; we map only `s-tab`.

---

## Customization ideas

* **Validation & coercion**: add per‑field validators (email/url/date/number) and block save until valid.
* **CLI flags**: `--out result.json`, `--open all`, `--theme dark`.
* **Type adapters**: convert `number` to int/float, parse ISO dates/times.
* **Searchable select**: replace `RadioList` with a filterable list for large `options`.
* **Theming**: edit the `Style.from_dict` block to change colors.

---

## Limitations

* No real file uploads (paths only).
* `range`, `date`, `time`, `color` are text inputs; no native picker widgets in TUI.
* Deeply nested containers render, but excessive nesting may reduce readability.
* No scrolling container (kept small via collapsible sections).

---

## Internal design notes

* Layout is an `HSplit` of: title → sections → output pane → footer.
* Collapsibles are `Button` headers + `ConditionalContainer` bodies.
* Focus management: we set an initial `focused_element` to the first visible input.
* Navigation keys call `layout.focus_next()` / `focus_previous()`.
