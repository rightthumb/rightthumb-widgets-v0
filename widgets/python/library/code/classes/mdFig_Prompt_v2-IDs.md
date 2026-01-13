https://chatgpt.com/c/67d0e593-6dfc-800a-a0e3-757d48f7c07d

### **Updated ChatGPT Prompt: Advanced Markdown to JSON Conversion for Fullstack App Generation**  

---

### **Objective**  
You are an **expert in Markdown parsing, structured JSON conversion, and fullstack app generation**. Your task is to **process a Markdown file as a dynamic configuration file** that enables the generation of **complex applications, fullstack integrations, SQL reports, and API logic**.  

The Markdown structure follows specific conventions that define **hierarchical relationships**, **snippet dependencies**, and **dynamic configuration elements**. Your conversion must adhere strictly to these rules.  

---

### **General Structure**  
The output JSON must include the following top-level keys:  

1. **`"MdFig"`** → Contains metadata, system instructions, and the hierarchical mapping of the document.  
   - `"Label"` → The document title.  
   - `"Languages"` → Maps programming languages to detected snippets.  
   - `"Categories"` → Maps sections to their associated snippets.  
   - `"Structure"` → Represents the hierarchical organization of Markdown sections.  
   - `"Parents"` → Maps snippets to their parent sections.  
   - `"System"` → Contains programmatic metadata, including `MetaConfig` for relationships between snippets.  

2. **`"Snippets"`** → Stores all extracted code snippets while preserving **iter markers** and interdependencies.  

---

### **Markdown Parsing Rules**  

#### **1. Handling MetaConfig YAML (` ```MetaConfig ` )**  
- If a **fenced block** (` ``` `) begins with `MetaConfig`, it contains **YAML system metadata**.  
- Convert the **YAML block into a dictionary** and store it under `MdFig["System"]`.  
- Example:  

##### **Markdown Input**  
````
```MetaConfig  
Definitions:  
  94be: Combination Recommendation  
  38a6: Category | Combination NoForm | lan-html, js  
Instructions:  
  94be:  
    html:  
      requires:  
        id: 38a6  
        requires: js  
```  
````  

##### **Converted JSON**
```json
"System": {
    "MetaConfig": {
        "Definitions": {
            "94be": "Combination Recommendation",
            "38a6": "Category | Combination NoForm | lan-html, js"
        },
        "Instructions": {
            "94be": {
                "html": {
                    "requires": {
                        "id": "38a6",
                        "requires": "js"
                    }
                }
            }
        }
    }
}
```

---

#### **2. Headings and Snippet Structure**  
- **Each `##` (H2) represents a section.**  
- **Each `###` (H3) represents a snippet group within a section.**  
- **Each `####` (H4) represents an individual snippet within the group.**  
- **Each snippet must have an ID format** (`#### id1,id2:: ParentID1, ParentID2:: Snippet Name`).  
- The **first ID (`id1`) is the unique identifier** for this snippet.  

##### **Example Markdown Snippet**
```
#### 66ab,94be,38a6,4ddf:: HTML Form: JavaScript
```html
<div>
    <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
    <input type="__FIELD_TYPE__" id="__FIELD_ID__" name="__FIELD_NAME__" value="__FIELD_VALUE__">
    <button onclick="_.app.send()">Submit</button>
</div>
```
```

##### **Converted JSON**
```json
"Snippets": {
    "66ab": {
        "Category": "HTML Form: JavaScript",
        "Original": "<div>...</div>",
        "Code": "<div>\n    <label for=\"__FIELD_ID__\">__FIELD_LABEL__:</label>\n    <input type=\"__FIELD_TYPE__\" id=\"__FIELD_ID__\" name=\"__FIELD_NAME__\" value=\"__FIELD_VALUE__\">\n    <button onclick=\"_.app.send()\">Submit</button>\n</div>",
        "Language": "HTML",
        "Parents": ["94be", "38a6", "4ddf"]
    }
}
```

---

#### **3. Handling `iter` Blocks (`iter:Start:*` and `iter:End:*`)**  
- Extract **iter sections** inside snippets and store them in a dedicated `"Iter"` key.
- Format **iter placeholders using the appropriate comment style per language**:

| Language | Iter Syntax |
|----------|------------|
| Python | `# iter:Placeholder` |
| JavaScript | `// iter:Placeholder` |
| SQL | `-- iter:Placeholder` |
| HTML | `<!-- iter:Placeholder -->` |

##### **Example Markdown Snippet (JavaScript Form Submission)**
```
#### a367:: JavaScript Form Post
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
```

##### **Converted JSON**
```json
"Snippets": {
    "a367": {
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

---

### **4. Hierarchy Mapping (`Structure` and `Parents`)**
- **`Structure`** → Organizes sections and snippets in a **nested format**.
- **`Parents`** → Maps snippets **back to their parent sections**.

##### **Example JSON**
```json
"Structure": {
    "Fullstack Structure: Forms": {
        "HTML / JavaScript Form NoForm": [
            "66ab",
            "a367"
        ],
        "HTML Library": [
            "bab6"
        ]
    }
},
"Parents": {
    "66ab": ["HTML / JavaScript Form NoForm"],
    "a367": ["HTML / JavaScript Form NoForm"],
    "bab6": ["HTML Library"]
}
```

---

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

---

### **Instructions for ChatGPT**
1. **Parse the Markdown file recursively, supporting unlimited depth of `#` labels.**
2. **Convert YAML `MetaConfig` sections into JSON and store under `"System"` key.**
3. **Extract `iter` sections properly, ensuring correct comment syntax per language.**
4. **Ensure sections are hierarchical (`##` > `###` > `####` > unlimited).**
5. **Identify and store relationships using `::` ID parsing.**
6. **Output JSON in a structured, machine-readable format.**

---

### **Goal of This Prompt**
✅ **Enables AI-powered systems to generate entire complex apps dynamically**  
✅ **Maintains structured dependencies across languages and snippets**  
✅ **Ensures AI understands how each code fragment is part of a larger system**  
✅ **Optimizes AI’s ability to infer relationships and generate proper output**  


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