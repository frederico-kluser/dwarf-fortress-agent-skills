# Announcement

> Fonte: [Announcement](https://dwarffortresswiki.org/index.php/Announcement) — Dwarf Fortress Wiki (GFDL/MIT)

An **announcement** is a message displayed at the top left of the game screen used to indicate something important. Major announcements will pause gameplay and center the camera on the event in question, and game-changing ones will both do that and provide a framed message box presenting the event in question. The announcements list () lists all game announcements in dated order; some (but not all) can be oomed to. (may be more confusing than helpful for v50 but leaving it for now -\> Announcements are not to be confused with eports, which detail combat results.)

When some major or important game-changing announcements occur, the following icon will appear, accompanied with a wooden ticking-like sound effect:\

## Controlling which announcements pause and recenter

You can control which types of announcements do and don't pause and/or recenter the game in the Announcements tab of Settings or by editing the `announcements.txt` file.

#### Announcement Settings

To change the behavior of announcements via the in game Settings, open Settings, select the Announcements tab. Then you'll need to find the setting of interest (announcements.txt wiki page may be able to help). You'll see the available options for each event includes, `Popup`, `Pause`, `Recenter`, and `Alert`. That's the functionality you're most likely to want to adjust. For example, if you want an Alert on the left side of the screen for combat strikes and wounds you would scroll down to 'Strike' and 'Wounds' and change the Alert column to 'Yes' - but don't get ambitious and change all the combat events to Alert, you'll regret it! (one at a time is recommended). More information on what each of these options do, including `Adv`, `Fort`, `Report`, and `Report (Active)` is available on the announcements.txt wiki page (and probably needs to become shared content between these two pages).

#### announcements.txt

To change the behavior of announcements via the `announcements.txt` file you'll need to adjust the `:options` for the particular event of interest. An announcement type containing ***:P**'' will pause when that announcement type is made, and one containing***:R**'' will re-center when that announcement type is made. For example,

`[MIGRANT_ARRIVAL:A_D:D_D:P:R]`

means that the game will pause and recenter upon the announcement of migrants arriving. You could change it to

`[MIGRANT_ARRIVAL:A_D:D_D:R]`

to cause the game to recenter on the arriving migrants, but to not pause the game.

**Note:**

- `/init/announcements.txt` is for the **Default** settings
- `/prefs/announcements.txt` is for the **Current** settings

## Announcements

***Note:** Some of the icons may be incorrect. A question mark placeholder icon is in place of unknown icons. Please update them with the correct ones as soon as possible.*

[TABLE]
