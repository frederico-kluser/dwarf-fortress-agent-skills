# Color scheme

> Fonte: [Color scheme](https://dwarffortresswiki.org/index.php/Color_scheme) — Dwarf Fortress Wiki (GFDL/MIT)

*(For a discussion of how DF displays different items, and decides which colors get altered and when, see color.)*

*Dwarf Fortress* uses **color schemes** to determine how the game will be presented during play, whether a ranger will appear bright Spring green or dark forest green, or whether microcline will be "eye-blasting blue" or something more calm. The default scheme is quite bold - other schemes are easily possible, even to better accommodate those of us with problems seeing standard color mixes, or just can't take "eye-blasting blue".

A color scheme is broken down into 16 color labels:

BLACK, DGRAY

BLUE, LBLUE

GREEN, LGREEN

CYAN, LCYAN

RED, LRED

MAGENTA, LMAGENTA

BROWN, YELLOW

LGRAY, WHITE

The color scheme data is located in the colors.txt file, found in the *Dwarf Fortress/data/init* folder.

DFColorgen is a web tool to create and visualize color schemes.

## What colors show up where

The easiest place to see all the colors next to each other is in the nits list, where the different professional categories all have their identifying colors. In that order (and with the default color values), they are...

[TABLE]

*(\* "On Break" is displayed in CYAN.)*

Some other color uses:

- Magma is LRED. (Magma 1 level lower than current view is RED.)
- Water is LBLUE. (Water 1 level lower than current view is BLUE.)
- Rivers and brooks are LCYAN on their surface (with water below).
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

# Custom color schemes

Players who are not satisfied with the default color scheme can alter things to suit their aesthetic tastes. In order for any scheme changes to take effect, the "colors.txt" file must be altered and saved. This file can be found in the data/init/ directory of your *Dwarf Fortress* installation. The changes will not take effect until after you close and restart *Dwarf Fortress*.

The 16 colors are not fixed, except by their definitions in colors.txt. If you wanted to change YELLOW to something slightly brighter or darker, or more orange, or into deep purple, you can by changing the values listed under the label "YELLOW". Note that the color names are *case sensitive* - the color is "YELLOW", not "Yellow" or "yellow".

When designing a custom color, 3 "lights" of color are used: **R**ed, **G**reen, and **B**lue (RGB), on a scale of 0-255. The more light (the higher the value), the brighter the color; the less light (the lower the value), the darker. Using "light" is not the same as using "pigment" *(the standard "paint mixing" formulae we learned in school, where Magenta, Yellow, and Cyan are the 3 basic ingredients)* - M+C does not give "blue" in this format.

Since we're using Red, Green and Blue light, some form of those three colors is relatively easy to achieve - but look at examples of the other standard colors below to understand how they mix together and how to "shade" or "tint", or brighten or darken a color - or you can simply find a color below that you like and go from that, or use one of these standard RGB colors. Always use caution to avoid ending up with colors that are "too similar".

To change to a new color scheme, copy/paste a color list (or part of one or more) found below (or make your own up) over the existing scheme - don't worry, if you don't like it, the original, default scheme is listed above.

*(Note also that when posting screenshots to this wiki (and the forum boards), custom color schemes (or tilesets) can cause confusion with players who do not use those specific mixes. This wiki requests you use one of the default set-ups that come with the game to post screenshots here.)*

------------------------------------------------------------------------

### Pre-v50 Default Scheme

The old default color scheme from earlier versions of Dwarf Fortress, for those who prefer it.

------------------------------------------------------------------------

### Lee's Colour scheme

A quest to provide the optimal set of colours: all colours very easily distinguishable and earthy/natural without being washed out or too bright and garish.

#### Lee's Colour Scheme v2

New and Improved! All colours have been altered slightly but most notably the brown is much better, the magentas are more of a grape/bubblegum mix, the greens are brighter and less depressing, and the whole thing feels more cohesive.

------------------------------------------------------------------------

### "Natural" scheme

This mix softens the glaring colors of the original to earthtones.

------------------------------------------------------------------------

### True Brown

Default scheme with BROWN actually being a shade of brown (rather than Olive Green). Created by Met.

------------------------------------------------------------------------

### Another natural scheme

------------------------------------------------------------------------

### Higher-visibility scheme

Tired of trying to see your metalsmiths (dark grey) and fishery workers (navy blue) against a black background? This scheme "brightens" most of the colors, while trying to stay true to the original tone when possible. (Except BROWN, which is now actually "brown", not olive green.)

*(\* unchanged*)

Original on the left, this scheme on the right...

[TABLE]

------------------------------------------------------------------------

### (Yet) Another scheme

------------------------------------------------------------------------

### True CGA Scheme

This scheme uses the genuine CGA palette, in case you're an old-school purist.

*(Note that the CGA "brown" can be difficult to distinguish from "red" unless it is immediately nearby. For a slightly more readable version, you can "cheat" and replace the* \[BROWN_G:85\] *with*\[BROWN_G:170\]. *)*

------------------------------------------------------------------------

### For the Chromatically Challenged

Colour blindness can result in colours being too similar, such as red and brown, so this scheme sacrifices true colour accuracy for a greater difference in hues. If you have normal colour vision, then this probably looks really weird.

------------------------------------------------------------------------

### Red/Green Colorblindness

A modification of the chromatically challenged color scheme above, made to the tastes of someone with Red/Green colorblindness.

------------------------------------------------------------------------

### Tango Scheme

Color scheme to match Tango palette. Cyan values were missing from palette, so blue/plum values are used instead.

------------------------------------------------------------------------

### AngleWyrm's Colorset

Blues greens and brown that are easy on the eyes.

------------------------------------------------------------------------

### Putnam's Fortbent Color Scheme

A color scheme designed for closest accuracy to Homestuck's colors; no accuracy to actual in-game colors guaranteed.

------------------------------------------------------------------------

### Vherid's Color Schemes

#### Default +

#### Natural

#### Warm

#### Bone

#### Mishka

#### Dusk

#### Sorrow

#### Jade

#### Dark Sand

#### Matrix

#### Ash

#### Fields

#### Heat

#### Lazer

#### Mud

#### Fallen

------------------------------------------------------------------------

### Monokai

------------------------------------------------------------------------

### Qud

A color scheme based on the game Caves of Qud. Original by Corporal_Klinger on the DF forums, modified for visibility by Mabelmabel on the CoQ discord.

------------------------------------------------------------------------

### Solarized

Based on Ethan Schoonover's syntax highlighting color scheme. Designed to be easily distinguishable and visible colors that also reduce eye strain and fatigue.

------------------------------------------------------------------------

### elementary

### Pseudo Naturalistic Color Scheme

Natural colours based on classic colours. Designed for Ironhand tileset and DF2014 (see discussion) but looks nice with ASCII too. Created by Harmonica.

This particularly works well with Ironhand due to the colour blending (nice minerals and plants), and also works nicely with the new trees.

------------------------------------------------------------------------

### CowThing's color schemes

This color scheme is for a softer, happier game. Colors were chosen for easy visibility and to be easy on the eyes.

A darker version of the above color scheme.

## Snackfox's color scheme

This color scheme was designed to be light, pretty, and easy on the eyes, with an emphasis on purples and blues.

------------------------------------------------------------------------

## Runeset Mapmaker

This color scheme was designed to work with Runeset to produce beautiful sepia toned fantasy maps.

## Runeset

A more playable version of Runeset Mapmaker that doesn't make every embark site look like the desert. It's a milder toned scheme with decent contrast.

------------------------------------------------------------------------

## Kyzer's Themes

### Kyzer's Light Scheme

A light color scheme meant to be easy on the eyes using yellows and relatively low contrast colors. **Note: cyan is now purple!**

### Kyzer's 'true color' Scheme

A high brightness color scheme with a lot of contrast, base colors (RED and BLUE, for example) are the most saturated and brightest they can be. Light colors are actually light versions of the previous colors now.

### Kyzer's Low Contrast Scheme

A low contrast, dark theme which prevents your eyes from having issues focusing because of overly bright tones. Basically, it has the same effect of turning your monitor down, without turning it down.

## Zippy's Themes

### Zippy's Vibrant

Colors here are designed to be much softer, richer and brighter than the game's default colors. Most colors are very slightly dimmed as to appear less over saturated than the original color scheme, but still manage to show as unique and vibrant colors.

### Zippy's Low Contrast

An alternate color scheme where the colors - as the title would denote - have less contrast, as all the colors are much closer to their counterparts. This color scheme may be hard to see on a darker monitor.
