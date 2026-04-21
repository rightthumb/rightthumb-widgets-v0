
def pathImp(path, module_name=None, register=False):
    """
    Import a Python module from a full file path.

    Args:
        path (str): Full path to .py file
        module_name (str): Optional custom module name
        register (bool): If True, adds to sys.modules

    Returns:
        module object
    """
    import importlib.util
    import sys
    import os
    path = os.path.abspath(path)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Module path not found: {path}")

    if module_name is None:
        module_name = os.path.splitext(os.path.basename(path))[0]

    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for: {path}")

    module = importlib.util.module_from_spec(spec)

    if register:
        sys.modules[module_name] = module  # optional global registration

    spec.loader.exec_module(module)

    return module