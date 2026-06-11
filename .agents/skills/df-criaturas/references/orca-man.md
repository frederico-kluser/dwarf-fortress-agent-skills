# Orca man

> Fonte: [Orca man](https://dwarffortresswiki.org/index.php/Orca_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes orca men for their great jumps.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Orca - Orca man - Giant orca**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Beaching · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 91,260 cm 3
- **Mid:** 1,267,500 cm 3
- **Max:** 2,535,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An aquatic person in the shape of an orca with arms.*

**Orca men** are animal people versions of the common orca, who can be found in savage oceans. They spawn in groups of 3-5 individuals and are generally content to keep to themselves, as they are restricted to the water. They are the joint second largest of all animal people, tied with elephant men and losing only to sperm whale men, being 42 times larger than a dwarf in comparison. Like their animal counterparts, they may rarely be subject to beaching.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like orca men for their *coloration* and their *great jumps*.

## Anatomy

The orca man has a body shaped like all whale men– a head on a body with no neck, a right flipper and left flipper attached to the upper body, also a right arm and left arm attached to the upper body, and a tail on the lower body. Each arm is jointed with an elbow, and on each hand has a thumb with two additional fingers. The total size of each arm is twice that of each flipper. Like all whale men, the orca man's fastest form of locomotion is swimming, though he can also climb, crawl, and perform a faster walk-crawl like snakes and merpeople.

There's no explanation of where the arms and side flippers are attached relative to each other. It might make sense for the arms to be below the flippers, though, so the longer arms don't cover the flippers while swimming. But maybe they are closer together with more dorsal side flippers and more ventral arms. Or maybe they are right on top of each other with the side flipper attached to the shoulder blades of the humanoid arms. On real-world orcas, their flippers are attached to shoulder blades and have bones equivalent to those in human arms, hands, and fingers with humeri, radii, ulnae, carpels, metacarpels, and phalanges.

    [CREATURE:ORCA_MAN]
        [COPY_TAGS_FROM:ORCA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:orca man:orca men:orca man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:orca woman:orca women:orca woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TAIL_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:528:352:176:1900:2900] 50 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:orca man:orca men:orca man]
        [DESCRIPTION:An aquatic person in the shape of an orca with arms.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'O']
        [COLOR:0:0:1]
