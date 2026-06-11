# Giant snail

> Fonte: [Giant snail](https://dwarffortresswiki.org/index.php/Giant_snail) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant snails for their shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Snail - Snail man - Giant snail**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Exotic mount · Shell**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-35
- **Butchering returns**
- **Food items**
- **Meat:** 28-67
- **Fat:** 10-18
- **Brain:** 4-5
- **Heart:** 2
- **Intestines:** 13-15
- **Eyes:** 2
- **Raw materials**
- **Shell:** 21-26
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a snail.*

**Giant snails** are predictably quite slow, as large as a grizzly bear and generally harmless. They are a good source of meat, fat, and especially shells (mostly for artifact requirements) in a pinch. They can cripple and may kill an unarmored dwarf with their push attacks, though, so you might want to send basic militia or a marksdwarf to hunt it. Giant snails can be tamed, but they are genderless and will not breed.

Like standard snails, giant snails can be found in every non-freezing savage biome. They may occasionally appear as mounts during a siege, but only fools would ride into battle on something as slow and relatively harmless as a giant snail.

Some dwarves like giant snails for their *shells*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

This is an image of a giant snail and a human. The giant snail is striking a menacing pose. The human looks terrified.

Humans are known to decorate their codices with images of this fearsome creature, indicating that this beast may have once been among the kings of beasts in the distant past.

    [CREATURE:GIANT_SNAIL]
        [COPY_TAGS_FROM:SNAIL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant snail:giant snails:giant snail]
        [CASTE_NAME:giant snail:giant snails:giant snail]
        [DESCRIPTION:A huge monster in the form of a snail.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:shells]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
