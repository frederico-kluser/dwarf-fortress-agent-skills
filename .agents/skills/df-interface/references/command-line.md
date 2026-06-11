# Command line

> Fonte: [Command line](https://dwarffortresswiki.org/index.php/Command_line) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

The *command line* is used for quick advanced world generation from prefs/world_gen.txt through the Windows command prompt or a Linux terminal window.

Here is the text from "command line.txt":

    See readme.txt for general information about the release.
    See release_notes.txt for information on handling saves and a brief writeup on the changes for this version.
    See file_changes.txt for new init/interface information.

    Dwarf Fortress Command Line Options

    Dwarf Fortress currently offers one command line option, a world generator, suggested by genmac.  You can use it as follows:

    FORMAT: "Dwarf Fortress.exe" -gen
    EXAMPLE:    "Dwarf Fortress.exe" -gen 1 3498 "MEDIUM ISLAND"
    EXAMPLE:    "Dwarf Fortress.exe" -gen 2 RANDOM CUSTOM6

    This will open a silent, introless dwarf fortress, generate a world with the given id number and seed, export the region files and a picture, and finally quit.  The window remains open so you can see what's going on.  You can still abort world generation while it is running.  If you attempt to create a world number that already exists, it will abort immediately.

On Linux, make sure to rename the **df** shell script to something else before putting it in your path, since a **df** command already exists and replacing it with the *Dwarf Fortress* launcher script could mess up your system.

### Mods

After the first gen, a default **Dwarf Fortress/gen_modlist.txt** will be created with an ordered list of vanilla mods ID, which will be used in all future gens.

### Example

To generate **32767** maps on Windows create a file "generate.bat" in the game folder with this content and run.

    --------------------------------------------------------
    :loop
    "Dwarf Fortress.exe" -gen %RANDOM% RANDOM "SMALL REGION"
    goto loop
    --------------------------------------------------------
