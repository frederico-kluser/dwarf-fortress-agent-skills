# Color

> Fonte: [Color](https://dwarffortresswiki.org/index.php/Color) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For an overview of graphics in Dwarf Fortress, see Graphics.*

*For user-compiled colors, see color scheme.*

*For lists of the colors of materials, professions, creatures, etc., see the "Color Lists" at the bottom of this page.*

*Dwarf Fortress* can use roughly 8424 **colors** to give many tiles such as foregrounds, backgrounds and sprites different colors. These colors make up the color scheme. Which of these colors are assigned to a given tile is often decided by values in its raw file. Whether a pixel shows foreground, background, black or anything in between is influenced by its brightness and opacity. These colors are shown at the right:

The original game used a simplistic 16-color palette, with 8 of those colors: black, blue, green, cyan, red, purple, yellow, grey, and a lighter version of those colors creating a total of 16. The game also has an option to use the classic ASCII visuals, mimicking the classic version of the game by using 16 colors. Even with the updated graphics turned on, the text in the GUI still references the color scheme. Color is also used to express various information, from a dwarf's profession, to the natural color of a terrain feature, to the material an item is made of.

Some sprite sheets contain their own dedicated color palettes.

## Overview

### The tileset influences color display

\

In the simplest case, a pixel on a tileset is either white (foreground) or transparent\* (background). However, black, and anything in between is possible as well (even color):

- a white pixel will show the foreground color
- a transparent\* pixel will show the background color
- a black pixel will stay black

The darker a white pixel is (i.e. a shade of gray), the darker the foreground color will be displayed. Similarly, a black pixel with lower opacity will result in a darker background color. A partially transparent, non-black pixel shows both the background and foreground color.\[Verify\]

\*magenta for .bmp files.

### Colors are assigned based on material and other raw values

To decide which colors to use for a tile in ASCII mode, DF looks at raw values for that object (color value or color token) and selects a foreground and background color from the 16 colors in the color scheme. When a color value is defined, it directly picks it from the 16. When instead a color token is defined, the game compares the color token definition to all 16 colors in the color scheme and picks the closest match.

For tiles in graphics mode, it instead uses a raw-defined palette. The default palette image is shown above. It checks for each color in the row defined by the PALETTE_DEFAULT token--in this case, the first row--and then maps it to the corresponding color in the same column, based on the STATE_COLOR of the object that the tile being printed corresponds to. For the vanilla raws, this is all in alphabetical order. New palettes and colors can be defined in the same way.

## How colors are assigned

Colors of Status icons, professions, text and the interface in general are hardcoded. Items, furniture, constructions, and geographic features get the color of their material. Dyes and material contaminants use color tokens.

### Wall and floor color

Phyllite (to the left) has `[``DISPLAY_COLOR``:0:7:1]` and `[``BASIC_COLOR``:7:0]`. The white sand present has `[``DISPLAY_COLOR``:DISPLAY_COLOR:7:6:1]` and so the actual floor color is `7:1` (white).

While the foreground, background and brightness shown in the RAW files will be applied to walls, the mineral's "secondary" color will end up different. Here is how it works:

- If the [`[BASIC_COLOR]`](/index.php/Material_definition_token#BASIC_COLOR "Material definition token") tag is specified, it will use that color. Note that the [`[BASIC_COLOR]`](/index.php/Material_definition_token#BASIC_COLOR "Material definition token") tag only has foreground and brightness as arguments.
- If [`[BASIC_COLOR]`](/index.php/Material_definition_token#BASIC_COLOR "Material definition token") is left out:
  - The background color is forced to 0 (effectively stripping it).
  - If the foreground color is 0, the game will display it as dark gray, color 8 (in other words, color 0 with brightness 1).

This is effective for stairs, floors, ramps, and constructions (in the case of stone). When stone is engraved, it uses the material's [`[TILE_COLOR]`](/index.php/Material_definition_token#TILE_COLOR "Material definition token") (which is the same as the [`[DISPLAY_COLOR]`](/index.php/Material_definition_token#DISPLAY_COLOR "Material definition token") unless overridden).

### Color values

Colors are primarily defined using the `[``COLOR``:x:y:z]` or `[``DISPLAY_COLOR``:x:y:z]` tokens. The three arguments are:

1.  Foreground color \[0-7\]
2.  Background color \[0-7\]
3.  Brightness of the foreground color \[0 or 1\]

The brightness of the background color is always 0.

By default\*, the following 8 pairs of colors are displayed. These are bright and dark shades of the primary colors, as well as black, white, and two grays:

|  |  |
|----|----|
| Col. / Bri. / Name / 0 / 0 / BLACK / 1 / 0 / BLUE / 2 / 0 / GREEN / 3 / 0 / CYAN / 4 / 0 / RED / 5 / 0 / MAGENTA / 6 / 0 / BROWN / 7 / 0 / LGRAY | Col. / Bri. / Name / Alt. / 0 / 1 / DGRAY / 8 / 1 / 1 / LBLUE / 9 / 2 / 1 / LGREEN / 10 / 3 / 1 / LCYAN / 11 / 4 / 1 / LRED / 12 / 5 / 1 / LMAGENTA / 13 / 6 / 1 / YELLOW / 14 / 7 / 1 / WHITE / 15 |

*(\* See color scheme for information about how to change the actual various colors as displayed.)*

Sometimes the color numbers are part of another token, e.g. `[``LEAVES``:quarry bush leaf:quarry bush leaves:6:7:0:0:0:0:1:LOCAL_PLANT_MAT:LEAF]` specifies the colors `7:0:0` for quarry bush leaves and `0:0:1` for wilted quarry bush leaves.

#### Values 8-15

If the brightness value is 1 or another nonzero number, it adds 8 to the foreground color. If the final value of the foreground or background is 8-15, it appears as a "bright" color.

As these values can be manually typed in instead of using the brightness value, you can also give the background a bright color with this method. For example, for a white background color, add 8 to 7 = 15. For a light green background color, you add 8 to 2 = 10.

### Color tokens

When in graphics mode, most things do not use color flags. Instead, they reference color tokens defined in `descriptor_color_standard.txt`. Color tokens are referenced by their token name, e.g. `[``STATE_COLOR``:SOLID:DARK_GREEN]` or `[``POWDER_DYE``:EMERALD]`. The defined RGB values are not displayed in-game; instead, it assigns colors in the sprite from the top row of the palette file (see Graphics#Palettes) to the row defined in `data/vanilla/vanilla_descriptors_graphics/graphics/palette_default.txt`, or any user-defined palette objects.

The following colors are grouped according to their corresponding display color in ASCII mode. Hexadecimal color values are not used in the raws, but correspond to the RGB values that are. For further information, see the Wikipedia article on web colors.

|  |  |
|----|----|
| DGRAY colors / Token / RGB / Hex / Palette / BLACK / 0 / 0 / 0 / \#000000 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CLEAR / 128 / 128 / 128 / \#808080 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GRAY / 128 / 128 / 128 / \#808080 / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAUPE_GRAY / 139 / 133 / 137 / \#8B8589 / █ / █ / █ / █ / █ / █ / █ / █ / █ |  |
| LGRAY colors / Token / RGB / Hex / Palette / SILVER / 192 / 192 / 192 / \#C0C0C0 / █ / █ / █ / █ / █ / █ / █ / █ / █ / ASH_GRAY / 178 / 190 / 181 / \#B2BEB5 / █ / █ / █ / █ / █ / █ / █ / █ / █ | WHITE colors / Token / RGB / Hex / Palette / WHITE / 255 / 255 / 255 / \#FFFFFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / BEIGE / 245 / 245 / 220 / \#F5F5DC / █ / █ / █ / █ / █ / █ / █ / █ / █ / IVORY / 255 / 255 / 240 / \#FFFFF0 / █ / █ / █ / █ / █ / █ / █ / █ / █ / LAVENDER / 230 / 230 / 250 / \#E6E6FA / █ / █ / █ / █ / █ / █ / █ / █ / █ / LAVENDER_BLUSH / 255 / 240 / 245 / \#FFF0F5 / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| RED colors / Token / RGB / Hex / Palette / MAROON / 128 / 0 / 0 / \#800000 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CHESTNUT / 205 / 92 / 92 / \#CD5C5C / █ / █ / █ / █ / █ / █ / █ / █ / █ / ROSE / 244 / 194 / 194 / \#F4C2C2 / █ / █ / █ / █ / █ / █ / █ / █ / █ / RED / 255 / 0 / 0 / \#FF0000 / █ / █ / █ / █ / █ / █ / █ / █ / █ / VERMILION / 227 / 66 / 52 / \#E34234 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_CHESTNUT / 152 / 105 / 96 / \#986960 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BURNT_SIENNA / 233 / 116 / 81 / \#E97451 / █ / █ / █ / █ / █ / █ / █ / █ / █ / MAHOGANY / 192 / 64 / 0 / \#C04000 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PALE_BROWN / 152 / 118 / 84 / \#987654 / █ / █ / █ / █ / █ / █ / █ / █ / █ / RASPBERRY_PINK / 255 / 25 / 128 / \#FF1980 / █ / █ / █ / █ / █ / █ / █ / █ / █ / RED_PURPLE / 178 / 0 / 75 / \#B2004B / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_PINK / 231 / 84 / 128 / \#E75480 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_SCARLET / 86 / 3 / 25 / \#560319 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CRIMSON / 220 / 20 / 60 / \#DC143C / █ / █ / █ / █ / █ / █ / █ / █ / █ / CARMINE / 150 / 0 / 24 / \#960018 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CARDINAL / 196 / 30 / 58 / \#C41E3A / █ / █ / █ / █ / █ / █ / █ / █ / █ | LRED colors / Token / RGB / Hex / Palette / RUST / 183 / 65 / 14 / \#B7410E / █ / █ / █ / █ / █ / █ / █ / █ / █ / PUMPKIN / 255 / 117 / 24 / \#FF7518 / █ / █ / █ / █ / █ / █ / █ / █ / █ / SEPIA / 112 / 66 / 20 / \#704214 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BROWN / 150 / 75 / 0 / \#964B00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CINNAMON / 123 / 63 / 0 / \#7B3F00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAN / 210 / 180 / 140 / \#D2B48C / █ / █ / █ / █ / █ / █ / █ / █ / █ / RAW_UMBER / 115 / 74 / 18 / \#734A12 / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAUPE_SANDY / 150 / 113 / 23 / \#967117 / █ / █ / █ / █ / █ / █ / █ / █ / █ / ECRU / 194 / 178 / 128 / \#C2B280 / █ / █ / █ / █ / █ / █ / █ / █ / █ / SCARLET / 255 / 36 / 0 / \#FF2400 / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| BROWN colors / Token / RGB / Hex / Palette / BURNT_UMBER / 138 / 51 / 36 / \#8A3324 / █ / █ / █ / █ / █ / █ / █ / █ / █ / AUBURN / 111 / 53 / 26 / \#6F351A / █ / █ / █ / █ / █ / █ / █ / █ / █ / CHOCOLATE / 210 / 105 / 30 / \#DC691E / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAUPE_PALE / 188 / 152 / 126 / \#BC987E / █ / █ / █ / █ / █ / █ / █ / █ / █ / COPPER / 184 / 115 / 51 / \#B87333 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_BROWN / 101 / 67 / 33 / \#654321 / █ / █ / █ / █ / █ / █ / █ / █ / █ / LIGHT_BROWN / 205 / 133 / 63 / \#CD853F / █ / █ / █ / █ / █ / █ / █ / █ / █ / BRONZE / 205 / 127 / 50 / \#CD7F32 / █ / █ / █ / █ / █ / █ / █ / █ / █ / OCHRE / 204 / 119 / 34 / \#CC7722 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GOLDENROD / 218 / 165 / 32 / \#DAA520 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GOLD / 212 / 175 / 55 / \#D4AF37 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BRASS / 181 / 166 / 66 / \#B5A642 / █ / █ / █ / █ / █ / █ / █ / █ / █ / OLIVE / 128 / 128 / 0 / \#808000 / █ / █ / █ / █ / █ / █ / █ / █ / █ | YELLOW colors / Token / RGB / Hex / Palette / DARK_PEACH / 255 / 218 / 185 / \#FFDAB9 / █ / █ / █ / █ / █ / █ / █ / █ / █ / ORANGE / 255 / 165 / 0 / \#FFA500 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PEACH / 255 / 229 / 180 / \#FFE5B4 / █ / █ / █ / █ / █ / █ / █ / █ / █ / SAFFRON / 244 / 196 / 48 / \#F4C430 / █ / █ / █ / █ / █ / █ / █ / █ / █ / AMBER / 255 / 191 / 0 / \#FFBF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PEARL / 240 / 234 / 214 / \#F0EBD6 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BUFF / 240 / 220 / 130 / \#F0DC82 / █ / █ / █ / █ / █ / █ / █ / █ / █ / FLAX / 238 / 220 / 130 / \#EEDC82 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GOLDEN_YELLOW / 255 / 223 / 0 / \#FFDF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / LEMON / 253 / 233 / 16 / \#FDE910 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CREAM / 255 / 253 / 208 / \#FFFDD0 / █ / █ / █ / █ / █ / █ / █ / █ / █ / YELLOW / 255 / 255 / 0 / \#FFFF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / LIME / 204 / 255 / 0 / \#CCFF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| GREEN colors / Token / RGB / Hex / Palette / TAUPE_DARK / 72 / 60 / 50 / \#483C32 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_TAN / 145 / 129 / 81 / \#918151 / █ / █ / █ / █ / █ / █ / █ / █ / █ / YELLOW_GREEN / 154 / 205 / 50 / \#9ACD32 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_OLIVE / 85 / 104 / 50 / \#556832 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GREEN-YELLOW / 173 / 255 / 47 / \#ADFF2F / █ / █ / █ / █ / █ / █ / █ / █ / █ / APPLE_GREEN / 97 / 178 / 53 / \#61B235 / █ / █ / █ / █ / █ / █ / █ / █ / █ | LGREEN colors / Token / RGB / Hex / Palette / CHARTREUSE / 127 / 255 / 0 / \#7BFF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BRIGHT_GREEN / 80 / 229 / 0 / \#50E500 / █ / █ / █ / █ / █ / █ / █ / █ / █ / LEAF_GREEN / 25 / 178 / 17 / \#19B211 / █ / █ / █ / █ / █ / █ / █ / █ / █ / ZESTY_GREEN / 55 / 229 / 45 / \#37E52D / █ / █ / █ / █ / █ / █ / █ / █ / █ / GREEN / 0 / 255 / 0 / \#00FF00 / █ / █ / █ / █ / █ / █ / █ / █ / █ / WOODLAND_GREEN / 15 / 153 / 49 / \#0F9931 / █ / █ / █ / █ / █ / █ / █ / █ / █ / GRASS_GREEN / 0 / 204 / 51 / \#00CC33 / █ / █ / █ / █ / █ / █ / █ / █ / █ / VIBRANT_GREEN / 25 / 255 / 82 / \#19FF52 / █ / █ / █ / █ / █ / █ / █ / █ / █ / EMERALD / 80 / 200 / 120 / \#50C878 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_GREEN / 1 / 50 / 32 / \#013220 / █ / █ / █ / █ / █ / █ / █ / █ / █ / JADE / 0 / 168 / 107 / \#00A86B / █ / █ / █ / █ / █ / █ / █ / █ / █ / MIDNIGHT_BLUE / 0 / 51 / 102 / \#003366 / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| CYAN colors / Token / RGB / Hex / Palette / RUSSET / 117 / 90 / 87 / \#755A57 / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAUPE_MEDIUM / 103 / 76 / 71 / \#674C47 / █ / █ / █ / █ / █ / █ / █ / █ / █ / FERN_GREEN / 79 / 121 / 66 / \#4F7942 / █ / █ / █ / █ / █ / █ / █ / █ / █ / MOSS_GREEN / 173 / 223 / 173 / \#ADDFAD / █ / █ / █ / █ / █ / █ / █ / █ / █ / MINT_GREEN / 152 / 255 / 152 / \#98FF98 / █ / █ / █ / █ / █ / █ / █ / █ / █ / EUCALYPTUS / 76 / 153 / 141 / \#4C998D / █ / █ / █ / █ / █ / █ / █ / █ / █ / LIGHT_BLUE / 173 / 216 / 230 / \#ADD8E6 / █ / █ / █ / █ / █ / █ / █ / █ / █ / SLATE_GRAY / 112 / 128 / 144 / \#708090 / █ / █ / █ / █ / █ / █ / █ / █ / █ / BLUE-GRAY / 186 / 202 / 226 / \#BACAE2 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PALE_CHESTNUT / 221 / 173 / 175 / \#DDADAF / █ / █ / █ / █ / █ / █ / █ / █ / █ | LCYAN colors / Token / RGB / Hex / Palette / SPRING_GREEN / 0 / 255 / 127 / \#00FF7F / █ / █ / █ / █ / █ / █ / █ / █ / █ / AQUAMARINE / 127 / 255 / 212 / \#7FFFD4 / █ / █ / █ / █ / █ / █ / █ / █ / █ / SEA_FOAM / 25 / 255 / 220 / \#19FFDC / █ / █ / █ / █ / █ / █ / █ / █ / █ / TURQUOISE / 48 / 213 / 200 / \#30D5C8 / █ / █ / █ / █ / █ / █ / █ / █ / █ / AQUA / 0 / 255 / 255 / \#00FFFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / GLACIER_BLUE / 25 / 220 / 255 / \#19DCFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / SKY_BLUE / 135 / 206 / 235 / \#87CEEB / █ / █ / █ / █ / █ / █ / █ / █ / █ / LILAC / 200 / 162 / 200 / \#C8A2C8 / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| BLUE colors / Token / RGB / Hex / Palette / SEA_GREEN / 46 / 139 / 87 / \#2E8B57 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PINE_GREEN / 1 / 121 / 111 / \#01796F / █ / █ / █ / █ / █ / █ / █ / █ / █ / TEAL / 0 / 128 / 128 / \#008080 / █ / █ / █ / █ / █ / █ / █ / █ / █ / CERULEAN / 0 / 123 / 167 / \#007BA7 / █ / █ / █ / █ / █ / █ / █ / █ / █ / RIVER_BLUE / 61 / 139 / 204 / \#3D8BCC / █ / █ / █ / █ / █ / █ / █ / █ / █ / CORNFLOWER / 76 / 174 / 255 / \#4CAEFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / AZURE / 0 / 127 / 255 / \#007FFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / ULTRAMARINE / 0 / 63 / 255 / \#003FFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / COBALT / 0 / 71 / 171 / \#0047AB / █ / █ / █ / █ / █ / █ / █ / █ / █ / DEEP_SEA_BLUE / 0 / 38 / 153 / \#002699 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_AZURE / 45 / 91 / 229 / \#2D5BE5 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_BLUE / 0 / 0 / 139 / \#00008B / █ / █ / █ / █ / █ / █ / █ / █ / █ / BLUE / 0 / 0 / 255 / \#0000FF / █ / █ / █ / █ / █ / █ / █ / █ / █ / PERIWINKLE / 204 / 204 / 255 / \#CCCCFF / █ / █ / █ / █ / █ / █ / █ / █ / █ / SAPPHIRE / 55 / 45 / 229 / \#372DE5 / █ / █ / █ / █ / █ / █ / █ / █ / █ | LBLUE colors / Token / RGB / Hex / Palette / TAUPE_ROSE / 144 / 93 / 93 / \#905D5D / █ / █ / █ / █ / █ / █ / █ / █ / █ / PALE_BLUE / 175 / 238 / 238 / \#AFEEEE / █ / █ / █ / █ / █ / █ / █ / █ / █ / CROCUS_PURPLE / 110 / 45 / 229 / \#6E2DE5 / █ / █ / █ / █ / █ / █ / █ / █ / █ / AMETHYST / 153 / 102 / 204 / \#9966CC / █ / █ / █ / █ / █ / █ / █ / █ / █ / VIOLET / 139 / 0 / 255 / \#8B00FF / █ / █ / █ / █ / █ / █ / █ / █ / █ / MAUVE_TAUPE / 145 / 95 / 109 / \#915F6D / █ / █ / █ / █ / █ / █ / █ / █ / █ |
| MAGENTA colors / Token / RGB / Hex / Palette / CHARCOAL / 54 / 69 / 79 / \#36454F / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_VIOLET / 66 / 49 / 137 / \#423189 / █ / █ / █ / █ / █ / █ / █ / █ / █ / DARK_INDIGO / 49 / 0 / 98 / \#310062 / █ / █ / █ / █ / █ / █ / █ / █ / █ / INDIGO / 75 / 0 / 130 / \#4B0082 / █ / █ / █ / █ / █ / █ / █ / █ / █ / FOXGLOVE / 165 / 45 / 229 / \#A52DE5 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PURPLE / 102 / 0 / 153 / \#660099 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PLUM / 102 / 0 / 102 / \#660066 / █ / █ / █ / █ / █ / █ / █ / █ / █ / TAUPE_PURPLE / 80 / 64 / 77 / \#50404D / █ / █ / █ / █ / █ / █ / █ / █ / █ / EGGPLANT / 97 / 64 / 81 / \#614051 / █ / █ / █ / █ / █ / █ / █ / █ / █ / MAUVE / 153 / 51 / 102 / \#993366 / █ / █ / █ / █ / █ / █ / █ / █ / █ | LMAGENTA colors / Token / RGB / Hex / Palette / HELIOTROPE / 223 / 115 / 255 / \#DF73FF / █ / █ / █ / █ / █ / █ / █ / █ / █ / ORCHID_PINK / 229 / 91 / 195 / \#E55BC3 / █ / █ / █ / █ / █ / █ / █ / █ / █ / FUCHSIA / 244 / 0 / 161 / \#F400A1 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PUCE / 204 / 136 / 153 / \#CC8899 / █ / █ / █ / █ / █ / █ / █ / █ / █ / PINK / 255 / 192 / 203 / \#FFC0CB / █ / █ / █ / █ / █ / █ / █ / █ / █ / PALE_PINK / 250 / 218 / 221 / \#FADADD / █ / █ / █ / █ / █ / █ / █ / █ / █ |

    descriptor_color_standard

    [OBJECT:DESCRIPTOR_COLOR]

    Most of these are from Wikipedia's color list.  Palettes only support 255 colors max currently.

    [COLOR:AMBER]
        [NAME:amber]
        [WORD:AMBER]
        [RGB:255:191:0]

    [COLOR:AMETHYST]
        [NAME:amethyst]
        [WORD:AMETHYST]
        [RGB:153:102:204]

    [COLOR:AQUA]
        [NAME:aqua]
        [WORD:AQUA]
        [RGB:0:255:255]

    [COLOR:AQUAMARINE]
        [NAME:aquamarine]
        [WORD:AQUAMARINE]
        [RGB:127:255:212]

    [COLOR:ASH_GRAY]
        [NAME:ash gray]
        [WORD:GRAY]
        [RGB:178:190:181]

    [COLOR:AUBURN]
        [NAME:auburn]
        [WORD:AUBURN]
        [RGB:111:53:26]

    [COLOR:AZURE]
        [NAME:azure]
        [WORD:AZURE]
        [RGB:0:127:255]

    [COLOR:BEIGE]
        [NAME:beige]
        [WORD:BEIGE]
        [RGB:245:245:220]

    [COLOR:BLACK]
        [NAME:black]
        [WORD:BLACK]
        [RGB:0:0:0]

    [COLOR:BLUE]
        [NAME:blue]
        [WORD:BLUE]
        [RGB:0:0:255]

    [COLOR:BRASS]
        [NAME:brass]
        [WORD:BRASS]
        [RGB:181:166:66]

    [COLOR:BRONZE]
        [NAME:bronze]
        [WORD:BRONZE]
        [RGB:205:127:50]

    [COLOR:BROWN]
        [NAME:brown]
        [WORD:BROWN]
        [RGB:150:75:0]

    [COLOR:BUFF]
        [NAME:buff]
        [WORD:BUFF]
        [RGB:240:220:130]

    [COLOR:BURNT_SIENNA]
        [NAME:burnt sienna]
        [WORD:SIENNA]
        [RGB:233:116:81]

    [COLOR:BURNT_UMBER]
        [NAME:burnt umber]
        [WORD:UMBER]
        [RGB:138:51:36]

    [COLOR:CARDINAL]
        [NAME:cardinal]
        [WORD:CARDINAL_COLOR]
        [RGB:196:30:58]

    [COLOR:CARMINE]
        [NAME:carmine]
        [WORD:CARMINE]
        [RGB:150:0:24]

    [COLOR:CERULEAN]
        [NAME:cerulean]
        [WORD:CERULEAN]
        [RGB:0:123:167]

    [COLOR:CHARCOAL]
        [NAME:charcoal]
        [WORD:CHARCOAL]
        [RGB:54:69:79]

    [COLOR:CHARTREUSE]
        [NAME:chartreuse]
        [WORD:CHARTREUSE]
        [RGB:127:255:0]

    [COLOR:CHESTNUT]
        [NAME:chestnut]
        [WORD:CHESTNUT]
        [RGB:205:92:92]

    [COLOR:CHOCOLATE]
        [NAME:chocolate]
        [WORD:CHOCOLATE]
        [RGB:210:105:30]

    [COLOR:CINNAMON]
        [NAME:cinnamon]
        [WORD:CINNAMON]
        [RGB:123:63:0]

    [COLOR:CLEAR]
        [NAME:clear]
        [WORD:CLEAR]
        [RGB:128:128:128]

    [COLOR:COBALT]
        [NAME:cobalt]
        [WORD:COBALT]
        [RGB:0:71:171]

    [COLOR:COPPER]
        [NAME:copper]
        [WORD:COPPER]
        [RGB:184:115:51]

    [COLOR:CREAM]
        [NAME:cream]
        [WORD:CREAM]
        [RGB:255:253:208]

    [COLOR:CRIMSON]
        [NAME:crimson]
        [WORD:CRIMSON]
        [RGB:220:20:60]

    [COLOR:DARK_BLUE]
        [NAME:dark blue]
        [WORD:BLUE]
        [RGB:0:0:139]

    [COLOR:DARK_BROWN]
        [NAME:dark brown]
        [WORD:BROWN]
        [RGB:101:67:33]

    [COLOR:DARK_CHESTNUT]
        [NAME:dark chestnut]
        [WORD:CHESTNUT]
        [RGB:152:105:96]

    [COLOR:DARK_GREEN]
        [NAME:dark green]
        [WORD:GREEN]
        [RGB:1:50:32]

    [COLOR:DARK_INDIGO]
        [NAME:dark indigo]
        [WORD:INDIGO]
        [RGB:49:0:98]

    [COLOR:DARK_OLIVE]
        [NAME:dark olive]
        [WORD:OLIVE]
        [RGB:85:104:50]

    [COLOR:DARK_PEACH]
        [NAME:dark peach]
        [WORD:PEACH]
        [RGB:255:218:185]

    [COLOR:DARK_PINK]
        [NAME:dark pink]
        [WORD:PINK]
        [RGB:231:84:128]

    [COLOR:DARK_SCARLET]
        [NAME:dark scarlet]
        [WORD:SCARLET]
        [RGB:86:3:25]

    [COLOR:DARK_TAN]
        [NAME:dark tan]
        [WORD:TAN]
        [RGB:145:129:81]

    [COLOR:DARK_VIOLET]
        [NAME:dark violet]
        [WORD:VIOLET]
        [RGB:66:49:137]

    [COLOR:ECRU]
        [NAME:ecru]
        [WORD:ECRU]
        [RGB:194:178:128]

    [COLOR:EGGPLANT]
        [NAME:eggplant]
        [RGB:97:64:81]

    [COLOR:EMERALD]
        [NAME:emerald]
        [WORD:EMERALD]
        [RGB:80:200:120]

    [COLOR:FERN_GREEN]
        [NAME:fern green]
        [WORD:GREEN]
        [RGB:79:121:66]

    [COLOR:FLAX]
        [NAME:flax]
        [WORD:FLAX]
        [RGB:238:220:130]

    [COLOR:FUCHSIA]
        [NAME:fuchsia]
        [WORD:FUCHSIA]
        [RGB:244:0:161]

    [COLOR:GOLD]
        [NAME:gold]
        [WORD:GOLD]
        [RGB:212:175:55]

    [COLOR:GOLDEN_YELLOW]
        [NAME:golden yellow]
        [WORD:GOLD]
        [WORD:YELLOW]
        [RGB:255:223:0]

    [COLOR:GOLDENROD]
        [NAME:goldenrod]
        [WORD:GOLDENROD]
        [RGB:218:165:32]

    [COLOR:GRAY]
        [NAME:gray]
        [WORD:GRAY]
        [RGB:128:128:128]

    [COLOR:GREEN]
        [NAME:green]
        [WORD:GREEN]
        [RGB:0:255:0]

    [COLOR:GREEN-YELLOW]
        [NAME:green-yellow]
        [WORD:GREEN]
        [WORD:YELLOW]
        [RGB:173:255:47]

    [COLOR:HELIOTROPE]
        [NAME:heliotrope]
        [WORD:HELIOTROPE]
        [RGB:223:115:255]

    [COLOR:INDIGO]
        [NAME:indigo]
        [WORD:INDIGO]
        [RGB:75:0:130]

    [COLOR:IVORY]
        [NAME:ivory]
        [WORD:IVORY]
        [RGB:255:255:240]

    [COLOR:JADE]
        [NAME:jade]
        [WORD:JADE]
        [RGB:0:168:107]

    [COLOR:LAVENDER]
        [NAME:lavender]
        [WORD:LAVENDER]
        [RGB:230:230:250]

    [COLOR:LAVENDER_BLUSH]
        [NAME:lavender blush]
        [WORD:LAVENDER]
        [RGB:255:240:245]

    [COLOR:LEMON]
        [NAME:lemon]
        [WORD:LEMON]
        [RGB:253:233:16]

    [COLOR:LIGHT_BLUE]
        [NAME:light blue]
        [WORD:BLUE]
        [RGB:173:216:230]

    [COLOR:LIGHT_BROWN]
        [NAME:light brown]
        [WORD:BROWN]
        [RGB:205:133:63]

    [COLOR:LILAC]
        [NAME:lilac]
        [WORD:LILAC]
        [RGB:200:162:200]

    [COLOR:LIME]
        [NAME:lime]
        [WORD:LIME]
        [RGB:204:255:0]

    [COLOR:MAHOGANY]
        [NAME:mahogany]
        [WORD:MAHOGANY]
        [RGB:192:64:0]

    [COLOR:MAROON]
        [NAME:maroon]
        [WORD:MAROON_COLOR]
        [RGB:128:0:0]

    [COLOR:MAUVE]
        [NAME:mauve]
        [WORD:MAUVE]
        [RGB:153:51:102]

    [COLOR:MAUVE_TAUPE]
        [NAME:mauve taupe]
        [WORD:MAUVE]
        [WORD:TAUPE]
        [RGB:145:95:109]

    [COLOR:MIDNIGHT_BLUE]
        [NAME:midnight blue]
        [WORD:BLUE]
        [RGB:0:51:102]

    [COLOR:MINT_GREEN]
        [NAME:mint green]
        [WORD:GREEN]
        [RGB:152:255:152]

    [COLOR:MOSS_GREEN]
        [NAME:moss green]
        [WORD:GREEN]
        [RGB:173:223:173]

    [COLOR:OCHRE]
        [NAME:ochre]
        [WORD:OCHRE]
        [RGB:204:119:34]

    [COLOR:OLIVE]
        [NAME:olive]
        [WORD:OLIVE]
        [RGB:128:128:0]

    [COLOR:ORANGE]
        [NAME:orange]
        [WORD:ORANGE]
        [RGB:255:165:0]

    [COLOR:PALE_BLUE]
        [NAME:pale blue]
        [WORD:BLUE]
        [RGB:175:238:238]

    [COLOR:PALE_BROWN]
        [NAME:pale brown]
        [WORD:BROWN]
        [RGB:152:118:84]

    [COLOR:PALE_CHESTNUT]
        [NAME:pale chestnut]
        [WORD:CHESTNUT]
        [RGB:221:173:175]

    [COLOR:PALE_PINK]
        [NAME:pale pink]
        [WORD:PINK]
        [RGB:250:218:221]

    [COLOR:PEACH]
        [NAME:peach]
        [WORD:PEACH]
        [RGB:255:229:180]

    [COLOR:PEARL]
        [NAME:pearl]
        [WORD:PEARL]
        [RGB:240:234:214]

    [COLOR:PERIWINKLE]
        [NAME:periwinkle]
        [WORD:PERIWINKLE]
        [RGB:204:204:255]

    [COLOR:PINE_GREEN]
        [NAME:pine green]
        [WORD:GREEN]
        [WORD:PINE]
        [RGB:1:121:111]

    [COLOR:PINK]
        [NAME:pink]
        [WORD:PINK]
        [RGB:255:192:203]

    [COLOR:PLUM]
        [NAME:plum]
        [WORD:PLUM]
        [RGB:102:0:102]

    [COLOR:PUCE]
        [NAME:puce]
        [WORD:PUCE]
        [RGB:204:136:153]

    [COLOR:PUMPKIN]
        [NAME:pumpkin]
        [WORD:PUMPKIN]
        [RGB:255:117:24]

    [COLOR:PURPLE]
        [NAME:purple]
        [WORD:PURPLE]
        [RGB:102:0:153]

    [COLOR:RAW_UMBER]
        [NAME:raw umber]
        [WORD:UMBER]
        [RGB:115:74:18]

    [COLOR:RED]
        [NAME:red]
        [WORD:RED]
        [RGB:255:0:0]

    [COLOR:RED_PURPLE]
        [NAME:red-purple]
        [WORD:RED]
        [WORD:PURPLE]
        [RGB:178:0:75]

    [COLOR:ROSE]
        [NAME:rose]
        [WORD:ROSE]
        [RGB:244:194:194] went with tea rose

    [COLOR:RUSSET]
        [NAME:russet]
        [WORD:RUSSET]
        [RGB:117:90:87]

    [COLOR:RUST]
        [NAME:rust]
        [WORD:RUST]
        [RGB:183:65:14]

    [COLOR:SAFFRON]
        [NAME:saffron]
        [WORD:SAFFRON]
        [RGB:244:196:48]

    [COLOR:SCARLET]
        [NAME:scarlet]
        [WORD:SCARLET]
        [RGB:255:36:0]

    [COLOR:SEA_GREEN]
        [NAME:sea green]
        [WORD:GREEN]
        [WORD:SEA]
        [WORD:OCEAN]
        [RGB:46:139:87]

    [COLOR:SEPIA]
        [NAME:sepia]
        [WORD:SEPIA]
        [RGB:112:66:20]

    [COLOR:SILVER]
        [NAME:silver]
        [WORD:SILVER]
        [RGB:192:192:192]

    [COLOR:SKY_BLUE]
        [NAME:sky blue]
        [WORD:BLUE]
        [RGB:135:206:235]

    [COLOR:SLATE_GRAY]
        [NAME:slate gray]
        [WORD:GRAY]
        [RGB:112:128:144]

    [COLOR:SPRING_GREEN]
        [NAME:spring green]
        [WORD:GREEN]
        [RGB:0:255:127]

    [COLOR:TAN]
        [NAME:tan]
        [WORD:TAN]
        [RGB:210:180:140]

    [COLOR:TAUPE_DARK]
        [NAME:dark taupe]
        [WORD:TAUPE]
        [RGB:72:60:50]

    [COLOR:TAUPE_GRAY]
        [NAME:taupe gray]
        [WORD:TAUPE]
        [WORD:GRAY]
        [RGB:139:133:137]

    [COLOR:TAUPE_MEDIUM]
        [NAME:taupe]
        [WORD:TAUPE]
        [RGB:103:76:71]

    [COLOR:TAUPE_PURPLE]
        [NAME:purple taupe]
        [WORD:PURPLE]
        [WORD:TAUPE]
        [RGB:80:64:77]

    [COLOR:TAUPE_PALE]
        [NAME:pale taupe]
        [WORD:TAUPE]
        [RGB:188:152:126]

    [COLOR:TAUPE_ROSE]
        [NAME:rose taupe]
        [WORD:TAUPE]
        [RGB:144:93:93]

    [COLOR:TAUPE_SANDY]
        [NAME:sandy taupe]
        [WORD:TAUPE]
        [RGB:150:113:23]

    [COLOR:TEAL]
        [NAME:teal]
        [WORD:TEAL]
        [RGB:0:128:128]

    [COLOR:TURQUOISE]
        [NAME:turquoise]
        [WORD:TURQUOISE]
        [RGB:48:213:200]

    [COLOR:VERMILION]
        [NAME:vermilion]
        [WORD:VERMILION]
        [RGB:227:66:52]

    [COLOR:VIOLET]
        [NAME:violet]
        [WORD:VIOLET]
        [RGB:139:0:255]

    [COLOR:WHITE]
        [NAME:white]
        [WORD:WHITE]
        [RGB:255:255:255]

    [COLOR:YELLOW]
        [NAME:yellow]
        [WORD:YELLOW]
        [RGB:255:255:0]

    [COLOR:YELLOW_GREEN]
        [NAME:yellow-green]
        [WORD:GREEN]
        [WORD:YELLOW]
        [RGB:154:205:50]

    [COLOR:BLUE-GRAY]
        [NAME:blue-gray]
        [WORD:GRAY]
        [RGB:186:202:226]

    [COLOR:APPLE_GREEN]
        [NAME:apple green]
        [WORD:GREEN]
        [RGB:97:178:53]

    [COLOR:BRIGHT_GREEN]
        [NAME:bright green]
        [WORD:GREEN]
        [RGB:80:229:0]

    [COLOR:LEAF_GREEN]
        [NAME:leaf green]
        [WORD:GREEN]
        [RGB:25:178:17]

    [COLOR:ZESTY_GREEN]
        [NAME:zesty green]
        [WORD:GREEN]
        [RGB:55:229:45]

    [COLOR:WOODLAND_GREEN]
        [NAME:woodland green]
        [WORD:GREEN]
        [RGB:15:153:49]

    [COLOR:GRASS_GREEN]
        [NAME:grass green]
        [WORD:GREEN]
        [RGB:0:204:51]

    [COLOR:VIBRANT_GREEN]
        [NAME:vibrant green]
        [WORD:GREEN]
        [RGB:25:255:82]

    [COLOR:EUCALYPTUS]
        [NAME:eucalyptus]
        [RGB:76:153:141]

    [COLOR:SEA_FOAM]
        [NAME:sea foam]
        [RGB:25:255:220]

    [COLOR:GLACIER_BLUE]
        [NAME:glacier blue]
        [WORD:BLUE]
        [RGB:25:220:255]

    [COLOR:RIVER_BLUE]
        [NAME:river blue]
        [WORD:BLUE]
        [RGB:61:139:204]

    [COLOR:CORNFLOWER]
        [NAME:cornflower]
        [RGB:76:174:255]

    [COLOR:DEEP_SEA_BLUE]
        [NAME:deep sea blue]
        [WORD:BLUE]
        [RGB:0:38:153]

    [COLOR:DARK_AZURE]
        [NAME:dark azure]
        [WORD:AZURE]
        [RGB:45:91:229]

    [COLOR:ULTRAMARINE]
        [NAME:ultramarine]
        [RGB:0:63:255]

    [COLOR:SAPPHIRE]
        [NAME:sapphire]
        [RGB:55:45:229]

    [COLOR:CROCUS_PURPLE]
        [NAME:crocus purple]
        [RGB:110:45:229]

    [COLOR:FOXGLOVE]
        [NAME:foxglove]
        [RGB:165:45:229]

    [COLOR:ORCHID_PINK]
        [NAME:orchid pink]
        [RGB:229:91:195]

    [COLOR:RASPBERRY_PINK]
        [NAME:raspberry pink]
        [RGB:255:25:128]raspberry pink

## Color lists

*For the different colors used to represent different professions, see Skill categories.*

*For a list of the colors of items listed in the k-stocks menu, see Stocks.*

*For the colors of the various creatures, see creature*

*For the colors of status icons, see status icon*

### Material by color

For those who want to know which materials display as which color, for levers, aesthetic concerns, etc.

\

#### ASCII Mode

Color names listed and the colors shown below match the colors from default init/color.txt. To change these from the default tones, see Color scheme.

|  |  |  |  |  |
|----|----|----|----|----|
| Color | Stones | Ores | Metals | Other |
| • WHITE | Alabaster, Alunite, Borax, Calcite, Chalk, Cryolite, Dolomite, Limestone, Marble, Marcasite, Periclase, Quartzite, Rock salt, Satinspar, Selenite, Talc | Galena, Horn silver, Native aluminum, Native platinum, Native silver | Silver, Platinum, Aluminum, Fine pewter, Nickel silver, Sterling silver | Crystal glass, Feather tree, Tower-cap |
| • LGRAY | Anhydrite, Dacite, Gneiss, Granite, Phyllite, Stibnite | Bismuthinite | Nickel, Tin, Zinc, Billon, Trifle pewter |  |
| • DGRAY | Andesite, Basalt, Claystone, Chromite, Diorite, Gabbro, Graphite, Hornblende, Ilmenite, Jet, Mica, Pyrolusite, Rhyolite, Shale, Slate, Obsidian | Bituminous coal, Lignite, Magnetite, Sphalerite, Tetrahedrite | Iron, Steel, Lead, Pig iron | Black-cap |
| • BROWN | Chert, Conglomerate, Mudstone, Puddingstone, Sandstone, Schist, Siltstone | Cassiterite, Native copper | Copper, Bronze | All other aboveground trees |
| • YELLOW | Brimstone, Orpiment, Orthoclase, Saltpeter, Sylvite, Gypsum | Limonite, Native gold | Gold, Bismuth bronze, Brass, Electrum | Fungiwood |
| • RED | Bauxite, Kaolinite | Hematite |  | Blood thorn |
| • LRED | Cinnabar, Petrified wood, Realgar |  |  | Goblin-cap |
| • GREEN | Olivine, Serpentine | Malachite |  | Green glass |
| • LGREEN |  | Garnierite |  |  |
| • CYAN |  |  | Lay pewter | Clear glass, Spore tree |
| • LCYAN | Microcline | Raw adamantine | Adamantine | Ice |
| • BLUE | Kimberlite |  |  | Nether-cap |
| • LBLUE | Cobaltite |  |  |  |
| • MAGENTA | Pitchblende, Rutile |  | Black bronze | Glumprong |
| • LMAGENTA |  |  | Bismuth, Rose gold | Tunnel tube |

|  |
|----|
| "Color" in other / Languages / Dwarven / : / dakas / Elven / : / mima / Goblin / : / zon / Human / : / rusna |
