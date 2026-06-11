# Sperm whale man

> Fonte: [Sperm whale man](https://dwarffortresswiki.org/index.php/Sperm_whale_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sperm whale men for their teeth.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Sperm whale - Sperm whale man - Giant sperm whale**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Beaching · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 250,700 cm 3
- **Mid:** 6,267,500 cm 3
- **Max:** 12,535,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge person with the head and flippers of a sperm whale.*

**Sperm whale men** are animal people counterparts of the common sperm whale, who live in savage oceans.

They are by far the largest of the animal people – half the weight of a fully-grown dragon, and roughly 33% larger than a giant. This makes taking them on very dangerous, but since they live in the water and are generally not aggressive, you'll be hard-pressed to have a sperm whale man problem – unless you have embarked on an evil ocean, but in that case, you brought that on yourself.

Like sperm whales, they have a 1/101 chance of being born with white skin instead of gray. They are also rarely subject to beaching.

While they can learn and would be able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface, and game doesn't feature aquatic civilizations.

Some dwarves like sperm whale men for their *teeth* and their *vengeful nature*.

    [CREATURE:SPERM_WHALE_MAN]
        [COPY_TAGS_FROM:SPERM_WHALE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:sperm whale man:sperm whale men:sperm whale man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:sperm whale woman:sperm whale women:sperm whale woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TAIL_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:sperm whale man:sperm whale men:sperm whale man]
        [DESCRIPTION:A huge person with the head and flippers of a sperm whale.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'W']
        [COLOR:7:0:0]
