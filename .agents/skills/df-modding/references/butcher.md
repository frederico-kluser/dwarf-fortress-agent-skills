# Butcher

> Fonte: [Butcher](https://dwarffortresswiki.org/index.php/Butcher) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Skill: Butcher

Sprite(s)

Association
 

Profession
Farmer

Job Title
Butcher

Labor
Butchery

Tasks

Butcher / animal

Workshop

Butcher's shop

Attributes

Strength / Agility / Endurance / Kinesthetic Sense

When he smells like dead lamb, you know he didn't miss work.

**Butchers** do the dirty job of killing tame animals and processing animal corpses, skeletons and body parts for meat, fat, skin, bones, skulls, and many other objects, at the Butcher's Shop.

## Fortress mode

The work of a butcher is divided into two categories: **slaughtering** and **butchering**. While both produce the same results (food and raw materials), they have distinctly different inputs - butchering is done on dead wild creatures (and takes a significant amount of time to perform), while slaughtering is done on live tame/trained creatures (and is instantaneous).

Most dwarves do not mind the grim work, but some get an unhappy thought from it, and a few even feel happy about it. Check the thoughts of a butcher immediately after a creature was slaughtered or butchered. It is a bit of micromanagement to find a dwarf who is "satisfied after slaughtering an animal", but few fortresses can afford wasting possible good thoughts.

### Slaughtering

To slaughter an animal, go to the u (Creatures) screen, then the Pets/Livestock tab and click on  to flag (or un-flag) for slaughtering. Assuming you have enabled "Slaughter any marked animal" in your standing orders, a Slaughter {name of the animal} (Tame) job will be queued to the next available Butcher's Shop. A butcher will then take the job and walk up to the animal, lead it to the butcher's shop, then strike down the creature. As mentioned above, slaughtering living animals is *instantaneous* - the moment the dwarf sets foot in the workshop, the animal dies and its body is split into individual parts. If "No automatic slaughter" is *enabled* in standing orders, then nothing at all will happen, since the "slaughter animal" job cannot be added manually. If multiple creatures are flagged for slaughtering, only one slaughter job *per workshop* at a time will be created. Only tame/trained creatures can be slaughtered.

### Butchering

If "Automatically butcher carcasses" is enabled in your standing orders, then any valid corpse located either in a stockpile or within 43 squares of a butcher's shop, will be automatically queued for butchering. During this job, the butcher will pick up the corpse, haul it to the workshop, and then slowly process it into individual parts at a speed based on skill level and clutter (which can take a long time for particularly large creatures such as forgotten beasts). If a hunter successfully kills their target, they will haul the corpse and place it directly inside an appropriate butcher's shop, but unless your butcher happens to be idle at the moment, the corpse will likely be removed from the workshop and placed in a stockpile.

Certain exceptionally large species of vermin, like creepy crawlers, can also be butchered for a small amount of meat. Any caught live ones are automatically queued for butchering: a dwarf will carry an animal trap containing one to a butcher's shop and butcher the vermin inside as if it were a corpse. Only live untamed vermin can be butchered this way, dwarves will not butcher tame ones or the remains of one.

Dwarves will not butcher the corpses of sapient creatures (due in part to the `[``EAT_SAPIENT_OTHER``:UNTHINKABLE]` ethic), and the corpses of tame creatures cannot be butchered (they must be slaughtered while still alive).

The type and number of objects produced from butchering a creature varies greatly, since not all creatures have the same parts. See each animal's page for a breakdown of what each animal can produce. Note that while a butcher's shop also has the "Extract from dead animal" task, this requires a certain type of living trapped vermin, and it is not done by a butcher, but by an animal dissector.

## Adventurer mode

How to butcher in adventurer mode:

1.  If the corpse is in your inventory, d drop it or equip it by r removing it. If the corpse is on the ground, move onto its tile.
2.  Equip a cutting implement or, alternatively, drop it on your tile. This can be any object with a sharp edge (i.e.has an EDGE attack type), from bladed weapons and tools, up to bolts and sharpened rocks.
3.  Press x to open the action menu. Then select a "Butcher", select the corpse that you want to butcher, pick the tool that you want to use.\

The adventurer will then proceed to butcher the corpse, dropping all of the products on their tile; also note that small animals, like ravens, cannot be butchered. The tool used for butchery (*as was stated, any object with a sharp edge*) will also be covered in the blood of the creature being butchered. Ergo, butchering certain creatures can have fun results.

## Effect of skill

A butcher's skill affects the speed of butchery, which can be important for processing a large number of corpses before they begin to rot. Note that butcher shops can become cluttered quickly, because most animals create a large number of different items of different categories when butchered, so make sure that you have nearby stockpiles for refuse, raw hides, meat, prepared organs and fat. To minimize the amount of miasma created, in case the rotting parts are not removed fast enough, a butcher's shop should always be blocked by a door.

Of course, placing the butcher's shop outside will prevent any and all miasma generated by rotting, but the dwarves won't haul the inedible parts away unless their global orders allow "Workers gather outdoor refuse" (y -\> Standing orders -\> Refuse and dumping, second option)

## Troubleshooting

If your butcher keeps cancelling jobs with "Needs butcherable unrotten nearby item", check the following:

- The corpse isn't rotten
- The corpse is in a stockpile, or within 20 tiles of the butcher shop
- The corpse is large enough for butcheringBug:0874
- The corpse wasn't sapient, tame or trained
- Your butcher can access the corpse and workshop
- The corpse isn't currently tasked for a job (such as hauling to a stockpile)
- The butcher workshop isn't restricted to taking from a stockpile that doesn't contain the corpse

## Butchering sapients

In the current version of the game, it isn't possible to butcher sapient creatures due to dwarven ethics forbidding it. In addition, the game is currently programmed to force the player (regardless of race or game mode) to not be able to use the returns of a butchered sapient creature (i.e. you can't eat goblin meat in adventurer mode, regardless of if you're playing a dwarf or an elf or an alligator man)Bug:9171. Butchered undead are not subject to this restriction. Discussion on the subject may be found in this Bay 12 forums thread.

While it is possible to mod ethics to allow the butchering of sapients for the dwarven civilization, ethics itself only plays its role during world generation, meaning you still won't get the option to butcher sapients in actual gameplay. The only way to reliably butcher sapients and use their returns is with the utility DFHack, as demonstrated here. Or you can simply eat the bones if the corpse has rotted away.

## Detailed butchering yields calculations

Yields are calculated on a per part, per layer basis. Each tissue layer on a part is considered individually, even if multiple layers of the same part are made of the exact same materials. (footnote 1)

Step 1: Get the base volume of the tissue layer

The base volume of a tissue layer is based on what percent of its body part volume it represents (based on the layer's RELATIVE_THICKNESS compared to the RELATIVE_THICKNESS of all other layers), which is based on what percent of the whole body's unmodified base volume (defined with BODY_SIZE) that the part represents (based on the part's RELSIZE compared to the RELSIZE of all other parts).

Only these aspects - the relsizes of body parts, the base body size, and the relative thickness of a tissue layer compared to others on its part - are what are considered at this stage. Things like whether the layer thickens with strength, if the part has size modifiers, etc. aren't factored in here. This is an important thing to note: they have no impact on the relative base volumes of parts in this calculation! (footnote 2)

Even if a layer is now missing (like fat having melted off), its defined relative thickness is still factored in to the calculations - the volume of muscle on a part doesn't suddenly increase because the fat layer is gone or anything like that.

Step 2: Apply modifiers to each tissue layer's base volume to get its modified volume There are multiple different modifiers that affect the base volume to get the modified volume. Because these modifications happen after relsizes and such have been considered, they don't impact the volume / yields of any of the other layers on its body part, or any other body parts.

Each of these modifiers is applied as a multiplier to the base volume.

### Body Modifiers

The HEIGHT, BROADNESS, and LENGTH of the creature's whole body is used as a modifier. The values for these can be set using the BODY_APPEARANCE_MODIFIER token (whenever these tokens are omitted, the default values are 100).

Modifier = (Body Height / 100) \*(Body Broadness / 100) \* (Body Length / 100)

### Body Part Modifiers

The HEIGHT, BROADNESS, and LENGTH of the body part are used as a modifier. The values for these can be set using the BP_APPEARANCE_MODIFIER token after selecting the part (whenever these tokens are omitted, the default values are 100).

Modifier = (Part Height / 100) \* (Part Broadness / 100) \* (Part Length / 100)

Stronk and chonk - THICKENS_ON_STRENGTH and THICKENS_ON_ENERGY_STORAGE

\
If the tissue has the THICKENS_ON_STRENGTH or THICKENS_ON_ENERGY_STORAGE tokens, modifiers based on the creature's stats are applied.

\

- If a layer has just THICKENS_ON_STRENGTH, the multiplier is the creature's STRENGTH/1000.

\

- If a layer has just THICKENS_ON_ENERGY_STORAGE, the multiplier is the creature's fat amount / 250,000. Because a creature's "normal" fat level is 500,000, you'll likely notice adding this token to a tissue will double the yields from that tissue, as that value gives a 2x multiplier.

\

- If a layer has both THICKENS_ON_STRENGTH and THICKENS_ON_ENERGY_STORAGE, the multiplier is the mean average of the two multipliers combined (so the multiplier is: (Strength/1000 + Fat amount/250,000) / 2). This means that it some cases, you could end up getting lower item yields having both tokens than just having one.

### Other Modifiers

The amount of a layer that's remaining after some of it has been lost does have some impact on its yield volume, however I didn't purposely investigate it. I'd assume that the % of layer that's remaining is used as a modifier. I did test what happens when a layer is fully gone, however - it yields 0 of its item, regardless of the special clauses (see: later).

Step 3: Get the item yields The number of items yielded from butchering the tissue layer is based on a simple formula (however, there are some special cases that can modify the number of items):

Number of items = Modified volume / 25,000 (rounded down)

In cases where the yield from this calculation is 0, there are two special clauses that can apply, based on the body part's size, and the modified volume of the tissue.

       Volume Clause: If the modified volume of a layer is at least 260, any yield of 0 is changed to 1.
       Part Size Clause: If the size of the body part that the tissue layer is a part of is at least 260, any yield of 0 is changed to 1. A layer could in practice represent even a tiny fraction of a volume unit, and yet still yield 1 item just because its part is 260 or bigger.

### Butcher Items

What items are actually yielded from butchering a tissue layer is based on the material it's made from. There are some specially-coded cases based on the materials tokens - for example, materials with the MEAT token will yield meat, materials with the BONE token will yield bone. The token BUTCHER_SPECIAL can be used to set the item yield to be any particular item you desire.

The item count isn't at all impacted by the size of the item being produced. If a layer's modified volume is big enough to yield 40 items, it'll yield 40 meat or 40 statues all the same. Items with standard dimensions (e.g. BARS, THREAD, CLOTH) seem to be produced at those standard dimensions. For example, with a BUTCHER_SPECIAL:THREAD:NONE material that has a modified volume large enough for an item yield of 10, a stack of 10 thread items will be produced, each item being at 15000 dimensions.

### Extra Butcher Objects/NOMEAT, NOBONES etc.

Extra butcher objects don't impact the yields of butchering layers associated with the parts at all. They also don't care if the part they're attached to is big enough to yield at least 1 item if it was butchered regularly. So, an extra butcher object that's attached to a body part whose volume is below 260 will still drop its item, even if butchering the layers on that part might not yield anything.

\
So how do the creature tokens such as NOMEAT and the like factor into yields for their items? They don't at all. Perhaps the tokens affect fort-mode butchering, or the tokens are depreciated from an old version, or they're not supposed to have anything to do with butchering and handle something like whether entries show up in the stockpiles screen or not.

## Bugs

- A dead tame animal that was not slaughtered cannot be butchered.Bug:1180 This includes tame animals killed due to age, starvation, or combat.
- Butchering returns of sentient creatures are unusable, regardless of the adventurer's ethics.Bug:9171
- Some animals can be too small to be butchered, such as buzzards, rabbits, and barn owls.Bug:0874

## See also

- Meat industry

|  |
|----|
| "Butcher" in other / Languages / Dwarven / : / lokast / Elven / : / uwale / Goblin / : / slust / Human / : / rashcat |
