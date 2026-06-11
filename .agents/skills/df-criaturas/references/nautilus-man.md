# Nautilus man

> Fonte: [Nautilus man](https://dwarffortresswiki.org/index.php/Nautilus_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes nautilus men for their many tentacles.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Nautilus - Nautilus man - Giant nautilus**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Shell · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the shell and tentacles of a nautilus.*

**Nautilus men** are animal people variants of the common nautilus who can be found in savage oceans. They spawn in groups of 1-3 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like nautilus men for their *shells* and their *many tentacles*.

Possible fetish fuel.

    [CREATURE:NAUTILUS_MAN]
        [COPY_TAGS_FROM:NAUTILUS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:nautilus man:nautilus men:nautilus man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:nautilus woman:nautilus women:nautilus woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:nautilus man:nautilus men:nautilus man]
        [DESCRIPTION:A person with the shell and tentacles of a nautilus.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'n']
        [COLOR:4:0:1]
