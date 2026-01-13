from types import SimpleNamespace

data = SimpleNamespace()
data.name = "Scott"
print(data.name)  # 'Scott'

class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__

d = DotDict({'name': 'Scott'})
print(d.name)  # 'Scott'
