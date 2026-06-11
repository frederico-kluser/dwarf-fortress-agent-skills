# Modding

> Fonte: [Modding](https://dwarffortresswiki.org/index.php/Modding) — Dwarf Fortress Wiki (GFDL/MIT)

**Modding**, or creating mods, refers to modifying the behavior of the base game (vanilla). *Dwarf Fortress* is remarkably moddable.

## Resource Overview

This section serves as a portal to all modding-related pages on the wiki.

Using Mods

- Installing mods
- Enabling mods in-game

Guides and references

- Modding Guide
- Modding pitfalls for troubleshooting

- Mod Format and Game folders and files
- Publish on Steam Workshop
- Memory hacking, Offset Finding Methods
- Character table

Where to get help?

- This forum is the official DF subforum dedicated to discussions about modding.
- Kitfox modding discord
- DFhack questions

Modding tools

There are several utilities that assist in modding efforts. There is a list of them on the Bay 12 Forums.

- Text Editors are used in all areas of modding. Use a good text editor to edit files and search into multiple files (like the free Notepad++ for example) or more advanced editors capable of highlighting and formatting the displayed text (like DF RAW Language server)
- Image Editor will be needed for doing custom graphics. Paint.NET, Photoshop and GIMP are the most used, but whatever supports the .png format will work.

### Documentation

Raw files

These object files, stored in `/data/vanilla/*/objects/`, define various specifics of game items, materials, and creatures, and can be changed using mods to alter how the game behaves. These are text based and can be edited with any text editor, however, editing the vanilla raw files is now discouraged.

See Token reference - It's always good to refer to tokens on the wiki. Even experienced modders have to look up tokens! A list of articles about tokens can be found here.

Graphics Files

The \`/data/art/\` subfolder of Dwarf Fortress is used to store user-customizable graphics sets.

Reactions

Language and Speech file

Sound and Music files

All sound and music files used by *Dwarf Fortress* are stored in the .ogg format within the `/data/sound/` subfolders. You can replace the existing ogg files with different ones. That has to be performed manually and isn't actually supported by the game. You can also change some of the definitions of when certain musical cues are played, using available music tokens and sound tokens in the raw files. However, you can't add new music or sounds other than replacing what's already there.

### Best practice

The current best practice is to not modify the original raw files, since most modifications can be made via mods. Mods can add new objects, add tokens to existing objects, and cut objects entirely. You should prefer SELECT over CUT, and prefer CUT over not loading vanilla raws.

## Guide

This is intended to be a guide to inform those new to *Dwarf Fortress* modding on what elements of the game can be modified, and how. After reading through this guide, a user should be capable of editing creatures, entities, materials *et al*, and creating their own.

Generally, breaking stuff is fine - nothing that can be changed will affect the DF executable, and new additions can be easily removed.

This guide is based on Teldin's guide, originally created for version 0.27.176.39c. Per wiki tradition, it has been updated through all the major releases since then; hopefully it reflects current knowledge.

### Token reference

It's always good to refer to tokens on the wiki. Even experienced modders have to look up tokens! A list of articles about tokens can be found here.

### Basics of DF modding

To make a mod, one must put a folder into the `/mods/` folder. The vast majority of modifications to the game can be done via this method. This folder should contain a file named "info.txt" and two subfolders: "graphics" (where you insert graphics sets), and "objects", which contains all the data for, generally, everything in the game that is not hardcoded.

The info.txt is formatted like so:

A mod should have all of these. There are a few more tokens, but the above are the important ones.

Most of the game's vanilla content is in the same format as mods. Many text files can be found in the subfolders of the `/data/vanilla` folder - these are the raw files, and using them as a basis for modification is quite easy. For now, we will take a look at one of the existing files. For example, if you open `/data/vanilla/vanilla_creatures/creature_standard.txt`, it should look something like this:

As you can see, each file comprises a header string stating the file name, a second header stating the type of object data it contains, followed by the contents of the file itself. These are all necessary elements of the file, and without them, the file will be ignored by the game.

**In other words, to be recognized by the game, a raw file must have all of the following:**

1.  A filename that refers to the type of objects contained therein. **Creature files must start with creature\_, entity files must start with entity\_, and so on.**
2.  The filename on the first line of the file.
3.  \[OBJECT:type\], where "type" is replaced with the relevant object type.

Below the headers, there begins a list of entries. Each entry is made up of its own header (in this case, "\[CREATURE:DWARF\]"), again stating the type of object, and then the object's unique identifier - if an identifier isn't unique, the game will mess up and you'll get some serious, and potentially very trippy, errors. (For example...) Below that, we have the body of the entry, which determines the entry's specific properties.

The body of an entry is made up of a series of "tokens", which are essentially flags that can be added or removed to affect the entry's attributes. Most of these effects are hardcoded: for example, it's possible to make a creature only eat meat with the \[CARNIVOROUS\] token, but it's impossible to create your own token detailing a specific diet for the creature.

Before we continue, a few key things to remember when modding the raw files:

- Try to avoid modifying the existing raw files when possible. You should make a mod instead!
- When adding files, token identifiers are all you need to include to ensure proper references are maintained. The game searches through all loaded raw files by tokens. For example, you can add a new pair of leather boots and not even have to add it to a file named item_shoes.txt, but rather your own file, say item_shoes_new.txt and ensure you have the token listed, ex. \[ITEM_SHOES:ITEM_SHOES_BOOTS_NEW\].

- When a new world is generated, the mods included are "baked in" and cannot be modified except to be updated--for this, the game checks that the mod used by the save is of a compatible NUMERIC_VERSION.
- There's nothing stopping you from just copying an existing creature/entity/whatever, changing the identifier, and modifying it. This can save you a lot of time, especially when it comes to entities.

### Modifying the vanilla objects

You should not modify the vanilla raws where they originally are if you can help it. Instead, patch them using the patching functions provided with *Dwarf Fortress* since v50.01.

There are two patching functions: SELECT and CUT. When SELECT is used, it lets you make changes to an object without needing the entire entry to be present in your mod file. When CUT is used, it forces the game to not use that object, even though it is still found in the vanilla raws (or in any other mods earlier in the load order). Both of these functions take the form of tokens. These functions are not universally applicable to any token found in any entry, just the following list of objects:

CREATURE, ENTITY, INTERACTION, ITEM, WORD, TRANSLATION, SYMBOL, INORGANIC, PLANT, MUSIC, REACTION, SOUND

The syntax required for these functions is: **\[**\**\_**\**:**\**\]**. For instance, \[CUT_PLANT:MUSHROOM_HELMET_PLUMP\] cuts the plump helmet object in the vanilla file plant_standard.txt, so the game will not use that object at all. However, \[SELECT_ITEM_HELM:ITEM_HELM_HELM\] does not select the helm object from the vanilla file item_helm.txt, even though that's how the object appears in that file, because there is no \[SELECT_ITEM_HELM\] token. Instead, the helm would be selected with \[SELECT_ITEM:ITEM_HELM_HELM\].

For example, if you wanted to mod beards onto dwarven women while also removing elephants from the game:

Or, say, add your own reaction and building to dwarves:

And in any of these, one can add the token \[LOG_CURRENT_ENTRY\] somewhere under one of the objects of the file, which logs the full contents of the object in question to logs\current_entry.txt. This can be useful to make sure that the patch is doing what you think it is. For instance if \[LOG_CURRENT_ENTRY\] were added on the next line after \[CREATURE:DWARF\] in your mod file, then the dwarf object would be the object detailed in the log entry.

...Speaking of, let's move on to modifying and adding entities.

### Modding civilizations (entities)

Entities - the objects that determine how civilizations work - are stored in `vanilla_entities/entity_default.txt` (though, like all other files, you may add more). They follow the same format as any other raw file:

Most of the time, it doesn't matter which order these tokens are in or where they're placed so long as they're below the "ENTITY:" identifier, but there are some important exceptions in the case of other files, especially creatures, which can contain a lot of "nested" tokens.

"\[CREATURE:\]" links the civilization with a specific creature defined in a creature file. This is the creature that'll be making up the entity's population, and, therefore, the creature you'll be playing as in fortress or adventure mode if the entity is a playable one. For example, if you wanted to do something silly, you could switch the "CREATURE:DWARF" entry in entity_default.txt with "CREATURE:ELF" and you would be marching elves around in fortress mode, although they would still use dwarven technology, language and names and so forth. Oh, and before you get any funny ideas - it *is* possible to define more than one creature for a civ, but that won't work in quite the way you probably expect; it will pick only one of the defined creatures at random to use for the civ. Later on, in the creature section, you'll learn about castes, which will provide a much more viable alternative, so try to bear with us until then.

"\[TRANSLATION:\]" defines the language file that the entity will be using, which will determine what their untranslated words are for things. This doesn't determine which words they use for naming things, only the way those words are spelled. The default language files are HUMAN, DWARF, ELF, and GOBLIN.

"\[BIOME_SUPPORT:\]" defines the biomes that civs will attempt to settle in. The "FREQUENCY" value determines the likelihood of them building there, but also raises an important point: most of the values you'll be setting for things are relative to each other. If one were to type:

This would have very much the same effect as:

This holds true for a lot of values throughout the files, excluding when it simply doesn't make sense, such as in materials.

You can find many details about the rest of the civilization tokens here.

Besides those mentioned, some fundamental ones are the `[SITE_CONTROLLABLE]` token, which lets you control the civ in fortress mode, the `[OUTSIDER_CONTROLLABLE]` token, which allows you to play in adventure mode as an outsider, and the `[ALL_MAIN_POPS_CONTROLLABLE]` token, which allows you to play a civ native (non-outsider) in adventure mode. Other tokens that you should pay attention to are START_BIOME and the ones regarding sites, but in general, you can just run through the aforementioned list and add or remove what you want.

If you have more than one civ with the `[SITE_CONTROLLABLE]` token, all the available civs from those entities will appear in the group selection section on the embark screen. It may not be immediately obvious from which species each civ may be - while this can be determined from legends mode, the topmost species in the "neighbors" display in the embark screen is always the same as the currently selected species; if your group is dwarven, dwarves will be topmost, whilst (say) elves will be topmost if your chosen group is elven. By default, the game seems to choose a civ (and therefore a species if there is more than one) at random.

You can also attempt to discern the civ yourself by the names it uses - this is the realm of "symbols", collections of words centered around a specific concept. The civ will use the words comprising whatever symbols are applicable to it for various things. This association might be a little confusing at first, so, let's refer to the DWARF entity:

Here, we can see that dwarves will generally name their wars first after words in the "NAME_WAR" symbol group, and then, after words in the "VIOLENT" symbol group. This might, for example, result in a war being named "The War of Carnage". The symbols used for the other types of conflict are arrayed in a similar fashion. It would be trivial to replace the instances of VIOLENT with, say, PEACE and end up with a battle called "The Clash of Calm" or something.

The above applies here. Dwarves are fond of naming their roads and tunnels after... roads and tunnels.

This section deals with everything else. The things that haven't already been dealt with (hence the "REMAINING") - such as site names, kingdom names, the names of individuals, and such - will have names from the ARTIFICE and EARTH symbol groups. After that, the dwarf entity is told to cull all inappropriate symbols - this applies to everything (hence the "ALL") so if the game happens to choose a symbol associated with, say, EVIL for one of the battles, it'll scrap that name and try again. This sort of thing adds a lot of flavour to DF's entities and can account for a lot of a civ's perceived personality.

Another basic thing to note: any entity token that's dealing with weapons, armor, clothing, etc., will state the items that the civ can build natively, not necessarily the ones they can wear or use. For example, you could create a species with no clothes specified, but then rob a clothes shop in adventurer mode and wear everything you want, or give them weapons that are too large to wield and they could sell them, but not use them.

An easy method of creating a civilization is just to copy-paste a similar one to the bottom of the entity_default.txt file and edit things to your liking. Remember to always change the civ's "ENTITY:" identifier! This can be anything, so long as it's not already existing.

At the end of some of the default entries you'll find a list of positions, both ones that'll directly affect you in fort mode (such as nobles) and ones that'll primarily affect worldgen and adventure mode. A list of the tokens applicable to positions can be found here; they don't require a great deal of explanation.

#### Trade

The following entity tokens affect the appearance of trading caravans:

- [\ACTIVE_SEASON\] - Defines the seasons when an entity may visit your fortress.
- [\PROGRESS_TRIGGER\_\*\] - Defines the triggers which control when an entity will become interested in your fortress.
- [\COMMON_DOMESTIC_PACK\] - Allows the civilization to use domestic pack animals. If an entity lacks pack animals (or ability to pull wagons), it will be unable to send caravans (showing as at the embark screen), unless it has domesticated any suitable animal species or is forced to use a non-suitable creature by the \[ANIMAL\] definition \[ALWAYS_WAGON_PULLER\] on creature, caste or class.
- [\COMMON_DOMESTIC_PULL\] - Allows the civilization to use domestic animals to pull wagons, assuming their KILL_PLANT ethic permits them to use wagons in the first place.
- [\MERCHANT_BODYGUARDS\] - Caravan will be guarded by soldiers.

### Modding creatures

Creature modding is great fun – you can change nearly any aspect of a creature, or make your own completely from scratch.

Modding creatures is very similar to modding civs: it's just a matter of editing, adding, or removing tokens, enclosed in square brackets underneath the creature's \[CREATURE:\] header. The creature entries contain all of the information about each and every non-random creature in the game, from animals to dwarves to goblins to even caravan wagons. A lot of the creature tokens are fairly self-explanatory; you can find a list of such tokens here. But before you start creating your own creatures, you'll want to learn how the tissues system works.

#### Creature materials and tissues

In the most basic sense, a creature is a series of body parts. These parts are defined in their own file, and we'll talk about them later, as a specific aspect of how creatures work, which throws off a lot of prospective modders, is the relationship between body parts, tissues, and materials. We're going to show you part of the creature entry for a bronze colossus (bear with us):

At the top, we can see the "BODY:" token, followed by a list of body parts. As you've probably guessed, these parts make up the physical form of the colossus. But the colossus has to be made out of something - it has to have tissues, and those tissues also have to be made out of something - in this case, bronze.

Below the BODY token you'll see a TISSUE token, followed by an identifier, much like the others we've seen. The TISSUE block is determining how the tissue works, and which purposes it'll serve. As the colossus is just going to be made out of this one tissue, this tissue needs to act like bone, muscle, and everything else combined, hence the MUSCULAR, FUNCTIONAL and STRUCTURAL tokens. The tissue also references a material - INORGANIC:BRONZE - the properties of which are declared in the inorganic materials file, and the tissue is subsequently made out of this material. With us so far?

Below the tissue definition is the TISSUE_LAYER line. TISSUE_LAYER allows you to control where each tissue is applied. Its first argument defines if it's to search by body part category (BY_CATEGORY), body part type (BY_TYPE), or look for a specific part (BY_TOKEN). That's followed by the parts argument itself, which is in this case ALL (so the game's looking for parts in all categories, which is to say, every body part). This is followed by the tissue to be applied, BRONZE. So the TISSUE_LAYER token is telling the game to select all body parts in every category and make them out of the tissue "BRONZE". The colossus is now made of bronze.

By now you're probably thinking "Wow, if this was for a creature made out of however many tissues, this would be amazingly longwinded" and you're right. Luckily, there are two methods by which we can speed things up a lot.

Firstly, there are material and tissue templates. Let's say you were going to make a lot of creatures out of bronze, and you didn't want to have to copy and paste the bronze tissue all over the place. Instead, you create a tissue template. This goes, as you've probably guessed, in a tissue template file.

Now, instead of applying the tissue to each and every bronze creature you're making, you can just refer to the template:

Material templates work in the same way, but refer to materials instead of tissues.

However, if we're looking at something like a dwarf, even with the templates, editing can get very slow indeed:

This is where body detail plans, which have their own file, and are designed to help automate some of the more common processes in creature creation, come in. The first entry in b_detail_plan_default.txt does exactly what we've been trying to do above: it takes all the common materials and shoves them into one plan, which can be referenced with a single token.

Much easier. But what about the TISSUE_LAYER tokens? Will we have to type out all of those manually?

Nope, detail plans have that covered as well. It's possible to place variable arguments into a detail plan. For example:

First an argument is placed in the plan (ARG1, ARG2 etc.), followed by the thickness of the tissue that will be inserted in place of the argument. So when we reference the VERTEBRATE_TISSUE_LAYERS plan, we'll be able to do something like this:

ARG1 in the detail plan is replaced by SKIN, the first tissue we entered. ARG2 is replaced by FAT, ARG3 by MUSCLE, ARG4 by BONE, and ARG5 by CARTILAGE. Hence, our creature's body part designated as BODY is made up of SKIN with thickness 1, FAT with thickness 5, and MUSCLE with thickness 50. Its nose is made up of SKIN (thickness 1) and CARTILAGE (thickness 4).

Things left out of the body plans aside, our dwarf's entire body, material, tissue and tissue layer tokens have been boiled down to this:

This can save you a lot of time and space if you're making lots of changes common to many creatures. In general, if you're making a creature that's fleshy or chitinous, there are detail plans already included in the game to help you out. You should only have to resort to declaring tissues individually (like our bronze colossus) if you're doing something really out-of-the-ordinary.

Another great thing about templates (and so, detail plans) is that they can be modified after being declared. Let's say we wanted our dwarves to be perpetually on fire (don't ask). We leave the body stuff declared normally:

We then, in our own mod, select the appropriate material:

We don't want them burning to death, so we'll need to stop that from happening:

Note that this makes use of DF's built-in temperature scale. You can read more about that on this page. We're also referencing material tokens, which we haven't gone over yet - we'll talk about making your own materials later.

#### Creature castes

Another potentially extremely powerful part of the creature raws is the caste system. The caste system handles both true biological castes and lesser variations, such as sexes.

To understand the true potential of the caste system, we only need to take a look at the raws for antmen, found in creature_subterrenean.txt:

It's evident that the process of creating and editing castes is comparable to the modifications we were making to tissues and materials earlier: A caste is declared, and modifications to the base creature are made. Declared castes can be selected and subsequently modified, again, just like tissues and materials.

In this case, each caste is declared, given its own name, and a POP_RATIO, which determines how commonly a birth results in that caste - for every 10000 workers born, there'll be an average of 1000 soldiers, 5 drones and one queen. You've probably also noticed that the DRONE and QUEEN castes have the MALE and FEMALE tokens respectively - these tokens determine how breeding works. A creature without both a MALE caste and a FEMALE caste will be unable to breed (no asexually reproducing creatures yet, unfortunately). As they lack FEMALE, the workers and soldiers are unable to breed with the male drones.

After this, there are some modifications to bodyparts. In this case, the drones have wings and the FLIER token, which the other castes lack. It's entirely possible for creatures of different castes to have completely different body structures, even to the extent that they don't resemble each other at all. If you read the section of this guide that dealt with entities, you may remember a passing mention of multi-creature civilisations and how they don't quite work as you may think they would. The castes system is your workaround. You could create a caste that is, for all intents and purposes, a human, and another caste of the same creature that acts exactly like a giant cave spider, put the creature in a civ, and get a human-spider civ. The only flaw in this approach is that the castes will interbreed.

That's the most complex components of creature creation out of the way. You should find the rest trivial by comparison.

### Modding items

Items are fairly simple to deal with. By default, each item type is contained in its own file; this may help make browsing for a specific item easier, but from a purely technical point of view, it's possible to throw all items into one file. Unfortunately, item definition tokens don't seem to be especially well-documented (at least not as well as the other object types), but you should be able to figure out most things by way of our explanations and your assumptions.

Let's look at the entry for, of course, the thong:

Most of these are pretty obvious if one compares them to the other entries in the file. There's a layer for the item, determining where it's worn; a coverage value to determine how well it protects you from cold and other things; a size token to determine how much it counts for when it's under something else; a layer permit token to determine how much can be worn under it; and a material size token to determine how much raw material it takes to make it.

Now, if you wanted to mod these to turn them into metal thongs (ouch!), you would simply have to add \[METAL\] to it somewhere. Simple! These tokens work by tying into material properties - some materials are designated as suitable for making hard items, some for soft, etc..

Weapons involve a little more detail:

SIZE determines how heavy the weapon is. This has a substantial effect on weapon effectiveness. SKILL determines which skill is used in using the weapon; a list of skills can be found on this page. MINIMUM_SIZE determines the minimum size a creature must be before the weapon can be wielded, while TWO_HANDED determines how large a creature must be in order to wield the weapon with one hand.

Attacks take a little more explanation. The first value determines the contact area of the weapon's attack; this should be high for slashing weapons and low for bludgeoning, piercing and poking ones. The second value determines how deep the weapon penetrates - for BLUNT attacks this value is ignored as they're not supposed to penetrate anyway, but in the case of EDGE attacks it should generally be lower for slashing attacks and higher for stabbing attacks.

Following these are the nouns and verb used; they should be self-explanatory. Finally, we have the velocity modifier, which has a multiplying effect on the weapon's size for the purposes of determining how powerful it is in combat. But more accurate it describe distribution of momentum across length of weapon. So STAB perfomed with only muscular power and modifier is x1 (1000). SLASH performed with some rotating momentum of cutting edge, but sword is pretty balanced thru it's length and modifier is just x1.25 (1250). Axes, hammers and maces have more unbalanced mass distribution and weapon mass concentrated far from grasp, so higher modifiers.

ATTACK_PREPARE_AND_RECOVER determine number of game frames to perform these actions. In vanilla almost not varies for different weapons.

Other, more miscellaneous items are generally simple and shouldn't require any further explanation.

Once you've made an item, you just add it to the civ entry so a civilization can actually craft it, and it's done.

### Modding language files

Let's say you added a whole new species. Sure, you could just swipe one of the existing translation files and steal their language for your species, but that's the lazy way! If you want to create a whole new language, it is very simple.

First, you'd need a whole new language_RACE file, such as language_LIZARDMAN.txt, along with "language_LIZARDMAN" at the top of the file proceeded by \[OBJECT:LANGUAGE\] and \[TRANSLATION:LIZARDMAN\]. After that, it's just a matter of copy-pasting one of the existing language lists and editing the finished 'translated' word. That's it! Then just add the translation link to your civ in entity_default.txt and it'll be added to the game on worldgen.

All raw files use Code Page 437 encoding, and you should make sure you are editing these files in that format. As many text editors default to UTF-8, some characters with diacritical marks may fail to show properly. Saving one of the default language raw files in this state will overwrite these characters with the unicode question mark, which will corrupt the file. To fix this replace the file with a clean one downloaded from the distributed version of DF.

(Note that the name of the file doesn't actually matter; however, it's good form to name the file after a creature if only that creature speaks the language.)

### Modding body parts

Imagine you have this fantastic idea for a multi-tentacled winged spider-monster. Sounds great! But in order to make this a reality you may need to create a new set of body parts for it. That's no problem! Making body parts is easy, though it may look complicated at first.

All of the default body definitions are located in body_default.txt and then linked to a creature in the creature's entry. We've talked about how bodyparts make up creatures earlier, in the creature section. You can mix and match them in the creature entry and it makes no difference, as long as they're there: each body part will link itself to the appropriate connection automatically when the creature is first created.

Body parts work by sections: you can add as many sections as you want to a body part definition, but generally you should keep it fairly low for ease of use. Each body section entry is in the, very simple, format:

The most important tokens are "CONTYPE" and "CON": CONTYPE means the body part in question is connected to a certain *type* of body part, while CON means it's connected to a *specific* one. TOKENID is yet another identifier, which should be unique, as it's referenced every time something uses CON or BY_TOKEN. DEFAULT_RELSIZE defines, of course, what the body part's size is in relation to the other parts. CATEGORY defines a category for the part, which can be unique or shared with other parts. This is referenced whenever BY_CATEGORY is used.

A list of body part tokens can be found here.

Let's take a simple example, a head:

It connects directly to an upper body.

These are a pair of eyes, connecting to the head.

An entire humanoid body. The foot bone's connected to the ankle bone...

"BODYGLOSS" entries, which you can sometimes find applied to creature entries, are simply replacement words for specific part name strings in a creature. For example, you'll find the bodygloss \[BODYGLOSS:CLAW_HAND:hand:claw\] in body_default.txt; you can then use this in a creature via "\[BODYGLOSS:CLAW_HAND\]" and it'll replace all instances of "hand" with "claw" in that creature. Be warned, however—if you were to, say make a bodygloss \[BODYGLOSS:EARSTALK:ear:stalk:ears:stalk\], it would not only change "ear" and "ears" to "stalk" and "stalks", it would also change "h**ear**t" to "h**stalk**t"! For all intents and purposes the body part will still function as the proper part, though.

### Modding plants

Plants are, again, not unlike creatures. With what you've learned so far in regard to tokens and the materials system, running through the notes included in plant_standard.txt should explain most things. Here's the list of plant-specific tokens.

Below is the plump helmet raw description:

Let's look at this line by line:\
First, we define its file name. In this case it's MUSHROOM_HELMET_PLUMP. Next we define its in-game name (plump helmet) and its adjective for if you were to craft with it (e.g. plump helmet earrings).

This defines the structure and material of the plant. It references STRUCTURAL_PLANT_TEMPLATE in the first line, so if you were to say, add wings to the template, the plump helmet plant would be winged. This is for the plant itself, not the end plump helmets.

After that we get our edible tokens. These say that vermin can eat the plant, and it can be eaten raw or cooked by your dwarves. So if you wanted a plant vermin would leave alone, you'd remove the \[EDIBLE_VERMIN\] token.

Next, \[PICKED_TILE:161\] is the character (161 in this case) shown when the crop is harvested. See character table for a table of usable tiles. \[PICKED_COLOR:6:13:0\] is the color used for the crop's tile when harvested. It's in a foreground:background:brightness format. See color for the colors usable.

\[GROWDUR:300\] is how long it takes for your crop to grow. There are 1008 growdur units in a season.\
\[VALUE:2\] Is the value of the harvested plant (default 1).

This defines the plant's alcohol states. \[STATE_NAME_ADJ:ALL_SOLID:\] is the frozen name, followed is the actual drink name, and then its boiling name. These are achieved by either Scorching or Freezing climates. \[DISPLAY_COLOR\] is, of course, color, and \[EDIBLE_RAW\] and \[EDIBLE_COOKED\] are saying you can drink the alcohol raw or cooked.

After that we get our seed template:

And all this says is that the seeds may be eaten by vermin or cooked. Then it gives the name of our plant's seed, its plural name, its foreground, background, and brightness colors, followed by its seed material; said material should have \[SEED_MAT\] to permit proper stockpiling.

And finally for the last chunk we have this:

First we define what season(s) the plant may grow in, then we define how frequently this plant is generated in a particular area, followed by how many harvested crop items may come from 1 plant. \[PREFSTRING:\] is what your dwarves like about the plant, which in this case is the rounded tops. \[WET\]\[DRY\] are the conditions under which the plant can grow. Wet means it can grow close to water, dry means it can grow away from water. This does not mean you can grow the plant on dry stone however. It is just for natural spawning of the plant.\
\[BIOME\] Is what biome the plant grows in. \[UNDERGROUND_DEPTH:Minimum:Maximum\] Is the highest and lowest cavern levels that the plant can appear in if its biome is subterranean. Dwarven civilizations will only export (via the embark screen or caravans) things that are available at depth 1. Defaults to 0:0 (surface only).\
Lastly, \[SHRUB_TILE\] is the character used for the naturally spawning shrub of this plant, \[DEAD_SHRUB\] is the dead shrub character. \[SHRUB_COLOR\] Is the shrub's color, and \[DEAD_SHRUB_COLOR\] is, of course, the dead shrub's color.

While this may or may not look like a lot of tokens, it's very easy. Just copy an existing plant and edit it to your new plant.\
For the rest of the tokens, see plant token.

#### Trees

Trees are another kind of plant that can be modded. Being plants, they use many of the same tokens as edible crops, but differ in having a few tree-specific tokens.

Below is the apple tree raw description:

The first lines are the same as the ones we saw being used in the plump helmets, defining the plant object, giving it a name, and deciding that it should use the standard STRUCTURAL_PLANT material for its structure.

Adding the token DISPLAY_COLOR directly after \[USE_MATERIAL_TEMPLATE\] would allow us to change the color of the tree.

would give us a dark blue apple tree. This method is used by the game in birches and various underground trees.

Next come the definitions of various other materials used by the tree:

From them, we get to know what the parts of the tree can be used for, as well as how they will appear when separated from the tree. Any alterations that can be done to materials normally can be done here, such as changing the value or adding a syndrome.

`   [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]`

\[TREE\] is what turns your plant object into an actual tree. The following argument describes what material the harvested logs should be made of. If NONE, the felled tree will give no logs. \[TREE_TILE\] is the tile the tree shows up as on the world map.

Note that all vanilla trees (that give logs) use the WOOD material defined above as the argument for \[TREE\], as opposed to the STRUCTURAL material. Thus, any changes to the properties of the wood harvested should be done to the WOOD material.

The following tokens decide the dimensions of the tree, and how it grows.

\[TRUNK_PERIOD\] and \[TRUNK_WIDTH_PERIOD\] determine how long it takes for the trunk to grow one tile taller respectively wider, in years. \[MAX_TRUNK_HEIGHT:3\] and \[MAX_TRUNK_DIAMETER:1\] determine the maximum value the above can reach. \[TRUNK_BRANCHING\] decides how "curvy" the tree is, with \[TRUNK_BRANCHING:0\] meaning the tree is entirely straight.

\[HEAVY_BRANCH_DENSITY:25\], \[HEAVY_BRANCH_RADIUS:1\], \[BRANCH_DENSITY:50\], \[BRANCH_RADIUS:2\], \[ROOT_DENSITY:5\], and \[ROOT_RADIUS:3\] determine the density (how many are there, integer ranging 0-100) and radius (in tiles) away from the trunk, of heavy branches, normal branches and roots respectively.

\[STANDARD_TILE_NAMES\] makes the tree use standard names for the trunk, branches etc. Otherwise custom ones can be used. (see full plant token list)

\[SAPLING\] ensures saplings of this tree are called "\[tree name\] sapling", instead of the standard "young \[tree name\]".

Lastly, we are introduced to the \[GROWTH\] token. \[GROWTH\] defines growths growing on a plant, in this case our apple tree. Apple trees have three growths: leaves, flowers and fruits.

First comes the name of the growth. Then, with \[GROWTH_ITEM\], what kind of growth it is, in this case a PLANT_GROWTH made out of the local FRUIT material. \[GROWTH_DENSITY\] says how densely the growth grows, and \[GROWTH_HOST_TILE\] where on the tree it grows. \[GROWTH_TIMING\] decides when the growth appears, in annual ticks. The growth then drops off, leaving no clouds (items to be picked up by your dwarves). \[GROWTH_PRINT\] sets it to look like a red '%', and \[GROWTH_HAS_SEED\] implies that eating this growth will leave you with a seed.

### Workshops

Workshops are raw-designed pretty differently from everything else in the game, being buildable structures rather than items or methods to gain items. However, they are fairly simple. For example, here's the raw for the soap maker's workshop:

A line-by-line breakdown:

These are the name of the workshop ("Soap Maker's Workshop") and color of the workshop's name when examined with 'q' (White with a black background).

DIM refers to how large the workshop will be, in this case 3 wide, 3 tall. WORK_LOCATION tells where the creature using it (usually a dwarf) will work, numbered from the top right--in this case, 2:2, or the middle. Multiple work locations can be defined, even outside the dim.

These refer to the worker required to build it (soap maker) and the key used to build it in the workshop menu (capital S).

This is a bit more complex, and is where we get to the meaty part of workshop making--the tiles' properties. BLOCK refers to which tiles will be untraversable--1 means blocked, 0 means unblocked. The first number refers to row, and the next 3 refer to column, so 1:0:0:0 means that, on the first row, all tiles will be unblocked. This is the case for all vanilla workshops, as of now.

The TILE token tells which tile will go where. note, however, that there are 5 entries here instead of 4. The first number, in this case, refers to build stage, numbered from 0 to 3; 3 or 1 is fully built (depending on whether there are stages), 0 is just placed, and 2 is always an intermediate stage, while 1 is usually an intermediate stage. Whether 1 is an intermediate stage or not depends on if there are a 2 and 3 stage; if 2 and 3 exist, 1 will be intermediate. The second number and beyond are similar to BLOCK; however, instead of 1s and 0s, you must input tiles. The tiles themselves can be given in quotes (as in ' ') or given as a number, which can be looked up here. Here, we have 150, which is û.

Color is as TILE, but with colors instead of tiles; however, colors are made up of 3 numbers each or MAT. MAT refers to the color of the material used to make it; the 3 numbers refer to foreground:background:foreground brightness, and can be looked up here. For example, 4:2:1 will give you bright red with a dark green background.

These refer to items required to build the building. These are in the same format as reaction reagents and products--quantity:item:material. You'll learn more about those on the article about reactions, though. The second BUILD_ITEM is special-- it uses modifiers exclusively to determine its requirements. BUILDMAT refers to wood logs, wood blocks, stone boulders, and stone blocks; WORTHLESS_STONE_ONLY means it can't use economic stone; CAN_USE_ARTIFACT means that it... can use artifacts. EMPTY, in the bucket's case, means that the bucket must be empty.

This is the text in the tooltip shown when the building is highlighted by the mouse in the workshops list.

More can be seen at the building tokens article.

### Reactions

Reactions are the crafting recipes used in workshops, and by the adventurer. By adding new reactions you can make new items available, or enable you to get items or materials in new ways. The reactions can also be given to entities, in which case they will make use of them during both world gen and play; making a reaction that creates steel directly from plant fibers, would allow the elves to craft steel and arrive clad in it in a siege.

Not all crafting reactions are defined in the raws, but some are, such as those for pottery and alloy making.

An in-depth guide for reactions is available here.

### Materials

As we've seen when talking about creatures, materials are vital. Materials show up in two forms: material templates, which generally show up in creatures, and specific materials (designated as "inorganic"), which are (by default, at least) consigned purely to metal and stone types.

Let's take a look at METAL_TEMPLATE in material_template_default.txt. It's evident that most of the basic properties of metals are already defined in the template - it goes red and melts at a high enough temperature, it's heavy, and (as noted by the very bottom token) is a metal. We already know just how useful templates can be to creatures, and the same applies to other materials.

Now let's take a look at inorganic_metal.txt. You can see that the metals here refer to the templates, and, just like we did with creatures, then modify the properties of that template and expand upon it.

Finally, let's look at inorganic_stone_mineral.txt. Here we can see that in addition to the changes made to the template, there are also ENVIRONMENT tokens - these tell the game where to place these minerals during worldgen.

Here's a list of material tokens. It should also help you out with any modifications you want to make regarding those creature modifications we were making a while back. See, it all ties together in the end. The beauty of the current materials system is that there's actually very little difference between, say, leather and iron - they're fundamentally the same thing, just with different properties, which is how things really should be.

## Selecting and Cutting

As explained above, existing raws can be altered with the use of SELECT, and can also be culled with CUT for more granular control, compared to simply unloading vanilla content in the mod loader. Token behavior when multiple tokens are added is dependent on the individual token. Removing tags from an object without cutting and recreating the object in question is typically impossible, except for creature object tags removed and/or replaced with the use of creature variation tokens.

The syntax for selecting and cutting objects is as follows:

## Examples

*Main articles: :Category:Modding_Examples*

The Hydling below was made by Mysteryguye (and annotated, updated and separated into blocks by Putnam), to act as an example creature.

## See also

- Raw file
- Token
- Modding pitfalls
- Cheating
- Bay 12 Guide:
