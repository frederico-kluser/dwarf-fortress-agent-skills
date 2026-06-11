# Graphics

> Fonte: [Graphics](https://dwarffortresswiki.org/index.php/Graphics) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a list of all Premium graphics tokens and basic usage, see Graphics token.*

*For a repository of all Classic tilesets used in DF, see Tileset repository.*

*For details on creating Classic tilesets, see Tileset repository.*

The **graphics** system in v50 is open-source. It is a custom solution which appears to involve compositing graphics sets directly in C++ before texmapping them to SDL. This blitting approach is software rendered and so largely doesn't use hardware acceleration on graphics cards. This system means that despite graphics sets supporting rudimentary animation, there is no traditional sprite mapping, which places extensive limits on the types of graphics that are possible. While the number of user editable graphics sets has increased significantly in v50, many game elements are still hard coded graphics sets, or using a tileset over the older style graphics from classic DF.

# Premium Graphics

*For a list of all Premium graphics tokens and basic usage, see Graphics token.*

The `[OBJECT:GRAPHICS]` object defines the use of various tile-based graphics in the game. As of version 50.01, graphics tokens have been greatly expanded to accommodate the release of the Steam & Itch premium version. This section is a basic description of how to define various types of graphics.

Making custom graphics requires multiple interacting files to function:

1.  An 8bit RGBA (sometimes called 32bit) "imagename.png" in the `\\graphics\images` folder
2.  A "tile_page_name.txt" in the `\\graphics` folder
3.  A "graphics_type_name.txt" in the `\\graphics` folder

Mods can reuse any graphics loaded ahead of them (including vanilla) by using the same tile page token.

\

## Tile Page

Tile pages link image files to a tile page token so they can be referenced by the graphics file. Just like all other Raw files, Tile Pages must be defined from within a properly named "tile_page\_.txt" file and follow:

    tile_page_

    [OBJECT:TILE_PAGE]

After the object type is defined as above, any number of tile pages can be defined according to the format below.

      [TILE_PAGE:]
         [FILE:images/imagename.png]
         [TILE_DIM::]
         [PAGE_DIM_PIXELS::]

- *tile page identifier*: The Internal ID being created for the image.
- *imagename.png*: The file name of the 8bit RGBA (sometimes called 32bit) in the `\graphics\images` folder of the mod.
- *tile x dim*: The width of each tile in pixels (usually 32, 8 for many interface elements, 96 for portrait elements, 16 for most world map elements and small gems).
- *tile y dim*: The height of each tile in pixels (usually 32, 12 for many interface elements, 96 for portrait elements, 16 for most world map elements and small gems).
- *page x dim*: The width of the image file in pixels.
- *page y dim*: The height of the image file in pixels.

For any of the other graphics tokens that refer to this defined identifier, and require position or width/height values, those values will be in multiples of these TILE_DIM values.

Known issues:

- Currently it is only recommended to use `[TILE_DIM:32:32]` other than for the above exceptions, as the game will resize other resolutions into a 32×32 tile. Depending on your zoom and interpolation settings, rescaled tiles can be subject to artefacting.
- It is important that the `[PAGE_DIM_PIXELS::]` matches the size of the referenced image exactly - as the game will stretch tile pages with a dimension larger than the actual image by inserting blank lines, and a tile page smaller than the image will cause a crash to desktop.

## Creature Graphics

*For a list of all known creature graphics tokens, see Graphics token#Creature Graphics.*.

Creature graphics are found within graphics_creature_x files (such as graphics_creature_domestic or graphics_creature_layered). All graphics files must begin with the file name, followed by the `[OBJECT:GRAPHICS]` token that tells the game that the file contains graphics definitions.

### Basic Graphics

An example of how X and Y positions are read, starting from the top left.

The most basic form of creature graphics is a single tile, defined below:

    [CREATURE_GRAPHICS:]
       [:::::]

- *condition*: The condition the creature needs to be in for this image to be displayed. Use `DEFAULT` for generic graphics.
- *creature id*: The Creature ID of the creature the graphics represent.
- *tile page identifier*: The Internal ID of the image defined in the Tile Page.
- *x position*: The x position of the graphic to be displayed in tiles counting from 0 (left→right).
- *y position*: The y position of the graphic to be displayed in tiles counting from 0 (top→bottom).
- *color type*: (optional) Uncertain function, frequently replaced with `AS_IS` in vanilla RAWs. ColorTypeEnum[1]

- *secondary condition*: (optional) An additional condition that must be satisfied for the image to be displayed.

When the condition [`[DEFAULT]`](/index.php/Graphics_token#DEFAULT "Graphics token") is used, this graphic will be displayed for the creature in all conditions unless additional, more specific conditions are also defined.

**Basic Conditions**

Different graphics can be defined for the same creature based on some properties about it. Below is a list of the most common creature conditions tokens.

|  |  |  |
|----|----|----|
| Condition | Accepts / Secondary | Description |
| [`[DEFAULT]`](/index.php/Graphics_token#DEFAULT "Graphics token") | No | The default condition that will be displayed unless overwritten by a more specific one below. |
| [`[CHILD]`](/index.php/Graphics_token#CHILD "Graphics token") | Yes | Will only be displayed if the creature is a [`[CHILD]`](/index.php/Creature_token#CHILD "Creature token") or [`[BABY]`](/index.php/Creature_token#BABY "Creature token") and is younger than one of those ages. |
| [`[ANIMATED]`](/index.php/Graphics_token#ANIMATED "Graphics token") | Yes | Displayed if the creature is raised from the dead, although it is not known how this is decided. Raised status is not related to having a syndrome with the class from [`[CONDITION_SYN_CLASS]`](/index.php/Graphics_token#CONDITION_SYN_CLASS "Graphics token") or from having [`[NOT_LIVING]`](/index.php/Creature_token#NOT_LIVING "Creature token")/[`[OPPOSED_TO_LIFE]`](/index.php/Creature_token#OPPOSED_TO_LIFE "Creature token"). |
| [`[CORPSE]`](/index.php/Graphics_token#CORPSE "Graphics token") | Yes | Displayed as soon as the creature dies. |
| [`[LIST_ICON]`](/index.php/Graphics_token#LIST_ICON "Graphics token") | Yes | Displayed in menus. Useful for large images that would extend beyond the menu boxes otherwise. |
| [`[CDI_LIST_ICON]`](/index.php/Graphics_token#CDI_LIST_ICON "Graphics token") | Yes | Displayed in interaction menus in Adventure Mode, overrides LIST_ICON when specified in a creature CAN_DO_INTERACTION using CDI:TOKEN:*token_name*. Accepts referenced *token_name* before standard secondaries\[Verify\]. |

### Caste Graphics

Creature caste graphics allow a simple alternative to Layered Graphics to represent males and females (or other castes) of a creature with different images.

    [CREATURE_CASTE_GRAPHICS::]
       [:::::]

- *caste id*: The Caste ID of the caste whose graphics are being defined.
- All other parameters are identical to basic graphics.

### Large Graphics

A 3×2 large image is rendered in the top center, with the central tile in red.

A 2×1 large image is left-justified.

The only difference between graphics for large creatures and small creatures is the addition of `LARGE_IMAGE` and additional coordinates to the line below:

       [::LARGE_IMAGE::::::]

- *LARGE_IMAGE*: This tag allows a rectangular image with multiple tiles to be defined by its upper left and lower right tiles. Valid for 1x1 - 3x2 tiles.
- *x1*: The x position of the upper left tile counting from 0 from the left of the tile page.
- *y1*: The y position of the upper left tile counting from 0 from the top of the tile page.
- *x2*: The x position of the lower right tile.
- *y2*: The y position of the lower right tile.
- All other parameters are identical to basic graphics.

Large images and small images can be used within the same `CREATURE_GRAPHICS` or `CREATURE_CASTE_GRAPHICS` definition, and in fact it is often useful to include a single tile image to act as a [`[LIST_ICON]`](/index.php/Graphics_token#LIST_ICON "Graphics token") for menus.

### Statue Graphics

Statue graphics are the generic images placed on top of a pedestal whenever a creature is the primary subject of a statue. The image is implied to occupy multiple tiles, and all examples in vanilla are 1×2 vertical rectangles. Statue graphics are defined as below:

    [STATUE_CREATURE_GRAPHICS:]
           [DEFAULT:::::]

    [STATUE_CREATURE_CASTE_GRAPHICS::]
           [DEFAULT:::::]

- *creature id*: The Creature ID the graphics represent.
- *caste id*: The Caste ID of the caste whose graphics are being defined.
- *x1*: The x position of the upper left tile counting from 0 from the left of the tile page.
- *y1*: The y position of the upper left tile counting from 0 from the top of the tile page.
- *x2*: The x position of the lower right tile.
- *y2*: The y position of the lower right tile.

The image (right) is an example of how a graphic would be aligned within the 1×2 grid. Vanilla statues customarily place the bottom row of pixels on the white line, with the gold box delineating where a 32px tall (exactly) sprite would fit. Statue graphics will be automatically recolored based on how their Color would appear in the default palette, like an item.

### Layered Graphics

Layered graphics are a method for displaying overlapping body parts, equipment, clothing, professions, hairstyles.. etc. They allow much more freedom in conditions than normal basic graphics, and they allow combinations of many graphical variations within the same creature to give your graphics more personality and display more information about the individuals. All layered graphics started as shown below:

    [CREATURE_GRAPHICS:]
        [LAYER_SET:]

- *creature id*: The Creature ID of the creature the graphics represent.
- *condition*: The condition the creature needs to be in for this set of layers to be displayed.

Once you start defining a Layer Set, you can begin adding individual layers from the bottom up to create your final image. For example, if you want to draw a helmet being worn on a head, you would define the head layer first, then define the helmet layer. Layers are defined according to this format:

    [LAYER:::::]
        []

- *layer name*: The internal name of the layer. Does not need to be unique. No known function at this time, but using a descriptive label is recommended.
- *tile page identifier*: The Internal ID of the image defined in the Tile Page.
- *x position*: The x position of the graphic to be displayed in tiles counting from 0 (left→right).
- *y position*: The y position of the graphic to be displayed in tiles counting from 0 (top→bottom).
- *LARGE_IMAGE:x1:y1:x2:y2*: (optional) Allows a multiple tile image to be displayed. Replaces :.
- *color type*: (optional) Uncertain function, frequently replaced with `AS_IS` in vanilla RAWs. ColorTypeEnum[2]

- *layer condition(s)*: One or more conditional tokens that define under what conditions the layer is displayed and how it interacts with other layers.

#### Portraits

96×96 portraitsv50.13 are shown in Adventure mode and when viewing a creature's sheet. They use the same tokens as layered graphics to display a more detailed view of a creature.

A single-layer portrait can be added to a \[CREATURE_GRAPHICS\] entry with this format:

     [LAYER_SET:PORTRAIT]
        [LAYER_GROUP]
        [LAYER:MAIN:::]
        [END_LAYER_GROUP]

See above for the explanation of each argument.

### Procedural Creature Graphics

Procedural graphics define layered graphics based on which body parts are present in each procedurally-generated forgotten beast, titan, or otherwise.

       [TILE_GRAPHICS_RECTANGLE::::::]

- *tile page identifier*: Internal ID of the image defined in Tile Page.
- *x*: The x position of the upper left tile counting from 0 from the left of the tile page.
- *y*: The y position of the upper left tile counting from 0 from the top of the tile page.
- *width*: How many tiles right the graphic spans. Usually this is 3.
- *height*: How many tiles down the graphic spans. Usually this is 2.
- *PCG layering token*: The internal ID of a procedural graphics layer, representing generated forgotten beast body types and body parts.

The `TILE_GRAPHICS_RECTANGLE` token displays a large image with the upper left corner being defined by , and the size defined by , . The PCG layering token is a conditional token that causes the graphics for each layer to be displayed only when the forgotten beast has that particular body type or part.

Humanoid experiments use `TILE_GRAPHICS` instead of `TILE_GRAPHICS_RECTANGLE`, which omits the and parameters.

The [`[PROCEDURAL_CREATURE_GRAPHICS]`](/index.php/Creature_token#PROCEDURAL_CREATURE_GRAPHICS "Creature token") token allows a creature to use the generation system for a given sprite type (which can be caste-specific), and each [`[PCG_LAYERING]`](/index.php/Creature_token#PCG_LAYERING "Creature token") entry will add that part to the assembled sprite.

## Item Graphics

Item graphics can also be defined, but are mostly hardcoded. This section of the wiki needs to be fleshed out.

## Workshop Graphics

Workshop graphics are displayed during each stage of construction and when it is completed. There are two layers, the base layer and an OVERLAY layer. The base layer shows the floor, tables, chairs and other basic features. The overlay shows various decorations that give the workshop its unique appearance.

base layer:

       [TILE_GRAPHICS::::WORKSHOP_CUSTOM::::]

overlay layer:

       [TILE_GRAPHICS::::WORKSHOP_CUSTOM_OVERLAY::::]

- *tile page identifier*: The Internal ID of the image defined in the Tile Page.
- *graphic tile x position*: The x position of the graphic in tiles counting from 0 (left→right).
- *graphic tile y position*: The y position of the graphic in tiles counting from 0 (top→bottom).
- *WORKSHOP_CUSTOM* and *WORKSHOP_CUSTOM_OVERLAY*: These tokens define the graphics as belonging to a custom workshop. These tokens do not exist in vanilla workshops except for the Soap maker and Screw press, which are used as examples for custom workshops.
- *workshop id*: The ID of the workshop defined in its raws.
- *building stage*: What building stage this graphic is displayed during.
- *workshop tile x position*: The x position of the workshop tile where the graphic is displayed counting from 0 (left→right).
- *workshop tile y position*: The y position of the workshop tile where the graphic is displayed counting from 0(top→bottom).

Note that an extra Y row is defined above the workshop. This allows for graphics that extend into the tile above the workshop.

Also note that currently custom furnaces do not properly work with premium graphics. The WORKSHOP_CUSTOM and WORKSHOP_CUSTOM_OVERLAY tokens ONLY work with custom workshops. If used with a custom furnace they give an error and the graphics will not appear in game. Custom furnaces can still be made to use graphics if they are defined as workshops in their raws.

These values can be validated by checking the RAW vanilla file `[DF Installion]\data\vanilla\vanilla_buildings_graphics\graphics\graphics_workshops.txt`

\

## World Map Graphics

World map graphics come in two variations:

       [TILE_GRAPHICS::::]
       [TILE_GRAPHICS:::::]

- *tile page identifier*: The Internal ID of the image defined in the Tile Page.
- *x position*: The x position of the graphic to be displayed in tiles counting from 0 (left→right).
- *y position*: The y position of the graphic to be displayed in tiles counting from 0 (top→bottom).
- *graphic id*: The Graphic Token of the world map tile the graphics represent.
- *variation {1 - 5}*: For Graphic IDs that allow variants.

These values can be validated by checking the RAW vanilla file `[DF Installion]\data\vanilla\vanilla_world_map\graphics\graphics_world_map.txt`

## Palettes

Palettes are used by graphics to render colorized objects. This is usually based on material colors, though arbitrary palettesv50.13 can be created and applied with [`[USE_PALETTE]`](/index.php/Graphics_token#USE_PALETTE "Graphics token").

       [PALETTE:]
           [FILE:images/imagename.png]
           [PALETTE_DEFAULT:] this is the one used in the images themselves
           [PALETTE_COLOR::]

- *name*: The Internal ID being created for the image. DEFAULT is used by most objects and requires a PALETTE_COLOR entry for each raw-defined color that exists.
- *imagename.png*: The file name of the 8bit RGBA (sometimes called 32bit) in the `\graphics\images` folder of the mod.
- *row*: The y position of the graphic to be displayed in pixels counting from 0 (top→bottom). It is customary to place the default palette at 0.
- *color*: A color token.

Each row of the vanilla palettes.png file is a palette. The PALETTE_DEFAULT row is the row of colors (aka palette) used to in the internal graphics (which are loaded by a tile page) and get replaced by the colors of one of the other rows as specified in the palette_default.txt file. It isn't shown in-game, but the exact RGB values are replaced by the row specified by `[PALETTE_COLOR]` or [`[USE_PALETTE]`](/index.php/Graphics_token#USE_PALETTE "Graphics token"). Each palette supports up to 18 colors.

Below is a set of color ramps used for vanilla graphics. The colors in the **Metal** and **Wood** columns will be replaced by the palette corresponding to the object's material color, and all other colors are off-palette and will not be colorized. **Fake Metal** is used for metallic details on non-metal objects, like the gray trim of a wooden buckler, and other ramps are used for workshop overlays. **Handle** is used throughout the game to represent brown materials, and wooden weapons are an example of how to convert it into the main palette.

**PALETTE_DEFAULT source colors**

|  |  |
|----|----|
| Metal / \#FFFFFF / \#C7C4B4 / \#A5A6A5 / \#8A9091 / \#6B7076 / \#5A5E65 / \#494C54 / \#3C3E46 / \#2F3038 | Wood / \#D7D3D2 / \#B3A59E / \#94877E / \#746A63 / \#605852 / \#564F49 / \#4E4743 / \#463E3D / \#2F3038 |

**Off-palette color ramps**

|  |  |  |  |
|----|----|----|----|
| Fake Metal / \#FFFEFF / \#CECAB9 / \#A9AAA9 / \#8B9293 / \#696F75 / \#565B62 / \#464951 / \#3F434C / \#393B44 | Fake Wood / \#D8B796 / \#B7926C / \#A57D5E / \#936850 / \#815E50 / \#6F5450 / \#5B4749 / \#473941 / \#2F3038 | Handle / \#E1CEAF / \#CDAC85 / \#B98B5B / \#9E674A / \#775653 / \#60474B / n / a / \#483743 / \#2E2A38 | Still / \#E5B076 / \#D1894A / \#BF703C / \#A35D3A / \#85534B / \#644249 / \#4B4047 / \#293945 / \#2F3038 |

# Classic Graphics

*For a list of all tile characters used in DF, see Tilesets.*

*For a chart with the default ASCII characters, see Character table.*

*For user-created creature tilesets, see Tileset repository.*

*For information about Graphic sets, see Graphic set.*

*For information on how tilesets get colored, see color.*

### General Information

Although commonly referred to as text or "ASCII"-graphics, classic DF uses a bitmap tileset\* with characters from the IBM Code Page 437, displayed with a foreground and background color picked from 16 predefined colors. Text files (and often hardcoded values) define the tile, and colors of all objects. Both color scheme and tileset can be changed (see below), and definitions that are in text files can be modified. In addition, interface text can be displayed with a TrueType font and creatures (which normally are displayed as letters) can be assigned to separate tilesets called graphic sets. The main tileset is sometimes called "character tileset", while the graphic sets are also referred to as "object tilesets".

\*except when using PRINT_MODE:TEXT

#### Tileset

The main tileset (also called 'character set' or just 'tileset') is an image in BMP or PNG format that contains the 256 different tiles, corresponding to the IBM Code Page 437, which are used to display all objects, creatures, and UI elements in game. The tiles are always arranged in a 16x16 grid, but its dimensions can be varied. You can have both square and non-square tiles, with 16x16 pixels being the most common size. Creatures are displayed as colored letters (a white 'B' is a polar bear, a brown 'd' a dog, and a grey 'c' is a cat).

As the tileset is limited to only 256 tiles, some objects share the same tile. Most notably, even with upper and lower case letters and 16 colors, a lot of creatures still look identical (goblin, goat, various gibbons, gremlin, goose, etc.). The tile for bins, up/down stairs and the cursor are the same; bags use the same tile as the symbol for "male"; and the "female" symbol shares a graphic with amulets. Roads and large rivers on the world map, minecart tracks and walls all share the same tiles as well.

Some of those can be changed in the raws and init files, and creatures can have separate graphics, but in most cases they are hardcoded.

That also can be used to categorize custom tilesets: Those that are made for and come bundled with modified raws/init files, and those that are made for and work with the default raws. Usually, the latter are more symbolic, or 'ASCII-like', while the former are often more pictographic, detailed or "pixel-arty". These sometimes are also bundled with their own creature graphics. Tilesets that are made for default raws have the advantage that you can use them immediately without any work for any new version that is released. With modified raws, you need to manually edit the new raws again, or wait for the maintainer to do that.

#### Graphic set

Graphic sets are additional tilesets used to give objects different graphics. As opposed to the main tileset, any number of tiles can be arranged in any grid configuration. Currently, DF only supports graphic sets for creatures. Every graphic set needs a corresponding text file that assigns a tile to a creature.

#### Color

In general, a tileset has white tiles with a transparent background. White pixels show the foreground color, transparent pixels (magenta pixels for .bmp) the background color. Black pixels remain black. Shades of grey, partial transparency and even colored tiles can be used for various effects. Additionally, creature graphics can be set to be displayed in the colors they're drawn in.

Otherwise, the game selects from 16 colors (the color scheme) to decide the color: which of the 16 colors the game uses depends on the color value or color token of the material/item.

\

### Installation

#### Repositories

Users of the Steam version can subscribe to mods on Steam Workshop. The wiki has repositories for tilesets, graphic sets, and color schemes. You will find more in the bay 12 graphics subforum and on DFFD. Some graphic sets and tilesets are additionally maintained on github. Often, tileset creators offer preinstalled downloads or folders you just have to drop into your DF folder and overwrite files when prompted. They usually come with installation instructions either in a readme file or in their respective forum thread. In addition, there are various launcher applications that let you install and change graphics automatically.

For manual installation of the various components, see here:

#### Tileset

Put the tileset you want to use into the data/art/ folder. Open up init.txt (in data/init/) with a text editor and change the entries FONT, FULLFONT, GRAPHICS_FONT, and GRAPHICS_FULLFONT to the filename of your new tileset.

#### Creature Graphics

Put the graphic set *into a subfolder* in raw/graphics and the corresponding text file directly in raw/graphics. If you have an active save you will have to put them into the raw folder of your save as well (data/save//raw/graphics). Finally, set GRAPHICS to YES in data/init/init.txt

#### Color Scheme

Replace colors.txt in data/init with your new colors.

### True Type Font

Replace font.ttf in data/art with your new font.

\

## See Also

- Creature token
- Syndrome
- Creature examples
