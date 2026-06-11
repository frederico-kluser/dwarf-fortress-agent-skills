# Dipscript

> Fonte: [Dipscript](https://dwarffortresswiki.org/index.php/Dipscript) — Dwarf Fortress Wiki (GFDL/MIT)

A **dipscript**, or "diplomat script", is what controls the behavior of visiting diplomats when they meet with your nobles. Dipscripts were originally used to trigger special events at specific points in the lifetime of one's fortress (such as undead invasions), but much of this was stripped out by the time the first version of *Dwarf Fortress* was actually released.

Only 5 different dipscripts are ever executed during gameplay, and they are defined in records 13-17 of the game's "index" file: ELVES_FIRSTCONTACT, HUMAN_STANDARD, DWARF_LIAISON, HUMAN_TRADE, and ELVES_STANDARD. The dipscript files themselves are compressed - with the proper tools, editing them is fairly straightforward.

## Script Tokens

| Token | Meaning |
|----|----|
| INITIAL_LOAD | Presumably indicates that the dipscript should be loaded on game startup instead of on-demand. All of the default dipscripts specify this, as the game does not appear to contain logic for dynamic loading. |
| DIPSCRIPT:name | Specifies the script's name. Must be one of the names defined above if you want the game to ever execute it. |
| VAR:type:name | Declares a variable. Type can either be UNIT or LONG. |
| SETVAR:dest_class:dest_name:src_class:src_name | Sets one variable to another. See below for more information. |
| IF:class1:name1:comparison:class2:name2 | Compares the two specified variables and performs the following script steps if the condition is true. |
| ELSE | Performs the following script steps if the above IF condition was false. |
| ENDIF | Ends the above IF statement |
| TEXTVIEWER:filename:varname | Opens a text viewer using the specified filename (located within data/dipscripts/text). Second parameter is optional - if specified, indicates a LONG script variable which will be set based on the hyperlink selected. |
| CONSTRUCTTOPICLIST | Builds a list of appropriate discussion topics (discuss current agreement, request peace treaty, propose tree quota, establish land holder, promote land holder, establish export agreement, establish import agreement, make small talk, or report recent world events), based on the type of civilization the diplomat came from. |
| TOPICDISCUSSION | Discuss all topics selected via CONSTRUCTTOPICLIST. |
| DISCUSS:length | Inserts a delay into the meeting. Valid lengths are SHORT (500-1000 steps, about a half a day) and LONG (2-4 days). |
| HISTORY_DIPEV:type | Records a historical event once the diplomat leaves your fortress. The only valid event type is FIRSTCONTACT, used by the Elves to control whether or not they will send their diplomat to propose logging quotas. |
| ACTION:type:subtype | Has no effect. In previous versions, DREAM:UNDEAD_ARMY would cause one of your dwarves to have "a terrifying nightmare about an army of the dead". |
| DIPEVENT:parm1:parm2:parm3:parm4:parm5 | Has no effect. Most likely, pre-release versions used this to perform special actions. |
| INVASION:parm | Has no effect. Most likely, pre-release versions used this to trigger invasions of specific types. |

## Variables

Dipscripts (and their text screens) can make use of any number of special variables. Each variable has a class, name, and type.

### Readable variables

| Class | Name | Type | Description |
|----|----|----|----|
| GLOBAL | DIPLOMACYFLAG_SUCCESS | Integer | Value 4, to be used with DIPEV:ADD_FLAG and DIPEV:REMOVE_FLAG. |
| GLOBAL | DIPLOMACYFLAG_FAILURE | Integer | Value 2, to be used with DIPEV:ADD_FLAG and DIPEV:REMOVE_FLAG. |
| GLOBAL | YOURCIV | Entity | Your fortress's parent civilization. |
| GLOBAL | YOURFORT | Plot Info | Your fortress itself. |
| GLOBAL | TREESREMOVED | Integer | The number of trees that have been destroyed at your fortress, whether by cutting them down or by smashing them with ballista bolts. |
| GLOBAL | NULL | Null | A null pointer. Used during comparisons to detect unset variables. |
| GLOBAL | LOCAL_LARGE_PREDATOR | Creature Definition | A random large predator that can be found near your fortress. |
| GLOBAL | RANGE.min.max | Integer | A random number between 'min' and 'max'. |
| GLOBAL | number | Integer | An explicit integer value. |
| DIPEV | DIPLOMAT | Unit | The diplomat who is meeting with your noble. |
| DIPEV | ASSOCIATE | Unit | The diplomat's associate. By default, this is null. |
| MEETING | ACTOR | Unit | The diplomat who is meeting with your noble. |
| MEETING | NOBLE | Unit | Your noble who is meeting with the diplomat. |
| DIPSCRIPT | varname | Integer or Unit | A variable you have declared using the VAR command above. |

### Writable variables

| Class | Name | Type | Description |
|----|----|----|----|
| GLOBAL | TREESREMOVED | Integer | The number of trees that have been destroyed at your fortress. |
| DIPEV | ADD_FLAG | Integer | A specific flag to set in the diplomacy event. Valid values are GLOBAL:DIPLOMACYFLAG_SUCCESS (4) and GLOBAL:DIPLOMACYFLAG_FAILURE (2). |
| DIPEV | REMOVE_FLAG | Integer | A specific flag to set in the diplomacy event. Valid values are GLOBAL:DIPLOMACYFLAG_SUCCESS (4) and GLOBAL:DIPLOMACYFLAG_FAILURE (2). |
| DIPEV | DIPLOMAT | Unit | The diplomat who is meeting with your noble. Changing this may have unexpected effects. |
| DIPEV | ASSOCIATE | Unit | The diplomat's associate. If you set this to a unit in your fortress, then that unit will bid you farewell and depart from your fortress with the diplomat. |
| MEETING | ACTOR | Unit | The diplomat who is meeting with your noble. Changing this may have unexpected effects. |
| MEETING | NOBLE | Unit | Your noble who is meeting with the diplomat. Changing this may have unexpected effects. |
| DIPSCRIPT | varname | Integer or Unit | A variable you have declared using the VAR command above. |

### Displayable variables

Some of the above variables can be displayed in custom screens opened by the TEXTVIEWER command using the syntax \[C:VAR:class:name\] (to set the text color) and \[VAR:format:class:name\] to output the value in a particular format. Certain formats are only valid with specific types - trying to use it on the wrong type will likely result in a blank string.

| Format | Type | Description |
|----|----|----|
| TITLENAME | Unit | Displays the unit's profession. Noble professions will be prefixed with "the ". |
| HISTNAME | Historical Figure | Displays the historical figure's name and race. |
| NAME_PLURAL | Creature Definition | Displays the plural name for the creature selected. |
| NATIVENAME | Unit | Displays the unit's name in its native language. |
| NATIVENAME | Entity | Displays the civilization's name in its native language. |
| NATIVENAME | Plot Info | Displays your fortress's name in its native language. |
| TRANSLATEDNAME | Unit | Displays the unit's name, translated into English. |
| TRANSLATEDNAME | Entity | Displays the civilization's name, translated into English. |
| TRANSLATEDNAME | Plot Info | Displays your fortress's name, translated into English. |
| \[anything\] | Integer | Displays the number in decimal form. |
