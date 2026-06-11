# Item token

> Fonte: [Item token](https://dwarffortresswiki.org/index.php/Item_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

Item tokens are the first part in defining the target item in reactions, containing the item type and subtype. They determine the most basic form of the item, made more specific by material tokens. Most item tokens do not have a subtype; for these, either NO_SUBTYPE or NONE **must** be specified.

Nearly all items are made of a material, though several types expect a creature ID and caste ID (e.g. ANT:SOLDIER) instead.

Actually defining an item in the item raws is done with item definition tokens.

## Standard item tokens

|  |  |  |  |
|----|----|----|----|
| \# | Token | Subtype | Description |
| 0 |  BAR | NONE | Bars, such as metal, fuel, or soap. Standard dimension = 150. |
| 1 |  SMALLGEM | NONE | Cut gemstones usable in the jeweler's workshop |
| 2 |  BLOCKS | NONE | Blocks of any kind. |
| 3 |  ROUGH | NONE | Rough gemstones or raw glass. |
| 4 |  BOULDER /  STONE | NONE | Raw mined stone. |
| 5 |  WOOD | NONE | Wooden logs. |
| 6 |  DOOR | NONE | Doors and glass portals. |
| 7 |  FLOODGATE | NONE | Floodgates. |
| 8 |  BED | NONE | Beds. |
| 9 |  CHAIR | NONE | Chairs and thrones. |
| 10 |  CHAIN | NONE | Chains and ropes. |
| 11 |  FLASK | NONE | Flasks, vials, and waterskins. |
| 12 |  GOBLET | NONE | Goblets, mugs, and cups. |
| 13 |  INSTRUMENT | item_instrument.txt | Musical instruments. There is no vanilla item_instrument.txt as all vanilla instruments are generated. |
| 14 |  TOY | item_toy.txt | Toys. |
| 15 |  WINDOW | NONE | Glass windows. |
| 16 |  CAGE | NONE | Cages and terrariums. |
| 17 |  BARREL | NONE | Barrels. |
| 18 |  BUCKET | NONE | Buckets. |
| 19 |  ANIMALTRAP | NONE | Animal traps. |
| 20 |  TABLE | NONE | Tables. |
| 21 |  COFFIN | NONE | Coffins, caskets, and sarcophagi. |
| 22 |  STATUE | NONE | Statues. |
| 23 |  CORPSE | NONE | Corpses. Does not have a material that can be specified for reactions, but GET_MATERIAL_FROM_REAGENT will return the "dominant" material (normally flesh). |
| 24 |  WEAPON | item_weapon.txt | Weapons. |
| 25 |  ARMOR | item_armor.txt | Armor and clothing worn on the upper body. |
| 26 |  SHOES | item_shoes.txt | Armor and clothing worn on the feet. |
| 27 |  SHIELD | item_shield.txt | Shields and bucklers. |
| 28 |  HELM | item_helm.txt | Armor and clothing worn on the head. |
| 29 |  GLOVES | item_gloves.txt | Armor and clothing worn on the hands. |
| 30 |  BOX | NONE | Chests (wood, default), coffers (stone), and boxes (glass). |
| 31 |  BAG | NONE | Bags (plant cloth, silk or leather). |
| 32 |  BIN | NONE | Bins. |
| 33 |  ARMORSTAND | NONE | Armor stands. |
| 34 |  WEAPONRACK | NONE | Weapon racks. |
| 35 |  CABINET | NONE | Cabinets. |
| 36 |  FIGURINE | NONE | Figurines. |
| 37 |  AMULET | NONE | Amulets. |
| 38 |  SCEPTER | NONE | Scepters. |
| 39 |  AMMO | item_ammo.txt | Ammunition for hand-held weapons. |
| 40 |  CROWN | NONE | Crowns. |
| 41 |  RING | NONE | Rings. |
| 42 |  EARRING | NONE | Earrings. |
| 43 |  BRACELET | NONE | Bracelets. |
| 44 |  GEM | NONE | Large gems. |
| 45 |  ANVIL | NONE | Anvils. |
| 46 |  CORPSEPIECE | NONE | Body parts. Does not have a material that can be specified for reactions, but GET_MATERIAL_FROM_REAGENT will return the "dominant" material. |
| 47 |  REMAINS | NONE | Dead vermin bodies. Material is CREATURE_ID:CASTE. |
| 48 |  MEAT | NONE | Butchered meat. |
| 49 |  FISH | NONE | Prepared fish. Material is CREATURE_ID:CASTE. |
| 50 |  FISH_RAW | NONE | Freshly-caught fish. Material is CREATURE_ID:CASTE. |
| 51 |  VERMIN | NONE | Live vermin. Material is CREATURE_ID:CASTE. |
| 52 |  PET | NONE | Tame vermin. Material is CREATURE_ID:CASTE. |
| 53 |  SEEDS | NONE | Seeds from plants. |
| 54 |  PLANT | NONE | Plants. |
| 55 |  SKIN_TANNED | NONE | Leather. |
| 56 |  PLANT_GROWTH | growth ID | Plant growths. Subtype is the GROWTH's identifier within the plant raws (e.g. "LEAVES" or "FLOWERS" for most trees) |
| 57 |  THREAD | NONE | Thread (made at the farmer's workshop), webs (collected or undisturbed), and strands extracted from suitable stones. Standard dimension = 15000. |
| 58 |  CLOTH | NONE | Cloth made at the loom. Standard dimension = 10000. |
| 59 |  TOTEM | NONE | Skull totems. |
| 60 |  PANTS | item_pants.txt | Armor and clothing worn on the legs. |
| 61 |  BACKPACK | NONE | Backpacks. |
| 62 |  QUIVER | NONE | Quivers. |
| 63 |  CATAPULTPARTS | NONE | Catapult parts. |
| 64 |  BALLISTAPARTS | NONE | Ballista parts. |
| 65 |  SIEGEAMMO | item_siegeammo.txt | Siege engine ammunition. |
| 66 |  BALLISTAARROWHEAD | NONE | Ballista arrow heads. |
| 67 |  TRAPPARTS | NONE | Mechanisms. |
| 68 |  TRAPCOMP | item_trapcomp.txt | Trap components. |
| 69 |  DRINK | NONE | Alcoholic drinks. Standard dimension = 150. |
| 70 |  POWDER_MISC | NONE | Powders such as flour, dye, sand, or gypsum plaster. Standard dimension = 150. |
| 71 |  CHEESE | NONE | Pieces of cheese. |
| 72 |  FOOD | item_food.txt | Prepared meals. |
| 73 |  LIQUID_MISC | NONE | Liquids such as water, lye, and extracts. Standard dimension = 150. |
| 74 |  COIN | NONE | Coins. |
| 75 |  GLOB | NONE | Fat, tallow, pastes/pressed objects, and small bits of molten rock/metal. Standard dimension = 150. |
| 76 |  ROCK | NONE | Small rocks (usually sharpened and/or thrown in adventurer mode). |
| 77 |  PIPE_SECTION | NONE | Pipe sections and glass tubes. |
| 78 |  HATCH_COVER | NONE | Hatch covers. |
| 79 |  GRATE | NONE | Grates. |
| 80 |  QUERN | NONE | Querns. |
| 81 |  MILLSTONE | NONE | Millstones. |
| 82 |  SPLINT | NONE | Splints. |
| 83 |  CRUTCH | NONE | Crutches. |
| 84 |  TRACTION_BENCH | NONE | Traction benches. |
| 85 |  ORTHOPEDIC_CAST | NONE | Casts. |
| 86 |  TOOL | item_tool.txt | Tools. |
| 87 |  SLAB | NONE | Slabs, memorials, and shop signs. |
| 88 |  EGG | NONE | Eggs. Material is CREATURE_ID:CASTE; in reactions this currently works in PRODUCTs but not REAGENTs. |
| 89 |  BOOK | NONE | Books. |
| 90 |  SHEET | NONE | Sheets. Paper, papyrus, or parchment. Used for making quires and scrolls. |
| 91 |  BRANCH | NONE | Branches plucked from trees, used for making stone axes in adventurer mode. |
| 92 |  BOLT_THROWER_PARTS | NONE | Bolt thrower parts. |

## Special use item tokens

In several specific locations, the values below can be substituted for the item type and subtype (and be followed directly by the material token).

|  |  |  |  |
|----|----|----|----|
| Token | Subtype | Valid Uses | Description |
|  ANY_CRAFT | NONE | Reaction \[REAGENT\] | Matches FIGURINE, AMULET, SCEPTER, CROWN, RING, EARRING, or BRACELET. |
|  ANY_RAW_MATERIAL | NONE | Reaction \[REAGENT\] | Matches POWDER_MISC, BAR, BOULDER, or GLOB. |
|  CRAFTS | NONE | Reaction \[PRODUCT\] | Produces 1-3 items of any type possible to make with the specified material, normally the types FIGURINE, AMULET, SCEPTER, CROWN, RING, EARRING, or BRACELET, however GEM is also possible for some materials and there may be other possible results. The output depends entirely on the material used, and incredibly unusual materials may produce nothing at all, although most vanilla materials will produce GEMs at the very least. |

## Related tokens

These tokens are not Item Tokens at all, but can take the place of them in some circumstances.

|  |  |  |  |
|----|----|----|----|
| Token | Subtype | Valid Uses | Description |
|  METAL_ORE | Metal | Reaction \[REAGENT\] | Matches a BOULDER item made of a material having \[METAL_ORE::###\]. |

## See also

- Material token
- Reactions
