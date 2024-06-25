# -*- coding: utf-8 -*-
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

bl_info = {
    "name": "Color and Curve Pie",
    "author": "CDMJ",
    "version": (1, 0, 1),
    "blender": (2, 93, 0),
    "location": "",
    "description": "Simple Color Picker and Curve Falloff for 3D View and Image Editor",
    "warning": "Simple code",
    "category": "3D View"
}

import bpy
from bpy.types import Menu

addon_keymaps = []

class ColorCurvePie(Menu):
    bl_label = 'Set Colors and Brush falloff'
    bl_idname = 'OBJECT_MT_color_curve_pie'

    def draw(self, context):
        ts = context.tool_settings
        ups = ts.unified_paint_settings
        ptr = ups if ups.use_unified_color else ts.image_paint.brush
        brush = ts.image_paint.brush

        pie = self.layout.menu_pie()
        # Add a color swatch that can popup a color picker
        box = pie.box()
        box.template_color_picker(ptr, 'color', value_slider=True)
        box.prop(ptr, 'color')
        box.prop(ptr, 'secondary_color')
        
        # Show the brush falloff curve editor
        box = pie.box()
        box.template_curve_mapping(brush, "curve", brush=True)


def register():
    bpy.utils.register_class(ColorCurvePie)

    # Register keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Image PaintB', space_type='EMPTY')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'B', 'PRESS', ctrl=False, shift=True)
    kmi.properties.name = "OBJECT_MT_color_curve_pie"
    addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_class(ColorCurvePie)

    # Unregister keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
