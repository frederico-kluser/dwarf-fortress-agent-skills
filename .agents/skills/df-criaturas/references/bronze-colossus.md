# Bronze colossus

> Fonte: [Bronze colossus](https://dwarffortresswiki.org/index.php/Bronze_colossus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bronze colossuses for their height.**
- **Biome**
- **Any Land**
- **Attributes**
- **Building destroyer : Level 2**
- **Megabeast · Genderless · No Stun · No Pain · No Exert · Fanciful · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 20,000,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **☼ bronze statue ☼ (worth 280☼)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic magic statue made of bronze and bent on mayhem.*

Estimated size comparison between a bronze colossus, and a dwarf.

A **bronze colossus** (plural: **bronze colossuses** from the raws) is a megabeast taking the form of a gigantic humanoid construct, made of bronze. When one takes up residence near a fortress, it's up to those within to make an end of it, or it will make an end of them. Upon its death by means other than melting, a bronze colossus becomes a masterwork bronze statue of itself (worth 280☼), a decent decoration for a grand entrance hall.

Rough calculations have placed the colossus somewhere between thirty-five and forty feet tall (11.53 meters), or about 1/4th the height of the Statue of Liberty. This, of course, assumes it is sculpted in the form of a nude male – a clothed or female figure might be shorter or taller.

Some dwarves like bronze colossuses for their *height*.

## Fortress Mode

Unless you are using whips or marksdwarves (but you will need a **lot** of bolts to kill a bronze colossus), a bronze colossus takes no serious damage from any material inferior to steel\[Verify\], but can still be defeated with cumulative damage. Attacks that cause cumulative damage will be reported as *chipping* or *denting* the colossus in the combat log [1]. Adamantine short swords and battle axes can also lop off entire limbs and heads if you have access to them.

Similarly to other construct-like creatures such as the amethyst man and the gabbro man, bronze colossuses feel no emotion or exertion, are immune to pain, and cannot be stunned or nauseated. Like other large creatures, a bronze colossus cannot be atom smashed. Raising and retractable bridges do not operate while underneath a colossus either. However, the great weight of a colossus can be exploited by sending it into a multi-floor fall with a controlled cave-in. While the colossus may not die from the fall, it will likely lose all its limbs and any combat effectiveness, which turns it into a great training dummy.

Magma, the solution to all dwarven problems, is also effective against a bronze colossus. It may take an extremely long time to melt one unless large amounts of magma are used, however. A tamed dragon can also be quite effective, since a colossus can be melted with dragonfire, which is also much faster than small amounts of magma. Freezing in water, solidifying in obsidian, and cave-ins are also effective tactics.

On the other hand, why kill a 165-tonne colossus when you can trap it in a wooden cage and use it as a centerpiece for a zoo? Or, since a colossus takes no damage from wood and bone bolts, with a little engineering and lots of ammo it can become an easy source of limitless marksdwarf experience.

## Adventure Mode

Bronze colossuses inhabit shrines "Shrine (megabeast)") - you may find the location of a nearby shrine by asking locals about "beasts".

Even a relatively weak and unskilled adventurer can easily cripple a bronze colossus with a whip. Other weapons with small contact areas retain some effectiveness too, and cumulative damage will eventually bring down a colossus. Stronger and more skillful adventurers can opt for swords and axes, as they can occasionally lop off limbs and heads. Since bronze colossuses are incapable of learning and have no skills, they have a hard time detecting adventurers that are hidden in ambush, even in close proximity. One can take advantage of this by attacking the colossus' feet and legs early in the battle from hiding, as this will bring it to the ground, greatly lowering its speed and preventing it from charging you. Bronze colossuses also have a unique weakness to water, due to having [`[SWIMS_LEARNED]`](/index.php/Creature_token#SWIMS_LEARNED "Creature token") but *not* [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") - a bronze colossus will not drown in water, but will flounder around helplessly, making it an easy target for adventurers with a good swimming skill (or if the adventurer stands on a land tile next to the water tile the colossus is in).

Even with just a copper spear, most adventurers can apply their vulnerability to cumulative damage if they have some method of increasing their strength beyond the norm. This is effectively the only instance where attacks with the shaft will prove more effective than stabbing.

Great tip for early adventurers: throwing a gold coin can prove to be effective, you can easily grab one from the stockpile where the colossus has hoarded its loot.

Artist rendering of a bronze colossus by Mechlin (post)

## Statue

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
A bronze colossus leaves a masterwork bronze statue of itself after death, but said statue weighs only 495Γ, a tiny fraction of the 165,000Γ the colossus weighed in life. Because of these factors, it is theorized that fighting a colossus entails slowly carving it into a puny dwarf-sized version of itself with whatever tools are available, at which point it ashamedly admits defeat and agrees to stand immobile forever as a decoration in your fortress.

Veteran hammer lords and chisel lords boast of laying low a bronze colossus and returning with a trophy depicting a wholly different species. Contemporary adventurers dismiss these tales as fabrications by the blacksmith's guild to fetch a higher price at the trade depot.

## Trivia

- In previous versions of the game, bronze colossuses were nigh-invincible in combat, save via decapitation. Only one such feat has been documented in an epic battle. Because the bronze colossus is a creature with the current highest [`[DIFFICULTY]`](/index.php/Creature_token#DIFFICULTY "Creature token") in the game of 15 points, it does (according to the game) surpass Hidden Fun Stuff in terms of challenge, and also causes them not to be assigned for quests.
- The plural "colossuses" was reported as a bugBug:1953, but it was deemed an acceptable alternate and remains the official term. "Colossi" is however also widely used, not that you'd be likely to ever encounter several of them, if any.

    [CREATURE:COLOSSUS_BRONZE]
        [DESCRIPTION:A gigantic magic statue made of bronze and bent on mayhem.]
        [NAME:bronze colossus:bronze colossuses:bronze colossus]
        [CASTE_NAME:bronze colossus:bronze colossuses:bronze colossus]
        [CREATURE_TILE:'C'][COLOR:6:0:0]
        [CREATURE_CLASS:FOOTWEAR_TRACKING_SYMBOL]
        [MEGABEAST][DIFFICULTY:15] 11 or higher does not get assigned as adv mode quests
            [ATTACK_TRIGGER:3:3:3]
        [FANCIFUL]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [SPHERE:METALS]
        [SPHERE:STRENGTH]
        [SPHERE:WAR]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_LAND]
        [EQUIPS]
        [NOFEAR]
        [PREFSTRING:height]
        [NOBONES]
        [ODOR_LEVEL:0] no smell
        [SMELL_TRIGGER:10000] cannot smell
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:HUMANOID_JOINTS:5FINGERS:5TOES]
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
        [BODY_SIZE:0:0:20000000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ITEMCORPSE:STATUE:NO_SUBTYPE:INORGANIC:BRONZE]
        [ITEMCORPSE_QUALITY:5]
        [DIURNAL]
        [LAIR:SHRINE:100]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_LEARNED]
