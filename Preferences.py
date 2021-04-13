import bpy
import pathlib

class PA_user_preferences(bpy.types.AddonPreferences):

    bl_idname = __package__

    show_object: bpy.props.BoolProperty(default=False)

    def draw(self, context):

        layout = self.layout

        row = layout.row(align=True)
        row.operator("pa.add_blend_file", text="Import Blend File")
        row.operator("pa.show_object_folder", text="Show Folder")



        Dir = pathlib.Path(__file__).parent
        path = pathlib.Path("{}/Objects/".format(Dir))

        files = path.glob("*.blend")

        box = layout.box()

        box.prop(self, "show_object", text="List Object")

        for file in files:
            row = box.row()
            row.label(text=file.name, icon="FILE_BLEND")
            # row.operator("pa.remove_blend_file", text="", icon="TRASH").file = str(file)

            row = box.row()

            if self.show_object:
                with bpy.data.libraries.load(str(file)) as (data_from, data_to):

                    for object in data_from.objects:
                        row.separator()

                        row.label(text="", icon="OBJECT_DATAMODE")
                        row.label(text=object)
                        row = box.row()



classes = [PA_user_preferences]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)




def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
