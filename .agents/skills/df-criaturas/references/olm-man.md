# Olm man

> Fonte: [Olm man](https://dwarffortresswiki.org/index.php/Olm_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes olm men for their gills.**
- **Biome**
- **Underground Depth: 1-2**
- **Variations**
- **Olm - Olm man - Giant olm**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An animal person with the head of the amphibious olm. It lives underground near water.*

**Olm men** are the humanoid versions of the common olm and are one of the many races of underground tribal animal people found living in small groups on any cavern level.

Despite being labelled as hostile in the unit list, olm men initially found in the caverns will ignore your citizens unless provoked. They will usually be observed carrying wooden spears, blowguns and shields, although they are sometimes seen using metal items instead. These can range from copper to steel, and are presumably caused by a bug. Depending on which other subterranean creatures they have access to, their blowdarts will be covered in different poisons, which can vary from mildly annoying cave spider venom to highly dangerous giant cave spider toxins. You can preemptively check for poisons by selecting a blowgunner, looking in their items tab and viewing their blowdarts.

Olm men may launch group attacks on your fort. When this happens, all tribesmen on the map will become hostile, even if they were peaceful minutes prior to the invasion. They may arrive with pets and mounts, some of which will be able to fly or easily catch up to your fleeing civilians. These invaders, unlike their above-ground counterparts, will not leave after some time has passed, even if your fort is completely sealed off from the caverns, nor will they prevent migrants, caravans or other invaders from arriving; including more waves of olm men. Because of this, several unchallenged assaults from them can quickly cause your game's FPS to drop to single-digit levels, thus making your fort completely unplayable.

Olm men are, predictably, amphibious, meaning that they can swim through your reservoirs in order to get through your defenses, or will lie in wait to ambush your fisherdwarves, so plan your defenses accordingly. Fortunately, it turns out that being in the water washes any blowdarts clean of their venom, meaning that blowgunners that travel aquatically will have their threat level minimized.

Some dwarves like olm men for their *gills*.

An Olm man with wizard-like abilites!\
*Art by ThisIsTheFool*

    [CREATURE:OLM_MAN]
        [COPY_TAGS_FROM:OLM]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:olm man:olm men:olm man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:olm woman:olm women:olm woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:olm man:olm men:olm man]
        [DESCRIPTION:An animal person with the head of the amphibious olm.  It lives underground near water.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:7:0:1]
        [LOW_LIGHT_VISION:10000]

    Entity (
    civilization
    ) Raws

    [ENTITY:SUBTERRANEAN_ANIMAL_PEOPLES]
        [LAYER_LINKED]
        [CREATURE:AMPHIBIAN_MAN]
        [CREATURE:REPTILE_MAN]
        [CREATURE:SERPENT_MAN]
        [CREATURE:RODENT MAN]
        [CREATURE:BAT_MAN]
        [CREATURE:ANT_MAN]
        [CREATURE:OLM_MAN]
        [CREATURE:CAVE_SWALLOW_MAN]
        [CREATURE:CAVE_FISH_MAN]
        [WEAPON:ITEM_WEAPON_SPEAR]
        [WEAPON:ITEM_WEAPON_BLOWGUN]
            [AMMO:ITEM_AMMO_BLOWDARTS]
        [SHIELD:ITEM_SHIELD_SHIELD]
        [SHIELD:ITEM_SHIELD_BUCKLER]
        [WOOD_WEAPONS]
        [WOOD_ARMOR] shields
        [USE_ANY_PET_RACE]
        [INDOOR_WOOD]
        [USE_CAVE_ANIMALS]
        [USE_ANIMAL_PRODUCTS]
        [EQUIPMENT_IMPROVEMENTS]
        [FRIENDLY_COLOR:1:0:1]
        no site or biome or attack info for now
        [MAX_STARTING_CIV_NUMBER:100] all irrelevant right now
        [MAX_POP_NUMBER:10000]
        [MAX_SITE_POP_NUMBER:120]
        [PERMITTED_JOB:CARPENTER]
        [PERMITTED_JOB:WOODCUTTER]
        [PERMITTED_JOB:ANIMAL_CARETAKER]
        [PERMITTED_JOB:ANIMAL_TRAINER]
        [PERMITTED_JOB:HUNTER]
        [PERMITTED_JOB:WOODCRAFTER]
        [PERMITTED_JOB:LEATHERWORKER]
        [PERMITTED_JOB:BONE_CARVER]
        [PERMITTED_JOB:FISHERMAN]
        [PERMITTED_JOB:FISH_CLEANER]
        [PERMITTED_JOB:COOK]
        [PERMITTED_JOB:BUTCHER]
        [PERMITTED_JOB:TANNER]
        [PERMITTED_REACTION:TAN_A_HIDE]
        *** ethics copied from kobolds for now
        [ETHIC:KILL_ENTITY_MEMBER:PUNISH_EXILE]
        [ETHIC:KILL_NEUTRAL:REQUIRED]
        [ETHIC:KILL_ENEMY:REQUIRED]
        [ETHIC:KILL_ANIMAL:ACCEPTABLE]
        [ETHIC:KILL_PLANT:ACCEPTABLE]
        [ETHIC:TORTURE_AS_EXAMPLE:UNTHINKABLE]
        [ETHIC:TORTURE_FOR_INFORMATION:NOT_APPLICABLE]
        [ETHIC:TORTURE_FOR_FUN:ACCEPTABLE]
        [ETHIC:TORTURE_ANIMALS:UNTHINKABLE]
        [ETHIC:TREASON:UNTHINKABLE]
        [ETHIC:OATH_BREAKING:NOT_APPLICABLE]
        [ETHIC:LYING:NOT_APPLICABLE]
        [ETHIC:VANDALISM:NOT_APPLICABLE]
        [ETHIC:TRESPASSING:NOT_APPLICABLE]
        [ETHIC:THEFT:NOT_APPLICABLE]
        [ETHIC:ASSAULT:PERSONAL_MATTER]
        [ETHIC:SLAVERY:UNTHINKABLE]
        [ETHIC:EAT_SAPIENT_OTHER:UNTHINKABLE]
        [ETHIC:EAT_SAPIENT_KILL:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_SAME_RACE:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_SAPIENT:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_ANIMAL:UNTHINKABLE]
        *** later
        [VALUE:LAW:0]
        [VALUE:LOYALTY:0]
        [VALUE:FAMILY:0]
        [VALUE:FRIENDSHIP:0]
        [VALUE:POWER:0]
        [VALUE:TRUTH:0]
        [VALUE:CUNNING:0]
        [VALUE:ELOQUENCE:0]
        [VALUE:FAIRNESS:0]
        [VALUE:DECORUM:0]
        [VALUE:TRADITION:0]
        [VALUE:ARTWORK:0]
        [VALUE:COOPERATION:0]
        [VALUE:INDEPENDENCE:0]
        [VALUE:STOICISM:0]
        [VALUE:KNOWLEDGE:0]
        [VALUE:INTROSPECTION:0]
        [VALUE:SELF_CONTROL:0]
        [VALUE:TRANQUILITY:0]
        [VALUE:HARMONY:0]
        [VALUE:MERRIMENT:0]
        [VALUE:CRAFTSMANSHIP:0]
        [VALUE:MARTIAL_PROWESS:0]
        [VALUE:SKILL:0]
        [VALUE:HARD_WORK:0]
        [VALUE:SACRIFICE:0]
        [VALUE:COMPETITION:0]
        [VALUE:PERSEVERANCE:0]
        [VALUE:LEISURE_TIME:0]
        [VALUE:COMMERCE:0]
        [VALUE:ROMANCE:0]
        [VALUE:NATURE:0]
        [VALUE:PEACE:0]
        [AMBUSHER]
        [STONE_SHAPE:OVAL_CABOCHON]
        [GEM_SHAPE:OVAL_CABOCHON]
