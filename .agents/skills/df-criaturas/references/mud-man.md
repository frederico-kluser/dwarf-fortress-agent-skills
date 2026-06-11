# Mud man

> Fonte: [Mud man](https://dwarffortresswiki.org/index.php/Mud_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mud men for their peculiar smell.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Building destroyer : Level 2**
- **Genderless · No Stun · No Pain · No Exert · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Glob of mud**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid made of mud which lives near water underground.*

**Mud men** are extremely rare construct creatures made of solid mud, found exclusively at the third layer of the caverns. Like other construct creatures, they are non-sentient, feel no pain or fear, cannot be stunned and don't need to breathe. They are as large as humans and are level 2 building destroyers. Mud men are immortal and only die to violence.

Mud is not a particularly strong material, and even an unarmed dwarf civilian should be able to fight them one-on-one and emerge victorious with only a few bruises. An armored squad will make even quicker work of them, making them one of the less dangerous elemental men. When killed, mud men turn into a glob of mud which can't be used for anything. In adventurer mode, the player can smell mud men from a distance with o, with them being appropriately described as smelling like "mud".

Some dwarves like mud men for their *peculiar smell*.

Filthy in bed.

|  |
|----|
| "Mud man" in other / Languages / Dwarven / : / ol udos / Elven / : / salapa onino / Goblin / : / gob ngorûg / Human / : / vum abo |

    [CREATURE:ELEMENTMAN_MUD]
        [DESCRIPTION:A humanoid made of mud which lives near water underground.]
        [NAME:mud man:mud men:mud man]
        [CASTE_NAME:mud man:mud men:mud man]
        [CREATURE_TILE:'M'][COLOR:6:0:0]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:3:3]
        [FREQUENCY:1]
        [POPULATION_NUMBER:15:30]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [PREFSTRING:peculiar smell]
        [ODOR_STRING:mud]
        [ODOR_LEVEL:90]
        [SMELL_TRIGGER:10000] cannot smell
        [NOBONES]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [TISSUE:MUD]
            [TISSUE_NAME:mud:NP]
            [TISSUE_MATERIAL:MUD]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:MUD]
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
        [ITEMCORPSE:GLOB:NO_SUBTYPE:MUD:NONE]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_LEARNED]
