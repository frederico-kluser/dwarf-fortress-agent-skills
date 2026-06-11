# Ibex man

> Fonte: [Ibex man](https://dwarffortresswiki.org/index.php/Ibex_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ibex men for their long horns.**
- **Biome**
- **Any Grassland Any Desert**
- **Variations**
- **Ibex - Ibex man - Giant ibex**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 12,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A horned person with the head of an ibex.*

**Ibex men** are the animal person version of the ibex, found in savage grasslands and deserts (spawning in groups of 1-5 individuals), and are roughly the size of a dwarf. They are one of the few animal people species able to wear dwarf-sized armor and clothing, making them a good choice for adventurers starting in a dwarven civilization. Both ibex men and women have horns, but these are mostly decorative, as they can’t use them for goring attacks. Their hooves add some ”punch” to their kicks, though.

Some dwarves like ibex men for their *long horns*.

Has to constantly hear unfunny "Feeling horny?" jokes...\
*Art by Operation Graphite*

    [CREATURE:IBEX_MAN]
        [COPY_TAGS_FROM:IBEX]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:ibex man:ibex men:ibex man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:ibex woman:ibex women:ibex woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:ibex man:ibex men:ibex man]
        [DESCRIPTION:A horned person with the head of an ibex.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'i']
        [COLOR:6:0:0]
