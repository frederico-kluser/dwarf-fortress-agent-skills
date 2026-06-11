# Adamantine

> Fonte: [Adamantine](https://dwarffortresswiki.org/index.php/Adamantine) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Melee Weapons Crossbows Bolts Picks Armor Anvils Metal crafting Clothing Construction**
- **Ore**
- **Raw adamantine**
- **Properties**
- **Material value 300☼ Impact strength 5 GPa Shear strength 5 GPa ×10 Fire-safe Magma-safe Melting point 25000 °U Boiling point 50000 °U Ignition point none Solid density 200 kg/m³ Liquid density 2600 kg/m³ Specific heat 7500 J/kg·K Color aqua**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

**Adamantine** is a rare, high-value metal which is impossibly lightweight, strong, and sharp. Adamantine is refined from raw adamantine, and can be woven into cloth or smelted into wafers, useful for making almost any item in the game. Armor and edged weapons made from adamantine are absurdly valuable and wonderfully effective. Adamantine weapons have special graphics.

## Processing

Unlike what a player would expect, one does not simply make adamantine wafers directly from raw adamantine. You must first extract adamantine strands from the raw adamantine, and those are then processed into wafers or cloth. Despite the unique process of making adamantine into wafers, it will still graphically appear as a light blue bar, looking like any other metal bar.

Adamantine strands are extracted from raw adamantine at a craftsdwarf's workshop by a strand extractor. Strand extraction is an extremely long process for an unskilled laborer, making it potentially worthwhile to focus extraction experience on one or two individual dwarves. Extracted strands are considered a special metallic form of thread, and after extraction each strand can either be woven into adamantine cloth at a loom or smelted into an adamantine wafer at a smelter (removing any dye); thankfully these tasks are performed just as quickly as other weaving and smelting jobs.

Given this extra step of extraction before the smelting phase, most players will want to build additional craftsdwarves' workshops and stockpiles near the smelters and forges. Note that the strands of adamantine are stored in cloth/thread stockpiles. When processing adamantine, it is a good idea to smelt the strands into wafers as fast as possible, as your medical dwarves may use the valuable adamantine strands for suturing wounds, since, to them, it's just another type of thread.

Adamantine cloth is used to make ultra high-value clothing, but it is no more resistant to wear than less exotic materials. Adamantine wafers are functionally identical to metal bars and can be used to forge the full range of metal goods, but are far smaller in size, requiring about three times as many units of material per unit as regular metal bars:

- Weapons, armor/clothing, and trap components require the item's MATERIAL_SIZE in wafers/units of cloth
- Most types of furniture (door, floodgate, throne, coffin, table, chest, bin, armor stand, weapon rack, cabinet, statue, anvil, barrel, pipe section, hatch cover, grate, quern, millstone, and slab) require 9 wafers.
- Cages, minecarts and wheelbarrows require 6 wafers.
- Blocks, chains, and ballista arrowheads require 4 wafers.
- Animal traps, buckets, mechanisms, and crutches require 3 wafers.
- Backpacks and quivers require 2 units of cloth, and splints require 2 wafers.
- All other items require 1 wafer.
- Strange moods require 1 wafer, regardless of the end product.

Raw adamantine cannot be spawned in the object testing arena, but adamantine-derived gear is spawnable as of v50.07. Adamantine (raw or otherwise) cannot be purchased in the embark screen, presumably for balance reasons.

## Application

|  |
|----|
| "Adamantine" in other / Languages / Dwarven / : / ebsas / Elven / : / lire / Goblin / : / kumo / Human / : / medi |

Adamantine has extreme material properties: it is nigh-weightless (weighing about as much as cork), extremely strong, and razor-sharp. These properties make it ideal for edged weapons and armor, but unfortunately, likewise, make it near-useless for blunt weapons, which will simply bounce off of foes: considering the lethality of hammerer and fortress guard beatings, this may be the point. Armor made of adamantine provides unmatched protection against slashing and piercing attacks, but blunt attacks and ranged weapons have high armor penetration capacity, so a full kit of adamantine armor is nonetheless not a recipe for combat invulnerability. Mail armor is especially lacking, as the incredible protective qualities of adamantine are overridden with the flexibility of chain.

Because the metal's material properties are irrelevant in other applications and because it's so rare and hard to produce, using adamantine for other things is generally a waste. Adamantine statues are ten times as valuable as gold ones, but are prohibitively expensive to produce, requiring nine wafers per statue. Some of the highest values per wafer for a normal adamantine product can be realised by forging adamantine flasks. However, by the time you have adamantine available, you're likely not to be in serious need of such valuable export products. By far the most wealth can be generated simply by adding adamantine to artifacts – a single stone, wafer, block or bolt of cloth can add hundreds of thousands of dwarfbucks in value, making your fortress the envy of all the neighbors. Additionally, your Monarch will insist on having a "true throne" made of adamantine upon arriving at your fortress along with seven symbols of equal worth (though they will settle for one made of divine metal, which is itself risky to acquire).

One significant application of adamantine is through metal duplication. However, this is generally considered an exploit, so depending on your preferences, you may not want to do this.

    [INORGANIC:ADAMANTINE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:adamantine]
        [STATE_NAME_ADJ:LIQUID:molten adamantine]
        [STATE_NAME_ADJ:GAS:boiling adamantine]
        [DISPLAY_COLOR:3:3:1]
        [BUILD_COLOR:3:3:1]
        [MATERIAL_VALUE:300]
        [SPEC_HEAT:7500]
        [MELTING_POINT:25000]
        [BOILING_POINT:50000]
        [ITEMS_WEAPON][ITEMS_WEAPON_RANGED][ITEMS_AMMO][ITEMS_DIGGER][ITEMS_ARMOR][ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [ITEMS_SOFT]
        [WAFERS]
        [SOLID_DENSITY:200]
        [LIQUID_DENSITY:2600]
        [MOLAR_MASS:55845]
        [IMPACT_YIELD:5000000]
        [IMPACT_FRACTURE:5000000]
        [IMPACT_STRAIN_AT_YIELD:0]
        [COMPRESSIVE_YIELD:5000000]
        [COMPRESSIVE_FRACTURE:5000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:0]
        [TENSILE_YIELD:5000000]
        [TENSILE_FRACTURE:5000000]
        [TENSILE_STRAIN_AT_YIELD:0]
        [TORSION_YIELD:5000000]
        [TORSION_FRACTURE:5000000]
        [TORSION_STRAIN_AT_YIELD:0]
        [SHEAR_YIELD:5000000]
        [SHEAR_FRACTURE:5000000]
        [SHEAR_STRAIN_AT_YIELD:0]
        [BENDING_YIELD:5000000]
        [BENDING_FRACTURE:5000000]
        [BENDING_STRAIN_AT_YIELD:0]
        [MAX_EDGE:100000]
        [DEEP_SPECIAL]
        [STOCKPILE_THREAD_METAL]
        [STATE_COLOR:ALL_SOLID:AQUA]

|  |  |
|:--:|----|
|  | This article contains **massive spoilers**. If you do not wish to have your game experience spoiled, **do not scroll down**! |

~~Un~~fortunately, breaching any of the tubular veins leads to the HFS, for lots of Fun.

Might be a bit too close to the underworld...\
*Art by Darkie*

## Origins of Adamantine and Slade

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Back in the mists of time, the Gods decided to create the World. To do so they had to find a way to heat it in the cold voids of space. Demonkind had already forged their own world out of the vile substance Slade, a stone anathema to all creation and only able to be worked through the vile rituals they had created, for slade was truly "dead" stone, with no life in it at all.

Deciding both to imprison their greatest enemies and to create a home for their creations, the Gods poured into the skies of the Demons' world "living" stone (known to mortals as semi-molten rock - rock burning hot with the fresh life of Creation). The Gods knew that if it were not constantly heated, this living rock would cool, and yet the Demons, fools that they were, constantly attacked the living rock, not realizing that their attacks simply heated the rock again and again, keeping it alive. Unfortunately, as the Gods began to pour more and more of the rock onto their creation, they found it quickly lost its life when removed too far from the Demons. It would only remelt once it touched the living rock, creating vast seas of magma that heated the tunnels above. Worse, the living rock itself had been disturbed by this process, creating gaping holes through which the Demons escaped, killing and maiming the first creations of the Gods, warping those they could find into the terrible Forgotten Beasts, leaving only the Titans safe on the surface.

Knowing this state of affairs could not last if their weaker creations, the first mortals, were to survive, the Gods created a new substance, imbued with their power: Adamantine. The beautiful aqua-colored ore was poured into the holes, sealing the entrances that the living rock could no longer seal, preventing the Demons from escaping, for its power totally repelled Demonkind.

Unfortunately, as time passed and the first mortals began to carve their civilization from both the surface and the underworld, they discovered the vast shafts of this amazing substance and began to mine it, instantly realizing its divine potency. In doing so, they removed the great barriers the gods had placed in order to keep the Demons sealed. The Demons rose up, slaughtering thousands and escaping into the World, often rising to lead mortal civilizations, such as that of the Goblins. Upon these sites they raised towers carved from the vile Slade that only they could work. Brave adventurers and champions of the Gods forged special swords made from the divine Adamantine and ventured into these dark places to seal the Demons within hell once more. Leaving their swords buried in these places, those who survived swore to defend them for all eternity, binding themselves with oaths of such might that they surpassed death itself. They remain, even today, as zombies and skeletons, driven by their undying thought "none must take the sword!" and nothing more. These undead are totally obsessed with their duty to defend the ancient demonic structures from all interlopers and have been the death of many an unwary explorer.

In retrospect, all this could probably have been avoided if the Gods had bothered to make their all-powerful metal capable of withstanding the swing of a copper pick.

## The Great Adamantine Space Elevator

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Source

In a great fluke, a new world was created in the midst of Armok shaving. No one quite understands why this happened, but the whisker of the holy one landed vertically. The material can only be described as a super adamantine. It is over 2000 z-levels high. And the map continues on.

Year after year, the dwarves of \[SUBJECT CIVILIZATION HERE\] send an expedition out into the world in order to ascertain the fate of last year's expedition. It has long-since been forgotten exactly when this series of fruitless expeditions started, but the dwarves are a sort that demand an answer.

It happens year after year, when they head northeast to the ominous shrubland that has been known only in name: "The Hill of Spit." The hill lies beyond a ruined elven settlement, a stone's throw away from a brook that has come to be known as "Troublemysteries." By the time they arrive, it is already too late.

They embark year after year, and there they stand, awe-struck with their implements of dwarven duty left undisturbed at their feet. All about them are the decrepit wagons and bleached bones of those who heralded their grim arrival -- barrels filled with rot and worm, picks covered in rust and dust. There they stand with their eyes open wide and jaws agape, and they stare upward into the dome of the heavens. What they see is beyond the ken of mortal beard. It reaches from the ground higher than any bird has flown; higher than any cloud has drifted; higher than any man, dwarf, beast or monster has ever or will ever ascend, twisting and writhing upward in ways that can only transfix the gaze of unwary observers in their fundamentally impossible geometries -- a spiraling needle of pure adamantine, ascending beyond the vanishing-point into the sky.

They stand there, motionless and breathless, and wait only for time to wear them down into the dust of the earth from whence they came, leaving that siren spire standing amidst a graveyard of wagons and barrels to call more of their bearded kind to an emaciated doom.

Another year, another expedition unheard of, another question unanswered, another expedition prepared.

## Color Misconceptions

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some people, upon hearing of the legendary metal known as Adamantine, imagine a blood red, crimson metal, befitting of the God of Blood Armok... They may have been playing some other Dwarvideo games, or just confused, but for some reason, those unacquainted with Adamantine always seem to think it is red.

## Trivia

- Adamantine's origins are tied to Greek mythology, though in the mythos, biblical stories and other works, the material is referred to as "adamant". The word's meaning is "unbreakable, unconquerable and untameable", representing the material's nature and hardness.
- Adamantine as portrayed in Dwarf Fortress is inspired by *mithril*, a fictional metal that appears in the works of J.R.R. Tolkien. Much like adamantine, *mithril* was impossibly light, yet stronger than steel, and greed for it ultimately led to the fall of the fortress of Khazad-dum.

The most expensive armor ever made.\
*Art by inkundus*
