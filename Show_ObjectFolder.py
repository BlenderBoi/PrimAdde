import bpy
import bpy_extras
import pathlib
import os



def showfolder(filepath):
    os.startfile(filepath)



class PA_Show_ObjectFolder(bpy.types.Operator):
    """Show Object Folder"""
    bl_idname = "pa.show_object_folder"
    bl_label = "Show Object Folder"


    def execute(self, context):

        Addon_Folder = pathlib.Path(__file__).parent
        Addon_Object_Folder = "{}/Objects/".format(Addon_Folder)
        showfolder(Addon_Object_Folder)

        return {'FINISHED'}





def register():
    bpy.utils.register_class(PA_Show_ObjectFolder)


def unregister():
    bpy.utils.unregister_class(PA_Show_ObjectFolder)


if __name__ == "__main__":
    register()
