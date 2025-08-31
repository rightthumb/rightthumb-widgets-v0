
import ast
def pyClassesFunctions(code: str) -> dict:
    """
    Extracts class names with their function names and top-level functions from the given Python code.

    Args:
        code (str): Python code as a string.

    Returns:
        dict: A dictionary with two keys:
              - "classes": A dictionary of class names and their methods.
              - "top_level_functions": A list of functions defined outside of any class.
    """
    result = {
        "classes": {},
        "top": []
    }
    
    try:
        tree = ast.parse(code)
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                functions = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                result["classes"][class_name] = functions
            elif isinstance(node, ast.FunctionDef):
                result["top"].append(node.name)
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
    
    result["ranges"] = ranges(code, result)
    return result

def ranges(code, dic):
    classes = {}
    functions = {}
    for k in dic["classes"]:
        t = 'class '+k+':'
        o = code.index(t)+len('class ')
        c = o+len(k)
        classes[o] = c
        for f in dic["classes"][k]:
            t = 'def '+f+'('
            o = code.index(t)+len('def ')
            c = o+len(f)
            functions[o] = c
    for f in dic["top"]:
        t = 'def '+f+'('
        o = code.index(t)+len('def ')
        c = o+len(f)
        # print(code[o:c])
        functions[o] = c
    return {
        "classes": classes,
        "functions": functions
    }

