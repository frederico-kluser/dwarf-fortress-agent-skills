# Command line

> Fonte: [Command line](https://dwarffortresswiki.org/index.php/Command_line) — Dwarf Fortress Wiki (GFDL/MIT)

The *command line* is used for generating worlds quickly from the Command Prompt in Windows or a terminal window in Linux. Here is the text from command_line.txt:

    See readme.txt for the license.
    See release_notes.txt for information on handling saves and a brief writeup on the changes for this version.
    See file_changes.txt for new init/interface information.
    See command_line.txt for information on world generation from command lines.
    Go to http://www.bay12games.com/dwarves/faq.html for Frequently Asked Questions and their answers.
    Go to http://www.bay12games.com/dwarves/dev_now.html to see a full list of changes.

    Dwarf Fortress Command Line Options

    Dwarf Fortress currently offers one command line option, a world generator, suggested by genmac.
    You can use it as follows:

    FORMAT: dwarfort.exe -gen
    EXAMPLE:    dwarfort.exe -gen 1 3498 STANDARD
    EXAMPLE:    dwarfort.exe -gen 2 RANDOM CUSTOM6

    This will open a silent, introless dwarf fortress, generate a world with the given id number and seed,
     export the region files and a picture, and finally quit.  The window remains open so you can see
     what's going on.  You can still abort world generation while it is running.  If you attempt to create
     a world number that already exists, it will abort immediately.

On Linux, make sure to rename the **df** shell script to something else before putting it in your path, since a **df** command already exists and replacing it with the *Dwarf Fortress* launcher script could mess up your system.

To generate **32767** maps on Windows create file "generate.bat" in game folder with this content and run.

    --------------------------------------------------------
    :loop
    "Dwarf Fortress.exe" -gen %RANDOM% RANDOM "SMALL REGION"
    goto loop
    --------------------------------------------------------

\]\]
