### **Objective**  

You are an **expert in python, Markdown parsing, structured JSON conversion, and fullstack app generation**. Your task is to **process a Markdown file as a dynamic configuration file**, enabling the generation of **complex applications, fullstack integrations, SQL reports, and API logic**.  

This approach **does not rely on strict ID-based relationships** but instead **uses the inner text of headers as structure**, with IDs included as a `"SnippetID"` field when they exist.  

___

### **General Structure**

The output JSON must include the following top-level keys:  

1. **`"MdFig"`** → Contains metadata, system instructions, and hierarchical mapping of the document.  
   - `"Label"` → The document title.  
   - `"Languages"` → Maps programming languages to detected snippets.  
   - `"Categories"` → Maps sections to their associated snippets.  
   - `"Structure"` → Represents the hierarchical organization of Markdown sections.  
   - `"Parents"` → Maps snippets to their parent sections.  
   - `"System"` → Contains programmatic metadata, including `MetaConfig` for relationships between snippets.  

2. **`"Snippets"`** → Stores all extracted code snippets while preserving **iter markers** and interdependencies.  

___

### **Markdown Parsing Rules**  

#### **1. Handling MetaConfig YAML (` ```MetaConfig ` )**  

- If a **fenced block** (` ``` `) begins with `MetaConfig`, it contains **YAML system metadata**.  
- Convert the **YAML block into a dictionary** and store it under `MdFig["System"]`.  

##### **Example Markdown Input**  

`````
```MetaConfig  
Definitions:  
  FormHandling: HTML and JavaScript combined form  
  SQLReports: Complex SQL queries with performance optimizations  

Instructions:  
  FormHandling:  
    html:  
      requires: js  
      recommended: StandardValidation  
```
`````

##### **Converted JSON**

```json
"System": {
    "MetaConfig": {
        "Definitions": {
            "FormHandling": "HTML and JavaScript combined form",
            "SQLReports": "Complex SQL queries with performance optimizations"
        },
        "Instructions": {
            "FormHandling": {
                "html": {
                    "requires": "js",
                    "recommended": "StandardValidation"
                }
            }
        }
    }
}
```

___

#### **2. Headings and Snippet Structure**  

- **Each `##` (H2) represents a section.**  
- **Each `###` (H3) represents a snippet group within a section.**  
- **Each `####` (H4) represents an individual snippet within the group.**  
- **If an ID is present in the header (`#### id:: Snippet Title`), it is stored in `"SnippetID"`**, but it does **not** define hierarchy.  

##### **Example Markdown Snippet**

`````
#### 66ab:: HTML Form: JavaScript
```html
<div>
    <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
    <input type="__FIELD_TYPE__" id="__FIELD_ID__" name="__FIELD_NAME__" value="__FIELD_VALUE__">
    <button onclick="_.app.send()">Submit</button>
</div>
```
`````

##### **Converted JSON**
```json
"Snippets": {
    "HTML Form: JavaScript": {
        "SnippetID": "66ab",
        "Category": "HTML Form: JavaScript",
        "Original": "<div>...</div>",
        "Code": "<div>\n    <label for=\"__FIELD_ID__\">__FIELD_LABEL__:</label>\n    <input type=\"__FIELD_TYPE__\" id=\"__FIELD_ID__\" name=\"__FIELD_NAME__\" value=\"__FIELD_VALUE__\">\n    <button onclick=\"_.app.send()\">Submit</button>\n</div>",
        "Language": "HTML"
    }
}
```

___

#### **3. Handling `iter` Blocks (`iter:Start:*` and `iter:End:*`)**  

- Extract **iter sections** inside snippets and store them in a dedicated `"Iter"` key.
- Format **iter placeholders using the appropriate comment style per language**:

| Language | Iter Syntax |
|_________-|____________|
| Python | `# iter:Placeholder` |
| JavaScript | `// iter:Placeholder` |
| SQL | `-- iter:Placeholder` |
| HTML | `<!-- iter:Placeholder -->` |

##### **Example Markdown Snippet (JavaScript Form Submission)**

`````
#### JavaScript Form Post
```js
_.app = {
    send: function(callback) { 
        $.post(
            '__POST_URL__', {
                // iter:Start:Fields
                '__FIELD_NAME__': $('#__FIELD_ID__').val(),
                // iter:End:Fields
            },
            function(data) {
                if (typeof callback === 'function') {
                    callback(data);
                }
            }
        );
    },
};
```

`````

##### **Converted JSON**

```json
"Snippets": {
    "JavaScript Form Post": {
        "Category": "JavaScript Form Post",
        "Original": "_.app = { send: function(callback) {...} };",
        "Code": "_.app = { send: function(callback) { $.post('__POST_URL__', { // iter:Fields }, function(data) { if (typeof callback === 'function') { callback(data); } }); } };",
        "Language": "JavaScript",
        "Iter": [
            {
                "Reference": "// iter:Fields",
                "Subject": "Fields",
                "Replace": {
                    "Start": "// iter:Start:Fields",
                    "End": "// iter:End:Fields"
                },
                "Code": "'__FIELD_NAME__': $('#__FIELD_ID__').val()"
            }
        ]
    }
}
```

___

### **4. Hierarchy Mapping (`Structure` and `Parents`)**

- **`Structure`** → Organizes sections and snippets in a **nested format**, using **header text, not IDs**.  
- **`Parents`** → Maps snippets **back to their parent sections**.  

##### **Example JSON**

```json
"Structure": {
    "Fullstack Structure: Forms": {
        "HTML / JavaScript Form NoForm": [
            "HTML Form: JavaScript",
            "JavaScript Form Post"
        ],
        "HTML Library": [
            "Basic HTML Form"
        ]
    }
},
"Parents": {
    "HTML Form: JavaScript": ["HTML / JavaScript Form NoForm"],
    "JavaScript Form Post": ["HTML / JavaScript Form NoForm"],
    "Basic HTML Form": ["HTML Library"]
}
```

___

### **Final JSON Format Overview**

The final JSON structure should follow this format:

```json
{
    "MdFig": {
        "Label": "Multi Use Case Example",
        "Languages": {...},
        "Categories": {...},
        "Structure": {...},
        "Parents": {...},
        "System": {
            "MetaConfig": {...}
        }
    },
    "Snippets": {...}
}
```

___

### **Instructions for ChatGPT**

1. **Parse the Markdown file recursively, supporting unlimited depth of `#` labels.**
2. **Convert YAML `MetaConfig` sections into JSON and store under `"System"` key.**
3. **Extract `iter` sections properly, ensuring correct comment syntax per language.**
4. **Ensure sections are hierarchical (`##` > `###` > `####` > unlimited).**
5. **Use header text as the snippet key, adding `"SnippetID"` only if present.**
6. **Output JSON in a structured, machine-readable format.**

___

### **Goal of This Prompt**

✅ **Avoids dependency on strict IDs while preserving structure.**  
✅ **Uses header text as structure, making it adaptable for markdown files with or without IDs.**  
✅ **Optimizes AI’s ability to infer relationships and generate correct output.**  

Start with:
class MdFig:
    LANGUAGE_MAP = {
        "js": "JavaScript", "py": "Python", "php": "PHP", "java": "Java", "c": "C",
        "cpp": "C++", "cs": "C#", "ruby": "Ruby", "sql": "SQL", "swift": "Swift",
        "html": "HTML", "xml": "XML", "yml": "YAML", "yaml": "YAML", "css": "CSS",
        "scss": "SCSS", "sass": "SASS", "rs": "Rust", "ada": "Ada", "spark": "SPARK",
        "go": "Go", "ts": "TypeScript", "sh": "Shell", "bash": "Bash", "zsh": "Zsh",
        "bat": "Batch", "cmd": "Batch", "ps1": "PowerShell", "psm1": "PowerShell",
        "dart": "Dart", "kotlin": "Kotlin", "perl": "Perl", "lua": "Lua", "r": "R",
        "json": "JSON", "toml": "TOML", "ini": "INI", "makefile": "Makefile",
        "dockerfile": "Dockerfile", "gitignore": "GitIgnore", "cmake": "CMake",
        "asm": "Assembly", "nasm": "NASM", "arm": "ARM Assembly", "verilog": "Verilog",
        "vhdl": "VHDL"
    }

    ITER_COMMENTS = {
        "py": ["#"], "php": ["//", "/* {} */"], "js": ["//", "/* {} */"], "java": ["//", "/* {} */"],
        "c": ["//", "/* {} */"], "cpp": ["//", "/* {} */"], "cs": ["//", "/* {} */"], "ruby": ["#"],
        "sql": ["--", "/* {} */"], "yml": ["#"], "yaml": ["#"], "css": ["/* {} */"], "scss": ["//", "/* {} */"],
        "sass": ["//"], "rs": ["//"], "ada": ["--"], "spark": ["--"], "go": ["//"], "ts": ["//", "/* {} */"],
        "sh": ["#"], "bash": ["#"], "zsh": ["#"], "bat": ["REM", "::"], "cmd": ["REM", "::"],
        "ps1": ["#"], "psm1": ["#"], "dart": ["//"], "kotlin": ["//"], "perl": ["#"], "lua": ["--"],
        "r": ["#"], "json": ["//"], "toml": ["#"], "ini": ["#"], "makefile": ["#"], "dockerfile": ["#"],
        "gitignore": ["#"], "cmake": ["#"], "asm": [";"], "nasm": [";"], "arm": [";"], "verilog": ["//"],
        "vhdl": ["--"]
    }


Sample markdown input file:
# Multi Use Case Example

```MetaConfig
Definitions:
  FormHandling: HTML and JavaScript combined form
  SQLReports: Complex SQL queries with performance optimizations

Instructions:
  FormHandling:
    html:
      requires: js
      recommended: StandardValidation
```

---

## Fullstack Structure: Forms

### HTML / JavaScript Form NoForm

#### 66ab:: HTML Form: JavaScript

```html
<div>
    <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
    <input type="__FIELD_TYPE__" id="__FIELD_ID__" name="__FIELD_NAME__" value="__FIELD_VALUE__">
    <button onclick="_.app.send()">Submit</button>
</div>
```

#### JavaScript Form Post

```js
_.app = {
    send: function(callback) { 
        $.post(
            '__POST_URL__', {
                // iter:Start:Fields
                '__FIELD_NAME__': $('#__FIELD_ID__').val(),
                // iter:End:Fields
            },
            function(data) {
                if (typeof callback === 'function') {
                    callback(data);
                }
            }
        );
    },
};
```

---

### HTML Library

#### Basic HTML Form

```html
<div>
    <form action="#" method="post">
        <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
        <input type="__FIELD_TYPE__" id="__FIELD_ID__" name="__FIELD_NAME__" value="__FIELD_VALUE__">
        <button type="submit">Submit</button>
    </form>
</div>
```

---

## Complex SQL Queries for Reporting

### SQL Reports

#### SQL Query - Multi-Join User & Orders Report

```sql
SELECT 
    users.id AS user_id, 
    users.name AS user_name, 
    orders.id AS order_id, 
    orders.total AS order_total, 
    payments.payment_status 
FROM users
INNER JOIN orders ON users.id = orders.user_id
LEFT JOIN payments ON orders.id = payments.order_id
WHERE users.status = 'active';

/* iter:Start:DateFilter */
AND orders.created_at >= '2024-01-01'
/* iter:End:DateFilter */
```

#### SQL Query - Indexed Performance Optimization

```sql
CREATE INDEX idx_users_id ON users(id);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_payments_order ON payments(order_id);
```


Expected Output:
