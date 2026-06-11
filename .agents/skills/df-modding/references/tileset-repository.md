# Tileset repository

> Fonte: [Tileset repository](https://dwarffortresswiki.org/index.php/Tileset_repository) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

*For user-created graphic sets, see Graphics set repository.*

A character set, or simply tileset, is an image in BMP or PNG format that contains the 256 different tiles, corresponding to the IBM Code Page 437 (sometimes called Extended ASCII). They are used to display the text elements in graphics mode and everything in ASCII mode. This page serves as a repository for custom tilesets made by users, including instructions on how to install them.

## Background

The default tilesets (640×300 and 800×600) render 8×12 and 10×12 characters respectively, with majuscule latin letters occupying a 7×9 box, and appear broadly similar to the IBM MDA font based on the shape of the "0", "g", and "f" characters (but with slight differences including the "0", "W", and "y"). The exact origin of the DF font is unknown.

## Installation

**Currently, using some tilesets can cause the lower and right edges of the screen to not react to the mouse.**Bug:13462 This is dependent on size; the 8×12 and 10×12 that come with the game are fine, but the 16×16 is not. Maximizing the window or setting the game to fullscreen may avoid this.

Other issues that can appear when using a different tileset:

- In graphics mode, the minimap frame will scale to the tileset, but the minimap image will not.
- In graphics mode, using a tileset with a different aspect ratio will stretch UI elements.
- In graphics mode, some UI elements do not scale to the tileset.
- In either mode, and even with the default tileset at some scales and game display sizes, some menus may not have enough space to display all elements; the Nobles menu especially.

To use a specific tileset with *Dwarf Fortress*, you must perform the following steps:

1.  Download the tileset to your computer. Each tileset is just an image, so there is no separate download link. (**Right-Click** on the tileset image and **Save-As**.) Alternatively, export a BMP from Fontraption.
2.  If necessary, convert the tileset to the correct image format for the version of DF you are using:
    1.  Under **ANY** circumstances, you **MUST NOT** just change the extension to .bmp or .png or the tileset will be unusable, because the extension is changed, but not the file header and encoding. You **MUST** use a program like MS Paint to save it properly.
    2.  For *DF 0.28.181.40d or older:* open the file in an image editor and save it as a **24-bit bitmap** (BMP) if it isn't already in that format.
    3.  For *DF 0.31.01 or newer:* open the file in an image editor and save it as a **PNG** with *transparency* if it isn't already in that format.
3.  Move or copy the file to the DF art directory (`data/art`), which is in the game installation folder.
    1.  Alternatively, depending on the the portable mode setting, files in the *Local User*`/data/art` folder will override the files in the installation folder.
4.  Edit the `data/init/init_default.txt` file to specify the tileset file to use. There are three lines that can be changed:
    1.  **\[FONT:\]** — the tileset for a windowed display.
    2.  **\[FULLFONT:\]** — the tileset for a full-screen display.
    3.  **\[BASIC_FONT:\]** — the tileset for initial loading and menu display.
    4.  All three can be set to the same file. In fact, setting them to different files can give unexpected results.
    5.  Once you have made the changes you need to remember to save the file.
5.  If the selected tileset requires modifications to the Raws, you will have to make those edits. What those changes are will depend on the tileset itself, and may only be valid for older versions. Likewise, some tilesets may suggest changes to `d_init.txt`, such as `[PILLAR_TILE:255]`, but those options, sadly, no longer exist.

Once the file is saved and the required changes are made, you are ready to play DF with your new tileset! The game does not save these FONT options in `prefs/init.txt`, so adding them there will only be temporary.

# Square tilesets

## 1×1

|  |  |  |
|----|----|----|
|  | Title / Monoscii Lite.png / Author / Loud Whispers / Dated / 2015-03-30 / Tile Size / 1×1 / Resolution / 80×25 / Versions / Comments / So on suggestion I made the new version of Monoscii which has every tile be 1 pixel, the entire map nearly fits into the screen just fine. Monoscii Lite is superior in every way, the information is denser, crisper and cleaner. pUrists will finally be one step closer to the most pUrist DF possible. ( / forum post link / ) | Monoscii Lite |

## 5×5

|  |  |  |
|----|----|----|
|  | Title / Kein_400x125.png / Author / Kein / Dated / 2008-8-7 / Tile Size / 5×5 / Resolution / 400×125 / Versions / Comments / A large 257x257 DFMA world gen map can be found / here. / Updated 08 / 06 / 08. Changed most text characters as well as some others to 4x4 with blackspace to avoid tiling. Most characters have been revised to be spaced out to be more distinguishable in such a small set. After seeing the dev update earlier today about increasing your view size I decided to create this small font. This has been built completely from scratch, mostly while at work today. I may be making a shaded version in the future. The first image to the right is from the Abbeyverse succession game. | Kein's 5x5 |

|  |  |  |
|----|----|----|
|  | Title / Zaratustra_custom_5x5.png / Author / Zaratustra / Dated / 2008-11-20 / Tile Size / 5×5 / Resolution / 400×125, 800×250, 800×500 / Versions / Comments |  |

## 6×6

|  |  |  |
|----|----|----|
|  | Title / Geti_custom_6x6.png / Author / Geti / Dated / 2010-08-04 / Tile Size / 6×6 / Resolution / 480×150, 960times;300 / Versions / Comments / A 6x6 Tileset optimised for legibility through personal use. Not shaded on most glyphs, aiming for a crisper look. Best at 2x2 pixels. |  |

|  |  |  |
|----|----|----|
|  | Title / Lord Nightmare 6x6font01.png / Author / Lord Nightmare / Dated / 2007-11-5 / Tile Size / 6×6 / Resolution / 480×150 / Versions / Comments / Made in 5 hours on 11 / 5 / 07 (I was bored and dissatisfied with other fonts). Most glyphs are really 5×6, with a separator column. |  |

|  |  |  |
|----|----|----|
|  | Title / Lord Nightmare 6x6font02.png / Author / Lord Nightmare / Dated / 2007-11-12 / Tile Size / 6×6 / Resolution / 480×150 / Versions / Comments / Version 2.05. Updated 11 / 12 / 07 to de-fuzz uppercase letters, added serifs and clarified lowercase letters, made horizontal spacing consistent throughout character set, fixed one error in the double horizontal-left-right, single-vertical-up-down character, made exclamation points consistent, thinned out question mark and inverse question mark, sharpened sideways stemless arrows, clarified international characters, and clarified some Greek letters. Since v2.0: fixed 'i' 'g', fixed Yen symbol, fixed smiley 0x01 to not have an extra line to its right, lowered the period and colon characters, fixed position of 'x'. Thanks to Markavian for ideas on how to improve the font, as well as an occasional character glyph. | Lord Nightmare's 6x6 v2 |

|  |  |  |
|----|----|----|
|  | Title / Mkv_curses_480x150.png / Author / Markavian / Dated / 2007-10-30 / Tile Size / 6×6 / Resolution / 480×150 / Versions / Comments / The first version of the tiny tileset, superseded by the version below. |  |

|  |  |  |
|----|----|----|
|  | Title / Mkv_curses_480x150_v2.png / Author / Markavian / Dated / 2007-10-30 / Tile Size / 6×6 / Resolution / 480×150 / Versions / Comments / My second version of the tiny tileset, for uber small resolution DF, with improved visibility of several symbols. / Available in / mkv curses 12×12 and 6×6 v2.zip / . | Markavian's 6x6 v2 |

|  |  |  |
|----|----|----|
|  | Title / nobbins6x6.png / Author / Nobbins / Dated / 2010-01-10 / Tile Size / 6×6 / Resolution / 480×150, 960×300 / Versions / Comments / Tiny tileset for small screens, with experimental colour blending and pseudo-curved walls. |  |

|  |  |  |
|----|----|----|
|  | Title / nobbin_ts_v2.png / Author / Nobbins / Dated / 2010-06-28 / Tile Size / 6×6 / Resolution / 480×150, 960×300 / Versions / Comments / Tiny tileset for small screens / large projects, using slightly Monaco-styled serifs. Transparency-supporting version needed. / Forum thread. |  |

## 7×7

|  |  |  |
|----|----|----|
|  | Title / Herrbdog_7x7_tileset.gif / Author / herrbdog / Dated / 2007-10-30 / Tile Size / 7×7 / Resolution / 560×175 / Versions / Comments | herrbdog's 7x7 tileset |

|  |  |  |
|----|----|----|
|  | Title / terbert_7x7.png / Author / Terbert / Dated / 2009-6-30 / Tile Size / 7×7 / Resolution / 560×175 / Versions / Comments / This is a 7x7 tileset made for overseeing large constructions |  |

## 8×8

|  |  |  |
|----|----|----|
|  | Title / Anikki_square_8x8.png / Author / Anikki / Dated / 2008-7-27 / Tile Size / 8×8 / Resolution / 640×200 native. / Versions / Comments / Based on the original IBM CGA Character set with a lot of tweaks. The characters remain as descriptive yet universal as possible. I chose the CGA set because it is in my opinion the square set with the best readability. This set is for those who like the basic ASCII look where every pixel has meaning or (multiple meanings). / Download the BMP / There is also an upscaled / 16x16 version / of this set available for fullscreen use below. |  |

|  |  |  |
|----|----|----|
|  | Title / cheepicus_8x8 / Author / Cheepicus / Dated / 2014-4-3 / Tile Size / 8×8 / Resolution / 640×200 / Versions / Comments / An 8x8 tileset I made. Hand-made, mostly ASCII, with just a few special characters, like my other tilesets. | cheepicus_8x8 sample |

|  |  |  |
|----|----|----|
|  | Title / Jdpage_8x8.png / Author / Jdpage / Dated / 2010-09-15 / Tile Size / 8×8 / Resolution / 640×200 native. / Versions / Comments / Modified version of the / Anikki 8x8 tileset / . Just prettifies it a bit; some characters are tweaked to make them work slightly better for one of their jobs without disturbing the rest. Others are redesigned entirely. Most importantly, dwarves were given beards. |  |

|  |  |  |
|----|----|----|
|  | Title / CGA8x8thick.png / Author / Lord Nightmare / IBM / Dated / 2007-10-30 / Tile Size / 8×8 / Resolution / 640×400 / Versions / Comments / The original IBM CGA Character set, thick variant, dumped from addresses 0x1800-0x1fff the 5788005 IBM Character Generator ROM. This is the far more common 'thick' variant. Best viewed at 8:5 aspect ratio. |  |

|  |  |  |
|----|----|----|
|  | Title / CGA8x8thin.png / Author / Lord Nightmare / IBM / Dated / 2008-6-6 / Tile Size / 8×8 / Resolution / 640×400 / Versions / Comments / The original IBM CGA Character set, thin variant, dumped from addresses 0x1000-0x17ff the 5788005 IBM Character Generator ROM. This is the less common 'thin' variant, which required soldering on two pins and jumpering them on the CGA card to use. Best viewed at 8:5 aspect ratio. | Lord Nightmare's 8×8 CGA tileset |

|  |  |  |
|----|----|----|
|  | Title / LN_EGA8x8.png / Author / Lord Nightmare / IBM / Dated / 2007-10-30 / Tile Size / 8×8 / Resolution / 640×400 / Versions / Comments / The IBM EGA 8×8 Character set, dumped from the 6277356 IBM EGA BIOS ROM. This is ALMOST 100% IDENTICAL to the CGA thick font, but has minor modifications (23 pixels total) done to four characters: the capital 'S', the club sign, the spade sign, and the large asterisk (the one with a hole in the middle, char 0x0f, not the shift-8 one which is char 0x2a). There is no thin variant of this font. Best viewed at 8:5 aspect ratio. |  |

|  |  |  |
|----|----|----|
|  | Title / RDE_8x8.png / Author / RedDeadElite / Dated / 2018-08-17 / Tile Size / 8×8 / Resolution / 640×200 / Versions / Comments / Meant to resemble the vanilla curses tileset, which itself is similar to Microsoft's 8x12 Terminal font. Glyphs sourced from various bitmap fonts and / or modified by hand. | RedDeadElite's 8x8 tileset with / Phoebus's color scheme / . |

|  |  |  |
|----|----|----|
|  | Title / Pastiche_8x8.png / Author / tejón / Dated / 2012-6-12 / Tile Size / 8×8 / Resolution / 640×200 @ 80×25. / Versions / Comments / A mishmash of the CGA, Acorn and C64 character fonts (and just a hint of Fixedsys), with a few pixels nudged here and there and several symbols shifted to make world maps look nicer. |  |

|  |  |  |
|----|----|----|
|  | Title / Potash_8x8.png / Author / tejón / Dated / 2012-6-12 / Tile Size / 8×8 / Resolution / 640×200 @ 80×25. / Versions / Comments / I like packing as much on the screen as I can, but 8×8 is just too crowded for 1920×1080 fullscreen. I intended to make a 10×10 version of Pastiche, but I had to make countless little changes to maintain visual consistency between the two sizes. I finally gave up, called it a new font, and changed some more stuff just because! Like Pastiche, Potash is a pure ASCII / CP437 font, suitable for use outside of / Dwarf Fortress / should you happen to find yourself stuck in 1985. |  |

|  |  |  |
|----|----|----|
|  | Title / Acorntileset8x8.png / Author / Xenomorph / Dated / 2008-8-9 / Tile Size / 8×8 / Resolution / 640×200 / Versions / Comments / This is the tileset used by Acorn computers, starting with the BBC Micro. This version is as it would have appeared in 40-column modes (and shuffled a little to adapt it to CP437). It also looks nice at double resolution. / Download the BMP. |  |

|  |  |  |
|----|----|----|
|  | Title / yayo_c64_640x200.png / Author / Yayo / Dated / 2007-10-30 / Tile Size / 8×8 / Resolution / 640×200 / Versions / Comments / Name: Yayo's C64; Based on the charset of the Commodore 64. It's a flat style, but it's clean and also highly readable. I recreated all the missing chars like letters with accents and symbols, trying to get a c64 style as much as possible. If it's too small, use the 16×16 version / below / . :) | yayo's c64 Tileset |

|  |  |  |
|----|----|----|
|  | Title / Zaratustra_msx.png / Author / Zaratustra / Dated / 2007-10-30 / Tile Size / 8×8 / Resolution / 640×200 or 640×400 / Versions / Comments / The MSX and MSX2 font, shuffled around to fit the char set. Double lines were added. | Zaratustra's 8×8 tileset |

## 9×9

|  |  |  |
|----|----|----|
|  | Title / 720x225_SmoothWalls.PNG / Author / Dorten / Dated / 2009-2-13 / Tile Size / 9×9 / Resolution / 720×225 / Versions / Comments / It's improved Savok's tileset, which is changed to make walls look smooth. Plus another little differences. | Dorten's smooth-walled version of Savok's tileset. (Without fix for 7s) |

|  |  |  |
|----|----|----|
|  | Title / 720x225_SmoothWalls7.png / Author / Dorten / Dated / 2009-2-13 / Tile Size / 9×9 / Resolution / 720×225 / Versions / Comments / Minor tweak so the 7's don't look like question marks. |  |

|  |  |  |
|----|----|----|
|  | Title / Nostalgia_720x225.png / Author / maus / Dated / 2007-10-30 / Tile Size / 9×9 / Resolution / 720×225 / Versions / Comments / Another square tileset that's usable on low resolutions, modelled after a common font used on the Nintendo Entertainment System. I also made a / 18x18 version / to fit my 1440x900 screen, back when the aspect ratio of DF was locked. If you like your set a bit more graphical, check out / Teeto_K's version / . |  |

|  |  |  |
|----|----|----|
|  | Title / DortenSolid.png / Author / Qjet / Dated / 2009-2-13 / Tile Size / 9×9 / Resolution / 720×225 / Versions / Comments / Mod of Dortens super sexy 9\*9 tileset, this time to provide solid backgrounds to tiles, avoids designation problems by using PNG transparency. | Qjet's solid-background mod of Dorten's smooth-walled edit of Savok's tileset. |

|  |  |  |
|----|----|----|
|  | Title / Curses_720x225_8d6752.png / Author / Savok / Dated / 2007-10-30 / Tile Size / 9×9 / Resolution / 720×225 / Versions / Comments / There is no doubt that this tileset is old. This must be distinctly understood if anything wonderful is to come of your use of it. You may like / Dorten's revision / more. The following is the original description: / I dislike curses_640x300.bmp due to its lack of any kind of graphics for things like a bed or a barrel and the fact that it distorts my beautiful circles, so I made a similarish tileset to fix those. | Savok's tiny, non-updated tileset. |

## 10×10

|  |  |  |
|----|----|----|
|  | Title / Anikki_square_10x10.png / Author / Anikki / Dated / 2008-7-27 / Tile Size / 10×10 / Resolution / 800×250 native. / Versions / Comments / Based primarily on Tocky and Plac1d's sets (which are brilliant). The characters remain as descriptive as possible with some tweaks to the font for better readability and some changes to symbols for more consistency. This set is for those who like the basic ASCII look where every pixel has meaning or (multiple meanings). / Download the BMP / (Note: The up and down ramps are reversed.) |  |

|  |  |  |
|----|----|----|
|  | Title / buddy.png / Author / buddy / Dated / 2014-07-12 / Tile Size / 10×10 / Resolution / Versions / Comments / I wanted every character in this set to be the very best text symbol it could possibly be, while still looking good in-game. / A hidden feature of this tileset is that the border around the white tile only has its red color-component changed, which means that a nice clear grid shows up over (brown) designations, while (blue) ice walls still look perfectly smooth. / \[PILLAR_TILE:10\] |  |

|  |  |  |
|----|----|----|
|  | Title / buddy--graphical.png / Author / buddy / Dated / 2014-07-16 / Tile Size / 10×10 / Resolution / Versions / Comments / The graphical version of my tileset. / data / init / d_init.txt: / \[PILLAR_TILE:10\] / \[TREE_BRANCHES:171\] / raw / objects / creature_standard.txt: / \[CREATURE:GOBLIN\] ... \[CREATURE_TILE:255\] |  |

|  |  |  |
|----|----|----|
|  | Title / ddw.png / Author / Ddw / Dated / 2011-03-10 / Tile Size / 10×10 / Resolution / 800×250 native / Versions / Comments / Based on / Anikki / , with some simplifications and modifications. I like Markavian's walls, so I did something similar. The bottom right tile, number 255, I use for pillars. You can set that in your d_init.txt, the line should look like \[PILLAR_TILE:255\] / Example / . |  |

|  |  |  |
|----|----|----|
|  | Title / Paul_10x10.png / Author / Paul / Dated / 2008-9-5 / Tile Size / 10×10 / Resolution / 800×250 for 80×25 grid size, others just multiply grid by 10. / Versions / Comments / Custom tileset I made for my own use when the adjustable grid sizes were released for DF. Some accented letters cut slightly to allow for larger letter display. Contains several of Tocky's tiles (barrels, some trees, dimple cups, coins, slightly modified armor stand). Others are either made by me or adjusted from curses_800x600 tiles. |  |

|  |  |  |
|----|----|----|
|  | Title / Potash_10x10.png / Author / tejón / Dated / 2012-6-12 / Tile Size / 10×10 / Resolution / 800×250 @ 80×25. / Versions / Comments / The "full size" version of Potash. I insist on using a square font to maintain sanity when judging sizes and distances, but I'm not a fan of how text usually looks with square glyphs -- the letters are either too wide, or spaced too far apart. I've tried balance those two flaws against each other as much as possible, and I think this font is very readable as a result. Nearly all the 10×10 glyphs have empty borders on all four sides, to prevent confusing (or just ugly) connections between adjacent tiles. |  |

|  |  |  |
|----|----|----|
|  | Title / Taffer 10x10.png / Author / Taffer / Dated / 2017-01-10 / Tile Size / 10×10 / Resolution / Looks decent at almost any resolution. / Versions / Comments / A sharp looking, vanilla styled tileset that strives to strike a good balance between nice, attractive graphics, while avoiding graphical oddities. I find the cumulative differences from the ASCII add to the game. Feel free to leave me a / note / . This has turned into a / \[1\] / , and includes alternate walls, fonts, and racial graphics. |  |

|  |  |  |
|----|----|----|
|  | Title / Terbert_10x10.png / Author / Terbert / Dated / 2009-6-30 / Tile Size / 10×10 / Resolution / 800×250 / Versions / Comments / This is Terbert's First tileset |  |

|  |  |  |
|----|----|----|
|  | Title / Tocky_square_10x10.png / Author / Tocky / Dated / 2007-11-15 / Tile Size / 10×10 / Resolution / 800×250 native, 800×500 for fullscreen. / Versions / Comments / I tried to make all the pictographic symbols as descriptive as possible: the only ones I've spotted that show up in odd places are the staircase symbols, '\', which are used as tags on barrel descriptions, and don't match -- but I'm willing to live with that in order to be able to tell up-stairs from down-ones. With everything else, I just tried to maximize clarity and readability and to keep them consistent. I'm really very pleased with how this set turned out. |  |

## 11×11

|  |  |  |
|----|----|----|
|  | Title / terminus.png / Author / Gekz / Dated / 2010-1-08 / Tile Size / 11×11 / Resolution / 880×275 / Versions / Comments / This works great on my EeePCs shoddy resolution of 1024x600, and this is why I made it. This is basically the / Terminus font / converted for use on DF. I chose this font due to its readability at a low resolutions, and soon I'll convert some of the non-letter characters into actually objects like beds and dwarves, so keep a look out for an updated version that I'll add below. / This forum thread / has the slightly 'graphical' test version. Quite amusing. Check there for updates. | Terminus Tileset |

## 12×12

|  |  |  |
|----|----|----|
|  | Title / DB_curses_12x12.PNG / Author / Hanuman / Dated / 2008-7-23 / Tile Size / 12×12 / Resolution / 900×300 / Versions / Comments / This is basically the curses_800x600.bmp file converted to 12x12. It may be slightly different but it is close enough for me. / Get the .BMP here. / Note: If the tileset doesn't look right played at 900x300, try changing the resolution to 966x325. |  |

|  |  |  |
|----|----|----|
|  | Title / Alloy_curses_12x12.png / Author / Alloy / Dated / 2010-12-3 - v1.1 / Tile Size / 12×12 / Resolution / 960×300 native. / Versions / Comments / Much like / Hanuman's conversion / , this is based on the default curses_640x300 tileset, converted to 12x12. There are no significant modifications to the tiles, smoothing, etc - just some cosmetic changes mostly to take advantage of 4 extra horizontal pixels. For people who like the original tileset's look and size but want a square version of it. |  |

|  |  |  |
|----|----|----|
|  | Title / Haberdash_curses_12x12.png / Author / Haberdash / Dated / 2014-07-24 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / Similar to / Alloy's conversion / , this is based on the default curses_800x600 tileset, converted to 12x12. I wrote a GIMP python plugin to add padding to bring each tile up to the required size, and then I manually tidied up the places where the images no longer went all the way to the edge of the tile. This ensures that the positioning of each image within each tile stays exactly the same as in the original tileset, but with a single pixel column added on both sides of the tile to bring it up to size. For people who like the 800x600 original tileset's look and size but want a square version of it. |  |

|  |  |  |
|----|----|----|
|  | Title / Curses_classic_square_12x12.png / Author / DPh Kraken / Dated / 2025-1-1 / Tile Size / 12×12 / Resolution / 1024×768 / Versions / Comments / The vanilla tileset, resized to 12x12 with no added frills. Some non-text characters have been additionally centered within the wider margins. |  |

|  |  |  |
|----|----|----|
|  | Title / cheepicus_12x12 / Author / Cheepicus / Dated / 2010-8-4 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / I wanted a 12x12 ASCII graphics set, sharp, with pleasant text, so I wound up making one myself from scratch. It's a little influenced by Guybrush, which I love, but after awhile the blurriness got to me. / (This tileset is not entirely ASCII; I changed the equals sign to a pattern, so that stockpiles would look the way I like.) | cheepicus_12x12 sample |

|  |  |  |
|----|----|----|
|  | Title / Unknown curses 12x12 & Markvii Walls.png / Author / DDR & Others / Dated / 2010-9-3 / Tile Size / 12×12 / Resolution / 960×300 native / Versions / Comments / A remix of the Unknown 12x12 curses with Markvii's diagonal walls. Works quite nicely together. | A dwarf practicing archery. He died later. |

|  |  |  |
|----|----|----|
|  | Title / Herrbdog_144.png / Author / Herrbdog / Dated / 2007-10-30 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / A larger version of this tileset is available / below / . |  |

|  |  |  |
|----|----|----|
|  | Title / Dullard_Exponent_12x12.png / Author / Lord Dullard / Exponent / Dated / 2009-3-30 / Tile Size / 12×12 / Resolution / 960×300 native / Versions / Comments / Adjusted by Exponent, and with new dwarf characters added. A version of the Unknown 12×12 tileset with smoothed walls. Example: / Wiltedblight / . |  |

|  |  |  |
|----|----|----|
|  | Title / mkv_solidcurses_stairs_960x300.png / Author / Markavian / Dated / 2007-12-4 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / This revision is designed to work with DF version 0.27.169.33a with special tiles for / stairs / and / ramps / , as well as the changes present in the earlier version such as bones, walls, trees and swords. / Available in / mkv curses 12×12 and 6x6 v2.zip / . As seen in the fortress of / Axegear / . |  |

|  |  |  |
|----|----|----|
|  | Title / Mkv_solidcurses_960x300.png / Author / Markavian / Dated / 2007-10-30 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / An older revision of my square tileset, featuring more detailed symbols, with alterations to certain text characters to look more like ingame items. The walls are infilled now. / Available in / mkv curses 12×12 and 6x6 v2.zip / . As seen in the fortress of / Inkflew / . |  |

|  |  |  |
|----|----|----|
|  | Title / Markvii.png / Author / Turnip / Dated / 2009-7-9 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / My revision of Markavian's tileset, made to be more "curvy" |  |

|  |  |  |
|----|----|----|
|  | Title / Tileset_unknown_960x300_02.png / Author / Unknown / Dated / 2007-10-30 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / This is a tileset submitted by an unknown user from the IP address 86.43.81.125. |  |

|  |  |  |
|----|----|----|
|  | Title / Unknown_curses_12x12.png / Author / Unknown / Dated / 2007-11-24 / Tile Size / 12×12 / Resolution / 960×300 / Versions / Comments / This is very similar to the above tileset, but has some noticeable differences. I have no idea where I got it from. It's great on a 1024x768 CRT monitor in windowed mode. I use it in a 1000x500 window with \[BLACKSPACE:YES\]. -- / JT | Unknown 12×12 v2 |

|  |  |  |
|----|----|----|
|  | Title / nice_curses_12x12.png / Author / Vidumec / Dated / 2013-01-30 / Tile Size / 12×12 / Resolution / 960×300 native / Versions / Comments / This tileset is a square version of Plac1d's tileset with some modifications, like duller ground tiles and other. |  |

|  |  |  |
|----|----|----|
|  | Title / zesty_curses_12x12.png / Author / ZesT / Dated / 2022-11-3 / Tile Size / 12×12 / Resolution / 960×300 native / Versions / Comments / A fresh spin on Vidumec's "nice curses" tileset - includes a couple different graphics that both keep the ASCII feel and provide better visual representations while preventing text artefacts, including new graphics for sheets, plus a Moai statue since making the statue specifically humanoid didn't feel generalisable enough. / A / 24x24 version / is available. |  |

## 13×13

|  |  |  |
|----|----|----|
|  | Title / Kren_13x13.png / Author / krenshala / Dated / 2015-12-27 (Updated 2017-08-27) / Tile Size / 13×13 / Resolution / Versions / Comments / I wanted a tileset smaller than 15x15 that would still display nicely on a netbook (e.g. 1366×768), but still be clearly legible. I think I have succeeded in that goal. On a 1680×1050 display the resolution is 129×80 with this tileset. |  |

|  |  |  |
|----|----|----|
|  | Title / yayo_tunur_1040x325.png / Author / Yayo / Dated / 2007-10-30 / Tile Size / 13×13 / Resolution / 1040×325 / Versions / Comments / Name: Yayo's Tunur; According to the language files of DF, Tunur means "style" in dwarf language. It may require a bit to get used to some symbols, but it's a very clean tileset. (It's just a bit weird. :P) | yayo's Tunur Tileset |

## 14×14

|  |  |  |
|----|----|----|
|  | Title / cheepicus_14x14 / Author / Cheepicus / Dated / 2018-11-28 / Tile Size / 14×14 / Resolution / 1120×350 / Versions / Comments / Back on my bullshit. I made this because I wanted a bold, low-eyestrain tileset. | cheepicus_14x14 sample / cheepicus_14x14 sample |

## 15×15

|  |  |  |
|----|----|----|
|  | Title / cheepicus_15x15 / Author / Cheepicus / Dated / 2012-5-6 / Tile Size / 15×15 / Resolution / 1200×375 / Versions / Comments / I find the text hard to read in most other tilesets, so I made a new one. Mostly ASCII with a few graphical nods. Lower right char is for PILLAR:255 in df_init. | cheepicus_15x15 sample |

|  |  |  |
|----|----|----|
|  | Title / Talryth_square_15x15.png / Author / Talryth / Dated / 2010-06-18 / Tile Size / 15×15 / Resolution / 1440×900 (96×60 grid size) / 1680×1050 (112×70 grid size) / Versions / Comments / Built from scratch, this ASCII tileset is made with two common 16:10 resolutions in mind. The odd tile size fills the above resolutions without artifacts and it gives an advantage in design, making for sharp features and equal spacing between characters. The manual anti-aliasing gives the set a nice and clean look. Transparent PNG support is needed for this one. |  |

|  |  |  |
|----|----|----|
|  | Title / Vidumec_15x15.png / Author / Vidumec / Dated / 2011-09-05 / Tile Size / 15×15 / Resolution / 1440×900 (96×60 grid size) / 1680×1050 (112×70 grid size) / Actually looks good on any resolution / Versions / Comments / I liked the great Talryth square 15x15 very much! However dwarves tiles were a litlle bit out of the style, so I changed them to default-like ones. Also added background so the there is no more black background which with bright ASCII was hard to my eyes. Again thanks to Talryth for his amazing job! |  |

## 16×16

|  |  |  |
|----|----|----|
|  | Title / Anno_16x16.png / Author / AbuDhabi / Dated / 2011-03-19 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / Based on / Anikki's 16x16 tileset / , but smoothed / enhanced and with the dwarf images reworked. |  |

|  |  |  |
|----|----|----|
|  | Title / Aesomatica_16x16.png / Author / Aesomatica / Dated / 2008-11-29 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / Tileset intended to build upon / Sphr's / and / Jackard's / work, as well as others. Some tiles are original, some are variants and most are copied from various sets the author found pleasing. Notable originals include the broken bolt / ashes tiles, the ballista heads / large hills, the small hills, the ore (gear animation is pleasing, though axle animation is unimproved), ground tiles, and vermin. Also, bins look decent and up / down stairs look okay. This set looks its best with Sphr's graphics. |  |

|  |  |  |
|----|----|----|
|  | Title / LCD_Tileset.png / Author / Agm / Dated / 2020-02-07 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Semi-graphical ASCII tileset, original work. Font used is Kelora. Suggested that you set \[PILLAR_TILE:255\] in d_init.txt. |  |

|  |  |  |
|----|----|----|
|  | Title / 16x16-RogueYun-AgmEdit.png / Author / Agm / Dated / 2017-10-21 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / ASCII Edit of / Rogue Yun / 's tileset with diagonal walls and other edited tiles. Suggested that you set \[PILLAR_TILE:255\] in d_init.txt. |  |

|  |  |  |
|----|----|----|
|  | Title / Anikki_square_16x16.png / Author / Anikki / Dated / 2008-7-27 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / Based on the original IBM CGA Character set with a lot of tweaks. The characters remain as descriptive yet universal as possible. I chose the CGA set because it is in my opinion the square set with the best readability. This set is for those who like the basic ASCII look where every pixel has meaning or (multiple meanings). This is a scaled up version for fullscreen use. / Download the BMP |  |

|  |  |  |
|----|----|----|
|  | Title / Bisasam_16x16.png / Author / Bisasam / Dated / 2010-01-11 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / This is the 16x16 version of my 24x24 tileset. A DF version supporting transparent PNGs must be used. In order to use unscaled tiles, horizontal resolution must be at least 1280. |  |

|  |  |  |
|----|----|----|
|  | Title / cheepicus_8x8x2 / Author / Cheepicus / Dated / 2014-4-3 / Tile Size / 16×16 (doubled 8x8) / Resolution / 1280×400 native. / Versions / Comments / I liked the font on my 8x8 tileset, but it was too small to use every day. So I doubled it and the result has a nice 8-bit feel. Hand-made, mostly ASCII. | cheepicus_8x8x2 sample |

|  |  |  |
|----|----|----|
|  | Title / cheepicus_16x16 / Author / Cheepicus / Dated / 2014-5-10 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / Mostly ASCII 16x16 with an art deco / Nixie tube inspired kind of font. | cheepicus_16x16 sample / cheepicus_16x16 sample |

|  |  |  |
|----|----|----|
|  | Title / Cooz_curses_square_16x16.png / Author / Cooz / Dated / 2009-2-28 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / v1.1 - 3px wide walls and some other tweaks. Based on Klokjammer and Marble Dice tilesets. Some tiles were taken from other sets, some were made from scratch. The aim was to keep feel of default curses font in 16×16 tileset. There's also / version without shading / . | Cooz's Tileset |

|  |  |  |
|----|----|----|
|  | Title / Guybrush_square_16x16.png / Author / Guybrush / Dated / 2007-11-15 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A 16×16 tileset based on the very nice Herrbdog's one, and for use with the superb / Dystopian Rhetoric objects / . A slightly modified version of Herrbdog's tileset is available below if you want to keep the original ASCII symbols for some objects (just do some cut & paste). It's just a little brighter and with some very slight changes. The tileset shown is a tileset with graphic objects added, for use with Fortress Mode. / I recommend to have a look at the / color schemes page / to find your favorite color settings. The color scheme I used for the screenshots is / this one / . | Guybrush Tileset / the wilderness... |

|  |  |  |
|----|----|----|
|  | Title / GuybrushASCII_curses_square_16x16.png / Author / Herrbdog, modified by / Guybrush / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Here is the slightly modified version of Herrbdog's tileset which still has all the ASCII characters intact |  |

|  |  |  |
|----|----|----|
|  | Title / Herrbdog_16x16_tileset.gif / Author / Herrbdog / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / The 16×16 version of Herrbdog's tileset. |  |

|  |  |  |
|----|----|----|
|  | Title / Oddball-16 / Author / HexaBlu / Dated / 2021-07-05 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / "A silly and whimsical 16x16 Tileset focused on unique graphics, Made completely from scratch. The font is designed off of my bad handwriting. " / Forum Page | A screenshot of what the landscape looks like using Oddball-16. |

|  |  |  |
|----|----|----|
|  | Title / MRC_square_16x16.png / Author / Inquisitor Saturn / Dated / 2008-5-18 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Another 16 by 16 tileset. This one is notable because of the subtle shadowing and a completely original, hand-made font. |  |

|  |  |  |
|----|----|----|
|  | Title / Redjack17.png / Author / Jackard / Dated / 2008-7-22 / Tile Size / 16x16 / Resolution / 1280x400 / Versions / Comments / This combines content from other tilesets with Nintendo sprites to give the game a classic dungeon look. / Note: Bins are hard to see using this tileset because the "bin" tile is also used as the "up / down staircase" tile. / Aesomatica / and / Martin / improve upon this tileset making the bin tile easier to see. / You may download all variations of this tileset here. |  |

|  |  |  |
|----|----|----|
|  | Title / Kai-1280x400-v2 7512b5.png / Author / Kaishaku / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A square 1280×400 font. Simple and legible. Converted from roarl's 16×16 nethack font, on top of super foul egg's template, extended manually and with ideas from lucida console. This is version 1, created in one morning. Screenshots available / here / . |  |

|  |  |  |
|----|----|----|
|  | Title / Kelora_16x16_diagonal.png / Author / Kelora / Dated / 2009-7-26 / Tile Size / 16×16 / Resolution / Versions / Comments / A square tileset using the diagonal wall concept from Belal and others but simplified drastically to improve the appearance. All the walls line up correctly and have consistent widths. / I did not use much of the pretty but confusing art I see in many of the other sets. I tried for a while to incorporate many of these but found that with the multiple uses for most characters they were just wrong far too often to be useful. The only ones that seem to work are the dwarves which I took from Flying Mage / Guybrush. The pretty 3Dish fonts as well just seem to look muddier and be less legible. I love it and my husband has been happily playing it for months. |  |

|  |  |  |
|----|----|----|
|  | Title / Kelora_16x16_diagonal-clouds.png / Author / Kelora / Dated / Tile Size / 16×16 / Resolution / Versions / Comments / A square tileset using the diagonal wall concept from Belal and others but simplified drastically to improve the appearance. All the walls line up correctly and have consistent widths. / I did not use much of the pretty but confusing art I see in many of the other sets. I tried for a while to incorporate many of these but found that with the multiple uses for most characters they were just wrong far too often to be useful. The only ones that seem to work are the dwarves which I took from Flying Mage / Guybrush. The pretty 3Dish fonts as well just seem to look muddier and be less legible. This tileset is a copy of my first with more realistic clouds I hope. |  |

|  |  |  |
|----|----|----|
|  | Title / Kenran.png / Author / Kenran / Dated / Tile Size / 16×16 / Resolution / Versions / Comments / This tileset is for the most part identical to the great one by Kelora above. I fixed an error with the single lines and curves (used for instance for rivers on the world map) where two tiles didn't connect correctly. I also adjusted the diagonal walls a bit. |  |

|  |  |  |
|----|----|----|
|  | Title / Kjammer square 16x16 v02.png / Author / Klokjammer / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Name: / "Masked Adventurer" / - after tile (0,4), where '@' used to be. A somewhat abstract version of the original curses square tileset, but with the alpha numeric characters shaped so as not to look distorted. Other symbols are either borrowed from or improved from curses, and some (including the dwarves) were created from the ground up. Alternate variations, are available / here / . |  |

|  |  |  |
|----|----|----|
|  | Title / Kjammer square 16x16 v00.png / Author / Klokjammer / Dated / 2007-10-31 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A "clean" version of the above set, one without any fancy tiles (except for the dwarves). |  |

|  |  |  |
|----|----|----|
|  | Title / Md_curses_16x16.png / Author / Marble Dice / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / This tileset attempts to modify the size and aspect ratio of the classic 8x12 terminal / curses font employed by many roguelikes without sacrificing the distinctive character. |  |

|  |  |  |
|----|----|----|
|  | Title / Runeset_16x16.png / Author / monkeyfritz / Dated / 2018-3-23 / Tile Size / 16×16 / Resolution / 256×256 / Versions / Comments / Runeset is an RSCII (Runic Standard Code for Information Interchange) font pack for / Dwarf Fortress / . Much more dwarfy than that American standards stuff. Best used with / Runeset Mapmaker / or / Runeset / color schemes. | Runeset Maps |

|  |  |  |
|----|----|----|
|  | Title / PTTGV2tiles.png / Author / PTTG / Dated / 2007-11-21 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A new version! Clean, sharp, and clear. All-original, and large size for big screens! Also features coloured indicators for levers, helping to remove the guesswork. It is good stand-alone, or with my / graphics set / . |  |

|  |  |  |
|----|----|----|
|  | Title / Fnord 16x16.png / Author / PopTart / Dated / 2016-5-08 / Tile Size / 16×16 / Resolution / 1280×400 native. / Versions / Comments / "FnordSet contributes a bold Roman font that takes advantage of the square tile. Baskerville served as the main model. This set was also inspired by (and borrows from) the bold geometry of Rogue Yun's Simple Mood and the seriffed grace of the Duerer set. It also draws inspiration from the Ishmeria tileset, which I think complements it nicely as text in TWBT. (Nowadays I use the nicely contrasting sans serif tileset Jecfox for the text font.)" / Forum thread |  |

|  |  |  |
|----|----|----|
|  | Title / Msgothic.png / Author / User:Random832 / Dated / 2009-4-22 / Tile Size / 16×16 / Resolution / 1280×800 etc / Versions / Comments / Based on the ＭＳ ゴシック (MS Gothic) japanese font, with some gaps filled in from the VGA 8x16 font, and some other characters tweaked by hand. |  |

|  |  |  |
|----|----|----|
|  | Title / Raving_1280x400.png / Author / RavingManiac / Dated / 2010-3-13 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A heavily modified version of Tyrving's tileset, with smoothed walls based on those from Tahin's. This tileset was made to retain the feel of the original curses in a square tileset with smoothed walls. / Download the BMP. |  |

|  |  |  |
|----|----|----|
|  | Title / 16x16_sm.png / Author / Rogue Yun / Dated / 2015-06-09 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / I recommend setting all the pillar tiles in d_init.txt to tile 10. Possible updates may be on / this thread / . |  |

\

|  |  |  |
|----|----|----|
|  | Title / 16x16_sb_ascii.png / Author / Rogue Yun / Dated / 2018-11-04 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / A good solid ASCII Tileset. See the / Something Boxy / thread for more information and updates. |  |

|  |  |  |
|----|----|----|
|  | Title / Sapphos_square_16x16.png / Author / Sappho / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Another square font, target resolution 1280×400. This one is exactly the same as the default font except it has been made square, painstakingly edited to ensure that nothing looks squished. |  |

|  |  |  |
|----|----|----|
|  | Title / Savok_curses_1280x400_517caa.png / Author / Savok / Dated / 2008-6-16 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Unsatisfied with any existing tileset, I decided to go about creating my own. Since I can't create from scratch, I had to take tiles from other tilesets and modify them, in an evolution-like manner, until they became how I wanted them. Since most are dramatically different from the tileset I took them from, I believe I can call them original. / In the raws, change the tag \[TILE:'U'\] for humans to \[TILE:172\]. This changes both the image and corpse of humans to a unique image, which creature graphics cannot do. The elves also get a different tile, \[TILE:171\]. I plan to make a separate goblin symbol. / If you use it and like it, please leave a message for at / my talk page / or at / the DFFD page / . This will greatly speed progress, since I won't be doing it just for myself. / Note: The / DFFD version / is updated more frequently and has the changelist. |  |

|  |  |  |
|----|----|----|
|  | Title / SFE_Curses_square_16x16.png / Author / Super Foul Egg / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / The font is rough as hell and some of the characters still need attention, but it'll do for now. Since this tileset is for graphics mode I'd rather wait for more complete object support than hack in pictures and gum up the UI. Uppercase from / this site |  |

|  |  |  |
|----|----|----|
|  | Title / Tahin_16x16_rounded.png / Author / Tahin / Dated / 2007-12-28 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Based on Marble Dice's tileset, above. Smoothed corners are "rounded", which takes some getting used to but look quite nice, in my opinion. I have managed to get all of the standard "L" tiles to fit together nicely, but "T" and "+" don't quite match up. It's not a problem that comes up often, and it still doesn't look that bad, but I'll get to it eventually. |  |

|  |  |  |
|----|----|----|
|  | Title / DF-Nordic_v1.png / Author / Techhead / Dated / 2009-3-26 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / My first attempt at a unique curses-style tileset with a Nordic Theme. Some characters have been altered. |  |

|  |  |  |
|----|----|----|
|  | Title / Markx.png / Author / TurnipII / Dated / 2018-8-2 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Descended from the original MarkVII tileset. Has Markavian inspired walls, and many of Anikki's characters. |  |

|  |  |  |
|----|----|----|
|  | Title / Tyr_1280x400.PNG / Author / Tyrving / Dated / 2008-2-15 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / None of the existing modifications of curses_square satisfied me, so I made my own. The bulk of it is from Klokjammer's set, with the dwarf symbols and @ taken from Sappho's. Quite a few minor alterations have been made, and I feel that it's become distinct enough to release it. |  |

|  |  |  |
|----|----|----|
|  | Title / Winterwing_Curses_16x16_lucon.png / Author / Winterwing / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Like usual, lucida console with cleartype. Creative, huh. :) | Lucida Console with Dystopian Rhetoric objects |

|  |  |  |
|----|----|----|
|  | Title / Yayo_c64_1280x400_83b157.png / Author / Yayo / Dated / 2007-10-30 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Name: Yayo's C64; The 16×16 version of Yayo's tileset. |  |

|  |  |  |
|----|----|----|
|  | Title / Zaratustra_16x16.png / Author / Zaratustra / Dated / 2007-11-10 / Tile Size / 16×16 / Resolution / 1280×400 / Versions / Comments / Because everyone is making one. |  |

|  |  |  |
|----|----|----|

---
*Parte 1 de 2 de «Tileset repository». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Tileset_repository*
