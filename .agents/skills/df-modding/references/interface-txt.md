# Interface.txt

> Fonte: [Interface.txt](https://dwarffortresswiki.org/index.php/Interface.txt) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|                                                    |
|----------------------------------------------------|
| File |
| prefs                                              |
| interface.txt                                      |

*See Controls for the default key binds.*

**Key bindings** determine how the game responds to the user (you) pressing different keys on their keyboard, numberpad, laptop, whatever.

The game key bindings are stored in **interface.txt**. They can be configured in the Key Bindings section of the in-game options screen or by editing this file directly.

Each action can be bound to any number of keys, either by keyboard location or letter. They can also be given a repeat style which specified what happens when any of the bound keys are held:

|  |  |
|----|----|
| Repeat Style | Behavior |
| Don't repeat | The action does not repeat at all; pressing the key performs the action exactly once, no matter how long it is held. |
| Delayed repeat | The action repeats after a delay of `KEY_HOLD_MS` milliseconds. |
| Immediate repeat | The action repeats immediately. |

## Changing key bindings in-game

When in-game, press Esc to open the options screen and select Key Bindings. This shows the various game mode/screen categories (and Macros).

Selecting one shows all of the bindable game commands in that category. On the left is a list of bindable commands and on the right are options to add bindings and change the action's repeat style. Use the left and right selection keys to move between them.

Use Backspace on a binding to remove it.

For example if you wanted to add 9 to "Select" command (odd, but your choice) you would then select the General category, press right on the first command(Select) and hit Enter on the "Add binding" option to open a key registration prompt and then press 9 and select whether you want to bind by position or by key and hit Enter or if you hit the wrong button Esc (or whatever you have set to "Main menu" or "Leave screen" keys) to abort.

Adding bindings does not remove any other binding that also uses this key. This is almost never what you want, so you'd then have to find any command that is also bound to your added key, or you'll be sending both commands every time.

## Useful custom bindings

### Scrolling without keypad

If you're on a laptop or using a restricted keyboard, using + and  \* to scroll on some menus is inconvenient since it requires the Shift key. To scroll with `-=[]` instead of `-+/*`, add:

|  |  |  |
|----|----|----|
| Category | Command | Key |
| General | Move secondary selector down | = |
| General | Page secondary selector up | \[ |
| General | Page secondary selector down | \] |

### Change z-level without shift

You can use the comma , and period ., rather than \ and \> (the same keys + Shift) for up/down z-levels, thus avoiding the need to use two hands/keys for this common action.

Add the following:

|  |  |  |
|----|----|----|
| Category | Command | Key |
| General | Move view/cursor up (z) | , |
| General | Move view/cursor down (z) | . |

Then remove the following to avoid clashing:

|  |  |  |
|----|----|----|
| Category | Command | Key |
| Dwarf mode | Main: One-Step | . |

## interface.txt

The current key bindings are stored in the `prefs/interface.txt` file, and the defaults in `data/init/interface.txt`: the location of the `prefs` folder depends on the portable mode setting (there can also be a `data` folder there, but if you put a `data/init/interface.txt` there it will not be read).

### Default settings

    Edit

### Key syntax

A key bindings block has this structure:

    [BIND:Action:Repeat_Style]
    [SYM:Modifiers:Key]
    [KEY:Key]

It is made of two parts:

- The `BIND` part, which defines what the key does,
- And the `SYM/KEY<` part, which defines which key the action is mapped to.

#### BIND

`BIND` begins a block of key bindings for a specified action in the Key Bindings menu.

Syntax:

    [BIND:Action:Repeat_Style]

Each `BIND` is followed by a block of one or more key bindings (`SYM` or `KEY`; see below) terminated either by the next `BIND` or by the end of file.

The repeat style is given as one of the following:

|               |                  |
|---------------|------------------|
| String        | Repeat Style     |
| `REPEAT_NOT`  | Don't repeat     |
| `REPEAT_SLOW` | Delayed repeat   |
| `REPEAT_FAST` | Immediate repeat |

It is not possible to specify key bindings with different repeat styles for the same action; if more than one `BIND` exists for the same action, the repeat style of the last `BIND` is used for all bound keys.

Vanilla interface.txt already includes `BIND` entries for all valid actions. It is possible to remove all key bindings for a given action by removing all `SYM` and `KEY` entries after the action's `BIND`, and (optionally) removing the `BIND` itself. This, however, can result in frequent warnings output to the terminal if the game wants to display a key binding for the action (e.g. ;: Movies in the Dwarf Mode side bar; one can mitigate this by closing the side bar with Tab).

#### SYM

`SYM` is used for keys listed as By position in the Key Bindings menu.

Syntax:

    [SYM:Modifiers:Key]

The modifiers are represented as the sum of their codes listed below:

|          |       |
|----------|-------|
| Modifier | Value |
| Shift    | 1     |
| Ctrl     | 2     |
| Alt      | 4     |

For example, `[SYM:0:A]` represents a, `[SYM:1:Enter]` represents Shift-Enter, and `[SYM:6:Left]` represents Ctrl-Alt-←.

The key can be any letter or number, or can be listed by name. This is useful when typing the actual symbol would cause a syntax error (for example, `[SYM:0:]]` and `[SYM:0::]` cause errors instead of representing \] and :), or when the symbol isn't type-able (it's hard to insert a backspace character in a basic text editor without deleting something).

#### KEY

`KEY` is a simpler version of `SYM`, only allowing plain keys (no modifiers). These are listed as By letter in the Key Bindings menu.

Syntax:

    [KEY:Key]

For example, `[KEY:a]` represents the a key.

Unlike the above, the key must be given as an actual symbol. Entries such as `[KEY:]]` and `[KEY::]` work as one might expect, i.e., representing \] and :, respectively.

#### Differences between `KEY` and `SYM`

`KEY` **does** allow special characters **if** they are able to be typed. For example, `[KEY:%]` is equivalent to `[SYM:1:5]`. Note that `SYM` requires the key on the keyboard, while `KEY` requires the letter generated.

### Mac-specific

- Some keys unavailable on the keyboard (such as PgDown) can be generated with the fn key. Dwarf fortress sees these as *independent keys*; the fn key is essentially invisible to DF. There is no modifier code for fn.
- Characters like å aren't recognized when typed as alt-a.
- The Command key is unrecognized by DF and can't be used as a modifier.
