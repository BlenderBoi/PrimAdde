

bl_info = {
    "name": "Prim_Adde",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Add Blend File as Object Primitive",
    "warning": "Things can get laggy or even crashable if you have too much file or objects in the blend file",
    "wiki_url": "",
    "category": "Object",
}


import bpy
from . import Prim_Adde
from . import Add_BlendFile
from . import Preferences
from . import Show_ObjectFolder
# from . import Remove_BlendFile

modules =  [Prim_Adde, Add_BlendFile, Preferences, Show_ObjectFolder]

def register():


    for module in modules:
        module.register()

def unregister():


    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
