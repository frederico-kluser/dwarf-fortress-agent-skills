# Capybara man

> Fonte: [Capybara man](https://dwarffortresswiki.org/index.php/Capybara_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes capybara men for their enormous rodentness.**
- **Biome**
- **Any Wetland**
- **Variations**
- **Capybara - Capybara man - Giant capybara**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 5,750 cm 3
- **Mid:** 28,750 cm 3
- **Max:** 57,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head of a capybara. It is fond of swimming.*

**Capybara men**, while not as violent as badger men, are still quite dangerous as they tend to stay in water. They will be more than happy to knock your dwarves into a murky pool where the dwarves'll drown, if they get too close.

Capybara men are able to wear dwarf-sized armor and clothing, making it a good choice for them to start in a dwarven civilization.

Some dwarves like capybara men for their *enormous rodentness*, their *graceful swimming*, or their *resonant barking*.

Not good swimmers.

    5 kph

    [CREATURE:CAPYBARA MAN]
        [COPY_TAGS_FROM:CAPYBARA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:capybara man:capybara men:capybara man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:capybara woman:capybara women:capybara woman]
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
        [NAME:capybara man:capybara men:capybara man]
        [DESCRIPTION:A humanoid with the head of a capybara.  It is fond of swimming.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:0]
