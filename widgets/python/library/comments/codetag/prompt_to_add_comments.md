# Prompt: “Annotate with Registration Headers + Smart Comments”

**Role:** You are a senior code annotator. Add concise, high-signal comments and machine-parsable registration headers without changing program behavior.

## Inputs (fill before running)

* **Language(s):** `<LANGS>`
* **Project purpose:** `<PURPOSE>`
* **Audience:** `<AUDIENCE>` (e.g., teammates, future me)
* **Density:** terse | standard | thorough → `<DENSITY>`
* **Process context:** `<PROCESS>` (e.g., `file.(python).contents.block.index-version` or `~python`)
* **Sections to freeze (optional):** `<FREEZE_HINTS>` (e.g., regex, markers)
* **Code:** paste file(s) or region(s)

## What to produce

1. **Registration headers** (use no-quotes JSON-ish attributes):

   * **Top of file (single line):**

     ```
     <app Name v=<v> id=<id> lang=<LANG> process=<PROCESS> scope=down />
     ```

     (alias for `<reg/>`)
   * **Top of function (single line):**

     ```
     <fn FuncName v=<v> id=<id> tags=[function] process=<PROCESS> scope=down />
     ```

     (alias for `<unit/>`)
   * **Top of section (single line):**

     ```
     <sec Label v=<v> id=<id> process=<PROCESS> scope=down />
     ```

     (alias for `<block/>`)
   * Use classic open/close forms when you need explicit spans:

     ```
     <block Label v=<v> id=<id> meta={ desc:"...", owner:"" }>
     ...
     </block Label>
     ```
   * Use `<under lines=N ...>` for short, gated spans:

     ```
     <under lines=3 process=<PROCESS> tags=[if,documentation]>
     ```
   * If you update a region, **bump `v`** and set `ts=<ISO-8601>`. Preserve unknown keys.

2. **Inline comments & docstrings** (language-idiomatic):

   * Explain **intent, invariants, contracts, edge cases**; don’t narrate the obvious.
   * Python → docstrings; JS/TS → JSDoc; SQL/Bash → idiomatic comments.
   * Keep to \~100 cols unless the language dictates otherwise.

3. **Freeze/untouched regions** (when requested):

   * Wrap exact-literal snippets with:

     ```
     <sec Frozen v=<v> id=<id> meta={ desc:"do not modify" } freeze:true scope=down />
     ...exact content...
     ```
   * Never alter content inside `freeze:true`.

4. **Process routing** (very important):

   * Accept any of: literal (`python`), dotted (`file.(python).contents.block`), list (`[python, index]`), regex (`~python`).
   * Include `process` in headers so downstream tools can filter.

5. **Validation & self-check (before returning)**

   * Exactly one `<app/>` per file; `<fn/>` above public/complex functions; `<sec/>` around meaningful logic.
   * Ensure open/close tag names match; spans are correct; `lines` in `<under>` covers intended lines.
   * No behavior changes, no secrets.

## Output format

* Return the **fully annotated code only** (no extra prose). Preserve original code except for added comments/headers.

---

## Micro version (one-liner)

> Add concise, high-signal comments and our registration headers (`<app|fn|sec/>`, `<under>`) to the code. Use no-quotes JSON-ish attrs, include `process=<PROCESS>`, bump `v/ts` when updating, add docstrings for public API, wrap at 100 cols, keep logic unchanged, freeze exact snippets using `<sec ... freeze:true />`. Return annotated code only.

---

## Paste-in “prompt block” (drop at file top to self-document)

```python
#<app CommentPolicy v=1 id=prompt-annotator lang=python process=file.(python).contents.block scope=down />
# Instructions to tools:
# - Add <fn/> above functions and <sec/> above non-trivial regions; use <under lines=N> for short gates.
# - Use no-quotes JSON-ish attributes; include process routing; bump v/ts if region changed.
# - Keep code behavior identical; for literal sections, wrap with <sec ... freeze:true />.
# - Comment intent/invariants; avoid restating code. 100-col wrap; no secrets.
```
