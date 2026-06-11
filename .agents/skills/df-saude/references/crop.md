# Crop

> Fonte: [Crop](https://dwarffortresswiki.org/index.php/Crop) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*(This article is about crop plants. If you want information about trees, see Tree.)*

**Crops** are plants that can be farmed (this happens at farm plots), traded for, or acquired by plant gathering. There are two types of crops: aboveground and subterranean (underground). The seeds of subterranean crops may be brought from the starting embark screen or, with some small luck, purchased from dwarven caravans. Above ground crops and seeds may be purchased from human or elven caravans or gathered by dwarves with the plant gathering labor enabled. Seeds may also be collected by processing the plants or eating them (but not by cooking!). There is a limit of 200 seeds per type (adjustable in settings), after which no additional seeds will be produced.

A few of the plants listed below are not strictly crops, as they have no seeds and can't be planted (see note "4", below). "Wet" and "Dry" determine where plants are found in proximity to watercourses when gathering wild plants, and do not affect farm plots.

Most plants can be brewed into alcohol, each plant type producing a different variation, and dwarves do prefer *some* variety in their drink. Some plants may be eaten raw, others must be cooked first, others must be processed (by milling or plant processing) before they are edible, and still others are inedible, producing only non-food products (their seeds may be edible, though). Drinks may be cooked as ingredients in prepared meals, but at least one of the ingredients must be a non-liquid.

All drinks require a spare barrel or large pot for storage, and some other products also require specific containers for storage. Plants can be stored in barrels or without a container; seeds are stored individually or in bags which can then be put into barrels. It may be advisable to have a small stockpile that accepts only seeds next to your farm(s), since dwarves will happily carry entire pots of seeds across the map to pick up a single seed, leading to cancellation spam and irregular planting.

## Standard plants

These are the plants defined in the file plant_standard.txt. Standard plants have been changed very little from the previous version; tiles and colors have been upgraded, and brewing, pressing and processing plants to bags have been re-implemented as reactions, which means these options will be unavailable in the workshop if materials are missing.

### Dwarven crops

There are only 6 underground (aka "dwarven") crops. Five can be used for food, booze and other fortress needs, and one (dimple cups) is dye only (although the seeds can be cooked). All six are (usually) available on embark and included in the default embark profile.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Tile | Graphic | Name | Biome / & / seasons | Align | Value | Drink | Drink / value / 1 | Eat | Cook2 | Product(s) / 5 / & value |
| `♠` |  | Plump helmet | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Dwarven wine | 10☼ | Yes | Yes | · / plump helmet spawn / 1☼ |
| `τ` |  | Pig tail | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Dwarven ale | 10☼ | No | No | · / pig tail seed / 1☼ / φ / pig tail thread (p) / 12☼ / ≈ / pig tail slurry (h) / 2☼ |
| `τ` |  | Cave wheat | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Dwarven beer | 10☼ | No | Pr3 | · / cave wheat seed / 1☼ / · / dwarven wheat flour (m) / 20☼ |
| `Φ` |  | Sweet pod | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Dwarven rum | 10☼ | No | Pr3 | · / sweet pod seed / 1☼ / · / dwarven sugar (m) / 20☼ / ≈ / dwarven syrup (l) / 100 / 1 / ☼ |
| `♣` |  | Quarry bush | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | Pr3 | ♠ / quarry bush leaf (b) / 50 / 1 / ☼ / · / rock nut / 1☼ / ≈ / rock nut paste (m) / 1☼ / ≈ / rock nut press cake (s) / 1☼ / ≈ / rock nut oil (s) / 5☼ |
| `♥` |  | Dimple cup | Subterranean Water / (Layers 1-3) / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | No | · / dimple cup spawn / 1☼ / · / dimple dye (m) / 20☼ |

### Above-ground plants

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Tile | Graphic | Name | Biome / & / seasons | Align | Value | Drink | Drink / value / 1 | Eat | Cook2 | Product(s) / 5 / & value |
| `τ` |  | Muck root | Any Wetland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 1☼ | Swamp whiskey | 5☼ | Yes | Yes | · / muck root seed / 1☼ |
| `Φ` |  | Bloated tuber | Any Wetland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Tuber beer | 10☼ | Yes | Yes | · / bloated tuber seed / 1☼ |
| `Φ` |  | Kobold bulb4 | Any Wetland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 5☼ | *None* | — | No | No | ≈ / gnomeblight / (e) / 500 / 1 / ☼ |
| `:` |  | Prickle berry | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 1☼ | Prickle berry wine | 5☼ | Yes | Yes | · / prickle berry seed / 1☼ |
| `:` |  | Strawberry | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Strawberry wine | 10☼ | Yes | Yes | % / strawberry fruit / 1☼ / : / strawberry plant / 1☼ / · / strawberry seed / 1☼ |
| `τ` |  | Longland grass | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Longland beer | 10☼ | No | Pr3 | · / longland grass seed / 1☼ / · / longland flour (m) / 20☼ |
| `ÿ` |  | Valley herb4 | Temperate Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 10☼ | *None* | — | No | Yes | ≈ / golden salve / (v) / 500 / 1 / ☼ |
| `τ` |  | Rat weed | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 1☼ | Sewer brew | 5☼ | Yes | Yes | · / rat weed seed / 1☼ |
| `:` |  | Fisher berry | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Fisher berry wine | 10☼ | Yes | Yes | · / fisher berry seed / 1☼ |
| `ƒ` |  | Rope reed | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | River spirits | 10☼ | No | No | · / rope reed seed / 1☼ / φ / rope reed thread (p) / 12☼ / ≈ / rope reed slurry (h) / 2☼ |
| `τ` |  | Blade weed | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | No | · / blade weed seed / 1☼ / · / emerald dye (m) / 20☼ |
| `τ` |  | Hide root | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 1☼ | *None* | — | No | No | · / hide root seed / 1☼ / · / redroot dye (m) / 10☼ |
| `τ` |  | Sliver barb | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | Evil | 1☼ | Gutter cruor | 5☼ | No | No | · / sliver barb seed / 1☼ / · / sliver dye (m) / 20☼ |
| `:` |  | Sun berry | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | Good | 9☼ | Sunshine | 25☼ | Yes | Yes | · / sun berry seed / 1☼ |
| `§` |  | Whip vine | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | Savage | 1☼ | Whip wine | 15☼ | No | Pr3 | · / whip vine seed / 1☼ / · / whip vine flour (m) / 25☼ |

**Notes:**

1 This is the value for a stack of 5 units, which is the number rendered from a single plant.

2 Anything that can be cooked is edible afterwards. Note that cooking leaves no seeds for re-planting.

3 These plants cannot be eaten/cooked until they are further processed, either by milling or extracting; see "products" column for process product.

4 These plants cannot be grown on a farm plot (in unmodded games) as they have no seeds. They can only be acquired through plant gathering (in season only) or trade.

5 To get the products/extracts from the plants they have to be processed, in the following workshops, using the following labors:

- **m**: mill (cave wheat, sweet pod, longland grass, whip vine, dimple cup, blade weed, hide root, sliver barb): at quern or millstone, using milling.
- **b**: process to bag (quarry bush): at farmer's workshop, using plant processing.
- **s**: press paste into oil (quarry bush): at screw press.
- **l**: process to barrel (sweet pod): at farmer's workshop, using plant processing.
- **p**: process plant (pig tail, rope reed): at farmer's workshop, using plant processing.
- **h**: mash plant (pig tail, rope reed): at quern or millstone, using papermaking.
- **v**: process to vial (valley herb): at farmer's workshop, using plant processing.
- **e**: extract plant essence (kobold bulb): at still, using plant gathering.

6 'Not Freezing' Biome refers to all land biomes except Mountains, Glaciers, and Tundras.

## Garden plants

All garden plants are above-ground, and can grow year-round. Garden plants are defined in a separate file from standard plants, named, somewhat predictably, plant_garden.txt.

Unlike standard plants, garden plants will also produce growths - leaves, buds, flowers, pods and fruits. As a general rule, leaves can only be cooked, buds can be both cooked and brewed.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Tile | Graphic | Name | Biome / & / seasons | Align | Value | Drink | Drink / value / 1 | Eat | Cook2 | Product(s) / 5 / & value |
| `:` |  | Artichoke | Temperate Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Artichoke wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / heart / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Asparagus | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Bambara groundnut6 | Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / fruit / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | String bean6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Broad bean6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Beet | Temperate Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Beetroot wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Bitter melon6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Cabbage | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Caper | Any Desert / Any Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / % / fruit / 2☼ / ♣ / flower / — / % / bud / 2☼ / · / seed / 1☼ |
| `:` |  | Wild carrot | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Carrot wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Cassava | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Cassava beer | 10☼ | No | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Celery6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Chickpea6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Chicory6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Cowpea6 | Tropical Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Cucumber | Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Eggplant | Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Garden cress6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Garlic6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / bulb / 2☼ / ü / flower / — / · / seed / 1☼ |
| `:` |  | Horned melon | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / \* / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Leek6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Lentil6 | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Lettuce6 | Any Temperate / Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Mung bean6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Muskmelon | Any Temperate / Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Onion6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / bulb / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Parsnip | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Parsnip wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Pea6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Peanut6 | Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / fruit / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Pepper | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Potato | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Potato wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Radish | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Radish wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Red bean6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Rhubarb6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Soybean6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Spinach6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Squash | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Sweet potato | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Sweet potato wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Taro6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | Yes | ♠ / leaf / — / ♣ / flowers / — / · / seed / 1☼ |
| `:` |  | Tomato | Tropical Dry Broadleaf Forest / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Tomato wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Tomatillo | Tropical Dry Broadleaf Forest / Tropical Grassland / Tropical Savanna / Tropical Shrubland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Tomatillo wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Turnip | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | Turnip wine | 10☼ | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Urad bean6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Seed | ♠ / leaf / — / % / pod / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Watermelon | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / o / fruit / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Winter melon | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / — / o / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Lesser yam6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Long yam6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Purple yam6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | White yam6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | No | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Passion fruit | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Passion fruit wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Grape | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Cranberry | Any Temperate / Tundra / Taiga / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Cranberry wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Bilberry | Any Temperate / Tundra / Taiga / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Bilberry wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Blueberry | Any Temperate / Tundra / Taiga / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Blueberry wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Blackberry | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Blackberry wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Raspberry | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Raspberry wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `:` |  | Pineapple | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Pineapple wine | 10☼ | Yes | Yes | ♠ / leaf / — / % / fruit / 2☼ / ♣ / flower / — / · / seed / 1☼ |

**Notes:**

1 This is the value for a stack of 5 units, which is the number rendered from a single plant.

2 Anything that can be cooked is edible afterwards. Note that cooking leaves no seeds for re-planting.

3 These plants cannot be eaten/cooked until they are further processed, either by milling or extracting; see "products" column for process product.

4 These plants cannot be grown on a farm plot as they have no seeds. They can only be acquired through plant gathering (in season only) or trade.

5 Some products may require processing; see plant page for details.

6 These plants, when grown from seed on a farm plot, don't yield products that can be processed for seeds.

## Crop plants

These plants are defined in the file plant_crops.txt. They grow above ground, in any season.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Tile | Graphic | Name | Biome / & / seasons | Align | Value | Drink | Drink / value / 1 | Eat | Cook2 | Product(s) / 5 / & value |
| `τ` |  | Single-grain wheat | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Single-grain wheat beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Two-grain wheat | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Two-grain wheat beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Soft wheat | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Soft wheat beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Hard wheat | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Hard wheat beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Spelt | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Spelt beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Barley | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Barley wine | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Buckwheat | Tropical Dry Broadleaf Forest / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Buckwheat beer | 10☼ | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Oats | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Alfalfa6 | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 4☼ | *None* | — | Yes | Yes | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ |
| `τ` |  | Rye | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Rye beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Sorghum | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Sorghum beer | 10☼ | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Rice | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Rice beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Maize | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Maize beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Quinoa | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Quinoa beer | 10☼ | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Kaniwa | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Kaniwa beer | 10☼ | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `:` |  | Bitter vetch6 | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / % / pod / — / · / seed / 1☼ |
| `τ` |  | Pendant amaranth | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Pendant amaranth beer | 10☼ | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Blood amaranth | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Blood amaranth beer | 10☼ | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Purple amaranth | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Purple amaranth beer | 10☼ | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Red spinach6 | Not Freezing / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `τ` |  | Elephant-head amaranth6 | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | Yes | Yes | ♠ / leaf / 2☼ / ♣ / flower / — / · / seed / 1☼ |
| `τ` |  | Pearl millet | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Pearl millet beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | White millet | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | White millet beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Finger millet | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Finger millet beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Foxtail millet | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Foxtail millet beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Fonio | Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Fonio beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Teff | Tropical Grassland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | Teff beer | 10☼ | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour (m) / 20☼ |
| `τ` |  | Flax | Tropical Grassland / Tropical Savanna / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / · / flour / 20☼ / ≈ / paste (m) / 1☼ / ≈ / p. cake (s) / 1☼ / ≈ / oil (s) / 5☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Jute | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | No | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Hemp | Any Temperate / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Pr3 | ♠ / leaf / — / · / seed / 1☼ / · / flour / 20☼ / ≈ / paste (m) / 1☼ / ≈ / p. cake (s) / 1☼ / ≈ / oil (s) / 5☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Cotton | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / ≈ / paste (m) / 1☼ / ≈ / p. cake (s) / 1☼ / ≈ / oil (s) / 5☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Ramie | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | No | ♠ / leaf / — / · / seed / 1☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Kenaf | Any Tropical / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | Pr3 | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / ≈ / paste (m) / 1☼ / ≈ / p. cake (s) / 1☼ / ≈ / oil (s) / 5☼ / φ / thread (p) / 12☼ / ≈ / slurry (h) / 2☼ |
| `τ` |  | Papyrus sedge | Any Tropical Wetland / Wet / Dry / Spring / Summer / Autumn / Winter | All | 2☼ | *None* | — | No | No | ♠ / leaf / — / ♣ / flower / — / · / seed / 1☼ / ⌡ / papyrus / 10☼ |

**Notes:**

1 This is the value for a stack of 5 units, which is the number rendered from a single plant.

2 Anything that can be cooked is edible afterwards. Note that cooking leaves no seeds for re-planting.

3 These plants cannot be eaten/cooked until they are further processed, either by milling or extracting; see "products" column for process product.

4 These plants cannot be grown on a farm plot as they have no seeds. They can only be acquired through plant gathering (in season only) or trade.

5 Some products may require processing; see plant page for details.

6 These plants, when grown from seed on a farm plot, don't yield products that can be processed for seeds.

## Best crop to grow

There is no "best" crop, but some are clearly superior to others, depending on your needs and available resources.

### All-purpose

Many dwarves prefer the humble plump helmet, which can be grown year-round, eaten raw, cooked, or brewed into wine, and many early fortresses rely on the plump helmet crop as a staple of their diet. All above-ground crops are all-seasons as well, the best of which are probably sun berries, hemp, and whip vines. See the above table summarizing the crop products, limitations, and values.

Because of occasional above-ground inconveniences, having an underground plump helmet farm, or, at least, some plump helmet spawn, may be useful emergency preparation.

### Booze

Four principal seeds available at the beginning of an expedition (cave wheat, pig tail, plump helmet, sweet pod) all produce underground crops that can be made into booze worth 10☼. Above ground crops will require you to trade or gather for seeds, but the best of them that can be farmed are sun berries, which produce sunshine worth 25☼.

Keep in mind that dwarves care more about the diversity of available booze than its value.

For quantity, cave wheat and sweet pod mature in 42 days, versus 25 for the other crops, so they may yield less alcohol per farm plot. Plump helmets mature in 25 days and grow year-round, which may be a good starting point for your alcohol industry, but exclusive dependence on it will cause stress.

Rope reeds and pig tails can be made into booze, but you might prefer to use them to make thread.

### Dye

There are four dye crops. Three 20☼ dye crops: blade weed and sliver barb (above ground) and dimple cups (underground). Hide root (above ground) is a 10☼ dye. Dyeing should be considered a low priority because all it does is change the color of cloth or thread and slightly increase its value. You might not want a dedicated farm to grow dye crops; it can be enough to forage for them with herbalism or import them from caravans.

### Food

In terms of sheer dwarfbucks, sweet pods produce the most valuable foodstuff: dwarven syrup (100☼). In terms of quantity and value, other good crops are quarry bushes (which yield 5 quarry bush leaves when processed) and whip vines (which can be milled into whip vine flour). Diversity in meals is also important to dwarves.

### Thread

All plant thread is equally valuable (at 2☼ per unit), so the main decision is between a seasonal underground crop (pig tails) or one of the year-round above-ground crops (cotton, rope reeds, hemp, flax, jute, ramie, kenaf). These plants are also equally useful for making paper. Papyrus is slightly easier to process if you want to make a lot of paper, but papyrus can't be used for any other purpose and it is only available in some tropical wetlands.

## Bugs

- Plant handling/processing is incomplete for some crops.Bug:6940 This results in plants that, when picked, are inedible because the wrong parts are picked, or where seeds are impossible to pull from the proper plant parts. Large numbers of crops are therefore incapable of being farmed.

## See also

- Farming
