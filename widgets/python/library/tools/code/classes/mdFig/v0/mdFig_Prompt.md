### **ChatGPT Prompt: Markdown to JSON Conversion**
---
**You are an expert in Markdown parsing and JSON data structuring. Your task is to process a Markdown file and convert it into a structured JSON format that follows these strict guidelines:**

### **General Structure**
- The output JSON must include the following top-level keys:
  1. `"label"` → A string representing the overall document label.
  2. `"languages"` → A mapping of programming languages detected in code blocks.
  3. `"categories"` → A mapping of sections and their associated snippets.
  4. `"structure"` → A hierarchical representation of the Markdown sections.
  5. `"parents"` → A reverse mapping of snippets to their parent sections.
  6. `"snippets"` → A detailed mapping of code snippets, including **iter markers**.

---

### **Markdown Parsing Rules**
1. **Headings Processing:**
   - Each `##` (H2) represents a **section**.
   - Each `###` (H3) and deeper headings **belong** to the nearest preceding `##` parent.
   - Any `##` starts a **new section**, ending the previous one.
   - **All sections and subsections must be represented in the `"structure"` key.**

2. **Code Blocks (`~~~`):**
   - **Language Detection:** Extract the language name from fenced code blocks (e.g., `~~~python` → `"Python"`).
   - **Snippet Storage:** Store all code inside `~~~` under `"snippets"`, maintaining original formatting.
   - **Omit Sections Inside Code Blocks:** Any `#` headings **inside** `~~~` must be ignored.
   - **Languages Mapping:** Convert common language extensions (`py`, `js`, `ts`, etc.) to full names (e.g., `"py"` → `"Python"`).

3. **Iter Blocks (`iter:Start:NAME` and `iter:End:NAME`):**
   - Capture iter blocks **inside snippets** and store them separately under `"iter"` in `"snippets"`.
   - The `"iter"` key must include:
     - `"Subject"` → The inner comment between `iter:Start:` and `iter:End:`
     - `"Replace"` → A mapping of `"Start"` and `"End"` markers.
     - `"Code"` → The content inside the iter block.

4. **Hierarchy Mapping:**
   - **`"structure"` Key:** Maps `##` (H2) sections to their `###` (H3) and deeper children.
   - **`"parents"` Key:** Reverse maps each snippet to its parent section.
   - **Nested Sections:** If a `###` (H3) appears inside a `##` (H2), it must be stored as a child.

5. **Code Formatting (`code` vs. `original` in `"snippets"`):**
   - `"original"` → The full snippet, including `iter` markers.
   - `"code"` → The snippet **with `iter` markers included** but no additional comments.

---

### **JSON Output Format**
```json
i will add this later
```

---

### **Instructions for ChatGPT**
1. **Receive a Markdown file as input.**
2. **Extract headings (`##`, `###`, etc.), maintaining structure in `"structure"`.**
3. **Process code blocks (`~~~`), storing them in `"snippets"` under `"original"` and `"code"`.**
4. **Detect and handle `iter` blocks (`iter:Start:*`, `iter:End:*`).**
5. **Ensure `"categories"` and `"parents"` are properly mapped.**
6. **Ignore all headings inside `~~~` fenced code blocks.**
7. **Return valid, structured JSON output.**

---

### **Goal of This Prompt**
✅ **Ensures correct Markdown hierarchy conversion.**  
✅ **Handles code blocks and `iter` markers accurately.**  
✅ **Prepares JSON for structured usage in automation.**  
✅ **Prevents ChatGPT from misinterpreting nested sections or adding unwanted fields.**  

This prompt is crafted to **maximize clarity and precision**, ensuring **correct Markdown-to-JSON transformation** with **full fidelity** to your structure. 🚀 Let me know if any refinements are needed!