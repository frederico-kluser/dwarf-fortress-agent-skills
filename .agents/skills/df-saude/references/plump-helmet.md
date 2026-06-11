# Plump helmet

> Fonte: [Plump helmet](https://dwarffortresswiki.org/index.php/Plump_helmet) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes plump helmets for their rounded tops.**
- **Seed**
- **/ Plump helmet spawn**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Underground Depth: 1-3**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Dwarven wine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Plump helmets** are the most basic, resilient, and versatile of the six underground plants for dwarves to grow. They appear as large mushrooms with a purple cap, and have burgundy-colored spores. They are one of the fastest growing plants and can be cooked, brewed into dwarven wine, and even eaten raw. They require an underground farm plot, which requires soil or muddy ground. They are the only plant food-item that can be purchased at embark.

Keep in mind that cooking plants destroys their seeds, or in this case their "spawn". Both eating a plant raw and brewing it will leave plump helmet spawn behind, which can then be transferred to a seed bag, then planted and used to grow more. New players should definitely farm this crop because it grows relatively quickly, can be planted in any season, may be used to make alcohol, or eaten raw if need be.

If you grow nothing but plump helmets over a large area, your fort may start drowning in plump helmets, a truly *terrible* condition wherein barrels upon barrels are needed to hold back the waves of purple mushrooms. There are two ways to combat this - firstly, start cooking them into meals, the fancier the better. These produce no spawn, and thus put a dent in the population. This will also level up a cook and produce happy thoughts in your dwarves. Secondly, rotate your crops to include such things as pig tail (to bootstrap a textile industry) or cave wheat (to provide some variety in the diet).

Plump helmet men are humanoid, intelligent versions of these plants.

Some dwarves like plump helmets for their *rounded tops*.

-

  There's an immature penis joke in there somewhere, but it'd be too long and hard to find.\
  *Art by Torgeir Fjereide*

-

  Mature Plump Helmets.

    [PLANT:MUSHROOM_HELMET_PLUMP]
        [NAME:plump helmet][NAME_PLURAL:plump helmets][ADJ:plump helmet]

        Every plant needs a structural material so that the game knows how it behaves when it's alive.

        Here the material is added to the plant, using a template from the material file.
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]

        Here the material is marked as the structural material (this could be below the edible tags which come next).  In general, you can use LOCAL_PLANT_MAT|
    , PLANT_MAT|
    |
    , CREATURE_MAT|
    |
     or INORGANIC|IRON (though the game might hiccup for a while specifically on plants that aren't structurally plants).
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]

            We also modify it a bit to make the plant edible.  Any token material can be used here to modify the material that was created from the template.
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:MUSHROOM:MUSHROOM_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [PICKED_TILE:6][PICKED_COLOR:5:0:0]
        [GROWDUR:300][VALUE:2]

        Next we establish an alcohol material in much the same way as the structural material.

        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            The material template is just called "alcohol" so we need to give it a proper name.
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven wine]
            [STATE_NAME_ADJ:LIQUID:dwarven wine]
            [STATE_NAME_ADJ:GAS:boiling dwarven wine]
            We also set a few more numbers to distinguish the alcohol from the template.
            [STATE_COLOR:ALL:AMETHYST]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]

        The seed material and information is established in a similar fashion.  Other plants (including trees) add materials in the same way, though trees cannot be used at this time with seeds/thread/drink etc.  They just use the TREE tag to obtain a wood material (they also have a structural material for their live form).

        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:plump helmet spawn:plump helmet spawn:4:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:rounded tops]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:5:0:0]
        [DEAD_SHRUB_COLOR:0:0:1]
