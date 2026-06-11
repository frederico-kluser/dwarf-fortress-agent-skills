# Elephant man

> Fonte: [Elephant man](https://dwarffortresswiki.org/index.php/Elephant_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elephant men for their trumpeting.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland**
- **Variations**
- **Elephant - Elephant man - Giant elephant**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 253,500 cm 3
- **Mid:** 1,267,500 cm 3
- **Max:** 2,535,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×5)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large person with the trunk and ears of an elephant.*

**Elephant men** are the humanoid versions of elephants, found in savage tropical forests and shrublands. They are the largest of the land-dwelling animal people and are joint second in size (along with orca men) only to the aquatic sperm whale men. However, they are smaller than some other land-dwelling humanoids such as giants and cyclopes.

As with other intelligent wilderness creatures, players can play as elephant men in adventurer mode. Their immense size makes them especially effective in combat. They also have a significantly larger carrying capacity than other adventurers, allowing them to easily carry many items around without slowing down.

In combat, elephant men's size makes it easy for them to break the grip of wrestlers and the impact from jumping into an opponent can easily send the unfortunate soul flying an average distance of seven tiles with no obstacles present. This is particularly useful when it is successfully performed to gain the initiative due to the likelihood that they will slam into a tree, wall, or other impassable obstacle, dealing additional damage and potentially incapacitating them long enough to get within melee range. Like elephants, the elephant man also has two tusks with which to gore enemies, which can be exceedingly useful should the player lodge their weapon in an agile enemy (most flying creatures).

Some dwarves like elephant men for their *strength*, their *amazing trunks*, their *calves' spirited antics*, their *tusks*, their *great weight*, their *social behavior*, their *flappy ears*, their *uprooting of trees*, their *aggressive sparring*, their *trumpeting*, their *tool use* and their *self-awareness*.

You wouldn't want his nose in your business.\
*Art by Loxodon*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite popular belief, elephant men are not humans with physical deformities featured as exhibits; though, some elephant men *do* have lots of deformities and scars, due to tanking lethal attacks of enemies while unarmored (it's hard to find elephant-sized armor nowadays).

    [CREATURE:ELEPHANT_MAN]
        [COPY_TAGS_FROM:ELEPHANT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:elephant man:elephant men:elephant man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:elephant woman:elephant women:elephant woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:elephant man:elephant men:elephant man]
        [DESCRIPTION:A large person with the trunk and ears of an elephant.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'E']
        [COLOR:7:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
