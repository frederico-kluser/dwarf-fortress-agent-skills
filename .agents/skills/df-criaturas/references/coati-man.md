# Coati man

> Fonte: [Coati man](https://dwarffortresswiki.org/index.php/Coati_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes coati men for their curiosity.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest**
- **Variations**
- **Coati - Coati man - Giant coati**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,800 cm 3
- **Mid:** 19,000 cm 3
- **Max:** 38,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a coati.*

**Coati men** are animal people variants of the common coati who can be found in savage temperate and tropical forests. They spawn in groups of 1-5 individuals and, much like their common precedential type specimens, are prone to stealing whatever items they can find and getting beaten to death by random civilians - sometimes even livestock - on sight. This will give your refuse stockpile's savior a fairly severe bad thought, just like killing any other sapient creature. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like coati men for their *curiosity*.

Less creepily awkward in-game.

    [CREATURE:COATI_MAN]
        [COPY_TAGS_FROM:COATI]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:coati man:coati men:coati man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:coati woman:coati women:coati woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:coati man:coati men:coati man]
        [DESCRIPTION:A person with the head and tail of a coati.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
