# Citizenship

> Fonte: [Citizenship](https://dwarffortresswiki.org/index.php/Citizenship) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Citizenship refers to belonging to a specific entity. Being a citizen of a civilization has many implications, such as adopting that civilization's ethics and being hostile to any enemy civilization and other named enemies.

## Fortress mode

### Types of citizens

#### Your dwarves

Your starting seven dwarves and subsequent migrants are always considered citizens of your fort, and your fort's parent civilization. If you expel them, they will lose citizenship of your fort, but will retain that of your civ.

You may also acquire non-dwarven citizens in some special cases, detailed below.

#### Visitors

After being granted long-term residency, and after about 2 years in your fort, visitors may apply for citizenship, and accepting will allow them to have labors in your fort. You will also be able to reassign their occupations. Mercenaries will never apply for citizenship, though it is worth noting that a bard or other visitor-turned-citizen will be able to become a militia captain, effectively enabling all-mercenary squads.

When a visitor petitions for citizenship, they will meet up with your mayor. All pending petitions are listed on the Petition screen with the name and reason of the visitor. You can then accept or deny the request.

Once you accept a visitor as a citizen, they will no longer be able to hold a room in a tavern as a long-term resident, and you will need to provide a room in the same way you would for a dwarf. They will accept labors and can be put to work, the same as any dwarves might be.

In a library, petitioned citizens will read books and scrolls, but cannot make them unless they are scholars.

\

#### Rescued prisoners

If you send squads on a rescue/recovery mission to a foreign site that happens to hold prisoners, your dwarves may free them and bring them back to your fort. These units become citizens of your fort, but their labors can't be changed and are set to whatever skills they had. Like visitors, rescued prisoners can be from any race.

#### Tamed sentients

You may acquire citizens by training sentient creatures that are trainable (i.e. have [`[PET]`](/index.php/Creature_token#PET "Creature token") or [`[PET_EXOTIC]`](/index.php/Creature_token#PET_EXOTIC "Creature token")). Currently, this only concerns gremlins. You can also get tamed sentients that could not be tamed in any other way (like goblins) through tributes. Pet sentients are subject to all sorts of weird behavior, which eventually disappears when they apply for citizenship after 2 years like visitors. However, they still need to be trained, and your animal trainer may die of thirst trying to follow around your pet (*or 'pet' as the case may be*) as it goes to its various errands, if you aren't careful. Note that any offspring that you train as children will become fully tame, as with any other animal, and won't need training.

### Risks and benefits of non-dwarven citizens

Multiracial forts have a number of benefits, but also carry risk due to the inherent differences between your dwarves and other races. There are some things to watch out for:

- Non-dwarf citizens may want to pray to their own deity, not the dwarven pantheon. They will be able to if you have a temple not dedicated to any specific deity.
- The different values of other creatures may cause negative thoughts, or even grudges, if arguments happen (can occur as part of the socialise task); or if, for example, an elf is asked to chop down a tree.
- Non-dwarves don't handle alcohol really well; this may result in brawls and various degrees of alcohol poisoning.
- If a visitor happens to be from one of the various animal people races, some traits carried over from the animal species can be... interesting. Some tags, such as [`[CURIOUSBEAST_GUZZLER]`](/index.php/Creature_token#CURIOUSBEAST_GUZZLER "Creature token"), [`[CURIOUSBEAST_EATER]`](/index.php/Creature_token#CURIOUSBEAST_EATER "Creature token"), [`[CURIOUSBEAST_ITEM]`](/index.php/Creature_token#CURIOUSBEAST_ITEM "Creature token"), or [`[MEANDERER]`](/index.php/Creature_token#MEANDERER "Creature token") may result in unexpected behaviour.
- Many need different-sized clothing. Elves can wear the same clothes as dwarves, but humans need larger clothes and goblins need smaller. You can specify the size of clothing made. Note that armorsmiths, clothes makers, etc. will make gear and clothes appropriate to their own size, regardless of the general racial population make-up of the fortress.

On the other hand:

- Non-dwarves don't suffer from cave adaptation, nor are they alcohol dependent (except for those hardened by trauma who "don't really care about anything anymore"). You can freely send them outside and they won't drink as much booze (make sure you have a clean water supply set up if you haven't already).
- Some races have intrinsic abilities, e.g. gremlins have natural ambusher skill and will hunt alongside your hunters.
- Some races have a different attribute distribution. Humans are considered to be average at everything. In comparison, dwarves are a little stronger and tougher but less agile. Elves have naturally-high agility, and so they would be good at jobs that require moving around a lot, like Shearing, Herbalism, or Milking.
- Some animal people races may have truly awesome perks, such as special abilities (like web walking) or immunities (to pain, stunning, dizziness, etc.), making them a good choice for your army. The rule of thumb is: if the animal in question has the perk, the citizen probably has it, too. Unfortunately, having visitors other than dwarves, elves, humans, and goblins is rare.

## In Adventure mode

During character creation, you may choose to become a citizen of one of the civilizations you'll start the game in (except if you choose to be an Outsider). As such, you will have access to all the knowledge acquired by that civilization: music/poetry/dance forms, bestiary, location of sites as well as a portion of the world map, and so on. Choosing one's starting civilization is therefore not a trivial choice.

## With DFHack

Through judicious use of DFHack's `tweak makeown` you can turn *any* sentient creature into a citizen of your fort. The possibilities are limitless. This may have side effects though, depending on whom you use this on. The base requirements for the creature to be considered a citizen appear to be [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") + [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token"). After using the command, the target will start behaving like a long-term resident of your fortress, and will petition for full citizenship after the requisite two years. To otherwise reassign their labors, you'd have to use utilities like `gui/gm-editor` if you didn't want to wait that long.\
