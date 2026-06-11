# Black mamba man

> Fonte: [Black mamba man](https://dwarffortresswiki.org/index.php/Black_mamba_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black mamba men for their aggression.**
- **Biome**
- **Tropical Savanna Tropical Shrubland Any Tropical Forest Any Tropical Swamp**
- **Variations**
- **Black mamba - Black mamba man - Giant black mamba**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 300 cm 3
- **Mid:** 18,750 cm 3
- **Max:** 37,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person in the form of a large black mamba with arms.*

**Black mamba men** are the animal people versions of black mambas, half-man, half-snake. Unlike their solitary basal creatures, they can appear in packs of up to 3. Their venom is just as deadly as their smaller cousins', able to paralyse and kill a dwarf quickly, and causes great pain and unconsciousness. Since they appear in packs, they are unbelievably dangerous if they begin biting. They can use equipment and will not bite if armed with a weapon.

They're slightly larger than a dwarven child, and not nearly so threatening as the giant black mambas, as they lack the size to bite off entire limbs like the giant version often does.

Because of their deadly bite, black mamba men should be left alone if possible. Use ranged weapons as much as possible to avoid bites, and make sure any dwarf you send into melee is well-armoured to lessen the chance a bite will actually reach flesh to inject venom.

Some dwarves like black mamba men for their *deadly bite* and their *aggression*.

Note: Receiving hickeys may result in death.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Black mamba men are especially noted for their competitiveness, their intensity, and their dedication to winning.

Some black mamba women are known to be incredibly vengeful, hunting down those that wrong them with a ☼steel long sword☼ and their Legendary striking skill. For this reason, it's ill-advised to interrupt a black mamba woman's wedding.

    [CREATURE:BLACK_MAMBA_MAN]
        [COPY_TAGS_FROM:BLACK_MAMBA]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:black mamba man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:black mamba man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:black mamba man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BLACK_MAMBA]
            [CVCT_REPLACEMENT:BLACK_MAMBA_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:black mamba man:black mamba men:black mamba man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:black mamba woman:black mamba women:black mamba woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:black mamba man:black mamba men:black mamba man]
        [DESCRIPTION:A person in the form of a large black mamba with arms.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:0:0:1]
