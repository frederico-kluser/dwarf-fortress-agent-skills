# Technical tricks

> Fonte: [Technical tricks](https://dwarffortresswiki.org/index.php/Technical_tricks) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Dwarf Fortress* has various settings that can affect the game experience. You can configure these in *Settings* accessed from the main menu or Esc menu. However, some settings can only be changed by directly editing the game configuration files, which include:

- announcements.txt - contains configuration for the various game announcements.
- arena.txt - contains layouts of object testing arena maps.
- colors.txt - contains the color scheme used to display various text.
- d_init.txt - contains settings that affect game features such as autosaving, interface, simulation, and population controls.
- embark_profiles.txt - contains embark presets saved from prepare carefully or copied from the embark profile repository.
- init.txt - contains settings pertaining video, audio, and input.
- interface.txt - contains keybinds.
- world_gen.txt - contains advanced world generation presets.
- macros - the folder where macro files are saved.

## Locating configuration files

These configuration files might be found in two of three places in the install folder:

- `data\init\` - files here contain the default values installed with the game and also may contain some explanations of the settings.
- `prefs\` - files here contain the current values saved by the game, the location of the `prefs` folder depends on the portable mode setting (there is also a `data` folder there, but `data\init\` files will always be in the game installation folder).

You can edit the configuration files with any plain text editing software, such as Notepad, Vim, or Emacs.

Most data in these files is in token form. Each token is defined by the text between an opening square bracket, `[`, and the next closing square bracket, `]`. The token identifier and any values are separated by a colons, `:`.

If anything goes wrong, you can completely reset the game's saved settings by deleting the `prefs\` folder, while the game is not running, assuming the defaults have not been changed. Individual files can also be deleted to just reset those settings. This does not work with the files in `data\init\`, so you should make backups of them before modifying them. The game also uses the last occurrence of a token, so you could add your changes after the default values. You could then just remove the leading `[` to disable your entries and use the defaults.

## d_init.txt

*All settings can be changed in game, see Settings.*

## init.txt

*For settings that can be changed in game, see Settings.*

- \[SOUND:YES\] - Change the argument from "YES" to "NO" to completely remove sound and music from the game. If this is "NO", it will not be possible to change the volume from the in game options menu.

- \[WINDOWED:PROMPT\] - Changes the window mode that *Dwarf Fortress* runs in. If this is "PROMPT" the game will ask you if you want to run in windowed or fullscreen mode. If this is "NO" the game will be fullscreen with no prompt, and if this is "YES" the game will be in windowed mode with no prompt.

**The game does not save the following font options to `/prefs/init.txt`; you can add them but they will be removed the next time you exit Settings in game.** To make them persistent add them to `/data/init/init_default.txt`.

- \[FONT:curses_640x300.png\] - The font file that *Dwarf Fortress* uses in windowed mode. These values can be any .bmp or .png image in the `/data/art` folder.

- \[FULLFONT:curses_800x600.png\] - The font file used in fullscreen mode.

- \[BASIC_FONT:curses_640x300.png\] - The font used during the initial load sequence and menus.

- \[FPS_CAP:0\] - Setting this to zero will cause it to be uncapped, allowing simulation to happen as fast as possible. This may cause the FPS display to show negative numbers when the game is paused and in the main menu.

- \[G_FPS_CAP:0\] - Setting this to zero will still use the default of 50 rather than it being uncapped.

## Resolution to grid ratios

Taken from [1]

Geometry
Character Size

Resolution
Aspect
8x8
12x12
16x16

800x600
4:3
100 x 75
66 x 50
50 x 37

1024x768
4:3
128 x 96
85 x 64
64 x 48

1152x864
4:3
144 x 108
96 x 72
72 x 54

1280x960
4:3
160 x 120
106 x 80
80 x 60

1600x1200
4:3
200 x 150
133 x 100
100 x 75

1280x1024
5:4
160 x 128
106 x 85
80 x 64

1440x900
16:10
180 x 75
135 x 56.25
90 x 37.5

1680x1050
16:10
210 x 131
140 x 87
105 x 65

1920x1080
16:9
240 x 135
160 x 90
120 x 67

1920x1200
16:10
240 x 150
160 x 100
120 x 75
