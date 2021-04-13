import bpy
import bpy_extras
import shutil
import pathlib


def copyfile(filepath, target):
    shutil.copy(filepath, target)

class PA_Add_BlendFile(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    """Add Blend File"""
    bl_idname = "pa.add_blend_file"
    bl_label = "Add Blend File"

    filename_ext = ".blend"

    filter_glob: bpy.props.StringProperty(
        default="*.blend",
        options={'HIDDEN'},
        maxlen=255,
    )

    def execute(self, context):

        Addon_Folder = pathlib.Path(__file__).parent
        Addon_Object_Folder = "{}/Objects/".format(Addon_Folder)

        copyfile(self.filepath, Addon_Object_Folder)

        return {'FINISHED'}





def register():
    bpy.utils.register_class(PA_Add_BlendFile)


def unregister():
    bpy.utils.unregister_class(PA_Add_BlendFile)


if __name__ == "__main__":
    register()
