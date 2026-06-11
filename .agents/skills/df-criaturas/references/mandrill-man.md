# Mandrill man

> Fonte: [Mandrill man](https://dwarffortresswiki.org/index.php/Mandrill_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mandrill men for their colorful faces.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Mandrill - Mandrill man - Giant mandrill**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A blue-rumped person with the head and tail of a mandrill.*

**Mandrill men** are animal people variants of the common mandrill who can be found in savage tropical moist broadleaf forests. They spawn in groups of 1-5 individuals and share their animal cousins' penchant for thievery, running off with any items or food they can get their grubby fingers on. In terms of size, they are a little over half the weight of the average dwarf. All mandrill men are born with Legendary skill in climbing.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like mandrill men for their *colorful faces*.

Easily annoyed at "going bananas" puns.\
*Art by Randy van der Vlag*

    [CREATURE:MANDRILL_MAN]
        [COPY_TAGS_FROM:MANDRILL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mandrill man:mandrill men:mandrill man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mandrill woman:mandrill women:mandrill woman]
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
        [NAME:mandrill man:mandrill men:mandrill man]
        [DESCRIPTION:A blue-rumped person with the head and tail of a mandrill.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:1:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
