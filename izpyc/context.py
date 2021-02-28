from ctypes import *
from .space import Space


class Context:
    iz = None
    # registered_array = []
    
    def __init__(self):
        self.label = None
        return


    def save(self):
        self.label = Space.iz.cs_saveContext()
        

    def __enter__(self):
        self.label = Space.iz.cs_saveContext()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        if self.label is None:
            return

        Space.iz.cs_restoreContextUntil(self.label)
        self.label = None
        

    def restore(self):
        if self.label is None:
            raise RuntimeError("context is already restored")

        Space.iz.cs_restoreContextUntil(self.label)
        self.label = None


    def forget_save(self):
        if self.label is None:
            raise RuntimeError("context is already forgotten")

        Space.iz.cs_forgetSaveContextUntil(self.label)
        self.label = None

def save_context():
    return Context()
