# Sponge man

> Fonte: [Sponge man](https://dwarffortresswiki.org/index.php/Sponge_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sponge men for their squishy texture.**
- **Biome**
- **Any Ocean Any Lake Any River**
- **Variations**
- **Sponge - Sponge man - Giant sponge**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Genderless · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person in the form of a sponge with arms and legs.*

**Sponge men** are humanoid versions of the common sponge and a species of animal people, found in most savage bodies of water. They are exactly as large as a dwarf and spawn in groups of 1-3 individuals. Because they are made of sponge tissue, they are incredibly fragile (even more so than normal sponges due to having many body parts to attack), making them harmless to all but the most unlucky of dwarves. Sponge men don't need to eat, drink or sleep to survive and are born as full-sized adults, never going through any growth during their lives.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like sponge men for their *squishy texture*.

"F" is for friends who do stuff together!"\
*Art by Arne*

### Creature behavior

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Sponge men are often known for wearing, unusually for an animal, trousers. Said trousers are often, even more unusually, square. They are known for their piercing, demonic laughter, and inability to commandeer a wagon. They are often at odds with squid men, although they are rarely aware of the fact. Sponge men tend to come under the employment of crab men, usually working in kitchens.

|  |
|----|
| "Sponge man" in other / Languages / Dwarven / : / adbok udos / Elven / : / meca onino / Goblin / : / gestrast ngorûg / Human / : / muma abo |

    [CREATURE:SPONGE_MAN]
        [COPY_TAGS_FROM:SPONGE]
        [GO_TO_TAG:BODY:BASIC_1PARTBODY]
        [BODY:HUMANOID_SIMPLE]
        [CV_REMOVE_TAG:BODY:BASIC_1PARTBODY_THOUGHT]
        [CV_REMOVE_TAG:NOTHOUGHT]
        [CV_REMOVE_TAG:IMMOBILE]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:sponge man:sponge men:sponge man]
        [CASTE_NAME:sponge man:sponge men:sponge man]
        [DESCRIPTION:A person in the form of a sponge with arms and legs.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:4:0:1]
