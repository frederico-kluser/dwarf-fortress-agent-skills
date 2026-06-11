# World painter

> Fonte: [World painter](https://dwarffortresswiki.org/index.php/World_painter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **world painter** tool allows you to paint features onto a map, that is then used when generating a world. It is very difficult to use properly, and tends to result in endless rejected worlds, unless you loosen or remove the restrictions placed on biomes and civilizations in the advanced settings. That being said, it is also a very powerful tool, and allows you to generate worlds more to your liking.

The game refers to this tool as "Set Preset Field Values".

This feature does not currently exist in the game. However, it is possible to use it in an older version, save the parameters sets, and use that world_gen.txt file in newer versions.

The output of the Perfect World DF utility also works with current versions.

## Usage

To start the world painter:

1.  Open *Dwarf Fortress*.
2.  Select "Design New World With Advanced Parameters".
3.  Select a parameter set using ↑↓.
4.  Press e to enter advanced parameters.
5.  Press p ("Set Preset Field Values") to open the world painter.

Unlike most other aspects of *Dwarf Fortress*, the world painter requires a mouse or other pointing device for basic functionality, such as navigation and parameter painting. Thus, disabling mouse use in init.txt will make this feature unusable.

Basic world painter window.

The interface is reasonably simple. Simply left click on a tile and the settings on the right side of the screen with be applied to that tile. To move the view, right click and your active tile will be centered at cursor's location. To make a tile active, paint something there or just press ENTER. You can left click on any of the text on the right to change the setting it represents. By clicking on the title of one of the settings, or the text to the right of it, you can replace the default view with a view representing just that parameter (You can return to the normal view by pressing ENTER. By clicking the text "brush = \_\_\_\_", you can change the value of that parameter. Clicking on the text "painting" will toggle whether the parameter is painted when you click on a tile, and clicking on "Will Be Saved", will allow the world generator to deal with that parameter, instead of using what was painted.

It's easier to start with elevation by setting painting on only there, and continue with rain and drainage together.

## The Settings

Rainfall goes from 0-100, with 0 making dry areas

Elevation goes from 1-400, with anything below 100 being water, and with 300+ being mountain.

The available temperature range depends on the min and max temperature setting, and has little visible effect in the editor, with the exception of creating glaciers and tundra near the edges.

Drainage goes from 0-100, with 0 making areas that retain water, such as swamps and deserts, and 100 making areas that lose any rainfall that comes, such as forests and badlands.

Savagery goes from 0-100, and has no effect on the land, but influences the wildlife that will spawn there.

Volcanism goes from 0-100, with 0 never having volcanoes and 100 always having them, unless a maximum is otherwise specified in the advanced options\[Verify\].

For more information, see biome.

## Resetting the World Painter

[1]

This is a link to the relevant thread on the Bay12 forums.

If you have inadvertently entered and exited the World Painter and are receiving world rejections, re-enter the world painter and click "Will be saved" to toggle the parameters to "Randomize at gen".
