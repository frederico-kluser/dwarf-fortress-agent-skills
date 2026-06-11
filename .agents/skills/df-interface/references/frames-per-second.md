# Frames per second

> Fonte: [Frames per second](https://dwarffortresswiki.org/index.php/Frames_per_second) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*"Step" redirects here. For other uses, see Stairs.*

**Frames per second** in *Dwarf Fortress*, often referred to as FPS or framerate, is the measure of the amount of computational ticks the game calculates in one second. Each tick requires the calculation of unit movement, fluid movement, and many checks for different events, such as cave-ins, damp/warm stone, weather conditions, and much more. **Graphical frame rate** (the typical definition of frames per second) is the speed at which the display refreshes, and is typically slower than the computational frame rate. (With the default settings in a new fortress, one graphical frame occurs every two computational frames.)

Ticks are also known as game calculation **steps**, but note these are not equivalent to creature movement steps.

To display your FPS (frames per second) in *Dwarf Fortress*, change “Show frames-per-second” from No to Yes under game in settings, or change \[FPS:NO\] to \[FPS:YES\] in init.txt, and your FPS will be displayed on the bottom of the screen. The first number is the current frame rate, while the number in parentheses is the current graphical frame refresh rate.

## Maximizing FPS

There are many methods to increase one's framerate, which can be found on the maximizing framerate page. These can be crucial, as a common reason for abandoning forts is that the framerate becomes too low from all the dwarves, animals, and explored tiles having to have calculations performed each tick. This is especially true if one or more of the caverns have been unearthed.

## Controlling FPS

By default, the framerate is set to not exceed 100. This can be changed in the settings under game by editing “Game frames-per-second cap”, or in the init.txt file, under [\[FPS_CAP\]](/index.php/Technical_tricks#FPS "Technical tricks"). Increasing or disabling (`[FPS_CAP:0]`) this setting will allow a fortress to progress more quickly, though eventually there will be a maximum reached as a result of CPU speed limits. This also requires more attention from the player, since designated jobs will be completed or cancelled more quickly, and potentially harmful events─such as wild animals, thieves, and invasions─will occur more frequently in a given span of real time.

Decreasing the FPS cap will slow down the progress of a fortress, though it may be useful if the framerate undergoes large, rapid changes, as it will smooth out the play experience. It can also be useful to slow down the game in order to handle other activities while still allowing the fortress to complete previously assigned tasks, reducing the need to babysit the game.

### Keybindings

By default, the FPS cap can be modified in-game by using Alt-= to increase the FPS cap and Alt-- to decrease it.
