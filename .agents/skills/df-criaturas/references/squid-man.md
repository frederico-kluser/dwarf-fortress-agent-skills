# Squid man

> Fonte: [Squid man](https://dwarffortresswiki.org/index.php/Squid_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes squid men for their ability to spray ink.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Squid - Squid man - Gigantic squid**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small person with a head bearing ten tentacles.*

**Squid men** are animal people versions of the common squid, who can be found in savage oceans. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Testing in the arena (5 undead squid men VS. 5 human swordsmen) has shown that one re-animated squid man, in addition to being able to travel on land, has the potential to quickly become an army of re-animated body parts, as they have twelve limbs and eight sets of hands, all of which are theoretically capable of holding a weapon or item.

Some dwarves like squid men for their *ability to spray ink*.

### Creature behavior

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Does this look unsure to you?!\
*Art by skorp77*

The squid man is considered the most sophisticated of the aquatic animal people, as it has been known to use tools and play instruments, the clarinet being most commonly used, although at least one individual was extremely proficient with an organ. It has also been observed to have a strange aversion to sponge men. More research is necessary to determine the cause of this.

Reports have also surfaced of squid man children competing deep below the waves for territory using their ink despite being born into adulthood. It is still a mystery among Dwarven biologists as to how and why such events are coordinated. However, one theory suggests they are training for their ongoing war with the octopus men.

|  |
|----|
| "Squid man" in other / Languages / Dwarven / : / gongith udos / Elven / : / nethitha onino / Goblin / : / ozstag ngorûg / Human / : / galel abo |

    [CREATURE:SQUID MAN]
        [COPY_TAGS_FROM:SQUID]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:squid]
            [CVCT_REPLACEMENT:squid man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:squid]
            [CVCT_REPLACEMENT:squid man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:squid man:squid men:squid man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:squid woman:squid women:squid woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:squid man:squid men:squid man]
        [DESCRIPTION:A small person with a head bearing ten tentacles.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:1]
