# Text viewer

> Fonte: [Text viewer](https://dwarffortresswiki.org/index.php/Text_viewer) — Dwarf Fortress Wiki (GFDL/MIT)

The **text viewer** is an interface in *Dwarf Fortress* used to display arbitrary formatted text to the player. It is used to read the in-game help, for meetings with diplomats, the various announcements that appear (embark, siege, stymied, etc.), and for various description screens (items, engravings, unit thoughts and preferences, etc.). Of these, the in-game help, meeting text, and announcements all come from files on disk which you can modify with the appropriate tools - after decompressing the files, they are of the following format:

- 32-bit integer, number of lines
- For each line:
  - 32-bit integer, length
  - 16-bit integer, length (same value as above)
  - Readable text of above-specified length

The first line is generally the filename itself, not including any path information.

## Tokens

| Token | Meaning |
|----|----|
| \[TITLE\]text\[/TITLE\] | Specifies the title text visible at the top of the screen (even when scrolling down). |
| \[HELP:filename\] | Specifies which text file will be opened if you press the Help key. The file must be located within the "data/help" directory, and a value of "NO_FILE" will suppress the Help function. |
| \[CHAR:num\] | Inserts an arbitrary symbol. |
| \[IKEY:keybind_name\] | Inserts the text for a custom keybinding, highlighted in green (e.g. "\[IKEY:D_STATUS\]" will appear as ). Keybinding names can be found in data/init/interface.txt. |
| \[C:fg:bg:br\] | Sets the text color. The default text color is 7:0:0. |
| \[C:VAR:class:name\] | Sets the text color appropriate for a specific dipscript variable. Only valid in announcements and diplomat conversation text. |
| \[VAR:format:class:name\] | Displays the value of a dipscript variable. Only valid in announcements and diplomat conversation text. |
| \[LINK:path/filename\]text\[/LINK\] | Inserts a hyperlink which leads to a new help page. The filename path is relative to your Dwarf Fortress base directory, so it should start with "data/help/" for help files. |
| \[LOCX:num\] | Prints the following text 'num' characters from the left margin. Used for creating tables. |
| \[B\] | Ends the current line and inserts an additional blank line. |
| \[P\] or \[R\] | Ends the current line. Doubling these up does not appear to have any effect. |
| \[PAUSE\] | Hides all text beyond this token until the player presses Enter or Space. Can be specified multiple times. |
| \[CHOICE\]text\[/CHOICE\] | Presents a choice to the player which can affect the behavior of a diplomat meeting. This only makes sense when used within dipscripts, and the script must also invoke the text viewer with a variable name to receive the value. The first choice has a value of 0, the second choice is 1, the third is 2, and so on. |
