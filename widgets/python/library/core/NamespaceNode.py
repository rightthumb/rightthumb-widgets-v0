"""
Proof-of-concept namespace + parallel meta tree
with use-case-based examples and YAML dump output.
"""

# ------------------------------------------------------------
# CORE CLASSES
# ------------------------------------------------------------

class NamespaceNode:
    """
    Path-aware namespace node.

    Features:
        - Auto-creates children on attribute access
        - Knows its own full dotted path
        - Resolves matching meta node from a parallel meta tree
        - Can access parent / ancestor meta
    """

    _reserved = {
        '_name',
        '_parent',
        '_root',
        '_meta_root',
        '_children',
        '_is_meta',
        '_reserved',
    }

    def __init__(self, name='', parent=None, root=None, meta_root=None, is_meta=False):
        object.__setattr__(self, '_name', name)
        object.__setattr__(self, '_parent', parent)
        object.__setattr__(self, '_root', self if root is None else root)
        object.__setattr__(self, '_meta_root', meta_root if meta_root is not None else self)
        object.__setattr__(self, '_children', {})
        object.__setattr__(self, '_is_meta', is_meta)

    def __getattr__(self, key):
        if key in self._reserved or key.startswith('__'):
            raise AttributeError(key)

        children = object.__getattribute__(self, '_children')
        if key not in children:
            child = NamespaceNode(
                name=key,
                parent=self,
                root=self._root,
                meta_root=self._meta_root,
                is_meta=self._is_meta
            )
            children[key] = child
            object.__setattr__(self, key, child)
        return children[key]

    def __setattr__(self, key, value):
        if key in self._reserved or key.startswith('__'):
            object.__setattr__(self, key, value)
            return
        object.__setattr__(self, key, value)

    @property
    def _path_list(self):
        parts = []
        node = self
        while node is not None and node._name:
            parts.append(node._name)
            node = node._parent
        return list(reversed(parts))

    @property
    def _path(self):
        return '.'.join(self._path_list)

    @property
    def _meta_path(self):
        return (self._path + '.meta') if self._path else 'meta'

    def _resolve_from(self, start_node, path):
        node = start_node
        if not path:
            return node
        for part in path.split('.'):
            node = getattr(node, part)
        return node

    @property
    def _meta(self):
        """
        Matching meta node for this node.

        Example:
            root.functions.parsers.python.extract._meta
            -> metaRoot.functions.parsers.python.extract.meta
        """
        return self._resolve_from(self._meta_root, self._meta_path)

    @property
    def _parent_meta(self):
        """
        Immediate parent's matching meta node.
        """
        if self._parent is None or not self._parent._name:
            return None
        return self._parent._meta

    def _ancestor_meta(self):
        """
        Return all ancestor meta nodes from nearest parent upward.
        """
        out = []
        node = self._parent
        while node is not None and node._name:
            out.append(node._meta)
            node = node._parent
        return out

    def _self_and_ancestor_meta(self):
        """
        Return [self meta, parent meta, grandparent meta, ...]
        """
        return [self._meta] + self._ancestor_meta()

    def __repr__(self):
        kind = 'MetaNode' if self._is_meta else 'Node'
        return f"<{kind} path='{self._path}'>"


def make_roots():
    metaRoot = NamespaceNode(name='', is_meta=True)
    root = NamespaceNode(name='', meta_root=metaRoot, is_meta=False)
    return root, metaRoot


# ------------------------------------------------------------
# YAML-ISH DUMP HELPERS
# ------------------------------------------------------------

def node_to_data(node, include_internal=False):
    """
    Convert NamespaceNode tree into a plain nested dict suitable for YAML output.
    """
    out = {}

    # Regular user-assigned attributes
    for k, v in node.__dict__.items():
        if k.startswith('_'):
            continue
        if isinstance(v, NamespaceNode):
            continue
        out[k] = v

    # Auto-created child nodes
    for child_name, child_node in node._children.items():
        out[child_name] = node_to_data(child_node, include_internal=include_internal)

    if include_internal:
        out['__internal__'] = {
            'path': node._path,
            'is_meta': node._is_meta,
        }

    return out


def to_yaml_like(data, indent=0):
    """
    Tiny YAML-like renderer so you can test without PyYAML.
    """
    lines = []
    pad = '  ' * indent

    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{pad}{k}:")
                lines.extend(to_yaml_like(v, indent + 1))
            else:
                lines.append(f"{pad}{k}: {scalar_to_yaml(v)}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(to_yaml_like(item, indent + 1))
            else:
                lines.append(f"{pad}- {scalar_to_yaml(item)}")
    else:
        lines.append(f"{pad}{scalar_to_yaml(data)}")

    return lines


def scalar_to_yaml(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        # keep it simple + safe
        if value == '' or ':' in value or '#' in value or value.strip() != value:
            return repr(value)
        return value
    return repr(value)


def print_yaml(title, data):
    print('\n' + '=' * 70)
    print(title)
    print('=' * 70)
    print('\n'.join(to_yaml_like(data)))


# ------------------------------------------------------------
# USE CASE EXAMPLES
# ------------------------------------------------------------

if __name__ == '__main__':
    root, metaRoot = make_roots()

    # =========================================================
    # USE CASE 1:
    # Build a callable namespace tree naturally
    # =========================================================

    # A callable-like location in the main tree
    node = root.functions.parsers.python.extract

    print('\n[USE CASE 1] basic path awareness')
    print('node              ->', node)
    print('node._path        ->', node._path)
    print('node._meta_path   ->', node._meta_path)

    # =========================================================
    # USE CASE 2:
    # Attach documentation only in the parallel meta tree
    # =========================================================

    # Top-level documentation
    metaRoot.functions.meta.description = 'Top-level function registry'
    metaRoot.functions.meta.kind = 'namespace'
    metaRoot.functions.meta.tags = ['functions', 'registry']

    # Parser group docs
    metaRoot.functions.parsers.meta.description = 'Parser-related callables'
    metaRoot.functions.parsers.meta.kind = 'group'
    metaRoot.functions.parsers.meta.tags = ['parsers', 'group']

    # Language-specific docs
    metaRoot.functions.parsers.python.meta.description = 'Python parser helpers'
    metaRoot.functions.parsers.python.meta.kind = 'language-group'
    metaRoot.functions.parsers.python.meta.tags = ['python', 'language']

    # Specific callable docs
    metaRoot.functions.parsers.python.extract.meta.description = 'Extract Python callables'
    metaRoot.functions.parsers.python.extract.meta.kind = 'callable'
    metaRoot.functions.parsers.python.extract.meta.aliases = ['extract', 'extract_callables']
    metaRoot.functions.parsers.python.extract.meta.example = 'root.functions.parsers.python.extract'
    metaRoot.functions.parsers.python.extract.meta.returns = 'structured callable payload'
    metaRoot.functions.parsers.python.extract.meta.callback_rule = 'run after parser stage'
    metaRoot.functions.parsers.python.extract.meta.dimension_router = {
        'language': 'python',
        'mode': 'callable-extract',
    }

    print('\n[USE CASE 2] self meta access')
    print('node._meta.description  ->', node._meta.description)
    print('node._meta.kind         ->', node._meta.kind)
    print('node._meta.aliases      ->', node._meta.aliases)

    # =========================================================
    # USE CASE 3:
    # Access parent meta natively from the node
    # =========================================================

    print('\n[USE CASE 3] parent meta access')
    print('parent meta path        ->', node._parent_meta._path)
    print('parent meta description ->', node._parent_meta.description)

    # =========================================================
    # USE CASE 4:
    # Walk up the meta chain for inherited or layered docs
    # =========================================================

    print('\n[USE CASE 4] self + ancestor meta chain')
    for m in node._self_and_ancestor_meta():
        print(f"meta path: {m._path}")
        print('  description:', getattr(m, 'description', None))
        print('  kind       :', getattr(m, 'kind', None))

    # =========================================================
    # USE CASE 5:
    # Attach a real callback / target to the main node
    # =========================================================

    def extract_python_callables(payload):
        return {
            'ok': True,
            'message': 'callables extracted',
            'input_preview': str(payload)[:30]
        }

    root.functions.parsers.python.extract.target = extract_python_callables
    root.functions.parsers.python.extract.enabled = True

    print('\n[USE CASE 5] callable/target assignment')
    result = root.functions.parsers.python.extract.target('def x(): pass')
    print('call result ->', result)

    # =========================================================
    # USE CASE 6:
    # Another callable nearby to prove parallel structure
    # =========================================================

    root.functions.parsers.python.comments.target = lambda text: {'comments_found': 3}
    root.functions.parsers.python.comments.enabled = True

    metaRoot.functions.parsers.python.comments.meta.description = 'Extract Python comments'
    metaRoot.functions.parsers.python.comments.meta.kind = 'callable'
    metaRoot.functions.parsers.python.comments.meta.aliases = ['comments', 'extract_comments']

    print('\n[USE CASE 6] sibling callable')
    sibling = root.functions.parsers.python.comments
    print('sibling._path             ->', sibling._path)
    print('sibling._meta.description ->', sibling._meta.description)

    # =========================================================
    # USE CASE 7:
    # Show that parent namespaces also know their own meta
    # =========================================================

    parent_node = root.functions.parsers.python

    print('\n[USE CASE 7] parent node introspection')
    print('parent_node._path         ->', parent_node._path)
    print('parent_node._meta._path   ->', parent_node._meta._path)
    print('parent_node._meta.kind    ->', parent_node._meta.kind)

    # =========================================================
    # YAML DUMPS
    # =========================================================

    related_globals = {
        'root_tree': node_to_data(root, include_internal=False),
        'meta_tree': node_to_data(metaRoot, include_internal=False),
        'focused_node_summary': {
            'path': node._path,
            'meta_path': node._meta._path,
            'parent_meta_path': node._parent_meta._path if node._parent_meta else None,
            'self_meta_description': getattr(node._meta, 'description', None),
            'ancestor_meta_paths': [m._path for m in node._ancestor_meta()],
        }
    }

    print_yaml('YAML DUMP: RELATED GLOBALS / MAIN + META TREES', related_globals)