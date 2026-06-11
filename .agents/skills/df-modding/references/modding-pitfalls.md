# Modding pitfalls

> Fonte: [Modding pitfalls](https://dwarffortresswiki.org/index.php/Modding_pitfalls) — Dwarf Fortress Wiki (GFDL/MIT)

When making a mod, there's a *lot* of things that can go wrong. Here's a bunch of common pitfalls that people might fall into.

## Errorlog

The errorlog is in a file called "errorlog.txt", located in the root directory of the game (the same folder as Dwarf Fortress's executable). Check that before you read on; your problem may in fact be in there.

## My mod won't load

Make sure you have an info.txt file and that your mod is in the root directory of the *mods* folder (*Dwarf Fortress\mods*), **not** in the *mod_upload* folder. Dwarf Fortress doesn't read *mod_upload* for using mods, but only to publish them to the steam workshop.

Make sure you have **every required token in your info.txt!**

Also make sure that the mod has a NUMERIC_VERSION which is an integer, and greater than or equal to EARLIEST_COMPATIBLE_NUMERIC_VERSION. So this is acceptable:

But this isn't: Nor is this:

## My mod loads, but my creature/plant/entity won't

Make sure the file has the correct name, and starts with the following lines:

1.  A filename that refers to the type of objects contained therein. **Creature files must start with creature\_, entity files must start with entity\_, and so on.**
2.  The filename on the first line of the file.
3.  \[OBJECT:type\], where "type" is replaced with the relevant object type, \[OBJECT:CREATURE\] etc

If your edit meets all of the above criteria, and still won't load, you can ask, or look for, specific advice from these modding resources.

Although you can edit currently installed mods directly from the *installed_mods* folder (*Dwarf Fortress\data\installed_mods*), this often leads to confusion over where/how errors or bugs are occurring, as well as increasing the risk of accidentally overwriting edits made there. Applying newly edited raws by adding them to the 'mods' folder and loading them in from the in-game menu can avoid many oversights in troubleshooting.

## My mod causes glitches in world generation/won't work with '(other mod)'

If you are editing an object already present in the vanilla raws, you will cause duplication errors if you don't use the CUT or SELECT functions to modify that object. The modding page lists which objects can be edited using these functions.

If your mod cuts an object and is loaded after another mod that edits the same object, your mod will completely replace that mod's edit. Generally speaking, if you are merely adding tags/tokens to an object, you can achieve the same results with SELECT, which effectively appends those edits to an already existing vanilla object rather than replacing it. At the moment, only creature objects can have tags removed without the use of the CUT function, by making use of the more advanced creature variation tokens.

## Creatures

### My civilization lives in "Nothing hamlets", "Nothing fortresses" or similar

You forgot to add a NAME. These use NAME rather than CASTE_NAME, so if you have a CASTE_NAME but no NAME, you'll see the individuals having a correct species name but their sites not having one.

### Creature edits not working or duplicate creatures/creature materials appearing in-game

You might have added a duplicate creature entry by forgetting to either SELECT or CUT the pre-existing vanilla creature entry.

## Reactions

### My custom reaction isn't appearing in the game

Make sure you have added the corresponding tokens to the relevant civilization entity object (PERMITTED_BUILDING/JOB/REACTION)").

### My custom armor/clothing reaction won't let user choose size

Currently only the internal make armor/clothing tasks can set the product size via the Details screen; custom reactions cannot do this. If you want to be able to size things when ordering them to be made, they have to be included in the entity using the ARMOR token. The size selection menu only displays if armor/clothing made from cloth, leather, or weapons-grade metal is being produced.

\]\]
