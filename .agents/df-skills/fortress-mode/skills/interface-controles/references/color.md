# Color

> Fonte: [Color](https://dwarffortresswiki.org/index.php/Color) — Dwarf Fortress Wiki (GFDL/MIT)

*Dwarf Fortress* can use roughly 8424 **colors** to give many tiles such as foregrounds, backgrounds and sprites different colors. These colors make up the color scheme. Which of these colors are assigned to a given tile is often decided by values in its raw file. Whether a pixel shows foreground, background, black or anything in between is influenced by its brightness and opacity. These colors are shown at the right:

The original game used a simplistic 16-color palette, with 8 of those colors: black, blue, green, cyan, red, purple, yellow, grey, and a lighter version of those colors creating a total of 16. The game also has an option to use the classic ASCII visuals, mimicking the classic version of the game by using 16 colors. Even with the updated graphics turned on, the text in the GUI still references the color scheme. Color is also used to express various information, from a dwarf's profession, to the natural color of a terrain feature, to the material an item is made of.

Some sprite sheets contain their own dedicated color palettes.

## Overview

### The tileset influences color display

In the simplest case, a pixel on a tileset is either white (foreground) or transparent\* (background). However, black, and anything in between is possible as well (even color):

- a white pixel will show the foreground color
- a transparent\* pixel will show the background color
- a black pixel will stay black

The darker a white pixel is (i.e. a shade of gray), the darker the foreground color will be displayed. Similarly, a black pixel with lower opacity will result in a darker background color. A partially transparent, non-black pixel shows both the background and foreground color.

\*magenta for .bmp files.

### Colors are assigned based on material and other raw values

To decide which colors to use for a tile in ASCII mode, DF looks at raw values for that object (color value or color token) and selects a foreground and background color from the 16 colors in the color scheme. When a color value is defined, it directly picks it from the 16. When instead a color token is defined, the game compares the color token definition to all 16 colors in the color scheme and picks the closest match.

For tiles in graphics mode, it instead uses a raw-defined palette. The default palette image is shown above. It checks for each color in the row defined by the PALETTE_DEFAULT token--in this case, the first row--and then maps it to the corresponding color in the same column, based on the STATE_COLOR of the object that the tile being printed corresponds to. For the vanilla raws, this is all in alphabetical order. New palettes and colors can be defined in the same way.

## How colors are assigned

Colors of Status icons, professions, text and the interface in general are hardcoded. Items, furniture, constructions, and geographic features get the color of their material. Dyes and material contaminants use color tokens.

### Wall and floor color

While the foreground, background and brightness shown in the RAW files will be applied to walls, the mineral's "secondary" color will end up different. Here is how it works:

- If the BASIC_COLOR tag is specified, it will use that color. Note that the BASIC_COLOR tag only has foreground and brightness as arguments.
- If BASIC_COLOR is left out:
  - The background color is forced to 0 (effectively stripping it).
  - If the foreground color is 0, the game will display it as dark gray, color 8 (in other words, color 0 with brightness 1).

This is effective for stairs, floors, ramps, and constructions (in the case of stone). When stone is engraved, it uses the material's TILE_COLOR (which is the same as the DISPLAY_COLOR unless overridden).

### Color values

Colors are primarily defined using the \[COLOR:x:y:z\] or \[DISPLAY_COLOR:x:y:z\] tokens. The three arguments are:

1.  Foreground color \[0-7\]
2.  Background color \[0-7\]
3.  Brightness of the foreground color \[0 or 1\]

The brightness of the background color is always 0.

By default\*, the following 8 pairs of colors are displayed. These are bright and dark shades of the primary colors, as well as black, white, and two grays:

[TABLE]

*(\* See color scheme for information about how to change the actual various colors as displayed.)*

Sometimes the color numbers are part of another token, e.g. `[LEAVES:quarry bush leaf:quarry bush leaves:6:7:0:0:0:0:1:LOCAL_PLANT_MAT:LEAF]` specifies the colors "7:0:0" for quarry bush leaves and "0:0:1" for wilted quarry bush leaves.

#### Values 8-15

If the brightness value is 1 or another nonzero number, it adds 8 to the foreground color. If the final value of the foreground or background is 8-15, it appears as a "bright" color.

As these values can be manually typed in instead of using the brightness value, you can also give the background a bright color with this method. For example, for a white background color, add 8 to 7 = 15. For a light green background color, you add 8 to 2 = 10.

### Color tokens

When in graphics mode, most things do not use color flags. Instead, they reference color tokens defined in descriptor_color_standard.txt. Color tokens are referenced by their token name, e.g. `[STATE_COLOR:SOLID:DARK_GREEN]` or `[POWDER_DYE:EMERALD]`. The defined RGB values are not displayed in-game; instead, it assigns colors in the sprite from the top row of the palette file (seen above) to the row defined in data/vanilla/vanilla_descriptors_graphics/graphics/palette_default.txt, or any user-defined palette objects.

The following colors are grouped according to their corresponding display color in ASCII mode. Hexadecimal color values are not used in the raws, but correspond to the RGB values that are. For further information, see the Wikipedia article on web colors.

[TABLE]

## Color lists

*For the different colors used to represent different professions, see Skill categories.*

*For a list of the colors of items listed in the -stocks menu, see Stocks.*

*For the colors of the various creatures, see creature*

*For the colors of status icons, see status icon*

### Material by color

For those who want to know which materials display as which color, for levers, aesthetic concerns, etc.

#### ASCII Mode

Color names listed and the colors shown below match the colors from default init/color.txt. To change these from the default tones, see Color scheme.

[TABLE]
