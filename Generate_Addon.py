import bpy
import bpy_extras
import shutil
import pathlib



class PA_Generate_Addon(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Generate Addon"""
    bl_idname = "pa.generate_addon"
    bl_label = "Generate Addon"

    filename_ext = ".blend"

    filter_glob: bpy.props.StringProperty(
        default="*.blend",
        options={'HIDDEN'},
        maxlen=255,
    )

    def execute(self, context):

        Addon_Folder = pathlib.Path(__file__).parent
        Addon_Object_Folder = "{}/Objects/".format(Addon_Folder)

        generate_addon(self.filepath, Addon_Object_Folder)

        return {'FINISHED'}





def register():
    bpy.utils.register_class(PA_Generate_Addon)


def unregister():
    bpy.utils.unregister_class(PA_Generate_Addon)


if __name__ == "__main__":
    register()
