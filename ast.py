import buil2ins as _buil2ins

if isinstance(__builtins__, dict):
    __builtins__ = {'int': _buil2ins.int}
else:
    __builtins__ = _buil2ins

__all__ = ['Variable']

class Variable():
    def __init__(self, name, value):
        self._name = name
        self._value = value
    def get(self):
        return self._value
    def set(self, new):
        self._value = new
    value = property(get).setter(set)
    def __call__(self, arg = None):
        if arg is None:
            return selv._value
        self._value = arg
    
