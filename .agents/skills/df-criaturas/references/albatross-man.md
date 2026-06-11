# Albatross man

> Fonte: [Albatross man](https://dwarffortresswiki.org/index.php/Albatross_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes albatross men for their large wings.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Albatross - Albatross man - Giant albatross**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,462.5 cm 3
- **Mid:** 19,500 cm 3
- **Max:** 39,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of an albatross.*

**Albatross men** are animal people variants of the common albatross, who inhabit savage oceans. They spawn in groups of anywhere between 1-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All albatross men are born with Legendary skill in climbing.

Like other savage animal people, albatross men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like albatross men for their *large wings*.

    [CREATURE:ALBATROSS_MAN]
        [COPY_TAGS_FROM:BIRD_ALBATROSS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:albatross man:albatross men:albatross man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:albatross woman:albatross women:albatross woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:albatross man:albatross men:albatross man]
        [DESCRIPTION:A person with the head and wings of an albatross.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:7:0:1]
