# Modding

> Fonte: [Modding](https://dwarffortresswiki.org/index.php/Modding) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a list of Dwarf Fortress mods, see List of mods.*

\
**Modding**, or creating mods, refers to modifying the behavior of the base game (vanilla). *Dwarf Fortress* is remarkably moddable.

## Resource Overview

This section serves as a portal to all modding-related pages on the wiki.

Using Mods

- Downloading mods
- Enabling mods in-game

Guides and references

- DF RAWs modding guide
- Modding pitfalls for troubleshooting

- Mod format and Game folders and files
- Official DFRaws repository and Wiki mirror
- Publish on Steam Workshop
- Character table
- String dump

- Source code for Dwarf Fortress's graphics/input/sound
- DFHack modding guide
- Memory hacking, Offset Finding Methods

Where to get help?

- The official modding subforum on the Bay 12 Forums.
- #modding-discussion and #modding-technical channels on Kitfox Games' Discord.
- DFHack questions

Modding tools

- There are several specialized utilities that assist in modding efforts. There is a longer list of them on the Bay 12 Forums.
  - Material Helper by User:Putnam3145, for calculating material properties.
  - DF Tools by User:Jose96xd, a collection of web tools.
  - DFLang (by Igfig) and LangCreate (by Talvieno) for generating translations.
  - Dwarf Portrait by Rose, for visualizing unit bodies.
- Text editors are used in all areas of modding. Use a good text editor to edit files and search into multiple files (like the free Notepad++ for example) or more advanced editors capable of highlighting and formatting the displayed text (like DF RAW Language server)
- Image editors are needed for doing custom graphics. Paint.NET, Photoshop and GIMP are the most used, but whatever supports the .png format will work.

### Documentation

Raw files

These object files, stored in `/data/vanilla/*/objects/`, define various specifics of game items, materials, and creatures, and can be changed using mods to alter how the game behaves. These are text based and can be edited with any text editor, however, editing the vanilla raw files is now discouraged.

See Token reference - It's always good to refer to tokens on the wiki. Even experienced modders have to look up tokens! A list of articles about tokens can be found here.

Graphics files

The `/data/art/` subfolder of Dwarf Fortress is used to store user-customizable tilesets while mods can include their own graphics files.

Reactions

Language and Speech file

Sound and Music files

All sound and music files used by *Dwarf Fortress* are stored in the .ogg format within the `/data/sound/` subfolders. Mods can load new audio files. You can also change some of the definitions of when certain musical cues are played, using available music tokens and sound tokens in the raw files.

An example mod by User:Putnam3145 is available on Github.

Lua scripting

An experimental feature used for procedural generation.

### Best practice

The current best practice is to not modify the original raw files, since most modifications can be made via mods. Mods can add new objects, add tokens to existing objects, and cut objects entirely. You should prefer `SELECT` over `CUT`, and prefer `CUT` over unloading (conflicting with) vanilla raws.

## Guide

This is intended to be a guide to inform those new to *Dwarf Fortress* modding on what elements of the game can be modified, and how. After reading through this guide, a user should be capable of editing creatures, entities, materials *et al*, and creating their own.

Generally, breaking stuff is fine - nothing that can be changed will affect the DF executable, and new additions can be easily removed.

This guide is based on Teldin's guide, originally created for version 0.27.176.39c. Per wiki tradition, it has been updated through all the major releases since then; hopefully it reflects current knowledge.

### Token reference

It's always good to refer to tokens on the wiki. Even experienced modders have to look up tokens! A list of articles about tokens can be found here.

### Basics of DF modding

To make a mod, one must put a folder into the `/mods/` directory in the game's AppData folder or the portable directory. When a mod is first installed, it is copied to `/data/installed_mods/` and the game loads all data from the installed copy. Changes are NOT immediately propagated from `/mods/` to `/data/installed_mods/`. You can create a new installed copy by deleting the old copy or by incrementing the version info - see modding pitfalls for more information. The vast majority of modifications to the game can be done via this method.

Your mod folder must contain a file named "info.txt" and subfolders depending on what your mod includes. The majority of mods will want to have an `objects/` folder, which can define most kinds of game content, and a `graphics/` folder, to add graphics.

     Mod Name
     ├  graphics
     ├  objects
     ├  scripts
     ├   init.lua
     ├  sound
     ├  info.txt
     └  preview.png

The info.txt is formatted like so:

    [ID:my_first_mod]
    [NUMERIC_VERSION:1]
    [DISPLAYED_VERSION:1.0.0]
    [EARLIEST_COMPATIBLE_NUMERIC_VERSION:1]
    [EARLIEST_COMPATIBLE_DISPLAYED_VERSION:1.0.0]
    [AUTHOR:Your Name Here]
    [NAME:My First Mod]
    [DESCRIPTION:A cool mod I made!]

A mod should have all of these. There are a few more tokens, but the above are the important ones.

Most of the game's vanilla content is in the same format as mods. Many text files can be found in the subfolders of the `/data/vanilla` folder - these are the raw files, and using them as a basis for modification is quite easy. For now, we will take a look at one of the existing files. For example, if you open `/data/vanilla/vanilla_creatures/objects/creature_standard.txt`, it should look something like this:

     creature_standard

     [OBJECT:CREATURE]

     [CREATURE:DWARF]
         [DESCRIPTION:A short, sturdy creature fond of drink and industry.]
         [NAME:dwarf:dwarves:dwarven]
         [CASTE_NAME:dwarf:dwarves:dwarven]
         [CREATURE_TILE:1][COLOR:3:0:0]
         [CREATURE_SOLDIER_TILE:2]
     ...

As you can see, each file comprises a header string stating the file name, a second header stating the type of object data it contains, followed by the contents of the file itself. These are all necessary elements of the file, and without them, the file will be ignored by the game.

**In other words, to be recognized by the game, a raw file must have all of the following:**

1.  A filename that refers to the type of objects contained therein. **Creature files must start with creature\_, entity files must start with entity\_, and so on.**
2.  The filename on the first line of the file.
3.  `[OBJECT:type]`, where "type" is replaced with the relevant object type.

Below the headers, there begins a list of entries. Each entry is made up of its own header (in this case, `[CREATURE:DWARF]`), again stating the type of object, and then the object's unique identifier - if an identifier isn't unique, the game will mess up and you'll get some serious, and potentially very trippy, errors. (For example...) Below that, we have the body of the entry, which determines the entry's specific properties.

The body of an entry is made up of a series of "tokens", which are essentially flags that can be added or removed to affect the entry's attributes. Most of these effects are hardcoded: for example, it's possible to make a creature only eat meat with the [`[CARNIVOROUS]`](/index.php/Creature_token#CARNIVOROUS "Creature token") token, but it's impossible to create your own token detailing a specific diet for the creature.

Before we continue, a few key things to remember when modding the raw files:

- Try to avoid modifying the existing raw files when possible. You should make a mod instead!
- When adding files, token identifiers are all you need to include to ensure proper references are maintained. The game searches through all loaded raw files by tokens.
  - For example, you can add a new pair of leather boots and not even have to add it to a file named `item_shoes.txt`, but rather your own file, say `item_shoes_new.txt`.
  - All objects must have a unique token identifier. Adding a consistent prefix or suffix to your mod's objects (ie: `[ITEM_SHOES:ITEM_SHOES_BOOTS_NEW]`) greatly reduces the chance that another mod uses the same token. If two mods define objects with the same token without cutting the other, then they will be incompatible due to duplicated raws.
- When a new world is generated, the mods included are "baked in" and cannot be modified except to be updated—for this, the game checks that the mod used by the save is of a compatible [`[NUMERIC_VERSION]`](/index.php/Mod_info_token#NUMERIC_VERSION "Mod info token").
- There's nothing stopping you from just copying an existing creature/entity/whatever, changing the identifier, and modifying it. This can save you a lot of time, especially when it comes to entities.
- **Check the errorlog.txt in the game's base folder whenever you load the mod**. Many problems show up in there, and it's bad form to publish a mod with errors.

### Modifying the vanilla objects

You should not modify the vanilla raws where they originally are if you can help it. Instead, patch them using the patching functions provided with *Dwarf Fortress* since v50.01.

There are two patching functions: `SELECT` and `CUT`. When `SELECT` is used, it lets you make changes to an object without needing the entire entry to be present in your mod file. When `CUT` is used, it forces the game to not use that object, even though it is still found in the vanilla raws (or in any other mods earlier in the load order). Both of these functions take the form of tokens. These functions are not universally applicable to any token found in any entry, just the following list of base objects:

- CREATURE
- ENTITY
- INTERACTION
- ITEM
- WORD, TRANSLATION, SYMBOL
- INORGANIC
- PLANT
- MUSIC, SOUND
- REACTION

The syntax required for these functions is: `[_:]`. For instance, `[CUT_PLANT:MUSHROOM_HELMET_PLUMP]` cuts the plump helmet object originally defined in the vanilla file plant_standard.txt, so the game will not use that object at all. However, `[SELECT_ITEM_HELM:ITEM_HELM_HELM]` does not select the helm object from the vanilla file item_helm.txt, even though that's how the object appears in that file, because there is no `[SELECT_ITEM_HELM]` token. Instead, the helm would be selected with `[SELECT_ITEM:ITEM_HELM_HELM]`.

For example, if you wanted to mod beards onto dwarven women while also removing elephants from the game:

    creature_mypatch

    [OBJECT:CREATURE]

    [SELECT_CREATURE:DWARF] starts editing DWARF from the end of the entry
        [SELECT_CASTE:FEMALE]
            [BODY_DETAIL_PLAN:FACIAL_HAIR_TISSUE_LAYERS]

    [CUT_CREATURE:ELEPHANT] removes the ELEPHANT creature

Or, say, add your own reaction and building to dwarves:

    entity_mypatch

    [OBJECT:ENTITY]

    [SELECT_ENTITY:MOUNTAIN]
        [PERMITTED_REACTION:MY_REACTION]
        [PERMITTED_BUILDING:MY_BUILDING]

And in any of these, one can add the token `[LOG_CURRENT_ENTRY]` somewhere under one of the objects of the file, which logs the full contents of the object in question to `logs\current_entry.txt`. This can be useful to make sure that the patch is doing what you think it is. For instance if `[LOG_CURRENT_ENTRY]` were added on the next line after `[CREATURE:DWARF]` in your mod file, then the dwarf object would be the object detailed in the log entry.

Note that it is not possible to remove an existing token from most objects using `SELECT` or `CUT` alone. Creatures can make use of [`[CV_REMOVE_TAG]`](/index.php/Creature_variation_token#CV_REMOVE_TAG "Creature variation token"); for other objects, it is currently necessary to `CUT` the entire object and redefine it.

...Speaking of, let's move on to modifying and adding entities.

### Modding civilizations (entities)

Entities - the objects that determine how civilizations work - are stored in vanilla_entities/objects/entity_default.txt (though, like all other files, you may add more). They follow the same format as any other raw file:

     entity_default

     [OBJECT:ENTITY]

     [ENTITY:ENTITYNAME]
         [CREATURE:CREATURETYPE]
         [TRANSLATION:LANGUAGETYPE]
         [BIOME_SUPPORT:BIOMETOKEN:FREQUENCY]
         ...[OTHER TAGS]...

Most of the time, it doesn't matter which order these tokens are in or where they're placed so long as they're below the `[ENTITY:]` identifier, but there are some important exceptions in the case of other files, especially creatures, which can contain a lot of "nested" tokens.

[`[CREATURE]`](/index.php/Entity_token#CREATURE "Entity token") links the civilization with a specific creature defined in a creature file. This is the creature that'll be making up the entity's population, and, therefore, the creature you'll be playing as in fortress or adventure mode if the entity is a playable one. For example, if you wanted to do something silly, you could switch the `[``CREATURE``:DWARF]` entry in `entity_default.txt` with `[``CREATURE``:ELF]` and you would be marching elves around in fortress mode, although they would still use dwarven technology, language and names and so forth. Oh, and before you get any funny ideas - it *is* possible to define more than one creature for a civ, but that won't work in quite the way you probably expect; it will pick only one of the defined creatures at random to use for the civ. Later on, in the creature section, you'll learn about castes, which will provide a much more viable alternative, so try to bear with us until then.

[`[TRANSLATION]`](/index.php/Entity_token#TRANSLATION "Entity token") defines the language file that the entity will be using, which will determine what their native words are for things. This doesn't determine which words they use for naming things, only the way those words are spelled. The default language files are `HUMAN`, `DWARF`, `ELF`, and `GOBLIN`, as well as the generated `GEN_DIVINE` and `GEN_IDENTITY`.v51.06-Lua

[`[BIOME_SUPPORT]`](/index.php/Entity_token#BIOME_SUPPORT "Entity token") defines the biomes that civs will attempt to settle in. The `FREQUENCY` value determines the likelihood of them building there, but also raises an important point: most of the values you'll be setting for things are relative to each other. If one were to type:

     [BIOME_SUPPORT:ANY_FOREST:1]
     [BIOME_SUPPORT:SAVANNA:2]

This would have very much the same effect as:

     [BIOME_SUPPORT:ANY_FOREST:5]
     [BIOME_SUPPORT:SAVANNA:10]

This holds true for a lot of values throughout the files, excluding when it simply doesn't make sense, such as in materials. For more information, see entity tokens.

Besides those mentioned, some fundamental ones are the [`[SITE_CONTROLLABLE]`](/index.php/Entity_token#SITE_CONTROLLABLE "Entity token") token, which lets you control the civ in fortress mode, and the [`[ALL_MAIN_POPS_CONTROLLABLE]`](/index.php/Entity_token#ALL_MAIN_POPS_CONTROLLABLE "Entity token") token, which allows you to play a civ native (non-outsider) in adventure mode. Other tokens that you should pay attention to are [`[START_BIOME]`](/index.php/Entity_token#START_BIOME "Entity token") and the ones regarding sites, but in general, you can just run through the aforementioned list and add or remove what you want.

Also see the creature-level [`[OUTSIDER_CONTROLLABLE]`](/index.php/Creature_token#OUTSIDER_CONTROLLABLE "Creature token") token, which allows you to play in adventure mode as an outsider.

By default, the game chooses a [`[SITE_CONTROLLABLE]`](/index.php/Entity_token#SITE_CONTROLLABLE "Entity token") civ (and therefore a species if there is more than one) at random when starting a fortress mode game. The group selection section on the embark screen lists all available civs and their primary creature.

You can also attempt to discern the civ yourself by the names it uses - this is the realm of symbols, collections of words centered around a specific concept. The civ will use words from whatever symbols are selected for it for various things. This association might be a little confusing at first, so, let's refer to the "MOUNTAIN" entity:

     [SELECT_SYMBOL:WAR:NAME_WAR]
     [SUBSELECT_SYMBOL:WAR:VIOLENT]
     [SELECT_SYMBOL:BATTLE:NAME_BATTLE]
     [SUBSELECT_SYMBOL:BATTLE:VIOLENT]
     [SELECT_SYMBOL:SIEGE:NAME_SIEGE]
     [SUBSELECT_SYMBOL:SIEGE:VIOLENT]

Here, we can see that dwarves will generally name their wars first after words in the "NAME_WAR" symbol group, and then, after words in the "VIOLENT" symbol group. This might, for example, result in a war being named "The War of Carnage". The symbols used for the other types of conflict are arrayed in a similar fashion. It would be trivial to replace the instances of VIOLENT with, say, PEACE and end up with a battle called "The Clash of Calm" or something.

     [SELECT_SYMBOL:ROAD:NAME_ROAD]
     [SELECT_SYMBOL:TUNNEL:NAME_TUNNEL]
     [SELECT_SYMBOL:BRIDGE:NAME_BRIDGE]
     [SELECT_SYMBOL:WALL:NAME_WALL]

The above applies here. Dwarves are fond of naming their roads and tunnels after... roads and tunnels.

     [SELECT_SYMBOL:REMAINING:ARTIFICE]
     [SELECT_SYMBOL:REMAINING:EARTH]
     [CULL_SYMBOL:ALL:DOMESTIC]
     [CULL_SYMBOL:ALL:SUBORDINATE]
     [CULL_SYMBOL:ALL:EVIL]
     [CULL_SYMBOL:ALL:FLOWERY]
     [CULL_SYMBOL:ALL:NEGATIVE]
     [CULL_SYMBOL:ALL:UGLY]
     [CULL_SYMBOL:ALL:NEGATOR]

This section deals with everything else. The things that haven't already been dealt with (hence the `REMAINING`) - such as site names, kingdom names, the names of individuals, and such - will have names from the ARTIFICE and PEACE symbol groups. After that, the dwarf entity is told to cull all inappropriate symbols - this applies to everything (hence the `ALL`) so if the game happens to choose a symbol associated with, say, EVIL for one of the battles, it'll scrap that name and try again. This sort of thing adds a lot of flavour to DF's entities and can account for a lot of a civ's perceived personality.

Another basic thing to note: any entity token that's dealing with weapons, armor, clothing, etc., will state the items that the civ can build natively, not necessarily the ones they can wear or use. For example, you could create a species with no clothes specified, but then rob a clothes shop in adventurer mode and wear everything you want, or give them weapons that are too large to wield and they could sell them, but not use them.

An easy method of creating a civilization is just to copy-paste a similar one to the bottom of an entity file and edit things to your liking. Remember to always change the civ's `[ENTITY:]` identifier! This can be anything, so long as it's not already existing.

At the end of some of the default entries you'll find a list of positions, both ones that'll directly affect you in fort mode (such as nobles) and ones that'll primarily affect worldgen and adventure mode. A list of the tokens applicable to positions can be found here; they don't require a great deal of explanation, but that can be found in Advanced Entity Position Mechanics.

#### Trade

The following entity tokens affect the appearance of trading caravans:

- [`[ACTIVE_SEASON]`](/index.php/Entity_token#ACTIVE_SEASON "Entity token") - Defines the seasons when an entity may visit your fortress.
- [`[PROGRESS_TRIGGER_*]`](/index.php/Entity_token#PROGRESS_TRIGGER_POPULATION "Entity token") - Defines the triggers which control when an entity will become interested in your fortress.
- [`[COMMON_DOMESTIC_PACK]`](/index.php/Entity_token#COMMON_DOMESTIC_PACK "Entity token") - Allows the civilization to use domestic pack animals. If an entity lacks pack animals (or ability to pull wagons), it will be unable to send caravans (showing as No Trade at the embark screen), unless it has domesticated any suitable animal species or is forced to use a non-suitable creature by the [`[ANIMAL]`](/index.php/Entity_token#ANIMAL "Entity token") definition [`[ALWAYS_WAGON_PULLER]`](/index.php/Entity_token#ALWAYS_WAGON_PULLER "Entity token") on creature, caste or class.
- [`[COMMON_DOMESTIC_PULL]`](/index.php/Entity_token#COMMON_DOMESTIC_PULL "Entity token") - Allows the civilization to use domestic animals to pull wagons, assuming their [`[ETHIC:KILL_PLANT]`](/index.php/Ethic#KILL_PLANT "Ethic") permits them to use wagons in the first place.
- [`[MERCHANT_BODYGUARDS]`](/index.php/Entity_token#MERCHANT_BODYGUARDS "Entity token") - Caravan will be guarded by soldiers.

### Modding creatures

Creature modding is great fun – you can change nearly any aspect of a creature, or make your own completely from scratch.

Modding creatures is very similar to modding civs: it's just a matter of editing, adding, or removing tokens, enclosed in square brackets underneath the creature's `[CREATURE:]` header. The creature entries contain all of the information about each and every non-random creature in the game, from animals to dwarves to goblins to even caravan wagons. A lot of the creature tokens are fairly self-explanatory; you can find a list of such tokens here. But before you start creating your own creatures, you'll want to learn how the tissues system works.

#### Creature materials and tissues

In the most basic sense, a creature is a series of body parts. These parts are defined in their own file, and we'll talk about them later, as a specific aspect of how creatures work, which throws off a lot of prospective modders, is the relationship between body parts, tissues, and materials. We're going to show you part of the creature entry for a bronze colossus (bear with us):

     ...
     [BODY:HUMANOID:2EYES:2EARS:NOSE:HUMANOID_JOINTS:5FINGERS:5TOES]
     [NO_THOUGHT_CENTER_FOR_MOVEMENT]
     [TISSUE:BRONZE]
         [TISSUE_NAME:bronze:bronze]
         [TISSUE_MATERIAL:INORGANIC:BRONZE]
         [MUSCULAR]
         [FUNCTIONAL]
         [STRUCTURAL]
         [RELATIVE_THICKNESS:1]
         [CONNECTS]
         [TISSUE_SHAPE:LAYER]
     [TISSUE_LAYER:BY_CATEGORY:ALL:BRONZE]
     ...

At the top, we can see the [`[BODY]`](/index.php/Creature_token#BODY "Creature token") token, followed by a list of body parts. As you've probably guessed, these parts make up the physical form of the colossus. But the colossus has to be made out of something - it has to have tissues, and those tissues also have to be made out of something - in this case, bronze.

Below the [`[BODY]`](/index.php/Creature_token#BODY "Creature token") token you'll see a [`[TISSUE]`](/index.php/Creature_token#TISSUE "Creature token") token, followed by an identifier, much like the others we've seen. The [`[TISSUE]`](/index.php/Creature_token#TISSUE "Creature token") block is determining how the tissue works, and which purposes it'll serve. As the colossus is just going to be made out of this one tissue, this tissue needs to act like bone, muscle, and everything else combined, hence the [`[MUSCULAR]`](/index.php/Tissue_definition_token#MUSCULAR "Tissue definition token"), [`[FUNCTIONAL]`](/index.php/Tissue_definition_token#FUNCTIONAL "Tissue definition token") and [`[STRUCTURAL]`](/index.php/Tissue_definition_token#STRUCTURAL "Tissue definition token") tokens. The tissue also references a material - `[INORGANIC:BRONZE]` - the properties of which are declared in the inorganic materials file inorganic_metal.txt, and the tissue is subsequently made out of this material. With us so far?

Below the tissue definition is the [`[TISSUE_LAYER]`](/index.php/Creature_token#TISSUE_LAYER "Creature token") line. [`[TISSUE_LAYER]`](/index.php/Creature_token#TISSUE_LAYER "Creature token") allows you to control where each tissue is applied. Its first argument defines if it's to search by body part category (`BY_CATEGORY`), body part type (`BY_TYPE`), or look for a specific part (`BY_TOKEN`). That's followed by the parts argument itself, which is in this case `ALL` (so the game's looking for parts in all categories, which is to say, every body part). This is followed by the tissue to be applied, "BRONZE". So the [`[TISSUE_LAYER]`](/index.php/Creature_token#TISSUE_LAYER "Creature token") token is telling the game to select all body parts in every category and make them out of the tissue "BRONZE". The colossus is now made of bronze.

By now, you're probably thinking "Wow, if this was for a creature made out of however many tissues, this would be amazingly longwinded!" and you're right. Luckily, there are two methods by which we can speed things up a lot.

Firstly, there are material and tissue templates. Let's say you were going to make a lot of creatures out of bronze, and you didn't want to have to copy and paste the bronze tissue all over the place. Instead, you create a tissue template. This goes, as you've probably guessed, in a tissue template file.

     [TISSUE_TEMPLATE:BRONZE_TEMPLATE]
         [TISSUE_NAME:bronze:bronze]
         [TISSUE_MATERIAL:INORGANIC:BRONZE]
         [MUSCULAR]
         [FUNCTIONAL]
         [STRUCTURAL]
         [RELATIVE_THICKNESS:1]
         [CONNECTS]
         [TISSUE_SHAPE:LAYER]

Now, instead of applying the tissue to each and every bronze creature you're making, you can just refer to the template:

     ...
     [BODY:HUMANOID:2EYES:2EARS:NOSE:HUMANOID_JOINTS:5FINGERS:5TOES]
     [NO_THOUGHT_CENTER_FOR_MOVEMENT]
     [USE_TISSUE_TEMPLATE:BRONZE:BRONZE_TEMPLATE]
     [TISSUE_LAYER:BY_CATEGORY:ALL:BRONZE]
     ...

Material templates work in the same way, but refer to materials instead of tissues.

However, if we're looking at something like a dwarf, even with the templates, editing can get very slow indeed:

         ...
         [USE_MATERIAL_TEMPLATE:SKIN:SKIN_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:FAT:FAT_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:BONE:BONE_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:CARTILAGE:CARTILAGE_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:HAIR:HAIR_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:TOOTH:TOOTH_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:EYE:EYE_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:NERVE:NERVE_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:BRAIN:BRAIN_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:LUNG:LUNG_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:HEART:HEART_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:LIVER:LIVER_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:GUT:GUT_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:STOMACH:STOMACH_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:PANCREAS:PANCREAS_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:SPLEEN:SPLEEN_TEMPLATE]
         [USE_MATERIAL_TEMPLATE:KIDNEY:KIDNEY_TEMPLATE]
         [USE_TISSUE_TEMPLATE:SKIN:SKIN_TEMPLATE]
         [USE_TISSUE_TEMPLATE:FAT:FAT_TEMPLATE]
         [USE_TISSUE_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
         ...

This is where body detail plans, which have their own file, and are designed to help automate some of the more common processes in creature creation, come in. The first entry in b_detail_plan_default.txt does exactly what we've been trying to do above: it takes all the common materials and shoves them into one plan, which can be referenced with a single token.

         ...
         [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
         ...

Much easier. But what about the [`[TISSUE_LAYER]`](/index.php/Creature_token#TISSUE_LAYER "Creature token") tokens? Will we have to type out all of those manually? Nope, detail plans have that covered as well. It's possible to place variable arguments into a detail plan. For example:

     [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS]
         [BP_LAYERS:BY_CATEGORY:BODY:ARG3:50:ARG2:5:ARG1:1]
         [BP_LAYERS:BY_CATEGORY:BODY_UPPER:ARG3:50:ARG2:5:ARG1:1]
         [BP_LAYERS:BY_CATEGORY:BODY_LOWER:ARG3:50:ARG2:5:ARG1:1]
         [BP_LAYERS:BY_CATEGORY:ARM:ARG4:25:ARG3:25:ARG2:5:ARG1:1]
         [BP_LAYERS:BY_CATEGORY:ARM_UPPER:ARG4:25:ARG3:25:ARG2:5:ARG1:1]
         ...
         [BP_LAYERS:BY_CATEGORY:NOSE:ARG5:4:ARG1:1]
         ...

First, an argument is placed in the plan (`ARG1`, `ARG2` etc.), followed by the thickness of the tissue that will be inserted in place of the argument. So when we reference the "VERTEBRATE_TISSUE_LAYERS" plan, we'll be able to do something like this:

         [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]

`ARG1` in the detail plan is replaced by "SKIN", the first tissue we entered. `ARG2` is replaced by "FAT", `ARG3` by "MUSCLE", `ARG4` by "BONE", and `ARG5` by "CARTILAGE". Hence, our creature's body part designated as `[``CATEGORY``:BODY]` is made up of "SKIN" with thickness 1, "FAT" with thickness 5, and "MUSCLE" with thickness 50. Its nose is made up of "SKIN" (thickness 1) and "CARTILAGE" (thickness 4).

Things left out of the body plans aside, our dwarf's entire body, material, tissue and tissue layer tokens have been boiled down to this:

         ...
         [BODY:HUMANOID:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:
         THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:FACIAL_FEATURES:TEETH:RIBCAGE]
         [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
         [BODY_DETAIL_PLAN:STANDARD_TISSUES]
         [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
         ...

This can save you a lot of time and space if you're making lots of changes common to many creatures. In general, if you're making a creature that's fleshy or chitinous, there are detail plans already included in the game to help you out. You should only have to resort to declaring tissues individually (like our bronze colossus) if you're doing something really out-of-the-ordinary.

Another great thing about templates (and so, detail plans) is that they can be modified after being declared. Let's say we wanted our dwarves to be perpetually on fire (don't ask). We leave the body stuff declared normally:

         ...
         [BODY:HUMANOID:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:
         THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:FACIAL_FEATURES:TEETH:RIBCAGE]
         [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
         [BODY_DETAIL_PLAN:STANDARD_TISSUES]
         [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
         ...

We then, in our own mod, select the appropriate material:

    [SELECT_CREATURE:DWARF]
         [SELECT_MATERIAL:SKIN]
             [MAT_FIXED_TEMP:10600]
         ...

We don't want them burning to death, so we'll need to stop that from happening:

    [SELECT_CREATURE:DWARF]
         [SELECT_MATERIAL:SKIN]
             [MAT_FIXED_TEMP:10600]
         [SELECT_MATERIAL:ALL]
             [HEATDAM_POINT:NONE]
         ...

Note that this makes use of DF's built-in temperature scale - you can read more about that on this page. We're also referencing material definition tokens, which we haven't gone over yet - we'll talk about making your own materials later.

#### Creature castes

Another potentially extremely powerful part of the creature raws, is the **caste system.** The caste system handles both true biological castes and lesser variations, such as sexes.

To understand the true potential of the caste system, we only need to take a look at the raws for antmen, found in creature_subterrenean.txt:

         ...
         [CASTE:WORKER]
             [CASTE_NAME:worker ant woman:worker ant women:worker ant woman]
             Female, but non-breeding.
             [POP_RATIO:10000]
         [CASTE:SOLDIER]
             [CASTE_NAME:soldier ant woman:soldier ant women:soldier ant woman]
             Female, but non-breeding.
             [POP_RATIO:1000]
         [CASTE:DRONE]
             [MALE]
             [CASTE_NAME:drone ant man:drone ant men:drone ant man]
             [POP_RATIO:5]
         [CASTE:QUEEN]
             [FEMALE]
             [CASTE_NAME:queen ant woman:queen ant women:queen ant woman]
             [POP_RATIO:1]
         [SELECT_CASTE:WORKER]
          [SELECT_ADDITIONAL_CASTE:SOLDIER]
          [SELECT_ADDITIONAL_CASTE:QUEEN]
             [BODY:HUMANOID_4ARMS:2EYES:HEART:GUTS:BRAIN:MOUTH]
             [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
         [SELECT_CASTE:DRONE]
             [BODY:HUMANOID_4ARMS:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
             [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
             [FLIER]
         [SELECT_CASTE:ALL]
             [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
             [BODY_DETAIL_PLAN:CHITIN_TISSUES]
             [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
             [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
             [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
                 [ATTACK_SKILL:GRASP_STRIKE]
                 [ATTACK_VERB:punch:punches]
         ...

It's evident that the process of creating and editing castes is comparable to the modifications we were making to tissues and materials earlier: A caste is declared, and modifications to the base creature are made. Declared castes can be selected and subsequently modified, again, just like tissues and materials.

In this case, each caste is declared, given its own name, and a [`[POP_RATIO]`](/index.php/Creature_token#POP_RATIO "Creature token"), which determines how commonly a birth results in that caste - for every 11,006 workers born, there'll be an average of 1000 soldiers, 5 drones and one queen. You've probably also noticed that the "DRONE" and "QUEEN" castes have the [`[MALE]`](/index.php/Creature_token#MALE "Creature token") and [`[FEMALE]`](/index.php/Creature_token#FEMALE "Creature token") tokens respectively - these tokens determine how breeding works. A creature without both a [`[MALE]`](/index.php/Creature_token#MALE "Creature token") caste and a [`[FEMALE]`](/index.php/Creature_token#FEMALE "Creature token") caste will be unable to breed (no asexually reproducing creatures yet, unfortunately). As they lack [`[FEMALE]`](/index.php/Creature_token#FEMALE "Creature token"), the workers and soldiers are unable to breed with the male drones.

After this, there are some modifications to bodyparts. In this case, the drones have wings and the [`[FLIER]`](/index.php/Creature_token#FLIER "Creature token") token, which the other castes lack. It's entirely possible for creatures of different castes to have completely different body structures, even to the extent that they don't resemble each other at all. If you read the section of this guide that dealt with entities, you may remember a passing mention of multi-creature civilisations and how they don't quite work as you may think they would. The castes system is your workaround. You could create a caste that is, for all intents and purposes, a human, and another caste of the same creature that acts exactly like a giant cave spider, put the creature in a civ, and get a human-spider civ. The only flaw in this approach is that the castes will interbreed and produce offspring of either caste.

That's the most complex components of creature creation out of the way. You should find the rest trivial by comparison.

### Modding items

Items are fairly simple to deal with. By default, each item type is contained in its own file; this may help make browsing for a specific item easier, but from a purely technical point of view, it's possible to throw all items into one file. Unfortunately, Item definition tokens don't seem to be especially well-documented (at least not as well as the other object types), but you should be able to figure out most things by way of our explanations and your assumptions.

Let's look at the entry for, of course, the thong:

     [ITEM_PANTS:ITEM_PANTS_THONG]
     [NAME:thong:thongs]
     [LAYER:UNDER]
     [COVERAGE:25]
     [LAYER_SIZE:10]
     [LAYER_PERMIT:30]
     [MATERIAL_SIZE:1]
     [SOFT]
     [LEATHER]
     [STRUCTURAL_ELASTICITY_WOVEN_THREAD]

Most of these are pretty obvious if one compares them to the other entries in the file. There's a layer for the item, determining where it's worn; a coverage value to determine how well it protects you from cold and other things; a size token to determine how much it counts for when it's under something else; a layer permit token to determine how much can be worn under it; and a material size token to determine how much raw material it takes to make it.

Now, if you wanted to mod these to turn them into metal thongs (ouch!), you would simply have to add [`[METAL]`](/index.php/Armor_token#METAL "Armor token") to it somewhere. Simple! These tokens work by tying into material properties - some materials are designated as suitable for making hard items, some for soft, etc..

Weapons involve a little more detail:

     [ITEM_WEAPON:ITEM_WEAPON_SWORD_2H]
     [NAME:two-handed sword:two-handed swords]
     [SIZE:900]
     [SKILL:SWORD]
     [TWO_HANDED:67500]
     [MINIMUM_SIZE:62500]
     [MATERIAL_SIZE:5]
     [ATTACK:EDGE:100000:8000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
     [ATTACK:EDGE:50:4000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
     [ATTACK:BLUNT:100000:8000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
     [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

[`[SIZE]`](/index.php/Weapon_token#SIZE "Weapon token") determines how heavy the weapon is. This has a substantial effect on weapon effectiveness. [`[SKILL]`](/index.php/Weapon_token#SKILL "Weapon token") determines which skill is used in using the weapon; a list of skills can be found on this page. [`[MINIMUM_SIZE]`](/index.php/Weapon_token#MINIMUM_SIZE "Weapon token") determines the minimum size a creature must be before the weapon can be wielded, while [`[TWO_HANDED]`](/index.php/Weapon_token#TWO_HANDED "Weapon token") determines how large a creature must be in order to wield the weapon with one hand.

Attacks take a little more explanation. The first value determines the contact area of the weapon's attack; this should be high for slashing weapons and low for bludgeoning, piercing and poking ones. The second value determines how deep the weapon penetrates - for `BLUNT` attacks this value is ignored as they're not supposed to penetrate anyway, but in the case of `EDGE` attacks it should generally be lower for slashing attacks and higher for stabbing attacks.

Following these are the nouns and verb used; they should be self-explanatory. Finally, we have the velocity modifier, which has a multiplying effect on the weapon's size for the purposes of determining how powerful it is in combat. But more accurate it describe distribution of momentum across length of weapon. So "STAB" perfomed with only muscular power and modifier is x1 (1000). "SLASH" performed with some rotating momentum of cutting edge, but sword is pretty balanced thru it's length and modifier is just x1.25 (1250). Axes, hammers and maces have more unbalanced mass distribution and weapon mass concentrated far from grasp, so higher modifiers.

[`[ATTACK_PREPARE_AND_RECOVER]`](/index.php/Weapon_token#ATTACK_PREPARE_AND_RECOVER "Weapon token") determines number of game frames to perform these actions. In vanilla, all attacks except lashing use 3:3.

Other, more miscellaneous items are generally simple and shouldn't require any further explanation.

Once you've made an item, you just add it to the civ entry so a civilization can actually craft it, and it's done.

### Modding language files

Let's say you added a whole new species. Sure, you could just swipe one of the existing translation files and steal their language for your species, but that's the lazy way! If you want to create a whole new language, it is very simple.

First, you'd need a whole new "language_NAME.txt" file, such as "language_LIZARDMAN.txt", along with "language_LIZARDMAN" at the top of the file, followed by `[OBJECT:LANGUAGE]` and `[TRANSLATION:LIZARDMAN]`. After that, it's just a matter of copy-pasting one of the existing language lists and editing the finished 'translated' word. That's it! Then just add the translation link to your civ in entity_default.txt and it'll be added to the game on worldgen.

All raw files use Code Page 437 encoding, and you should make sure you are editing these files in that format. As many text editors default to UTF-8, some characters with diacritical marks may fail to show properly. Saving one of the default language raw files in this state will overwrite these characters with the Unicode question mark, which will corrupt the file. To fix this, replace the file with a clean one downloaded from the distributed version of DF.

(Note that the name of the file doesn't actually matter; but it's typical to name the file after a creature if it's exclusive to their civilization.)

### Modding body parts

Imagine you have this fantastic idea for a multi-tentacled winged spider-monster. Sounds great! But in order to make this a reality you may need to create a new set of body parts for it. That's no problem! Making body parts is easy, though it may look complicated at first.

All of the default body definitions are located in body_default.txt and then linked to a creature in the creature's entry. We've talked about how bodyparts make up creatures earlier, in the creature section. You can mix and match them in the creature entry and it makes no difference, as long as they're there: each body part will link itself to the appropriate connection automatically when the creature is first created.

Body parts work by sections: you can add as many sections as you want to a body part definition, but generally you should keep it fairly low for ease of use. Each body section entry is in the, very simple, format:

     [BODY:BODYNAME]
     [BP:TOKENID:name][TOKENSGOHERE][DEFAULT_RELSIZE:][CATEGORY:WHATEVER]

The most important tokens are [`[CONTYPE]`](/index.php/Body_token#CONTYPE "Body token") and [`[CON]`](/index.php/Body_token#CON "Body token"): [`[CONTYPE]`](/index.php/Body_token#CONTYPE "Body token") means the body part in question is connected to a certain *type* of body part, while [`[CON]`](/index.php/Body_token#CON "Body token") means it's connected to a *specific* one. "TOKENID" is yet another identifier, which should be unique, as it's referenced every time something uses [`[CON]`](/index.php/Body_token#CON "Body token") or `BY_TOKEN`. [`[DEFAULT_RELSIZE]`](/index.php/Body_token#DEFAULT_RELSIZE "Body token") defines, of course, what the body part's size is in relation to the other parts. [`[CATEGORY]`](/index.php/Body_token#CATEGORY "Body token") defines a category for the part, which can be unique or shared with other parts. This is referenced whenever `BY_CATEGORY` is used.

A list of body part tokens can be found here.

Let's take a simple example, a head:

     [BODY:BASIC_HEAD]
     [BP:HD:head:STP][CONTYPE:UPPERBODY][HEAD][CATEGORY:HEAD]
     [DEFAULT_RELSIZE:300]

It connects directly to an upper body.

     [BODY:2EYES]
         [BP:REYE:right eye:STP][CONTYPE:HEAD][SIGHT][EMBEDDED][SMALL][RIGHT][CATEGORY:EYE]
             [DEFAULT_RELSIZE:5]
         [BP:LEYE:left eye:STP][CONTYPE:HEAD][SIGHT][EMBEDDED][SMALL][LEFT][CATEGORY:EYE]
             [DEFAULT_RELSIZE:5]

These are a pair of eyes, connecting to the head.

     [BODY:HUMANOID]
         [BP:UB:upper body:upper bodies][UPPERBODY][CATEGORY:BODY_UPPER]
             [DEFAULT_RELSIZE:1000]
         [BP:LB:lower body:lower bodies][CON:UB][LOWERBODY][CATEGORY:BODY_LOWER]
             [DEFAULT_RELSIZE:1000]
         [BP:HD:head:STP][CON:UB][HEAD][CATEGORY:HEAD]
             [DEFAULT_RELSIZE:300]
         [BP:RUA:right upper arm:STP][CON:UB][LIMB][RIGHT][CATEGORY:ARM_UPPER]
             [DEFAULT_RELSIZE:200]
         [BP:LUA:left upper arm:STP][CON:UB][LIMB][LEFT][CATEGORY:ARM_UPPER]
             [DEFAULT_RELSIZE:200]
         [BP:RLA:right lower arm:STP][CON:RUA][LIMB][RIGHT][CATEGORY:ARM_LOWER]
             [DEFAULT_RELSIZE:200]
         [BP:LLA:left lower arm:STP][CON:LUA][LIMB][LEFT][CATEGORY:ARM_LOWER]
             [DEFAULT_RELSIZE:200]
         [BP:RH:right hand:STP][CON:RLA][GRASP][RIGHT][CATEGORY:HAND]
             [DEFAULT_RELSIZE:80]
         [BP:LH:left hand:STP][CON:LLA][GRASP][LEFT][CATEGORY:HAND]
             [DEFAULT_RELSIZE:80]
         [BP:RUL:right upper leg:STP][CON:LB][LIMB][RIGHT][CATEGORY:LEG_UPPER]
             [DEFAULT_RELSIZE:500]
         [BP:LUL:left upper leg:STP][CON:LB][LIMB][LEFT][CATEGORY:LEG_UPPER]
             [DEFAULT_RELSIZE:500]
         [BP:RLL:right lower leg:STP][CON:RUL][LIMB][RIGHT][CATEGORY:LEG_LOWER]
             [DEFAULT_RELSIZE:400]
         [BP:LLL:left lower leg:STP][CON:LUL][LIMB][LEFT][CATEGORY:LEG_LOWER]
             [DEFAULT_RELSIZE:400]
         [BP:RF:right foot:right feet][CON:RLL][STANCE][RIGHT][CATEGORY:FOOT]
             [DEFAULT_RELSIZE:120]
         [BP:LF:left foot:left feet][CON:LLL][STANCE][LEFT][CATEGORY:FOOT]
             [DEFAULT_RELSIZE:120]

An entire humanoid body. The foot bone's connected to the ankle bone...

[`[BODYGLOSS]`](/index.php/Bodygloss "Bodygloss") entries, which you can sometimes find applied to creature entries, are simply replacement words for specific part name strings in a creature. For example, you'll find the bodygloss definition `[BODYGLOSS:CLAW_HAND:hand:claw]` in body_default.txt; you can then use this in a creature via `[BODYGLOSS:CLAW_HAND]` and it'll replace all instances of "hand" with "claw" in that creature. Be warned, however—if you were to, say make a bodygloss `[BODYGLOSS:EARSTALK:ear:stalk:ears:stalk]`, it would not only change "ear" and "ears" to "stalk" and "stalks", it would also change "h**ear**t" to "h**stalk**t"! For all intents and purposes the body part will still function as the proper part, though.

### Modding plants

Plants are, again, not unlike creatures. With what you've learned so far in regard to tokens and the materials system, running through the notes included in plant_standard.txt should explain most things. Here's the list of Plant tokens.

Below is the plump helmet raw description:

     [PLANT:MUSHROOM_HELMET_PLUMP]
        [NAME:plump helmet][NAME_PLURAL:plump helmets][ADJ:plump helmet]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [PICKED_TILE:6][PICKED_COLOR:5:0:0]
        [GROWDUR:300][VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven wine]
            [STATE_NAME_ADJ:LIQUID:dwarven wine]
            [STATE_NAME_ADJ:GAS:boiling dwarven wine]
            [STATE_COLOR:ALL:AMETHYST]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]

        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:plump helmet spawn:plump helmet spawn:4:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:rounded tops]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:5:0:0]
        [DEAD_SHRUB_COLOR:0:0:1]

Let's look at this line by line:\
First, we define its file name. In this case it's "MUSHROOM_HELMET_PLUMP". Next we define its in-game name, "plump helmet" and its adjective for if you were to craft with its materials (e.g. plump helmet plant earrings).

         [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]

---
*Parte 1 de 2 de «Modding». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Modding*
