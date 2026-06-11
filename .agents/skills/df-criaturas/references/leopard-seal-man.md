# Leopard seal man

> Fonte: [Leopard seal man](https://dwarffortresswiki.org/index.php/Leopard_seal_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leopard seal men for their fierce nature.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Leopard seal - Leopard seal man - Giant leopard seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 23,500 cm 3
- **Mid:** 117,500 cm 3
- **Max:** 235,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A legless person with the head and back flippers of a leopard seal.*

**Leopard seal men** are animal people variants of the common leopard seal who can be found in savage arctic oceans. They spawn in groups of 1-5 individuals and while not too aggressive, will fight back if provoked. In terms of size, they are almost four times larger than a dwarf and will overpower an untrained civilian very quickly if angered.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like leopard seal men for their *fierce nature*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Leopard seal men are relatively unimportant in the world of *Dwarf Fortress*, but then along came Bim Silversnarl the Hero of Balance, a demigod leopard seal man adventurer whose journey has bloomed to legendary proportions. A true display of pinniped potential, he built his own settlement and recruited an entourage of loyal honey badger men who unquestionably follow their natural born leader. In his quest to "balance" and abate the overgrown evil in the world, Bim was responsible for the slaughter of over 700 trolls *en masse* during a visit to the dark fortress. Blood the color of adamantine was spilled in great abundance; the carnage was so unchecked that his iron battle axe and long sword actually wore out from endlessly beating them against troll flesh. Armok would be proud, and on the plus side, lag was reduced considerably. An ☼engraving of Bim Silversnarl☼ was carved in honor of the extraordinary mammal. Leopard seals do indeed have a *fierce nature*, after all. The video series chronicling his epic adventure can be found here.

Artist rendering of Bim Silversnarl by Mechlin (post)

|  |
|----|
| "Leopard seal man" in other / Languages / Dwarven / : / mingkil gembish udos / Elven / : / icemì ricote onino / Goblin / : / utol uzbad ngorûg / Human / : / upur epo abo |

    [CREATURE:LEOPARD_SEAL_MAN]
        [COPY_TAGS_FROM:LEOPARD_SEAL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS]
            [CVCT_REPLACEMENT:REAR_BODY_FLIPPERS]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:leopard seal man:leopard seal men:leopard seal man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:leopard seal woman:leopard seal women:leopard seal woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:leopard seal man:leopard seal men:leopard seal man]
        [DESCRIPTION:A legless person with the head and back flippers of a leopard seal.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'L']
        [COLOR:0:0:1]
