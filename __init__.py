# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Color and Curve Pie",
           "author": "CDMJ",
           "version": (1, 0, 0),
           "blender": (2, 78, 0),
           "location": "",
           "description": "Simple Color Picker and Curve Falloff for 3D View and Image Editor",
           "warning": "Simple code",
           "category": "3D View"}


import bpy
from bpy.types import Menu

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)


class ColorCurvePie(bpy.types.Menu):
    bl_label = 'Set Colors and Brush falloff'
    bl_idname = 'OBJECT_MT_color_curve_pie'

    def draw(self, context):
        ts = context.tool_settings
        ups = ts.unified_paint_settings
        ptr = ups if ups.use_unified_color else ts.image_paint.brush
        brush = ts.image_paint.brush
        

        pie = self.layout.menu_pie()
        row = pie.row()
        # add a colour swatch that can popup a colour picker
        #row.prop(ptr, 'color')
        box = pie.box()
        #show the brush falloff curve editor
        box.template_curve_mapping(brush, "curve", brush=True)
        row = pie.row()
        box = pie.box()
        #show the colour picker directly
        box.template_color_picker(ptr, 'color', value_slider=True)
        box.prop(ptr, 'color')
        box.prop(ptr, 'secondary_color')
        
        
        



def register():
    bpy.utils.register_class(ColorCurvePie)


def unregister():
    bpy.utils.unregister_class(ColorCurvePie)


if __name__ == "__main__":
    register()

    #bpy.ops.wm.call_menu_pie(name="OBJECT_MT_colour_pie")
    
def register():
    bpy.utils.register_module(__name__)

    km_list = ['3D View', 'Image Paint']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new('wm.call_menu_pie', 'B', 'PRESS', ctrl=False, shift=True)
        kmi.properties.name = "OBJECT_MT_color_curve_pie"

def unregister():
    bpy.utils.unregister_module(__name__)

    km_list = ['3D View','Image Paint']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items \
                            if (kmi.idname == "OBJECT_MT_color_curve_pie")):
            km.keymap_items.remove(kmi)
        







if __name__ == "__main__":
    register()



