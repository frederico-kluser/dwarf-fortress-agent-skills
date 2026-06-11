# Audio

> Fonte: [Audio](https://dwarffortresswiki.org/index.php/Audio) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

*For "sounds" that disturb Dwarves while they sleep, see Noise.*

*Dwarf Fortress* contains music tracks which play at various points in game, including the main menu theme. Some types of **audio** seem to be triggered by events, while others play randomly while certain criteria are met. These seem to include some weather sounds, wild ambience, building sounds, river etc.

According to Tarn, there are different settings for every track. One depends on the caverns being opened, one plays only after the second year, one is a first year track. Strike the Earth plays when you first embark, and then gets mixed in with the others afterward. And so forth; there's a raw format for this so you can change it if you like.[1]

Game Audio settings can be adjusted in the settings menu.

## Modding

\
All sound and music files used by *Dwarf Fortress* are stored in the .ogg format within the `/data/sound/` subfolders. You can replace the existing ogg files with different ones. That has to be performed manually and isn't actually supported by the game. You can also change some of the definitions of when certain musical cues are played, using available music tokens and sound tokens in the raw files found in `\data\vanilla\vanilla_music\`. You can add new music and sounds with raws in the sound folderv0.50.09, formatted like so:

## Identifiers

To allow the game to read audio files consistently, they must be given an identifier. Identifiers can be any arbitrary string, just like any other raw object.

Identifier files are stored in a mod's `sound/` directory (not the `objects/` directory, where the logic for playing them is stored), and their name must start with `sound_file_` or `music_file_`.

Their first line must be the filename, followed by ` [OBJECT:SOUND_FILE]` or `[OBJECT:MUSIC_FILE]` respectively.

    sound_file_example
    [OBJECT:SOUND_FILE]
    [SOUND_FILE:]
        [FILE:file name]

    music_file_example
    [OBJECT:MUSIC_FILE]
    [MUSIC_FILE:]
        [FILE:file name]
        [AUTHOR:author name]
        [LOOPS] optional
        [TITLE:piece title]

|  |  |  |
|----|----|----|
| Token | Arguments | Extra Information |
|  FILE | path to audio | (Required) Usually stored as `sound/...ogg`. |
|  AUTHOR | string | (Music only) Displays as the song author on pause menu. |
|  LOOPS |  | (Music only) If set, should play continuously until interrupted.\[Verify\] |
|  TITLE | string | (Music only) Displays as track title on pause menu. |

## Sound effects

All vanilla sound tokens are found within `objects/sound_standard.txt`. All sound definition raws must begin with `sound_`, followed by the `[OBJECT:SOUND]` token that tells the game that the file contains sound definitions.

    [SOUND:]
        [FILE:]
        [ANNOUNCEMENT:]
        ...
        [ANNOUNCEMENT:]

|  |  |  |
|----|----|----|
| Token | Arguments | Extra Information |
|  FILE | sound file | (Required) File identifiers can be any of various hardcoded sounds (all present in the vanilla raws) or custom \[SOUND_FILE\] objects. |
|  ANNOUNCEMENT | announcement(s) | Trigger condition, can use more than one announcement in the list. |
|  SAVAGE_AREA |  | Played randomly in a savage area. |

## Music tracks

All vanilla music tokens are found within `objects/music_standard.txt`. All music logic raws must begin with `music_`, followed by the `[OBJECT:MUSIC]` token that tells the game that the file contains music definitions.

    [MUSIC:TRACK_02]
        [FILE:EXPANSIVE_CAVERN]
            [CARD:EXPANSIVE_CAVERN_CARD_1] for the shuffled deck of short bits
            [CARD:EXPANSIVE_CAVERN_CARD_2]
            [CARD:EXPANSIVE_CAVERN_CARD_3]
            [CARD:EXPANSIVE_CAVERN_CARD_4]
        [EVENT:FIRST_CAVERN_OPENED]
        [CONTEXT:CAVERNS_OPENED]
        [FREQUENCY:UNCOMMON]

|  |  |  |
|----|----|----|
| Token | Arguments | Extra Information |
|  FILE | music file | (Required) Can be any of the many hardcoded files for the soundtrack, or it can be a custom \[MUSIC_FILE\] object. |
|  CARD | music file(s) | Mostly unexplored, listed as a "shuffled deck of short bits." Appears to be played only if no song is currently playing? Before the song proper starts, the game will play a few of these in random order. You can find the parts in the subfolders in ...\common\Dwarf Fortress\data\sound\tracks folder. |
|  CONTEXT | context(s) | This song can randomly play if any of the contexts are met. |
|  EVENT | event(s) | When the chosen event occurs, this song automatically plays and overrides the current song. If multiple songs match the event, a random song will be played from among them. |
|  FREQUENCY | UNCOMMON or RARE | Can be set to 'UNCOMMON' to set the frequency half as often as the other candidates or 'RARE' to make it 1/5 as often as other candidates. |

### Contexts

|  |  |
|----|----|
| Token | Extra Information |
|  ANY | Can play at any time, including in menus. |
|  MAIN | The gamemode is Fortress Mode. |
|  FIRST_YEAR | You are controlling a fortress that is less than one year old. |
|  SECOND_YEAR_PLUS | Your fortress has been around for more than one year. |
|  CAVERNS_OPENED | Your fortress has access to the caverns. |
|  SPRING | The current season is spring. Appears to also be played in Legends mode and the main menu. |
|  SUMMER | The current season is summer. Appears to also be played in Legends mode and the main menu. |
|  AUTUMN | The current season is autumn. Appears to also be played in Legends mode and the main menu. |
|  WINTER | The current season is winter. |

### Events

|  |  |
|----|----|
| Token | Extra Information |
|  JUST_EMBARKED | Plays when founding a new fortress. |
|  SIEGE | A siege is announced. |
|  FIRST_CAVERN_OPENED | A new cave layer is discovered\[Verify\] |
|  MEGABEAST_ATTACK | Plays when a megabeast's arrival is announced. It is unknown if it is also relevant for semi-megabeasts or titans. |
|  FORGOTTEN_BEAST_ATTACK | Plays when a forgotten beast's arrival is announced. |
|  DEATH_SPIRAL | Many citizen deaths have occurred in short succession. |
|  TAVERN_MUSIC_PRESENT | Many units have gathered to perform or watch a musical form. |
|  TAVERN_DANCE_PRESENT | Many units have gathered to perform or watch a dance. |
|  LOST_FORT | Ending a game: a fortress has just been abandoned or retired or your adventurer has died. |
|  FORT_LEVELv51.01-beta28 | May relate to reaching higher ranks of Fortress#Nomenclature.\[Verify\] |
|  FIRST_GHOSTv51.01-beta28 | The first time a ghost attacks.\[Verify\] |

## See Also

- Soundtrack
- ambiences and music snippets
- Soundsense
- Example sound mod by Putnam
