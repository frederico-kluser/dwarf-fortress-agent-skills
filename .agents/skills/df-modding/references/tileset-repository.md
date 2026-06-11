# Tileset repository

> Fonte: [Tileset repository](https://dwarffortresswiki.org/index.php/Tileset_repository) — Dwarf Fortress Wiki (GFDL/MIT)

A character set, or simply tileset, is an image in BMP or PNG format that contains the 256 different tiles, corresponding to the IBM Code Page 437 (sometimes called Extended ASCII). They are used to display the main graphics. This page serves as a repository for custom tilesets made by users, including instructions on how to install them.

## Background

The default tilesets (640×300 and 800×600) render 8×12 and 10×12 characters respectively, with majuscule latin letters occupying a 7×9 box, and appear broadly similar to the IBM MDA font based on the shape of the "0", "g", and "f" characters (but with slight differences including the "0", "W", and "y"). The exact origin of the DF font is unknown.

There have been numerous graphics updates with the release of version 50. Unfortunately, at the moment, the latest release only renders properly with the default resolution and tile size. The default tileset is curses_640x300.png, so until there is an update, only 640×300 and 8×12 will render properly.

## Installation

To use a specific tileset with *Dwarf Fortress*, you must perform the following steps:

1.  Download the tileset to your computer. Each tileset is just an image, so there is no separate download link. (**Right-Click** on the tileset image and **Save-As**.)
2.  If necessary, convert the tileset to the correct image format for the version of DF you are using:
    1.  Do **not** just change the extension to .bmp or .png; you must use a program like MS paint to save it properly.
    2.  For *DF 0.28.181.40d or older:* open the file in an image editor and save it as a **24-bit bitmap** (BMP) if it isn't already in that format.
    3.  For *DF 0.31.01 or newer:* open the file in an image editor and save it as a **PNG** with *transparency* if it isn't already in that format.
3.  Move or copy the file to the DF art directory ().
4.  Edit the initialization configuration file () to specify the tileset file to use. There are three lines that can be changed:
    1.  **\[FONT:*\*\]** — the tileset for a windowed display.
    2.  **\[FULLFONT:*\*\]** — the tileset for a full-screen display.
    3.  **\[BASIC_FONT:*\*\]** — the tileset for initial loading and menu display.
    4.  All three can be set to the same file.
    5.  Once you have made the changes you need to remember to save the file.
5.  If the selected tileset requires modifications to the Raws, you will have to make those edits. What those changes are will depend on the tileset itself, and may only be valid for older versions. Likewise, some tilesets may suggest changes to , such as , but those options no longer exist.

Once the file is saved and the required changes are made, you are ready to play DF with your new tileset!

# Square tilesets

## 1×1

## 5×5

## 6×6

## 7×7

## 8×8

## 9×9

## 10×10

## 11×11

## 12×12

## 13×13

## 14×14

## 15×15

## 16×16

## 18×18

## 20×20

## 24×24

## 32×32

## 48×48

## 64×64

# Square tilesets for edited raws

*If you cannot find the altered raws of a tileset for your version of*Dwarf Fortress*have a look at the Raw tile selector tool.*

These tilesets require modified raws to work properly. Specifically, the tile numbers assigned to some objects (critters, stones, plants) need to be changed and accented characters usually need to be removed from all languages.

## 8×8

## 12×12

## 16×16

# Non-Square Tilesets

## 1×1.1875

## 4×6

## 5×6

## 6×8

## 6×9

## 6×10

## 8×12

## 8×14

## 8×15

## 8×16

## 9×12

## 9×14

## 9×16

## 10×12

## 10×16

## 12×20

## 14×16

## 16×20

## 16×24

## 16×32

## 20×32

## 24×32

## 24×36

## 48×72

\]\] \]\]
