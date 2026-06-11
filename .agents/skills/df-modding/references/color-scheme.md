# Color scheme

> Fonte: [Color scheme](https://dwarffortresswiki.org/index.php/Color_scheme) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*(For a discussion of how DF displays different items, and decides which colors get altered and when, see color.)*

*Dwarf Fortress* uses **color schemes** to determine how the game will be presented during play, with the default color scheme data located in the colors.txt file, found in the `Dwarf Fortress/data/init` folder, but `prefs/colors.txt`v52.02 will override that, if it exists.

DFColorgen is a web tool to create and visualize color schemes.

## What colors show up where

A color scheme is broken down into 16 color labels:

BLACK, DGRAY

BLUE, LBLUE

GREEN, LGREEN

CYAN, LCYAN

RED, LRED

MAGENTA, LMAGENTA

BROWN, YELLOW

LGRAY, WHITE

The easiest place to see all the colors next to each other is in the units list, where the different professional categories all have their identifying colors. In that order (and with the default color values), they are...

|  |  |  |  |
|----|----|----|----|
| BLACK / background / LCYAN / current job listing / LGRAY / Miners / YELLOW / Woodworkers | WHITE / Stoneworkers / GREEN / Rangers / DGRAY / Metalsmiths / LGREEN / Jewelers | LBLUE / Craftsdwarfs / BLUE / Fishery worker / BROWN / Farmers / LRED / Engineers | MAGENTA / Administrators / CYAN / Peasants / RED / Children / LMAGENTA / Monarchs / , / deceased |

Some other color uses:

- Magma is LRED. (Magma 1 level lower than current view is RED.)
- Water is LBLUE. (Water 1 level lower than current view is BLUE.)
- Brooks are LCYAN on their surface (with water below).
- For aesthetic purposes, almost all colours can be represented in stones (with the exception of LMAGENTA, CYAN, and BLACK).
  - BLACK: The background color, which should not be used by anything.
  - DGRAY: A wide variety of stones are DGRAY, one example being gabbro.
  - BLUE: Kimberlite is the only stone that is BLUE. Nether-caps also produce BLUE wood.
  - LBLUE: Cobaltite is the only stone that is LBLUE.
  - GREEN: Olivine is GREEN, as are malachite and serpentine.
  - LGREEN: Garnierite is the only LGREEN stone.
  - CYAN: While there are no stones, spore trees are CYAN.
  - LCYAN: Microcline is an LCYAN rock. Adamantine and its ore, raw adamantine, also display in LCYAN.
  - RED: Bauxite and kaolinite are RED, as is the blood thorn tree.
  - LRED: Realgar, petrified wood, and cinnabar are LRED. Goblin-caps are also LRED.
  - MAGENTA: Rutile and pitchblende are MAGENTA, and glumprongs are MAGENTA trees.
  - LMAGENTA: No stones are LMAGENTA, but tunnel tubes are.
  - BROWN: A lot of stones are BROWN; chert is one example.
  - YELLOW: Brimstone, gypsum, orthoclase and many other stones are YELLOW, as is the fungiwood tree.
  - LGRAY: Lots of stones are LGRAY, such as granite.
  - WHITE: Many stones are WHITE, such as limestone, or rock salt. The tower-cap and feather tree both produce WHITE wood.

See color for a more complete list.

# Default Scheme

The default *Dwarf Fortress* color scheme is based off the 16 standard HTML colors, as discussed here. (Some have been renamed in DF, but the tones themselves are the same.)

These are broken up into 8 pairs, one darker, one lighter, as ordered below. When a color is flashing or a displayed tile is "dark/bright" according to the game display, these colors are the two that work "together" to create that contrast. Keep this in mind if creating a custom color scheme, as described below. (See Color for a more complete discussion.)

If you lose the default scheme and neglected to make a backup *(didn't we warn you to use "care and caution" when modding?)*, you can find the standard scheme below, without having to download DF again.

Open Dwarf Fortress/data/init/colors.txt, and copy the text as seen below over the values found at the very bottom of the file. Save that file, restart *Dwarf Fortress*, and you're set.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:32]
    [BLUE_G:125]
    [BLUE_B:241]
    [GREEN_R:162]
    [GREEN_G:220]
    [GREEN_B:52]
    [CYAN_R:113]
    [CYAN_G:187]
    [CYAN_B:176]
    [RED_R:255]
    [RED_G:17]
    [RED_B:58]
    [MAGENTA_R:167]
    [MAGENTA_G:60]
    [MAGENTA_B:213]
    [BROWN_R:215]
    [BROWN_G:155]
    [BROWN_B:45]
    [LGRAY_R:192]
    [LGRAY_G:192]
    [LGRAY_B:192]
    [DGRAY_R:160]
    [DGRAY_G:160]
    [DGRAY_B:160]
    [LBLUE_R:140]
    [LBLUE_G:102]
    [LBLUE_B:255]
    [LGREEN_R:19]
    [LGREEN_G:253]
    [LGREEN_B:101]
    [LCYAN_R:18]
    [LCYAN_G:254]
    [LCYAN_B:207]
    [LRED_R:255]
    [LRED_G:113]
    [LRED_B:17]
    [LMAGENTA_R:232]
    [LMAGENTA_G:17]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:225]
    [YELLOW_B:17]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

# Custom color schemes

Players who are not satisfied with the default color scheme can alter things to suit their aesthetic tastes. In order for any scheme changes to take effect, the "colors.txt" file must be altered and saved. This file can be found in the data/init/ directory of your *Dwarf Fortress* installation. The changes will not take effect until after you close and restart *Dwarf Fortress*.

The 16 colors are not fixed, except by their definitions in colors.txt. If you wanted to change YELLOW to something slightly brighter or darker, or more orange, or into deep purple, you can by changing the values listed under the label "YELLOW". Note that the color names are *case sensitive* - the color is "YELLOW", not "Yellow" or "yellow".

When designing a custom color, 3 "lights" of color are used: **R**ed, **G**reen, and **B**lue (RGB), on a scale of 0-255. The more light (the higher the value), the brighter the color; the less light (the lower the value), the darker. Using "light" is not the same as using "pigment" *(the standard "paint mixing" formulae we learned in school, where Magenta, Yellow, and Cyan are the 3 basic ingredients)* - M+C does not give "blue" in this format.

Since we're using Red, Green and Blue light, some form of those three colors is relatively easy to achieve - but look at examples of the other standard colors below to understand how they mix together and how to "shade" or "tint", or brighten or darken a color - or you can simply find a color below that you like and go from that, or use one of these standard RGB colors. Always use caution to avoid ending up with colors that are "too similar".

To change to a new color scheme, copy/paste a color list (or part of one or more) found below (or make your own up) over the existing scheme - don't worry, if you don't like it, the original, default scheme is listed above.

*(Note also that when posting screenshots to this wiki (and the forum boards), custom color schemes (or tilesets) can cause confusion with players who do not use those specific mixes. This wiki requests you use one of the default set-ups that come with the game to post screenshots here.)*

\

------------------------------------------------------------------------

### Pre-v50 Default Scheme

The old default color scheme from earlier versions of Dwarf Fortress, for those who prefer it.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:128]
    [GREEN_R:0]
    [GREEN_G:128]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:128]
    [CYAN_B:128]
    [RED_R:128]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:128]
    [MAGENTA_G:0]
    [MAGENTA_B:128]
    [BROWN_R:128]
    [BROWN_G:128]
    [BROWN_B:0]
    [LGRAY_R:192]
    [LGRAY_G:192]
    [LGRAY_B:192]
    [DGRAY_R:128]
    [DGRAY_G:128]
    [DGRAY_B:128]
    [LBLUE_R:0]
    [LBLUE_G:0]
    [LBLUE_B:255]
    [LGREEN_R:0]
    [LGREEN_G:255]
    [LGREEN_B:0]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:0]
    [LRED_B:0]
    [LMAGENTA_R:255]
    [LMAGENTA_G:0]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### Lee's Colour scheme

A quest to provide the optimal set of colours: all colours very easily distinguishable and earthy/natural without being washed out or too bright and garish.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:30]
    [BLUE_G:85]
    [BLUE_B:165]
    [GREEN_R:70]
    [GREEN_G:125]
    [GREEN_B:55]
    [CYAN_R:45]
    [CYAN_G:145]
    [CYAN_B:135]
    [RED_R:170]
    [RED_G:20]
    [RED_B:0]
    [MAGENTA_R:130]
    [MAGENTA_G:40]
    [MAGENTA_B:115]
    [BROWN_R:120]
    [BROWN_G:80]
    [BROWN_B:50]
    [LGRAY_R:160]
    [LGRAY_G:160]
    [LGRAY_B:160]
    [DGRAY_R:100]
    [DGRAY_G:100]
    [DGRAY_B:100]
    [LBLUE_R:90]
    [LBLUE_G:130]
    [LBLUE_B:210]
    [LGREEN_R:110]
    [LGREEN_G:180]
    [LGREEN_B:55]
    [LCYAN_R:70]
    [LCYAN_G:215]
    [LCYAN_B:195]
    [LRED_R:215]
    [LRED_G:60]
    [LRED_B:0]
    [LMAGENTA_R:210]
    [LMAGENTA_G:85]
    [LMAGENTA_B:190]
    [YELLOW_R:235]
    [YELLOW_G:180]
    [YELLOW_B:0]
    [WHITE_R:250]
    [WHITE_G:250]
    [WHITE_B:250]

\

#### Lee's Colour Scheme v2

New and Improved! All colours have been altered slightly but most notably the brown is much better, the magentas are more of a grape/bubblegum mix, the greens are brighter and less depressing, and the whole thing feels more cohesive.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:21]
    [BLACK_G:19]
    [BLACK_B:15]
    [BLUE_R:45]
    [BLUE_G:90]
    [BLUE_B:160]
    [GREEN_R:80]
    [GREEN_G:135]
    [GREEN_B:20]
    [CYAN_R:25]
    [CYAN_G:140]
    [CYAN_B:140]
    [RED_R:160]
    [RED_G:20]
    [RED_B:10]
    [MAGENTA_R:135]
    [MAGENTA_G:60]
    [MAGENTA_B:130]
    [BROWN_R:150]
    [BROWN_G:75]
    [BROWN_B:55]
    [LGRAY_R:178]
    [LGRAY_G:175]
    [LGRAY_B:172]
    [DGRAY_R:116]
    [DGRAY_G:110]
    [DGRAY_B:113]
    [LBLUE_R:105]
    [LBLUE_G:135]
    [LBLUE_B:225]
    [LGREEN_R:125]
    [LGREEN_G:185]
    [LGREEN_B:55]
    [LCYAN_R:60]
    [LCYAN_G:205]
    [LCYAN_B:190]
    [LRED_R:220]
    [LRED_G:50]
    [LRED_B:20]
    [LMAGENTA_R:190]
    [LMAGENTA_G:110]
    [LMAGENTA_B:185]
    [YELLOW_R:230]
    [YELLOW_G:170]
    [YELLOW_B:30]
    [WHITE_R:232]
    [WHITE_G:227]
    [WHITE_B:232]

\

------------------------------------------------------------------------

### "Natural" scheme

This mix softens the glaring colors of the original to earthtones.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:13]
    [BLUE_G:103]
    [BLUE_B:196]
    [GREEN_R:68]
    [GREEN_G:158]
    [GREEN_B:53]
    [CYAN_R:86]
    [CYAN_G:163]
    [CYAN_B:205]
    [RED_R:151]
    [RED_G:26]
    [RED_B:26]
    [MAGENTA_R:255]
    [MAGENTA_G:110]
    [MAGENTA_B:187]
    [BROWN_R:120]
    [BROWN_G:94]
    [BROWN_B:47]
    [LGRAY_R:185]
    [LGRAY_G:192]
    [LGRAY_B:162]
    [DGRAY_R:88]
    [DGRAY_G:83]
    [DGRAY_B:86]
    [LBLUE_R:145]
    [LBLUE_G:202]
    [LBLUE_B:255]
    [LGREEN_R:131]
    [LGREEN_G:212]
    [LGREEN_B:82]
    [LCYAN_R:176]
    [LCYAN_G:223]
    [LCYAN_B:215]
    [LRED_R:255]
    [LRED_G:34]
    [LRED_B:34]
    [LMAGENTA_R:255]
    [LMAGENTA_G:167]
    [LMAGENTA_B:246]
    [YELLOW_R:255]
    [YELLOW_G:218]
    [YELLOW_B:90]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### True Brown

Default scheme with BROWN actually being a shade of brown (rather than Olive Green). Created by Met.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:128]
    [GREEN_R:0]
    [GREEN_G:128]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:128]
    [CYAN_B:128]
    [RED_R:128]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:128]
    [MAGENTA_G:0]
    [MAGENTA_B:128]
    [BROWN_R:120]
    [BROWN_G:94]
    [BROWN_B:48]
    [LGRAY_R:192]
    [LGRAY_G:192]
    [LGRAY_B:192]
    [DGRAY_R:80]
    [DGRAY_G:80]
    [DGRAY_B:80]
    [LBLUE_R:0]
    [LBLUE_G:0]
    [LBLUE_B:255]
    [LGREEN_R:0]
    [LGREEN_G:255]
    [LGREEN_B:0]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:0]
    [LRED_B:0]
    [LMAGENTA_R:255]
    [LMAGENTA_G:0]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### Another natural scheme

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:73]
    [BLUE_G:95]
    [BLUE_B:157]
    [GREEN_R:89]
    [GREEN_G:117]
    [GREEN_B:55]
    [CYAN_R:101]
    [CYAN_G:144]
    [CYAN_B:158]
    [RED_R:146]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:165]
    [MAGENTA_G:54]
    [MAGENTA_B:101]
    [BROWN_R:138]
    [BROWN_G:105]
    [BROWN_B:59]
    [LGRAY_R:128]
    [LGRAY_G:128]
    [LGRAY_B:128]
    [DGRAY_R:80]
    [DGRAY_G:80]
    [DGRAY_B:80]
    [LBLUE_R:111]
    [LBLUE_G:138]
    [LBLUE_B:165]
    [LGREEN_R:160]
    [LGREEN_G:200]
    [LGREEN_B:82]
    [LCYAN_R:159]
    [LCYAN_G:196]
    [LCYAN_B:210]
    [LRED_R:206]
    [LRED_G:73]
    [LRED_B:1]
    [LMAGENTA_R:239]
    [LMAGENTA_G:150]
    [LMAGENTA_B:207]
    [YELLOW_R:255]
    [YELLOW_G:198]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### Higher-visibility scheme

Tired of trying to see your metalsmiths (dark grey) and fishery workers (navy blue) against a black background? This scheme "brightens" most of the colors, while trying to stay true to the original tone when possible. (Except BROWN, which is now actually "brown", not olive green.)

|  |  |
|----|----|
| BLACK \* | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN \* | LCYAN  |
| RED  | LRED \* |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE \* |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:44]
    [BLUE_G:136]
    [BLUE_B:222]
    [GREEN_R:32]
    [GREEN_G:144]
    [GREEN_B:32]
    [CYAN_R:0]
    [CYAN_G:128]
    [CYAN_B:128]
    [RED_R:176]
    [RED_G:8]
    [RED_B:8]
    [MAGENTA_R:176]
    [MAGENTA_G:56]
    [MAGENTA_B:160]
    [BROWN_R:120]
    [BROWN_G:94]
    [BROWN_B:48]
    [LGRAY_R:176]
    [LGRAY_G:176]
    [LGRAY_B:176]
    [DGRAY_R:120]
    [DGRAY_G:120]
    [DGRAY_B:120]
    [LBLUE_R:144]
    [LBLUE_G:202]
    [LBLUE_B:255]
    [LGREEN_R:66]
    [LGREEN_G:232]
    [LGREEN_B:40]
    [LCYAN_R:128]
    [LCYAN_G:224]
    [LCYAN_B:216]
    [LRED_R:255]
    [LRED_G:0]
    [LRED_B:0]
    [LMAGENTA_R:255]
    [LMAGENTA_G:84]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:236]
    [YELLOW_B:48]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

*(\* unchanged*)

Original on the left, this scheme on the right...

|  |  |
|----|----|
| DGRAY / Metalsmiths / GREEN / Rangers / BLUE / Fishery worker / LBLUE / Craftsdwarfs / BROWN / Farmers / MAGENTA / Administrators / RED / Children | DGRAY / Metalsmiths / GREEN / Rangers / BLUE / Fishery worker / LBLUE / Craftsdwarfs / BROWN / Farmers / MAGENTA / Administrators / RED / Children |

------------------------------------------------------------------------

### (Yet) Another scheme

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:32]
    [BLUE_G:48]
    [BLUE_B:144]
    [GREEN_R:48]
    [GREEN_G:144]
    [GREEN_B:32]
    [CYAN_R:32]
    [CYAN_G:128]
    [CYAN_B:144]
    [RED_R:151]
    [RED_G:26]
    [RED_B:26]
    [MAGENTA_R:112]
    [MAGENTA_G:32]
    [MAGENTA_B:144]
    [BROWN_R:144]
    [BROWN_G:112]
    [BROWN_B:48]
    [LGRAY_R:176]
    [LGRAY_G:176]
    [LGRAY_B:176]
    [DGRAY_R:112]
    [DGRAY_G:112]
    [DGRAY_B:112]
    [LBLUE_R:40]
    [LBLUE_G:56]
    [LBLUE_B:255]
    [LGREEN_R:48]
    [LGREEN_G:240]
    [LGREEN_B:32]
    [LCYAN_R:56]
    [LCYAN_G:208]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:48]
    [LRED_B:32]
    [LMAGENTA_R:208]
    [LMAGENTA_G:56]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:224]
    [YELLOW_B:32]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### True CGA Scheme

This scheme uses the genuine CGA palette, in case you're an old-school purist.

*(Note that the CGA "brown" can be difficult to distinguish from "red" unless it is immediately nearby. For a slightly more readable version, you can "cheat" and replace the* \[BROWN_G:85\] *with* \[BROWN_G:170\]. *)*

\

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:170]
    [GREEN_R:0]
    [GREEN_G:170]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:170]
    [CYAN_B:170]
    [RED_R:170]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:170]
    [MAGENTA_G:0]
    [MAGENTA_B:170]
    [BROWN_R:170]
    [BROWN_G:85]
    [BROWN_B:0]
    [LGRAY_R:170]
    [LGRAY_G:170]
    [LGRAY_B:170]
    [DGRAY_R:85]
    [DGRAY_G:85]
    [DGRAY_B:85]
    [LBLUE_R:85]
    [LBLUE_G:85]
    [LBLUE_B:255]
    [LGREEN_R:85]
    [LGREEN_G:255]
    [LGREEN_B:85]
    [LCYAN_R:85]
    [LCYAN_G:255]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:85]
    [LRED_B:85]
    [LMAGENTA_R:255]
    [LMAGENTA_G:85]
    [LMAGENTA_B:255]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:85]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### For the Chromatically Challenged

Colour blindness can result in colours being too similar, such as red and brown, so this scheme sacrifices true colour accuracy for a greater difference in hues. If you have normal colour vision, then this probably looks really weird.

\

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:192]
    [GREEN_R:0]
    [GREEN_G:128]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:112]
    [CYAN_B:144]
    [RED_R:192]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:160]
    [MAGENTA_G:0]
    [MAGENTA_B:128]
    [BROWN_R:96]
    [BROWN_G:96]
    [BROWN_B:0]
    [LGRAY_R:192]
    [LGRAY_G:192]
    [LGRAY_B:192]
    [DGRAY_R:128]
    [DGRAY_G:128]
    [DGRAY_B:128]
    [LBLUE_R:48]
    [LBLUE_G:48]
    [LBLUE_B:255]
    [LGREEN_R:0]
    [LGREEN_G:208]
    [LGREEN_B:0]
    [LCYAN_R:64]
    [LCYAN_G:208]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:48]
    [LRED_B:48]
    [LMAGENTA_R:255]
    [LMAGENTA_G:64]
    [LMAGENTA_B:208]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:64]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### Red/Green Colorblindness

A modification of the chromatically challenged color scheme above, made to the tastes of someone with Red/Green colorblindness.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:240]
    [GREEN_R:0]
    [GREEN_G:128]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:112]
    [CYAN_B:144]
    [RED_R:240]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:160]
    [MAGENTA_G:0]
    [MAGENTA_B:128]
    [BROWN_R:128]
    [BROWN_G:96]
    [BROWN_B:0]
    [LGRAY_R:208]
    [LGRAY_G:208]
    [LGRAY_B:208]
    [DGRAY_R:112]
    [DGRAY_G:112]
    [DGRAY_B:112]
    [LBLUE_R:80]
    [LBLUE_G:80]
    [LBLUE_B:255]
    [LGREEN_R:0]
    [LGREEN_G:208]
    [LGREEN_B:0]
    [LCYAN_R:64]
    [LCYAN_G:208]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:80]
    [LRED_B:80]
    [LMAGENTA_R:255]
    [LMAGENTA_G:48]
    [LMAGENTA_B:240]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:64]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### Tango Scheme

Color scheme to match Tango palette. Cyan values were missing from palette, so blue/plum values are used instead.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:46]
    [BLACK_G:52]
    [BLACK_B:54]
    [BLUE_R:32]
    [BLUE_G:74]
    [BLUE_B:135]
    [GREEN_R:78]
    [GREEN_G:154]
    [GREEN_B:6]
    [CYAN_R:117]
    [CYAN_G:80]
    [CYAN_B:123]
    [RED_R:164]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:92]
    [MAGENTA_G:53]
    [MAGENTA_B:102]
    [BROWN_R:206]
    [BROWN_G:92]
    [BROWN_B:0]
    [LGRAY_R:186]
    [LGRAY_G:189]
    [LGRAY_B:182]
    [DGRAY_R:136]
    [DGRAY_G:138]
    [DGRAY_B:133]
    [LBLUE_R:52]
    [LBLUE_G:101]
    [LBLUE_B:164]
    [LGREEN_R:138]
    [LGREEN_G:226]
    [LGREEN_B:52]
    [LCYAN_R:114]
    [LCYAN_G:159]
    [LCYAN_B:207]
    [LRED_R:239]
    [LRED_G:41]
    [LRED_B:41]
    [LMAGENTA_R:173]
    [LMAGENTA_G:127]
    [LMAGENTA_B:168]
    [YELLOW_R:252]
    [YELLOW_G:233]
    [YELLOW_B:79]
    [WHITE_R:238]
    [WHITE_G:238]
    [WHITE_B:236]

\

------------------------------------------------------------------------

### AngleWyrm's Colorset

Blues greens and brown that are easy on the eyes.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:48]
    [BLUE_G:60]
    [BLUE_B:120]
    [GREEN_R:30]
    [GREEN_G:100]
    [GREEN_B:40]
    [CYAN_R:40]
    [CYAN_G:90]
    [CYAN_B:130]
    [RED_R:164]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:92]
    [MAGENTA_G:53]
    [MAGENTA_B:102]
    [BROWN_R:120]
    [BROWN_G:80]
    [BROWN_B:50]
    [LGRAY_R:128]
    [LGRAY_G:128]
    [LGRAY_B:128]
    [DGRAY_R:72]
    [DGRAY_G:72]
    [DGRAY_B:72]
    [LBLUE_R:80]
    [LBLUE_G:100]
    [LBLUE_B:180]
    [LGREEN_R:40]
    [LGREEN_G:150]
    [LGREEN_B:50]
    [LCYAN_R:114]
    [LCYAN_G:159]
    [LCYAN_B:207]
    [LRED_R:239]
    [LRED_G:41]
    [LRED_B:41]
    [LMAGENTA_R:173]
    [LMAGENTA_G:127]
    [LMAGENTA_B:168]
    [YELLOW_R:180]
    [YELLOW_G:170]
    [YELLOW_B:60]
    [WHITE_R:238]
    [WHITE_G:238]
    [WHITE_B:236]

\

------------------------------------------------------------------------

### Putnam's Fortbent Color Scheme

A color scheme designed for closest accuracy to Homestuck's colors; no accuracy to actual in-game colors guaranteed.

|  |  |
|----|----|
| BLACK  | DGRAY (Caliborn gray tumut) |
| BLUE (Equius B100) | LBLUE (Vriska Cerulean!!!!!!!!) |
| GREEN (:33 \ | LGREEN (Calliope's blood) |
| CYAN (T3R3Z1 T34L) | LCYAN  |
| RED (aradia red) | LRED  |
| MAGENTA (eridan vviolet) | LMAGENTA (meenah purple) |
| BROWN (uHH, tAVROS BROWN) | YELLOW (yucky mu2tard yellow) |
| LGRAY (Calliope gray!) | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:0]
    [BLUE_B:86]
    [GREEN_R:65]
    [GREEN_G:102]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:130]
    [CYAN_B:130]
    [RED_R:161]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:106]
    [MAGENTA_G:0]
    [MAGENTA_B:106]
    [BROWN_R:161]
    [BROWN_G:80]
    [BROWN_B:0]
    [LGRAY_R:146]
    [LGRAY_G:146]
    [LGRAY_B:146]
    [DGRAY_R:98]
    [DGRAY_G:98]
    [DGRAY_B:98]
    [LBLUE_R:0]
    [LBLUE_G:86]
    [LBLUE_B:130]
    [LGREEN_R:0]
    [LGREEN_G:255]
    [LGREEN_B:0]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:0]
    [LRED_B:0]
    [LMAGENTA_R:119]
    [LMAGENTA_G:0]
    [LMAGENTA_B:60]
    [YELLOW_R:161]
    [YELLOW_G:161]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

------------------------------------------------------------------------

### nocpur's Color Scheme

A soft, earth-toned color scheme. Used by nocpur in screenshots of the fortress Striketrampled.

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:21]
    [BLACK_G:19]
    [BLACK_B:15]
    [BLUE_R:43]
    [BLUE_G:134]
    [BLUE_B:161]
    [GREEN_R:91]
    [GREEN_G:135]
    [GREEN_B:34]
    [CYAN_R:26]
    [CYAN_G:153]
    [CYAN_B:106]
    [RED_R:160]
    [RED_G:24]
    [RED_B:56]
    [MAGENTA_R:135]
    [MAGENTA_G:43]
    [MAGENTA_B:114]
    [BROWN_R:150]
    [BROWN_G:90]
    [BROWN_B:30]
    [LGRAY_R:178]
    [LGRAY_G:175]
    [LGRAY_B:172]
    [DGRAY_R:116]
    [DGRAY_G:110]
    [DGRAY_B:113]
    [LBLUE_R:63]
    [LBLUE_G:164]
    [LBLUE_B:184]
    [LGREEN_R:165]
    [LGREEN_G:185]
    [LGREEN_B:31]
    [LCYAN_R:34]
    [LCYAN_G:212]
    [LCYAN_B:165]
    [LRED_R:201]
    [LRED_G:30]
    [LRED_B:53]
    [LMAGENTA_R:190]
    [LMAGENTA_G:110]
    [LMAGENTA_B:185]
    [YELLOW_R:222]
    [YELLOW_G:160]
    [YELLOW_B:53]
    [WHITE_R:255]
    [WHITE_G:253]
    [WHITE_B:252]

\

------------------------------------------------------------------------

### Vherid's Color Schemes

#### Default +

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:18]
    [BLUE_G:51]
    [BLUE_B:175]
    [GREEN_R:0]
    [GREEN_G:128]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:178]
    [CYAN_B:178]
    [RED_R:107]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:128]
    [MAGENTA_G:0]
    [MAGENTA_B:128]
    [BROWN_R:118]
    [BROWN_G:94]
    [BROWN_B:0]
    [LGRAY_R:192]
    [LGRAY_G:192]
    [LGRAY_B:192]
    [DGRAY_R:80]
    [DGRAY_G:80]
    [DGRAY_B:80]
    [LBLUE_R:0]
    [LBLUE_G:114]
    [LBLUE_B:255]
    [LGREEN_R:0]
    [LGREEN_G:255]
    [LGREEN_B:0]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:255]
    [LRED_R:255]
    [LRED_G:0]
    [LRED_B:0]
    [LMAGENTA_R:209]
    [LMAGENTA_G:0]
    [LMAGENTA_B:172]
    [YELLOW_R:255]
    [YELLOW_G:255]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

#### Natural

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:27]
    [BLACK_G:18]
    [BLACK_B:9]
    [BLUE_R:32]
    [BLUE_G:50]
    [BLUE_B:150]
    [GREEN_R:30]
    [GREEN_G:100]
    [GREEN_B:40]
    [CYAN_R:16]
    [CYAN_G:120]
    [CYAN_B:115]
    [RED_R:110]
    [RED_G:20]
    [RED_B:20]
    [MAGENTA_R:133]
    [MAGENTA_G:17]
    [MAGENTA_B:171]
    [BROWN_R:100]
    [BROWN_G:64]
    [BROWN_B:42]
    [LGRAY_R:116]
    [LGRAY_G:108]
    [LGRAY_B:84]
    [DGRAY_R:70]
    [DGRAY_G:65]
    [DGRAY_B:50]
    [LBLUE_R:0]
    [LBLUE_G:120]
    [LBLUE_B:255]
    [LGREEN_R:170]
    [LGREEN_G:255]
    [LGREEN_B:0]
    [LCYAN_R:27]
    [LCYAN_G:210]
    [LCYAN_B:205]
    [LRED_R:192]
    [LRED_G:36]
    [LRED_B:36]
    [LMAGENTA_R:230]
    [LMAGENTA_G:71]
    [LMAGENTA_B:170]
    [YELLOW_R:250]
    [YELLOW_G:180]
    [YELLOW_B:10]
    [WHITE_R:220]
    [WHITE_G:220]
    [WHITE_B:220]

\

#### Warm

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:27]
    [BLACK_G:18]
    [BLACK_B:9]
    [BLUE_R:26]
    [BLUE_G:65]
    [BLUE_B:165]
    [GREEN_R:110]
    [GREEN_G:123]
    [GREEN_B:21]
    [CYAN_R:0]
    [CYAN_G:120]
    [CYAN_B:96]
    [RED_R:82]
    [RED_G:25]
    [RED_B:0]
    [MAGENTA_R:76]
    [MAGENTA_G:0]
    [MAGENTA_B:55]
    [BROWN_R:98]
    [BROWN_G:61]
    [BROWN_B:38]
    [LGRAY_R:154]
    [LGRAY_G:132]
    [LGRAY_B:109]
    [DGRAY_R:62]
    [DGRAY_G:53]
    [DGRAY_B:44]
    [LBLUE_R:0]
    [LBLUE_G:108]
    [LBLUE_B:255]
    [LGREEN_R:196]
    [LGREEN_G:219]
    [LGREEN_B:38]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:204]
    [LRED_R:192]
    [LRED_G:61]
    [LRED_B:36]
    [LMAGENTA_R:255]
    [LMAGENTA_G:32]
    [LMAGENTA_B:141]
    [YELLOW_R:255]
    [YELLOW_G:191]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:237]
    [WHITE_B:218]

\

#### Bone

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:38]
    [BLACK_G:23]
    [BLACK_B:10]
    [BLUE_R:15]
    [BLUE_G:82]
    [BLUE_B:186]
    [GREEN_R:120]
    [GREEN_G:134]
    [GREEN_B:23]
    [CYAN_R:86]
    [CYAN_G:184]
    [CYAN_B:114]
    [RED_R:132]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:124]
    [MAGENTA_G:26]
    [MAGENTA_B:96]
    [BROWN_R:104]
    [BROWN_G:75]
    [BROWN_B:58]
    [LGRAY_R:154]
    [LGRAY_G:132]
    [LGRAY_B:109]
    [DGRAY_R:65]
    [DGRAY_G:53]
    [DGRAY_B:43]
    [LBLUE_R:0]
    [LBLUE_G:138]
    [LBLUE_B:255]
    [LGREEN_R:196]
    [LGREEN_G:219]
    [LGREEN_B:38]
    [LCYAN_R:72]
    [LCYAN_G:255]
    [LCYAN_B:184]
    [LRED_R:192]
    [LRED_G:61]
    [LRED_B:36]
    [LMAGENTA_R:255]
    [LMAGENTA_G:66]
    [LMAGENTA_B:130]
    [YELLOW_R:255]
    [YELLOW_G:195]
    [YELLOW_B:34]
    [WHITE_R:252]
    [WHITE_G:250]
    [WHITE_B:208]

\

#### Mishka

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:23]
    [BLACK_G:15]
    [BLACK_B:13]
    [BLUE_R:0]
    [BLUE_G:95]
    [BLUE_B:255]
    [GREEN_R:87]
    [GREEN_G:160]
    [GREEN_B:0]
    [CYAN_R:0]
    [CYAN_G:135]
    [CYAN_B:95]
    [RED_R:186]
    [RED_G:83]
    [RED_B:0]
    [MAGENTA_R:167]
    [MAGENTA_G:36]
    [MAGENTA_B:0]
    [BROWN_R:176]
    [BROWN_G:137]
    [BROWN_B:81]
    [LGRAY_R:121]
    [LGRAY_G:100]
    [LGRAY_B:75]
    [DGRAY_R:74]
    [DGRAY_G:52]
    [DGRAY_B:46]
    [LBLUE_R:0]
    [LBLUE_G:179]
    [LBLUE_B:255]
    [LGREEN_R:192]
    [LGREEN_G:214]
    [LGREEN_B:0]
    [LCYAN_R:0]
    [LCYAN_G:255]
    [LCYAN_B:180]
    [LRED_R:234]
    [LRED_G:132]
    [LRED_B:0]
    [LMAGENTA_R:255]
    [LMAGENTA_G:67]
    [LMAGENTA_B:16]
    [YELLOW_R:228]
    [YELLOW_G:179]
    [YELLOW_B:27]
    [WHITE_R:241]
    [WHITE_G:227]
    [WHITE_B:184]

\

#### Dusk

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:10]
    [BLACK_G:10]
    [BLACK_B:10]
    [BLUE_R:4]
    [BLUE_G:81]
    [BLUE_B:140]
    [GREEN_R:93]
    [GREEN_G:109]
    [GREEN_B:6]
    [CYAN_R:12]
    [CYAN_G:79]
    [CYAN_B:76]
    [RED_R:142]
    [RED_G:40]
    [RED_B:0]
    [MAGENTA_R:131]
    [MAGENTA_G:0]
    [MAGENTA_B:52]
    [BROWN_R:235]
    [BROWN_G:136]
    [BROWN_B:0]
    [LGRAY_R:128]
    [LGRAY_G:109]
    [LGRAY_B:99]
    [DGRAY_R:48]
    [DGRAY_G:38]
    [DGRAY_B:45]
    [LBLUE_R:0]
    [LBLUE_G:176]
    [LBLUE_B:238]
    [LGREEN_R:166]
    [LGREEN_G:176]
    [LGREEN_B:0]
    [LCYAN_R:12]
    [LCYAN_G:187]
    [LCYAN_B:160]
    [LRED_R:206]
    [LRED_G:73]
    [LRED_B:1]
    [LMAGENTA_R:160]
    [LMAGENTA_G:3]
    [LMAGENTA_B:7]
    [YELLOW_R:255]
    [YELLOW_G:183]
    [YELLOW_B:77]
    [WHITE_R:242]
    [WHITE_G:247]
    [WHITE_B:230]

\

#### Sorrow

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:5]
    [BLACK_G:0]
    [BLACK_B:17]
    [BLUE_R:46]
    [BLUE_G:73]
    [BLUE_B:94]
    [GREEN_R:85]
    [GREEN_G:83]
    [GREEN_B:42]
    [CYAN_R:67]
    [CYAN_G:125]
    [CYAN_B:66]
    [RED_R:142]
    [RED_G:40]
    [RED_B:0]
    [MAGENTA_R:123]
    [MAGENTA_G:38]
    [MAGENTA_B:54]
    [BROWN_R:129]
    [BROWN_G:101]
    [BROWN_B:53]
    [LGRAY_R:135]
    [LGRAY_G:142]
    [LGRAY_B:93]
    [DGRAY_R:57]
    [DGRAY_G:42]
    [DGRAY_B:32]
    [LBLUE_R:76]
    [LBLUE_G:136]
    [LBLUE_B:158]
    [LGREEN_R:175]
    [LGREEN_G:181]
    [LGREEN_B:75]
    [LCYAN_R:121]
    [LCYAN_G:189]
    [LCYAN_B:143]
    [LRED_R:182]
    [LRED_G:73]
    [LRED_B:38]
    [LMAGENTA_R:161]
    [LMAGENTA_G:86]
    [LMAGENTA_B:66]
    [YELLOW_R:203]
    [YELLOW_G:154]
    [YELLOW_B:69]
    [WHITE_R:255]
    [WHITE_G:247]
    [WHITE_B:130]

\

#### Jade

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:17]
    [BLACK_G:11]
    [BLACK_B:9]
    [BLUE_R:46]
    [BLUE_G:73]
    [BLUE_B:94]
    [GREEN_R:108]
    [GREEN_G:107]
    [GREEN_B:37]
    [CYAN_R:92]
    [CYAN_G:99]
    [CYAN_B:58]
    [RED_R:118]
    [RED_G:42]
    [RED_B:27]
    [MAGENTA_R:174]
    [MAGENTA_G:44]
    [MAGENTA_B:59]
    [BROWN_R:114]
    [BROWN_G:85]
    [BROWN_B:57]
    [LGRAY_R:69]
    [LGRAY_G:60]
    [LGRAY_B:49]
    [DGRAY_R:42]
    [DGRAY_G:30]
    [DGRAY_B:27]
    [LBLUE_R:76]
    [LBLUE_G:136]
    [LBLUE_B:158]
    [LGREEN_R:195]
    [LGREEN_G:193]
    [LGREEN_B:61]
    [LCYAN_R:112]
    [LCYAN_G:161]
    [LCYAN_B:108]
    [LRED_R:175]
    [LRED_G:101]
    [LRED_B:47]
    [LMAGENTA_R:171]
    [LMAGENTA_G:66]
    [LMAGENTA_B:30]
    [YELLOW_R:203]
    [YELLOW_G:154]
    [YELLOW_B:69]
    [WHITE_R:219]
    [WHITE_G:214]
    [WHITE_B:156]

\

#### Dark Sand

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:2]
    [BLACK_G:1]
    [BLACK_B:16]
    [BLUE_R:4]
    [BLUE_G:81]
    [BLUE_B:140]
    [GREEN_R:93]
    [GREEN_G:109]
    [GREEN_B:6]
    [CYAN_R:12]
    [CYAN_G:79]
    [CYAN_B:76]
    [RED_R:142]
    [RED_G:40]
    [RED_B:0]
    [MAGENTA_R:131]
    [MAGENTA_G:0]
    [MAGENTA_B:52]
    [BROWN_R:114]
    [BROWN_G:89]
    [BROWN_B:58]
    [LGRAY_R:51]
    [LGRAY_G:69]
    [LGRAY_B:85]
    [DGRAY_R:17]
    [DGRAY_G:35]
    [DGRAY_B:52]
    [LBLUE_R:0]
    [LBLUE_G:176]
    [LBLUE_B:238]
    [LGREEN_R:166]
    [LGREEN_G:176]
    [LGREEN_B:0]
    [LCYAN_R:12]
    [LCYAN_G:187]
    [LCYAN_B:160]
    [LRED_R:206]
    [LRED_G:73]
    [LRED_B:1]
    [LMAGENTA_R:160]
    [LMAGENTA_G:3]
    [LMAGENTA_B:7]
    [YELLOW_R:255]
    [YELLOW_G:183]
    [YELLOW_B:77]
    [WHITE_R:230]
    [WHITE_G:245]
    [WHITE_B:247]

\

#### Matrix

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:25]
    [BLACK_G:32]
    [BLACK_B:7]
    [BLUE_R:24]
    [BLUE_G:119]
    [BLUE_B:79]
    [GREEN_R:77]
    [GREEN_G:114]
    [GREEN_B:24]
    [CYAN_R:179]
    [CYAN_G:135]
    [CYAN_B:0]
    [RED_R:118]
    [RED_G:68]
    [RED_B:11]
    [MAGENTA_R:32]
    [MAGENTA_G:70]
    [MAGENTA_B:49]
    [BROWN_R:77]
    [BROWN_G:84]
    [BROWN_B:7]
    [LGRAY_R:107]
    [LGRAY_G:111]
    [LGRAY_B:75]
    [DGRAY_R:56]
    [DGRAY_G:58]
    [DGRAY_B:38]
    [LBLUE_R:13]
    [LBLUE_G:189]
    [LBLUE_B:117]
    [LGREEN_R:136]
    [LGREEN_G:190]
    [LGREEN_B:18]
    [LCYAN_R:255]
    [LCYAN_G:204]
    [LCYAN_B:0]
    [LRED_R:185]
    [LRED_G:103]
    [LRED_B:6]
    [LMAGENTA_R:82]
    [LMAGENTA_G:127]
    [LMAGENTA_B:57]
    [YELLOW_R:185]
    [YELLOW_G:218]
    [YELLOW_B:28]
    [WHITE_R:215]
    [WHITE_G:232]
    [WHITE_B:148]

\

#### Ash

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:73]
    [BLUE_G:73]
    [BLUE_B:73]
    [GREEN_R:103]
    [GREEN_G:103]
    [GREEN_B:103]
    [CYAN_R:165]
    [CYAN_G:165]
    [CYAN_B:165]
    [RED_R:37]
    [RED_G:37]
    [RED_B:37]
    [MAGENTA_R:85]
    [MAGENTA_G:85]
    [MAGENTA_B:85]
    [BROWN_R:60]
    [BROWN_G:60]
    [BROWN_B:60]
    [LGRAY_R:142]
    [LGRAY_G:142]
    [LGRAY_B:142]
    [DGRAY_R:52]
    [DGRAY_G:52]
    [DGRAY_B:52]
    [LBLUE_R:129]
    [LBLUE_G:129]
    [LBLUE_B:129]
    [LGREEN_R:219]
    [LGREEN_G:219]
    [LGREEN_B:219]
    [LCYAN_R:247]
    [LCYAN_G:247]
    [LCYAN_B:247]
    [LRED_R:80]
    [LRED_G:80]
    [LRED_B:80]
    [LMAGENTA_R:119]
    [LMAGENTA_G:119]
    [LMAGENTA_B:120]
    [YELLOW_R:182]
    [YELLOW_G:182]
    [YELLOW_B:182]
    [WHITE_R:255]
    [WHITE_G:255]
    [WHITE_B:255]

\

#### Fields

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:12]
    [BLACK_G:8]
    [BLACK_B:17]
    [BLUE_R:39]
    [BLUE_G:68]
    [BLUE_B:92]
    [GREEN_R:107]
    [GREEN_G:104]
    [GREEN_B:25]
    [CYAN_R:62]
    [CYAN_G:116]
    [CYAN_B:102]
    [RED_R:92]
    [RED_G:37]
    [RED_B:20]
    [MAGENTA_R:98]
    [MAGENTA_G:24]
    [MAGENTA_B:5]
    [BROWN_R:141]
    [BROWN_G:85]
    [BROWN_B:11]
    [LGRAY_R:79]
    [LGRAY_G:67]
    [LGRAY_B:58]
    [DGRAY_R:52]
    [DGRAY_G:45]
    [DGRAY_B:40]
    [LBLUE_R:47]
    [LBLUE_G:172]
    [LBLUE_B:199]
    [LGREEN_R:190]
    [LGREEN_G:188]
    [LGREEN_B:39]
    [LCYAN_R:157]
    [LCYAN_G:220]
    [LCYAN_B:133]
    [LRED_R:175]
    [LRED_G:59]
    [LRED_B:20]
    [LMAGENTA_R:164]
    [LMAGENTA_G:36]
    [LMAGENTA_B:5]
    [YELLOW_R:224]
    [YELLOW_G:164]
    [YELLOW_B:3]
    [WHITE_R:235]
    [WHITE_G:222]
    [WHITE_B:198]

\

#### Heat

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:23]
    [BLACK_G:10]
    [BLACK_B:10]
    [BLUE_R:57]
    [BLUE_G:75]
    [BLUE_B:69]
    [GREEN_R:125]
    [GREEN_G:111]
    [GREEN_B:16]
    [CYAN_R:81]
    [CYAN_G:122]
    [CYAN_B:78]
    [RED_R:110]
    [RED_G:44]
    [RED_B:12]
    [MAGENTA_R:116]
    [MAGENTA_G:30]
    [MAGENTA_B:3]
    [BROWN_R:156]
    [BROWN_G:92]
    [BROWN_B:7]
    [LGRAY_R:98]
    [LGRAY_G:74]
    [LGRAY_B:40]
    [DGRAY_R:71]
    [DGRAY_G:52]
    [DGRAY_B:27]
    [LBLUE_R:66]
    [LBLUE_G:176]
    [LBLUE_B:182]
    [LGREEN_R:199]
    [LGREEN_G:192]
    [LGREEN_B:26]
    [LCYAN_R:170]
    [LCYAN_G:222]
    [LCYAN_B:108]
    [LRED_R:186]
    [LRED_G:66]
    [LRED_B:12]
    [LMAGENTA_R:176]
    [LMAGENTA_G:42]
    [LMAGENTA_B:3]
    [YELLOW_R:228]
    [YELLOW_G:168]
    [YELLOW_B:1]
    [WHITE_R:238]
    [WHITE_G:224]
    [WHITE_B:181]

\

#### Lazer

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:9]
    [BLACK_G:9]
    [BLACK_B:0]
    [BLUE_R:0]
    [BLUE_G:51]
    [BLUE_B:33]
    [GREEN_R:136]
    [GREEN_G:109]
    [GREEN_B:35]
    [CYAN_R:8]
    [CYAN_G:131]
    [CYAN_B:19]
    [RED_R:98]
    [RED_G:32]
    [RED_B:11]
    [MAGENTA_R:74]
    [MAGENTA_G:13]
    [MAGENTA_B:2]
    [BROWN_R:132]
    [BROWN_G:78]
    [BROWN_B:6]
    [LGRAY_R:56]
    [LGRAY_G:64]
    [LGRAY_B:35]
    [DGRAY_R:41]
    [DGRAY_G:39]
    [DGRAY_B:1]
    [LBLUE_R:40]
    [LBLUE_G:112]
    [LBLUE_B:53]
    [LGREEN_R:239]
    [LGREEN_G:193]
    [LGREEN_B:64]
    [LCYAN_R:35]
    [LCYAN_G:202]
    [LCYAN_B:55]
    [LRED_R:175]
    [LRED_G:59]
    [LRED_B:20]
    [LMAGENTA_R:165]
    [LMAGENTA_G:33]
    [LMAGENTA_B:2]
    [YELLOW_R:233]
    [YELLOW_G:171]
    [YELLOW_B:3]
    [WHITE_R:204]
    [WHITE_G:239]
    [WHITE_B:115]

\

#### Mud

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:32]
    [BLACK_G:30]
    [BLACK_B:21]
    [BLUE_R:35]
    [BLUE_G:67]
    [BLUE_B:83]
    [GREEN_R:119]
    [GREEN_G:113]
    [GREEN_B:54]
    [CYAN_R:68]
    [CYAN_G:84]
    [CYAN_B:21]
    [RED_R:137]
    [RED_G:54]
    [RED_B:14]
    [MAGENTA_R:132]
    [MAGENTA_G:103]
    [MAGENTA_B:34]
    [BROWN_R:92]
    [BROWN_G:79]
    [BROWN_B:40]
    [LGRAY_R:78]
    [LGRAY_G:85]
    [LGRAY_B:55]
    [DGRAY_R:50]
    [DGRAY_G:55]
    [DGRAY_B:35]
    [LBLUE_R:48]
    [LBLUE_G:121]
    [LBLUE_B:143]
    [LGREEN_R:173]
    [LGREEN_G:164]
    [LGREEN_B:94]
    [LCYAN_R:118]
    [LCYAN_G:139]
    [LCYAN_B:32]
    [LRED_R:188]
    [LRED_G:74]
    [LRED_B:19]
    [LMAGENTA_R:204]
    [LMAGENTA_G:160]
    [LMAGENTA_B:54]
    [YELLOW_R:251]
    [YELLOW_G:166]
    [YELLOW_B:18]
    [WHITE_R:255]
    [WHITE_G:252]
    [WHITE_B:227]

\

#### Fallen

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:32]
    [BLACK_G:30]
    [BLACK_B:21]
    [BLUE_R:35]
    [BLUE_G:67]
    [BLUE_B:83]
    [GREEN_R:119]
    [GREEN_G:113]
    [GREEN_B:54]
    [CYAN_R:63]
    [CYAN_G:82]
    [CYAN_B:43]
    [RED_R:106]
    [RED_G:39]
    [RED_B:19]
    [MAGENTA_R:104]
    [MAGENTA_G:23]
    [MAGENTA_B:8]
    [BROWN_R:92]
    [BROWN_G:79]
    [BROWN_B:40]
    [LGRAY_R:78]
    [LGRAY_G:85]
    [LGRAY_B:55]
    [DGRAY_R:50]
    [DGRAY_G:55]
    [DGRAY_B:35]
    [LBLUE_R:48]
    [LBLUE_G:121]
    [LBLUE_B:143]
    [LGREEN_R:239]
    [LGREEN_G:193]
    [LGREEN_B:64]
    [LCYAN_R:115]
    [LCYAN_G:125]
    [LCYAN_B:38]
    [LRED_R:178]
    [LRED_G:76]
    [LRED_B:21]
    [LMAGENTA_R:181]
    [LMAGENTA_G:42]
    [LMAGENTA_B:11]
    [YELLOW_R:251]
    [YELLOW_G:166]
    [YELLOW_B:18]
    [WHITE_R:244]
    [WHITE_G:255]
    [WHITE_B:208]

\

------------------------------------------------------------------------

### Koumakan's Color Schemes

KMK Systems color schemes can be found at http://www.bay12forums.com/smf/index.php?topic=169671.0.

#### Soyuz

"The colorscheme shown is my Soyuz colorscheme I made for one of Taffer's more experimental variants of his tileset, check his stuff out if you haven't, it's easily one of the best ASCII sets for DF."

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:40]
    [BLACK_G:17]
    [BLACK_B:0]
    [BLUE_R:46]
    [BLUE_G:73]
    [BLUE_B:94]
    [GREEN_R:51]
    [GREEN_G:49]
    [GREEN_B:0]
    [CYAN_R:82]
    [CYAN_G:127]
    [CYAN_B:57]
    [RED_R:124]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:119]
    [MAGENTA_G:106]
    [MAGENTA_B:54]
    [BROWN_R:124]
    [BROWN_G:84]
    [BROWN_B:52]
    [LGRAY_R:185]
    [LGRAY_G:135]
    [LGRAY_B:100]
    [DGRAY_R:74]
    [DGRAY_G:50]
    [DGRAY_B:38]
    [LBLUE_R:76]
    [LBLUE_G:136]
    [LBLUE_B:158]
    [LGREEN_R:86]
    [LGREEN_G:87]
    [LGREEN_B:27]
    [LCYAN_R:163]
    [LCYAN_G:185]
    [LCYAN_B:52]
    [LRED_R:219]
    [LRED_G:39]
    [LRED_B:0]
    [LMAGENTA_R:239]
    [LMAGENTA_G:193]
    [LMAGENTA_B:64]
    [YELLOW_R:255]
    [YELLOW_G:154]
    [YELLOW_B:10]
    [WHITE_R:255]
    [WHITE_G:240]
    [WHITE_B:173]

\

#### Bonsai

"These colors are based off of Cyprinodon's work that you can see HERE I really liked his color scheme at the time and made a handful of tweaks years ago to try some things out while still keeping the original BG color."

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:46]
    [BLACK_G:0]
    [BLACK_B:24]
    [BLUE_R:4]
    [BLUE_G:67]
    [BLUE_B:183]
    [GREEN_R:7]
    [GREEN_G:111]
    [GREEN_B:41]
    [CYAN_R:29]
    [CYAN_G:150]
    [CYAN_B:97]
    [RED_R:113]
    [RED_G:0]
    [RED_B:0]
    [MAGENTA_R:128]
    [MAGENTA_G:35]
    [MAGENTA_B:78]
    [BROWN_R:114]
    [BROWN_G:78]
    [BROWN_B:47]
    [LGRAY_R:176]
    [LGRAY_G:127]
    [LGRAY_B:90]
    [DGRAY_R:68]
    [DGRAY_G:48]
    [DGRAY_B:37]
    [LBLUE_R:0]
    [LBLUE_G:153]
    [LBLUE_B:240]
    [LGREEN_R:39]
    [LGREEN_G:236]
    [LGREEN_B:72]
    [LCYAN_R:42]
    [LCYAN_G:255]
    [LCYAN_B:152]
    [LRED_R:211]
    [LRED_G:40]
    [LRED_B:0]
    [LMAGENTA_R:229]
    [LMAGENTA_G:89]
    [LMAGENTA_B:165]
    [YELLOW_R:255]
    [YELLOW_G:162]
    [YELLOW_B:0]
    [WHITE_R:255]
    [WHITE_G:239]
    [WHITE_B:160]

\

#### Gordon

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:21]
    [BLACK_G:15]
    [BLACK_B:10]
    [BLUE_R:25]
    [BLUE_G:58]
    [BLUE_B:145]
    [GREEN_R:51]
    [GREEN_G:75]
    [GREEN_B:14]
    [CYAN_R:8]
    [CYAN_G:196]
    [CYAN_B:159]
    [RED_R:85]
    [RED_G:15]
    [RED_B:10]
    [MAGENTA_R:86]
    [MAGENTA_G:46]
    [MAGENTA_B:115]
    [BROWN_R:98]
    [BROWN_G:76]
    [BROWN_B:1]
    [LGRAY_R:104]
    [LGRAY_G:76]
    [LGRAY_B:60]
    [DGRAY_R:50]
    [DGRAY_G:35]
    [DGRAY_B:15]
    [LBLUE_R:37]
    [LBLUE_G:149]
    [LBLUE_B:207]
    [LGREEN_R:136]
    [LGREEN_G:201]
    [LGREEN_B:34]
    [LCYAN_R:127]
    [LCYAN_G:232]
    [LCYAN_B:181]
    [LRED_R:239]
    [LRED_G:58]
    [LRED_B:12]
    [LMAGENTA_R:160]
    [LMAGENTA_G:58]
    [LMAGENTA_B:158]
    [YELLOW_R:255]
    [YELLOW_G:162]
    [YELLOW_B:0]
    [WHITE_R:239]
    [WHITE_G:216]
    [WHITE_B:161]

\

------------------------------------------------------------------------

### Monokai

|  |  |
|----|----|
| BLACK  | DGRAY  |
| BLUE  | LBLUE  |
| GREEN  | LGREEN  |
| CYAN  | LCYAN  |
| RED  | LRED  |
| MAGENTA  | LMAGENTA  |
| BROWN  | YELLOW  |
| LGRAY  | WHITE  |

    colors.txt

    [BLACK_R:0]
    [BLACK_G:0]
    [BLACK_B:0]
    [BLUE_R:122]

---
*Parte 1 de 2 de «Color scheme». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Color_scheme*
