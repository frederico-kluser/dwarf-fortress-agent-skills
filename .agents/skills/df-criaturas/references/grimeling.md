# Grimeling

> Fonte: [Grimeling](https://dwarffortresswiki.org/index.php/Grimeling) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grimelings for their weedy bodies.**
- **Biome**
- **Temperate Freshwater Swamp Temperate Saltwater Swamp Tropical Freshwater Swamp Tropical Saltwater Swamp Mangrove Swamp Temperate Freshwater Marsh Temperate Saltwater Marsh Tropical Freshwater Marsh Tropical Saltwater Marsh**
- **Attributes**
- **Alignment:** Evil
- **Amphibious · Genderless · No Stun · No Pain · No Exert · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An evil monster from the swamp. It resembles a knot of waterlogged weeds but will strike the unaware victim.*

**Grimelings** are exceptionally rare, evil-aligned creatures found in evil wetlands, resembling humanoids made out of waterlogged weeds. They stand as tall as a human and spawn one at a time, lurking in the water and attacking dwarves who get too close. All grimelings possess Legendary skill in climbing.

Grimelings are interesting creatures, different from the usual evil humanoid dwarf-harassers. They possess no organs to speak of, including internal ones such as hearts, guts, brains or even *eyes* (though they can still see through [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token")), feel no emotion or exertion, are immune to pain, fear and dizziness, and cannot be stunned. Weapons cannot get stuck on grimelings, their corpses do not produce miasma and they cannot be butchered even though they are not intelligent. While they are currently made of standard flesh and muscle, a comment in their raw files states they are supposed to be made of weeds, implying Toady One intends to turn them into actual plant monsters when he ever gets around to it. Grimelings are the only creatures in the game with the [`[VEGETATION]`](/index.php/Creature_token#VEGETATION "Creature token") token.

Some dwarves like grimelings for their *slithering nature* and their *weedy bodies*.

A grimeling, drawn in crayon by Bay 12 Games.

## Trivia

- Initially, the premium version had a sprite for a child grimeling. It was later removed from the game, because grimelings are adults at birth.\

    [CREATURE:GRIMELING]
        [DESCRIPTION:An evil monster from the swamp.  It resembles a knot of waterlogged weeds but will strike the unaware victim.]
        [NAME:grimeling:grimelings:grimeling]
        [CASTE_NAME:grimeling:grimelings:grimeling]
        [CREATURE_TILE:'g'][COLOR:2:0:0]
        [BIOME:SWAMP_TEMPERATE_FRESHWATER]
        [BIOME:SWAMP_TEMPERATE_SALTWATER]
        [BIOME:SWAMP_TROPICAL_FRESHWATER]
        [BIOME:SWAMP_TROPICAL_SALTWATER]
        [BIOME:SWAMP_MANGROVE]
        [BIOME:MARSH_TEMPERATE_FRESHWATER]
        [BIOME:MARSH_TEMPERATE_SALTWATER]
        [BIOME:MARSH_TROPICAL_FRESHWATER]
        [BIOME:MARSH_TROPICAL_SALTWATER]
        [LARGE_ROAMING][EVIL][FREQUENCY:5]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [LARGE_PREDATOR]
        [GRASSTRAMPLE:0]
        [AMPHIBIOUS][UNDERSWIM]
        [NOT_BUTCHERABLE][VEGETATION]
        [PREFSTRING:slithering nature]
        [PREFSTRING:weedy bodies]
        [NOSMELLYROT]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOSTUCKINS][NOSKULL][NOSKIN][NOBONES][NOMEAT][NOTHOUGHT][NOEXERT]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [NOFEAR]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        *** needs to be made out of weeds
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
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
        [ODOR_LEVEL:5]
        [CANOPENDOORS]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
