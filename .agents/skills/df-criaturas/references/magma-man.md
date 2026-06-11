# Magma man

> Fonte: [Magma man](https://dwarffortresswiki.org/index.php/Magma_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes magma men for their flowing movement.**
- **Biome**
- **Underground Depth: 3-4**
- **Attributes**
- **Building destroyer : Level 2**
- **Genderless · No Stun · No Pain · No Exert · Fire immune · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Obsidian stone**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Magma moving in the shape of a man. It has a cracked black crust.*

**Magma men** are dangerous and exceptionally rare inorganic construct creatures who inhabit the magma sea. They are composed of an inner liquid basalt core (which is to say, magma) and an outer, solid obsidian layer. As a result, they are much more durable than fire imps and especially fire men and their natural attacks are dangerous. They do not breathe fire or magma in any form, though. Like other inorganic construct creatures, magma men feel no emotion or exertion, are immune to pain and cannot be stunned. They are as large as humans and are immortal, only dying to violence.

Their hot temperature has the interesting effect of actually drying up water if they are submerged in it, as well as melting adjacent unmined ice. They will create steam upon touching water and being rained on, which will most likely lead to anyone caught in the steam clouds starting to cough. Additionally, they can create bursts of boiling blood if they step in a bloodied area, which displays the message Magma Man is caught in a burst of boiling blood!. Magma men are Level 2 building destroyers, which means that doors, hatches, bars, and other similar constructions are vulnerable to their rampage. When they die, they leave a usable chunk of obsidian instead of any carcass, although when you consider their rarity, there are much better sources of obsidian around.

Magma men can be captured in cage traps. However, if you use a wooden cage, it will slowly decay and eventually disappear, letting the magma man free to roam in your fortress, leading to much !FUN!.

Some dwarves like magma men for their *flowing movement*.

Can *literally* make blood boil.

    [CREATURE:ELEMENTMAN_MAGMA]
        [DESCRIPTION:Magma moving in the shape of a man.  It has a cracked black crust.]
        [NAME:magma man:magma men:magma man]
        [CASTE_NAME:magma man:magma men:magma man]
        [CREATURE_TILE:'M'][COLOR:4:0:1]
        [FIREIMMUNE][MAGMA_VISION]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_LAVA]
        [UNDERGROUND_DEPTH:3:4]
        [FREQUENCY:1][DIFFICULTY:2]
        [POPULATION_NUMBER:15:30]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [FIXED_TEMP:12000]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [PREFSTRING:flowing movement]
        [NOBONES]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [TISSUE:MAGMA]
            [TISSUE_NAME:magma:NP]
            [TISSUE_MATERIAL:INORGANIC:BASALT]
            [TISSUE_MAT_STATE:LIQUID]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:10]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:MAGMA]
        [TISSUE:CRUST]
            [TISSUE_NAME:crust:NP]
            [TISSUE_MATERIAL:INORGANIC:OBSIDIAN]
            [TISSUE_MAT_STATE:SOLID]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:CRUST]
        [BODY_SIZE:0:0:70000]
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
        [ITEMCORPSE:STONE:NO_SUBTYPE:STONE:USE_LAVA_STONE]
        [ODOR_LEVEL:0]
        [SMELL_TRIGGER:10000] cannot smell
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
