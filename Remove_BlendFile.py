import bpy
import bpy_extras
import shutil
import pathlib


def removefile(filepath):
    shutil.rmtree(filepath)

class PA_Remove_BlendFile(bpy.types.Operator):
    """Remove Blend File"""
    bl_idname = "pa.remove_blend_file"
    bl_label = "Remove Blend File"


    file : bpy.props.StringProperty()

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


    def execute(self, context):

        Addon_Folder = pathlib.Path(__file__).parent
        Addon_Object_Folder = "{}/Objects/".format(Addon_Folder)


        removefile(self.file)

        return {'FINISHED'}





def register():
    bpy.utils.register_class(PA_Remove_BlendFile)


def unregister():
    bpy.utils.unregister_class(PA_Remove_BlendFile)


if __name__ == "__main__":
    register()
