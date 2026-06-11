# Rhesus macaque man

> Fonte: [Rhesus macaque man](https://dwarffortresswiki.org/index.php/Rhesus_macaque_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rhesus macaque men for their mischief.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Rhesus macaque - Rhesus macaque man - Giant rhesus macaque**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,750 cm 3
- **Mid:** 18,750 cm 3
- **Max:** 37,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a rhesus macaque.*

**Rhesus macaque men** are humanoid versions of the common rhesus macaque and a species of animal people, found in savage temperate biomes. They are only a little over half the size of an adult dwarf, being unlikely to pose a threat to a civilian's life, though they retain their animal brethren's thieving habits; they can and will steal food and items in their reach, and due to being larger than a normal macaque, they may cause actual harm to dwarves who try to fight them.

Like other savage animal people, rhesus macaque men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like rhesus macaque men for their *mischief*.

Still as annoying as the animal version.\
*Art by Xu Tianhua*

    >[CREATURE:MACAQUE_RHESUS_MAN]
        [COPY_TAGS_FROM:MACAQUE_RHESUS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:rhesus macaque man:rhesus macaque men:rhesus macaque man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:rhesus macaque woman:rhesus macaque women:rhesus macaque woman]
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
        [NAME:rhesus macaque man:rhesus macaque men:rhesus macaque man]
        [DESCRIPTION:A person with the head and tail of a rhesus macaque.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
