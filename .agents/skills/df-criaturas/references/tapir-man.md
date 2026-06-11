# Tapir man

> Fonte: [Tapir man](https://dwarffortresswiki.org/index.php/Tapir_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tapir men for their floppy noses.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Tapir - Tapir man - Giant tapir**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Milkable · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 13,500 cm 3
- **Mid:** 67,500 cm 3
- **Max:** 135,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a tapir.*

**Tapir men** are humanoid versions of the common tapir and a species of unremarkable animal people, found in savage tropical most broadleaf forests. They are a little over twice the weight of a dwarf, and therefore should be approached with caution.

Like other savage animal people, tapir men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

As the animal person template does not remove it, tapir women produce milk.

Some dwarves like tapir men for their *floppy noses*.

A tapir man attacking a dwarf.\
*Art by bionictoast*

    [CREATURE:TAPIR_MAN]
        [COPY_TAGS_FROM:TAPIR]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:tapir]
            [CVCT_REPLACEMENT:tapir man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:tapir]
            [CVCT_REPLACEMENT:tapir man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:tapir man:tapir men:tapir man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:tapir woman:tapir women:tapir woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:tapir man:tapir men:tapir man]
        [DESCRIPTION:A person with the head of a tapir.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'T']
        [COLOR:7:0:1]
