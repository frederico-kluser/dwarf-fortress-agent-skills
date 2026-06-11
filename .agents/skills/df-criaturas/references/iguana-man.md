# Iguana man

> Fonte: [Iguana man](https://dwarffortresswiki.org/index.php/Iguana_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes iguana men for their head bobs.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Iguana - Iguana man - Giant iguana**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 138.75 cm 3
- **Mid:** 4,625 cm 3
- **Max:** 37,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of an iguana.*

**Iguana men** are humanoid versions of the common iguana, a species of unremarkable animal people found in savage tropical forests. They are a little over half the size of an adult dwarf and spawn in groups of 1-3 individuals, who are unlikely to pose any danger to your fortress.

Like other savage animal people, iguana men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Despite not being able to be butchered, iguana man products are worth twice as much as others.

Some dwarves like iguana men for their *dewlaps* and their *head bobs*.

Don't pat them on the back...\
*Art by Anna Shpylevska*

    [CREATURE:IGUANA_MAN]
        [COPY_TAGS_FROM:IGUANA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:iguana man:iguana men:iguana man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:iguana woman:iguana women:iguana woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:iguana man:iguana men:iguana man]
        [DESCRIPTION:A person with the head and tail of an iguana.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'i']
        [COLOR:2:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
