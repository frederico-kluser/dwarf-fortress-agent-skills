# Modding pitfalls

> Fonte: [Modding pitfalls](https://dwarffortresswiki.org/index.php/Modding_pitfalls) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a guide to getting started with modding, see Modding.*

\
When making a mod, there's a *lot* of things that can go wrong. Here's a bunch of common pitfalls that people might fall into.

## Errorlog

The error log is in a file called `errorlog.txt`, located in the root directory of the game (the same folder as Dwarf Fortress's executable). Check that before you read on; your problem may in fact be in there.

## My mod won't load

Make sure you have an info.txt file and that your mod is in the root directory of the `mods` folder (`Dwarf Fortress/mods`), **not** in the `mod_upload` folder. *Dwarf Fortress* doesn't read `mod_upload` for using mods, but only to publish them to the Steam Workshop.

Make sure you have **every required token in your info.txt!** Also, make sure that the mod has a [`[NUMERIC_VERSION]`](/index.php/Mod_info_token#NUMERIC_VERSION "Mod info token") which is an integer, and greater than or equal to [`[EARLIEST_COMPATIBLE_NUMERIC_VERSION]`](/index.php/Mod_info_token#EARLIEST_COMPATIBLE_NUMERIC_VERSION "Mod info token").

So, this is acceptable:

    [NUMERIC_VERSION:1]
    [EARLIEST_COMPATIBLE_NUMERIC_VERSION:1]

But this isn't:

    [NUMERIC_VERSION:1.05]
    [EARLIEST_COMPATIBLE_NUMERIC_VERSION:1.0]

Nor is this:

    [NUMERIC_VERSION:1]
    [EARLIEST_COMPATIBLE_NUMERIC_VERSION:5005]

## My mod loads, but my creature/plant/entity won't

Make sure the file has the correct name, and starts with the following lines:

1.  A filename that refers to the type of objects contained therein. **Creature files must start with `creature_`, entity files must start with `entity_`, and so on.**
2.  The filename on the first line of the file.
3.  `[OBJECT:type]`, where "type" is replaced with the relevant object type, `[OBJECT:CREATURE]` etc

If your edit meets all of the above criteria, and still won't load, you can ask, or look for, specific advice from these modding resources.

## My mod won't update

*Dwarf Fortress* only reads from `installed_mods` (`Dwarf Fortress/data/installed_mods`) when loading a world. If you have made changes to your mod since installing it, you will need to propagate your edits from `mods` to `installed_mods` to see them in-game. For quick testing, the easiest way to do so is by deleting the old copy in `installed_mods`. You can also increase [`[NUMERIC_VERSION]`](/index.php/Mod_info_token#NUMERIC_VERSION "Mod info token") and [`[EARLIEST_COMPATIBLE_NUMERIC_VERSION]`](/index.php/Mod_info_token#EARLIEST_COMPATIBLE_NUMERIC_VERSION "Mod info token") to create a new copy.

As of 52.01, the game defaults to non-portable storage. Even if working out of the portable copy of `mods`, this setting copies installed mods into the game's AppData folder.

Although you can edit currently-installed mods directly from the `installed_mods` folder , this often leads to confusion over where/how errors or bugs are occurring, as well as increasing the risk of accidentally overwriting edits made there. Applying newly-edited raws by working from the `mods` folder and loading them in from the in-game menu can avoid many oversights in troubleshooting.

## My mod causes glitches in world generation/won't work with '(other mod)'

If you are editing an object already present in the vanilla raws, you will cause duplication errors if you don't use the CUT or SELECT functions to modify that object. The modding page lists which objects can be edited using these functions.

If your mod cuts an object and is loaded after another mod that edits the same object, your mod will completely replace that mod's edit. Generally speaking, if you are merely adding tags/tokens to an object, you can achieve the same results with SELECT, which effectively appends those edits to an already existing vanilla object rather than replacing it. At the moment, only creature objects can have tags removed without the use of the CUT function, by making use of the more advanced creature variation tokens.

## Creatures

### My civilization lives in "Nothing hamlets", "Nothing fortresses" or similar

You forgot to add a [`[NAME]`](/index.php/Creature_token#NAME "Creature token"). These use [`[NAME]`](/index.php/Creature_token#NAME "Creature token") rather than [`[CASTE_NAME]`](/index.php/Creature_token#CASTE_NAME "Creature token"), so if you have a [`[CASTE_NAME]`](/index.php/Creature_token#CASTE_NAME "Creature token") but no [`[NAME]`](/index.php/Creature_token#NAME "Creature token"), you'll see the individuals having a correct species name but their sites not having one.

### Creature edits not working or duplicate creatures/creature materials appearing in-game

You might have added a duplicate creature entry by forgetting to either SELECT or CUT the pre-existing vanilla creature entry.

## Reactions

### My custom reaction isn't appearing in the game

Make sure you have added the corresponding tokens to the relevant civilization entity object ([`[PERMITTED_BUILDING]`](/index.php/Entity_token#PERMITTED_BUILDING "Entity token")/[`[PERMITTED_REACTION]`](/index.php/Entity_token#PERMITTED_REACTION "Entity token")).

### My custom armor/clothing reaction won't let the user choose the size

Currently, only the internal make armor/clothing tasks can set the product size via the Details screen; custom reactions cannot do this. If you want to be able to size things when ordering them to be made, they have to be included in the entity using the ARMOR token. The size selection menu only displays if armor/clothing made from cloth, leather, or weapons-grade metal is being produced.

### Workers are not using items from barrels even though they're using them otherwise

When defining reagents, not including an item type (e.g. PLANT:NONE, PLANT_GROWTH:NONE) will cause workers to be unable to find otherwise eligible reagents when they're stored in barrels.
