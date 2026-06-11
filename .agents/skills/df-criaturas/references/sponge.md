# Sponge

> Fonte: [Sponge](https://dwarffortresswiki.org/index.php/Sponge) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sponges for their squishy texture.**
- **Biome**
- **Any Ocean Any Lake Any River**
- **Variations**
- **Sponge - Sponge man - Giant sponge**
- **Attributes**
- **Aquatic · Genderless**
- **Cannot be tamed**
- **Size**
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-30
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny sea creature which dwells on the ocean floor, devoid of senses or motion.*

**Sponges** are aquatic creatures found in every above-ground water biome except murky pools. They are completely immobile and benign, ignoring any attempts to interact with them save for being occasionally overcome with terror. Sponges cannot survive out of water - if the body of water they inhabit is drained, they will asphyxiate and die. If confronted in melee range, a sponge will defend itself with push attacks.

While popularly known across the community in older versions of *Dwarf Fortress* for its invulnerability due to its lack of a brain and blood (with emphasis given to their giant cousins), sponges are exceptionally weak opponents in the current day. They are made out of unique sponge tissue, which is especially vulnerable to pulping damage from war hammers and maces, and slashing weapons, such as battle axes, will easily cleave them asunder in a few blows. While they are nearly as large as a dwarf, a sponge's push attack is unlikely to hurt anything much bigger than a dog. Sponges cannot be butchered and dwarves cannot naturally enter water, so your fortress is unlikely to have to worry about them beyond your hunters occasionally trying to kill one.

Sponges possess a pet value of 10, but lack the necessary tokens to be trainable. The fact they are both water-dwelling and immobile also presents a barrier, even if they were modded to be trainable.

Some dwarves like sponges for their *squishy texture*.

|  |
|----|
| "Sponge" in other / Languages / Dwarven / : / adbok / Elven / : / meca / Goblin / : / gestrast / Human / : / muma |

Admired for its *squishy texture*.

    50 kph

    Sponges were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:SPONGE]
        [DESCRIPTION:A tiny sea creature which dwells on the ocean floor, devoid of senses or motion.]
        [NAME:sponge:sponges:sponge]
        [CASTE_NAME:sponge:sponges:sponge]
        [CREATURE_TILE:'s'][COLOR:4:0:1]
        [PETVALUE:10]
        [FREQUENCY:100]
        [AQUATIC][NOBONES][IMMOBILE][UNDERSWIM]
        [BENIGN][NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_OCEAN]
        [BIOME:ANY_LAKE]
        [BIOME:ANY_RIVER]
        [NO_EAT]
        [NO_DRINK]
        [NOTHOUGHT]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [EXTRAVISION]
        [MUNDANE]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:squishy texture]
        [BODY:BASIC_1PARTBODY_THOUGHT]
        [USE_MATERIAL_TEMPLATE:SPONGE:SPONGE_TEMPLATE]
        [USE_TISSUE_TEMPLATE:SPONGE:SPONGE_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:ALL:SPONGE]
        [HAS_NERVES]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [BODY_SIZE:0:0:50000]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30] 2 to 200?
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SPONGE]
            [TL_COLOR_MODIFIER:RED:1]
                [TLCM_NOUN:body:SINGULAR]
