# Red panda man

> Fonte: [Red panda man](https://dwarffortresswiki.org/index.php/Red_panda_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes red panda men for their large striped tails.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Red panda - Red panda man - Giant red panda**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,750 cm 3
- **Mid:** 18,750 cm 3
- **Max:** 37,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized, walking red panda with arms and a tail. It prefers the forest and its beloved trees.*

**Red panda men** are animal people variants of the common red panda, found in savage temperate forests. They spawn in groups of 5-10 individuals and are generally content in keeping to themselves. Unlike their animal cousins, red panda men aren't restricted to eating just bamboo, though they'll only appear in areas where bamboo grows. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, red panda men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like red panda men for their *large striped tails*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Contrary to widespread rumors, there are no known records of a human woman transforming into a red panda woman.

There's a creature in the forest That you may not know He's got fur of red and white And a tail that's like a bow He walks on two legs like a man But he's not quite the same He's a red panda man And that's his name

Red panda man, red panda man He's the cutest thing you've ever seen Red panda man, red panda man He's a furry forest dream Red panda man, red panda man He's a gentle and a loyal friend Red panda man, red panda man He'll make you smile till the end

He lives among the bamboo trees And climbs them with ease He nibbles on the tender shoots And listens to the breeze He likes to keep his distance From the noisy crowd He's a red panda man And he's proud

Red panda man, red panda man He's the cutest thing you've ever seen Red panda man, red panda man He's a furry forest dream Red panda man, red panda man He's a gentle and a loyal friend Red panda man, red panda man He'll make you smile till the end

But sometimes he gets curious And wants to see the world He leaves his home and joins a band Of dwarves and men unfurled They welcome him with open arms And teach him many things He's a red panda man And he sings

Red panda man, red panda man He's the cutest thing you've ever seen Red panda man, red panda man He's a furry forest dream Red panda man, red panda man He's a gentle and a loyal friend Red panda man, red panda man He'll make you smile till the end

Red panda man, red panda man Red panda man, red panda man Red panda man, red panda man Red panda man, red panda man...

Usually appear slightly larger.\
*Art by Grosnez*

    [CREATURE:RED PANDA MAN]
        [COPY_TAGS_FROM:RED PANDA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:red panda man:red panda men:red panda man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:red panda woman:red panda women:red panda woman]
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
        [NAME:red panda man:red panda men:red panda man]
        [DESCRIPTION:A medium-sized, walking red panda with arms and a tail.  It prefers the forest and its beloved trees.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:4:0:0]
        [GO_TO_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
        [CV_ADD_TAG:SET_TL_GROUP:BY_CATEGORY:ARM_UPPER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:ARM_LOWER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:HAND:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FINGER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT:HAIR]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
