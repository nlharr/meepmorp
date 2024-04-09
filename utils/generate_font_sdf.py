import json


font_path = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'

import freetype
face = freetype.Face(font_path)
face.set_char_size( 48*64 )
face.load_char('S')
bitmap = face.glyph.bitmap
print(bitmap.buffer)


# Ok, what do we need to render fonts:
# Need an SDF of the glyphs
#
