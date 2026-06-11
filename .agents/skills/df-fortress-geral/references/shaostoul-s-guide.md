# Shaostoul's Guide

> Fonte: [Shaostoul's Guide](https://dwarffortresswiki.org/index.php/Shaostoul's_Guide) — Dwarf Fortress Wiki (GFDL/MIT)

Welcome to my wiki guide! By popular demand I did what I could to make this as easy and simple as I could and not as overwhelming...

There's a ton of information here and it "should" be able to help you with any simple reaction modding problems you run into at the moment.

This WILL be updated with creature editing, entity editing and whatever else.

------------------------------------------------------------------------

**MOST IMPORTANT NOTE FOR MODDING!** - With the way the "new" Dwarf Fortress is, when you are modding the easiest thing to do is just to generate a new world. This new version saves raw and graphic information IN the SAVE-\>(REGION1) folder. If you are editing an EXISTING world, you MUST edit the SAVE folder version and not the normal location for you to see the effects. To follow a safe motto for modding dwarf fortress... If you don't know if it needs a regen, just regen.

It seems many people don't realize the new method of save handling and reaction handling. There are multiple places that have to be altered in order for your custom reaction/building to show up to be used. For example...

If you add a smelting reaction, you have to add the reaction to the "reaction_smelter.txt", you then have to make your reaction permitted on the "entity_default.txt".\
When you add a reaction to the "entity_default.txt" it will be under the \[ENTITY:MOUNTAIN\] listing. Your permitted reaction should look like...\
\[PERMITTED_REACTION:XXXCUSTOM_REACTION_NAMEXXX\]\
When you add your custom building to the "entity_default.txt" it should look something like...\
\[PERMITTED_BUILDING:XXXCUSTOM_BUILDING_NAMEXXX\]\
YOU WILL CHANGE "XXXCUSTOM_REACTION_NAMEXXX" and "XXXCUSTOM_BUILDING_NAMEXXX" TO WHATEVER YOU HAVE IT LISTED AS.\

Now that, that is out of the way.

## Custom Build & Reaction

[TABLE]

## Various Reactions and Information

[TABLE]

[TABLE]

[TABLE]

[TABLE]

[TABLE]

## Finished Reactions/Buildings

### SKILLS

[TABLE]

### TREES & PLANTS

[TABLE]

### MINERALS, STONES, METALS, GEMS

[TABLE]

\]\]
