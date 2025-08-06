import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


def extract_top_level_callables(source_code: str) -> dict:
    """
    Execute the given source code and return a dictionary with 'functions' and 'classes'
    as keys, each containing their respective top-level callable objects.

    :param source_code: Python source code as a string.
    :return: Dict with 'functions' and 'classes' keys containing name: object mappings.
    """
import types
    scope = {}
    exec(source_code, scope)

    return {
        'def': {
            name: obj
            for name, obj in scope.items()
            if isinstance(obj, types.FunctionType) and not name.startswith("__")
        },
        'class': {
            name: obj
            for name, obj in scope.items()
            if isinstance(obj, type) and not name.startswith("__")
        }
    }


def js_extract_namespaced_assignments(code):
    import esprima # type: ignore
    tree = esprima.parseScript(code, {'range': True})
    assignments = {}

    for stmt in tree.body:
        if stmt.type == 'ExpressionStatement':
            expr = stmt.expression
            if expr.type == 'AssignmentExpression':
                left = expr.left
                right = expr.right

                # Reconstruct the full namespace path
                if left.type == 'MemberExpression':
                    parts = []
                    current = left
                    while current.type == 'MemberExpression':
                        if current.property.type == 'Identifier':
                            parts.insert(0, current.property.name)
                        elif current.property.type == 'Literal':
                            parts.insert(0, str(current.property.value))
                        current = current.object
                    if current.type == 'Identifier':
                        parts.insert(0, current.name)
                    full_path = '.'.join(parts)

                    # Extract the source code for the right-hand side using the range
                    start, end = right.range
                    assigned_code = code[start:end]

                    assignments[full_path] = assigned_code

    return assignments


def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)