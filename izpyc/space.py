from ctypes import *
from .util import iz_bool

class Space:
    iz = None
    ref_counter = 0
    registered_array = []
    
    def __init__(self, izlib):
        if Space.ref_counter == 0:
            Space.iz = izlib
            Space.iz.cs_init()

        Space.ref_counter += 1
        self.with_level = 0
        self.is_valid = True


    def __del__(self):
        if self.is_valid:
            self.destroy()
            

    def destroy(self):
        if self.is_valid:
            Space.ref_counter -= 1
            if Space.ref_counter == 0:
                Space.iz.cs_end()
                Space.iz = None
                
            print("destroyed")
            self.is_valid = False
        else:
            raise RuntimeError("Space object is already destroyed")


    def __enter__(self):
        self.with_level += 1
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.with_level -= 1
        if self.with_level == 0:
            self.destroy()
