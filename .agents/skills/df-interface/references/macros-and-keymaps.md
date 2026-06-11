# Macros and keymaps

> Fonte: [Macros and keymaps](https://dwarffortresswiki.org/index.php/Macros_and_keymaps) — Dwarf Fortress Wiki (GFDL/MIT)

Playing *Dwarf Fortress* means lots of typing. The game has an internal macro/keymap system. Using it or any external program can save you a great deal of time when dumping, rewalling, designating, and so forth.

## DF macros

### Creating macros

The controls for creating macros within DF are as follows:

- \+ = record (and finish recording)

- \+ = save

- \+ = load

- \++number = set to repeat \[number\] of times (maximum of 99)

- \+ = play

To create a macro, press + to begin recording your actions. When you have recorded all the actions that you want, stop recording by hitting + again and save (+) the macro. The macro is then added to your macro list. To load a macro from the list just press +. If you just recorded the macro, it is loaded even without saving. You can then play the macro by pressing + whenever you want. You can also set a macro to repeat by pressing +, typing a two digit number, and then pressing + to begin the playback session. Moving your mouse from the playing window, or otherwise losing focus on Dwarf Fortress, is an annoying way a good way to interrupt a macro session from continuing (also the only known method).

There is a directory data/init/macros for them. The macros are saved in .mak format. The first line of the macro file must match the filename, or the file will not be recognized as a valid macro. Even a recorded file for a simple macro - for example to create a 3 tiles wide ramp - may already consist of up to 50 commands listed. This is because every possible binding of the key pressed is included in the macro and put in a block (and for ramp has many by default).

    pressing_enter_recorded
            SELECT
            CLOSE_MEGA_ANNOUNCEMENT
            WORLD_PARAM_ENTER_VALUE
            SETUPGAME_SAVE_PROFILE_GO
            D_BURROWS_DEFINE
            D_MILITARY_ALERTS_SET
        End of group
            CUSTOM_CTRL_R
        End of group
    End of macro

For this example the recording was started, enter was pressed and the recording was stopped. When using this macro every underlying command in the file will be called, if possible. If you are in the designation menu, it will react as a select, the other commands will be ignored. If you are in the burrow menu, it will work like pressing enter there. The macro alway ends with a block containing the end of its recording. But executing macros seems to ignore this command. If you have changed your key bindings you'll get another result, because the underlying commands are recorded, not the keys pressed.\
When creating or editing your own macros it is a good idea to use only those commands you really want.

    ramping_created
            DESIGNATE_RAMP
        End of group
            CURSOR_DOWN_Z
        End of group
            SELECT
        End of group
            CURSOR_RIGHT
        End of group
            CURSOR_RIGHT
        End of group
            SELECT
        End of group
            CURSOR_LEFT
        End of group
            CURSOR_LEFT
        End of group
            CURSOR_UP
        End of group
    End of macro

This selfmade example will designate a 3 tiles wide ramp one z-level below and place the cursor to make the next execution of the macro continue the way down. The first line has to be the name of the file. You can see that there are grouping tags for every single keypress. These are important for a working macro.\
It is unknown if there is the possibility of creating loops/iterations, other programming features or comments.\
Removing macros in-game can be done by pressing and then selecting Keybindings \> Macros. Press on the macros you want to delete, then press and select "Save and Exit". This will also delete the corresponding macro file permanently. Otherwise, you can delete the corresponding .mak file from the init/macros/ folder, although that will only take effect the next time DF is run.

Changing macros while the game is running uses a counter-intuitive process. After editing the macro file, create a backup of it and remove the macro as described earlier. However, before saving the changes, place the backup file on the init/macros/ folder. Then save the changes and reload the macro with +.

Adding macros is also possible, resorting to the macro changing process. A "dummy" macro would be recorded and saved, then deleted. The macro that would be added would replace the dummy file.

    macroscreen
            OPTIONS
        End of group
            STANDARDSCROLL_DOWN
            CURSOR_DOWN
        End of group
            STANDARDSCROLL_DOWN
            CURSOR_DOWN
        End of group
            SELECT
        End of group
            SELECT
        End of group
    End of macro

### Tuning macros

The fewer commands a macro consists of, the faster it runs. This means you should avoid unnecessary steps by optimizing the "path" of your designations.

The second and most effective way to increase speed is to remove all unnecessary commands DF recorded. These may be found in the init/macros folder and edited with any basic text editing program. The extra commands are ignored by the game but they still take time to be processed. To move a cursor 3 (up/down) or 4 (right/left) commands are recorded, most other keys are bound to more commands. Pressing for example records more than 30 commands.

For example the code below is a simple macro that selects the digging designation, moves one square to the right, and then designates that tile to be dug.

    example
            OPTION4
            CUSTOM_D
            WORLD_PARAM_DELETE
            LEGENDS_EXPORT_DETAILED_MAP
            A_COMBAT_DODGE
            A_STATUS_DESC
            A_SLEEP_DAWN
            A_INV_DROP
            SETUP_NOTES_DELETE_NOTE
            BUILDJOB_TARGET_RIGHT
            BUILDJOB_BED_DORMITORY
            BUILDJOB_FARM_WINTER
            BUILDJOB_RACKSTAND_KILL2
            HOTKEY_BUILDING_DOOR
            HOTKEY_BUILDING_CONSTRUCTION_STAIR_DOWN
            HOTKEY_BUILDING_WORKSHOP_DYER
            BUILDING_ORIENT_RIGHT
            BUILDING_ADVANCE_STAGE
            BUILDING_TRIGGER_MAX_SIZE_DOWN
            BUILDING_TRACK_STOP_DUMP
            HOTKEY_GLASS_DOOR
            HOTKEY_CARPENTER_DOOR
            HOTKEY_MASON_DOOR
            HOTKEY_TRAP_DOOR
            BUILDJOB_STOCKPILE_DELETE_CHILD
            STOCKPILE_ARMOR
            STOCKPILE_SETTINGS_DISABLE
            STORES_DUMP
            ORDERS_DYED_CLOTH
            ORDERS_ZONE_DRINKING
            D_DESIGNATE
            D_HAULING_STOP_LC_DIR
            D_BURROWS_DELETE
            D_NOTE_DELETE
            D_NOTE_ROUTE_DELETE
            D_BITEM_DUMP
            D_LOOK_DUMP
            ARENA_CREATURE_SIDE_UP
            ASSIGNTRADE_SORT
            DESIGNATE_DUMP
            DESIGNATE_DIG
            ITEM_DUMP
            D_MILITARY_DISBAND_SQUAD
            D_MILITARY_ALERTS_DELETE
            D_MILITARY_AMMUNITION_REMOVE_ITEM
            D_MILITARY_DELETE_UNIFORM
            STRING_A100
        End of group
            STANDARDSCROLL_RIGHT
            CURSOR_RIGHT
            WORLD_PARAM_INCREASE
            A_MOVE_E
        End of group
            SELECT
            CLOSE_MEGA_ANNOUNCEMENT
            WORLD_PARAM_ENTER_VALUE
            SETUPGAME_SAVE_PROFILE_GO
            D_BURROWS_DEFINE
            D_MILITARY_ALERTS_SET
        End of group
            SELECT
            CLOSE_MEGA_ANNOUNCEMENT
            WORLD_PARAM_ENTER_VALUE
            SETUPGAME_SAVE_PROFILE_GO
            D_BURROWS_DEFINE
            D_MILITARY_ALERTS_SET
        End of group
            CUSTOM_CTRL_R
        End of group
    End of macro

Here is the same code but optimized through removal of all the excess commands. Each macro also contains an addition CUSTOM_CTRL_R command at the end that may be removed as well.

    example
            DESIGNATE_DIG
        End of group
            CURSOR_RIGHT
        End of group
            SELECT
        End of group
            SELECT
        End of group
    End of macro

The third way to increase the speed of macros is to change settings in the init-files. In the base init file (data/init/init.txt)") you will find the follow lines:

    If you set KEY_REPEAT_ACCEL_LIMIT above one, then after KEY_REPEAT_ACCEL_START repetitions
    the repetition delay will smoothly decrease until repetition is this number of times faster
    than at the start.

    [KEY_REPEAT_ACCEL_LIMIT:8]
    [KEY_REPEAT_ACCEL_START:10]

    This controls the number of milliseconds between macro instructions.

    [MACRO_MS:15]

- The `MACRO_MS` setting is the number of milliseconds between macro instructions (the default, 15, allows 1000/15 instructions per second, or about 66). Decreasing this makes macros run **faster**, although decreasing it too far can make the game unresponsive while the macro is running.
- The `KEY_REPEAT_ACCEL_START` and `KEY_REPEAT_ACCEL_LIMIT` settings are unrelated to macros (except while recording). See Technical tricks for more information.

## External utilities

### QuickFort

A spreadsheet-driven construction tool for Dwarf Fortress. Converts CSV files containing a "graphical" (or at least two-dimensional) representation of what you want to build into efficient DF macros. Comes with a number of scripts to get you started, some of them quite complex.

### AutoHotKey

AutoHotKey is a powerful easy-to-use scripting language that can simulate keystrokes. (among other functions)

To started:

1.  Go to the AutoHotKey website and download AutoHotKey. Installation is simple and the program uses very little system resources.
2.  Read through their quick-start guide and start write your macro scripts (file type .ahk), which may contain any number of commands. You activate scripts by double-clicking .ahk files or by assigning hotkeys to your macros. Both of these can be done at any time - even right in the middle of a game. AutoHotKey also allows for automated activation of scripts.

### Fluxbox + xvkbd

For linux, it's a quite cool solution. It's possible to create macros with outside tools, like fluxbox (linux window manager) + xvkbd (linux virtual keyboard for kiosks, with some macro capabilities). See the documentation here.

Pros:

- Faster execution
- Easier script writing
- Portable code

Cons:

- Sometime needs timing
- Need xvkbd (Linux at least)
- Need some special key reservation

**Please see also the 40d macros page, as much of what is there works perfectly fine. If you can verify it works, please move it to this page.**

## Useful Macro Ideas

The following are macro ideas that other players have found useful, and may make management of your fort easier. For most macros it's highly recommended to **pause the game** before hitting the play button to avoid your dwarves causing unexpected behavior, i.e. a dwarf giving birth or anything else that auto-zooms to a different location.

### Large Bedrooms

Bedrooms, especially larger ones or large blocks of identical ones, involve a lot of designations and build orders. These macros are designed to streamline the process. For all of these mass-building macros you may wish to temporarily forbid any of your artifact or masterwork furniture, to avoid giving overly-valuable items to your dwarf peasantry.

#### Placing Beds

So you've recorded a macro to dig out a series of bedrooms, and now you have to fill them. Bring up the uild menu, select ed, and go the first position you want to place a bed in.

Start a new macro (+) and place the bed (selecting the first bed from the list), then move to the next bedroom in sequence. Repeat this until you reach the end of the row. If you are placing beds into multiple long rows of bedrooms, move the cursor to the first bed in the next row to make things faster. Turn off macro recording (+), but don't exit the build menu. You can then save your macro if you wish, though it's not necessary. Play the macro (+), and you have just laid out another row. Repeat until you have enough bedrooms or you run out of beds.

#### Placing Coffers

Placing coffers (but *not* bags) requires an extra step. Pause the game (you *did* remember to pause before playing macros, didn't you?) and go to the Stocks menu. Forbid all bags, regardless of what's inside them or what they're being used for (this is temporary). Exit to main screen and repeat the steps above, this time placing containers in your rooms. You will end up placing only chests / coffers / boxes, ignoring any bags. Repeat and play back for the rest of your bedrooms, then un-forbid your bags before un-pausing the game.

#### Resizing Rooms

If the bedroom is finished (at least all the beds are hauled to place), you may want to create a new macro to designate each room as a bedroom. uery the building and select the first bed. Start a new macro and press to designate it as a bedroom, then press + a few times to fill the available space. If you are fine with the size of the bedroom you can press enter, move on to the next bed, and repeat this for the whole row. If you want bedrooms that fill all the room and not all your bedrooms are the same size, you may have to press + a bit more or less for the larger cases. Repeat this for the rest of the rows as above.

### Mass Selector

With this macro you can select a lot of things at once. Extremely helpful if you want to sell a lot of junk to the caravans. Record , then about 10-25 times in a row. (For some menus you may wish to use , then ) When the caravan arrives, your dwarves haul all the bins to your Trade Depot for sale as normal. At the trade menu, load the macro and play it as many times as you like. The macro will select all the items in your "for sale" list, saving the bins you carried them in for later use. Be sure to at least browse through the final list once you're done to avoid selling items you didn't wish to sell, i.e. items that were in the same bin as your trade goods that you wish to keep, or non-wood items if you're trading with the Elves.

### Mass Trap Builder

It's basically just the same as building items in bedrooms, but for traps. Useful for populating entire hallways with weapon or stone-fall traps.

### Custom Uniforms

Since custom uniforms are not saved from one fortress to another, it can be tedious to remake them after each new embark. Instead, you can record a few macros to create each of your custom uniforms (Axedwarves with full armor, Wrestlers with light armor, Archers, Civilians, etc.) It is recommended to start recording each macro from the main window, before entering the (m)ilitary screen, and to avoid naming the uniform as part of the macro. Because of the way the uniform menu is set up, you should also be careful not to move the cursor back into the uniform list during the recording of your macro, or problems may arise. As always, pause the game before you start recording or playback.

### Digging in Odd Directions/Shapes

While it is very simple and fast to designate mining in any of the 6 possible linear directions (North, East, South, West, Up, and Down) in very long sections, specialized mining, such as diagonal hallways, circular rooms, etc., are more difficult. It may be worth, for example, recording 4 macros that dig a short section of 3-tile wide hallway in non-standard directions (NE, NW, SW, and SE). This way, when you want a hallway dug at a 45 degree angle you just load the appropriate macro and keep playing it until the hallway is the desired length.

### Downshafts

Simple up/down stairs are easy to do, but if your standard fort layout includes stairs with empty spaces around them, like so...

           (rooms)

            %%..%%
            %....%
    (more   ..XX.. (still
     rooms) ..XX..  more
            %....%  rooms)
            %%..%%

           (etc...)

...it can be cumbersome to designate all of that for multiple Z-levels at once. Instead, create a macro from one reference point (say, the top-left staircase of the 2x2 shaft or some such) and hit record, then designate the staircase area as you see fit. Move the cursor back to your reference point and move down one Z-level, then stop recording. You can now load it up and play it wherever you need it.

For added awesomeness, trim out the extra commands in a text editor as described above. Then highlight the whole macro and copy/paste it into a new file, copying the commands 5 times or as many as you want. Then save the new macro as a separate file (be sure to rename it at the top of the macro text as well). In this way you can have easy-to-use macros for digging your own standard stairwell. Separate macros for 1 level, 5 levels, and 20 levels seem to work well.

## Troubleshooting Scripts

Users may experience some issues in getting external scripts to work, particularly when using looping scripts when experiencing low frame-rates.

- If experiencing low frame-rates, try adding delays ("Sleep 100" to pause for 100 milliseconds for example) within macros to allow the interface to keep up. If there are nested loops, sometimes adding a pause at the end of an inner loop is all that is needed to flush the keyboard buffer.
- Another way to add delay during and after each simulated key press is to put SetKeyDelay, 40, 40 at the start of the macro.
- Make sure that Dwarf Fortress maintains focus. IM windows are the enemy! Who needs friends anyhow? You've got Dwarf Fortress.
- This may go without saying, but most macros assume standard key-mappings. If you're using non-standard ones, you may have to edit the macro to get it to work.
- Visiting liaisons can bring up screens that eat keystrokes, throwing a long-looping script out-of-phase with where it expects the game to be. Wait for the farewell screen before running a long script, or just pause the game beforehand.
- The SendPlay function supports keys that the Send function does not, for example . According to the AutoHotKey documentation, SendPlay may also be better at preventing dropped keystrokes.

### General Fortress Mode Hotkeys Script

An attempt at speeding up various designations. Includes an up/down stair builder, a fast move up/down, and some select-and-advance keys. Please see user:DDR#Dwarf_Fortress_General_AHK_Script.
