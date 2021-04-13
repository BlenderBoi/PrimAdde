import bpy
import pathlib
import os

position_mode = [("CURSOR","3D Cursor","3D Cursor"),("CENTER","Center","Center")]

# position_mode = [("CURSOR","3D Cursor","3D Cursor"),("CENTER","Center","Center"),("SOURCE","Source","Source")]
# align_mode = [("CURSOR","Cursor","Cursor"),("WORLD","World","World"),("VIEW","View","View")]

#More Settings
#User Defined
#Save Metadata to be used instead of dynamic



class PrimAdde_MT_Menu(bpy.types.Menu):
    bl_label = "PrimAdde"
    bl_idname = "OBJECT_MT_primadde"

    def draw(self, context):
        layout = self.layout

        menu_func(self, context)



def get_obj_callback(self, context):

    Enum_Items = []

    blend_file = self.path

    with bpy.data.libraries.load(blend_file) as (data_from, data_to):

        for object in data_from.objects:

            Enum_Item = (object,object,object)
            Enum_Items.append(Enum_Item)

    return Enum_Items



class ABM_OT_Add_Base_Mesh(bpy.types.Operator):
    """Add Base Mesh"""
    bl_idname = "abm.add_base_mesh"
    bl_label = "Add Object"
    bl_options = {'REGISTER', 'UNDO'}

    path : bpy.props.StringProperty()
    name: bpy.props.StringProperty(default="Primitive")
    file: bpy.props.StringProperty()
    object_name: bpy.props.StringProperty()
    scale: bpy.props.FloatProperty(
        name="size",
        subtype="DISTANCE",
        default=1,
    )
    position_mode: bpy.props.EnumProperty(items=position_mode)

    object: bpy.props.EnumProperty(items=get_obj_callback)


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        layout = self.layout
        row = layout.row()
        row.prop(self, "name", text="Name")
        row = layout.row()
        row.prop(self, "scale", text="Scale")
        row = layout.row()
        row.prop(self, "position_mode", text="Position")
        row = layout.row()
        row.prop(self, "object", text="Object")


    def execute(self, context):


        File = self.file
        Dir = pathlib.Path(__file__).parent
        path = "{}/Objects/{}".format(Dir, File)

        section = "\\Object\\"
        directory = path + section
        filename = self.object

        bpy.ops.object.select_all(action='DESELECT')

        if pathlib.Path(path).is_file():
            bpy.ops.wm.append(filename=filename, directory=directory)

        selected = bpy.context.selected_objects
        context.view_layer.objects.active = selected[0]

        obj = context.active_object
        obj.scale = (self.scale, self.scale, self.scale)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        obj.name = self.name

        if self.position_mode == "CURSOR":
            obj.location = bpy.context.scene.cursor.location
        if self.position_mode == "CENTER":
            obj.location = (0, 0, 0)

        return {'FINISHED'}


def menu_func(self, context):

    Dir = pathlib.Path(__file__).parent
    path = pathlib.Path("{}/Objects/".format(Dir))

    files = path.glob("*.blend")

    for file in files:

        item = self.layout.operator(ABM_OT_Add_Base_Mesh.bl_idname, icon='OBJECT_DATA', text=file.stem)
        item.path = str(file)
        item.file = file.name
        item.name = file.stem


def Addon_Menu(self, context):

    layout = self.layout
    layout.menu("OBJECT_MT_primadde", icon="BLENDER")


classes = [ABM_OT_Add_Base_Mesh, PrimAdde_MT_Menu]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.prepend(Addon_Menu)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.prepend(Addon_Menu)

if __name__ == "__main__":
    register()
