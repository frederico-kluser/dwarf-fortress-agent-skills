# Material definition token

> Fonte: [Material definition token](https://dwarffortresswiki.org/index.php/Material_definition_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

The following tokens can be used in creating new material templates, as well as in material definitions (whether for inorganics or those within plants and creatures).

Material templates are used to define broad classes of materials (eg. "stone", or "milk"), the properties of which can be imported into other more specific material definitions (eg. "granite", or "llama milk") using the `[USE_MATERIAL_TEMPLATE:template_name]` token. When creating material templates, the `[OBJECT:MATERIAL_TEMPLATE]` token begins the definition of a material template raw file. Following this, each new material template definition begins with the `[MATERIAL_TEMPLATE:template_name]` token, where `template_name` is a unique identifier for the template, and that material's properties are then defined using the tokens listed below.

\

Urist asks...
Materials use specific, often bespoke, units. Are there any tools to help convert from real-world values?

Here are some web-based / utilities / designed for raw authoring. / For / yield / and / elasticity / : / https: / putnam3145.github.io / helper / For / temperature / : / https: / jose96xd.github.io / DF_Tools / Modules / TemperatureConverter.html

## Material properties

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Description |  |
|  USE_MATERIAL_TEMPLATE |  | Resets all material tokens back to their default values, then imports the tokens of the specified preexisting material template (overriding any tokens defined prior to itself in the material). This means USE_MATERIAL_TEMPLATE should be the first token present in any material using it. It cannot be used inside of a \[MATERIAL_TEMPLATE:X\] which prevents the creation of nested material template structures. |  |
|  PREFIX | or NONE | Applies a prefix to all items made from the material. For PLANT and CREATURE materials, this defaults to the plant/creature name. **Not permitted in material template definitions.** |  |
|  STONE_NAME |  | Overrides the name of BOULDER items (i.e. mined-out stones) made of the material (used for native copper/silver/gold/platinum to make them be called "nuggets" instead of "boulders"). |  |
|  IS_GEM | OVERWRITE_SOLID (optional) | Used to indicate that said material is a gemstone - when tiles are mined out, rough gems will be yielded instead of boulders. Plural can be "STP" to automatically append an "s" to the singular form, and OVERWRITE_SOLID will override the relevant STATE_NAME and STATE_ADJ values. |  |
|  TEMP_DIET_INFO |  | Specifies what the material should be treated as when drinking water contaminated by it, for generating unhappy thoughts. Valid values are BLOOD, SLIME, VOMIT, ICHOR, PUS, GOO, GRIME, and FILTH. |  |
|  POWDER_DYE | \ | Allows the material to be used as dye, and defines color of dyed items. |  |
|  TILE | \ | Specifies the tile that will be used to represent unmined tiles made of this material. Generally only used with stones. Defaults to 219 ('█'). |  |
|  ITEM_SYMBOL | \ | Specifies the tile that will be used to represent BOULDER items made of this material. Generally only used with stones. Defaults to 7 ('•'). |  |
|  DISPLAY_COLOR | \ / \ / \ | The on-screen color of the material. Uses a standard 3-digit color token. Equivalent to \[TILE_COLOR:a:b:c\], \[BUILD_COLOR:b:a:X\] (X = 1 if 'a' equals 'b', 0 otherwise), and \[BASIC_COLOR:a:c\] |  |
|  BUILD_COLOR | \ / \ / \ | The color of objects made of this material which use both the foreground and background color: doors, floodgates, hatch covers, bins, barrels, and cages. Defaults to 7:7:1 (white). |  |
|  TILE_COLOR | \ / \ / \ | The color of unmined tiles containing this material (for stone and soil), as well as engravings in this material. Defaults to 7:7:1 (white). |  |
|  BASIC_COLOR | \ / \ | The color of objects made of this material which use only the foreground color, including workshops, floors and boulders, and smoothed walls. Defaults to 7:1 (white). |  |
|  STATE_COLOR | \ / \ | Determines the color of the material at the specified state. Color comes from descriptor_color_standard.txt. The nearest color value is used to display contaminants and body parts made of this material in ASCII and to color items and constructions made from this material with graphics. Example: / \[STATE_COLOR:ALL_SOLID:GRAY\] |  |
|  STATE_NAME | \ | Determines the name of the material at the specified state, as displayed in-game. / \[STATE_NAME:ALL_SOLID:stone\] |  |
|  STATE_ADJ | \ | Like STATE_NAME, but used in different situations. Equipment made from the material uses the state adjective and not the state name. |  |
|  STATE_NAME_ADJ | \ | Sets both STATE_NAME and STATE_ADJ at the same time. |  |
|  ABSORPTION |  | The material's tendency to absorb liquids. Containers made of materials with nonzero absorption cannot hold liquids unless they have been glazed. Defaults to 0. |  |
|  IMPACT_YIELD |  | Specifies how hard of an impact (in kPa) the material can withstand before it will start deforming permanently. Used for blunt-force combat. Defaults to 10000. |  |
|  IMPACT_FRACTURE |  | Specifies how hard of an impact the material can withstand before it will fail entirely. Used for blunt-force combat. Defaults to 10000. |  |
|  IMPACT_STRAIN_AT_YIELD or  IMPACT_ELASTICITY | \ | Specifies how much the material will have given (in parts-per-100000) when the yield point is reached. Used for blunt-force combat. Defaults to 0. Apparently affects in combat whether the corresponding tissue is bruised (value \>= 50000), torn (value between 25000 and 49999), or fractured (value \<= 24999) |  |
|  COMPRESSIVE_YIELD |  | Specifies how hard the material can be compressed before it will start deforming permanently. Determines a tissue's resistance to pinching and response to strangulation. Defaults to 10000. |  |
|  COMPRESSIVE_FRACTURE |  | Specifies how hard the material can be compressed before it will fail entirely. Determines a tissue's resistance to pinching and response to strangulation. Defaults to 10000. |  |
|  COMPRESSIVE_STRAIN_AT_YIELD or  COMPRESSIVE_ELASTICITY | \ | Specifies how much the material will have given when it has been compressed to its yield point. Determines a tissue's resistance to pinching and response to strangulation. Defaults to 0. |  |
|  TENSILE_YIELD |  | Specifies how hard the material can be stretched before it will start deforming permanently. Determines a tissue's resistance to latching and shaking (50% chance, with torsion the other 50%). Defaults to 10000. |  |
|  TENSILE_FRACTURE |  | Specifies how hard the material can be stretched before it will fail entirely. Determines a tissue's resistance to latching and shaking (50% chance). Defaults to 10000. |  |
|  TENSILE_STRAIN_AT_YIELD or  TENSILE_ELASTICITY | \ | Specifies how much the material will have given when it is stretched to its yield point. Determines a tissue's resistance to to latching and shaking (50% chance). Defaults to 0. |  |
|  TORSION_YIELD |  | Specifies how hard the material can be twisted before it will start deforming permanently. Used for latching and shaking (50% chance). Defaults to 10000. |  |
|  TORSION_FRACTURE |  | Specifies how hard the material can be twisted before it will fail entirely. Used for latching and shaking (50% chance). Defaults to 10000. |  |
|  TORSION_STRAIN_AT_YIELD or  TORSION_ELASTICITY | \ | Specifies how much the material will have given when it is twisted to its yield point. Used for latching and shaking (50% chance). Defaults to 0. |  |
|  SHEAR_YIELD |  | Specifies how hard the material can be sheared before it will start deforming permanently. Used for cutting calculations. Defaults to 10000. |  |
|  SHEAR_FRACTURE |  | Specifies how hard the material can be sheared before it will fail entirely. Used for cutting calculations. Defaults to 10000. |  |
|  SHEAR_STRAIN_AT_YIELD or  SHEAR_ELASTICITY | \ | Specifies how much the material will have given when sheared to its yield point. Used for cutting calculations. Defaults to 0. |  |
|  BENDING_YIELD |  | Specifies how hard the material can be bent before it will start deforming permanently. Determines a tissue's resistance to being mangled with a joint lock. Defaults to 10000. |  |
|  BENDING_FRACTURE |  | Specifies how hard the material can be bent before it will fail entirely. Determines a tissue's resistance to being mangled with a joint lock. Defaults to 10000. |  |
|  BENDING_STRAIN_AT_YIELD or  BENDING_ELASTICITY | \ | Specifies how much the material will have given when bent to its yield point. Determines a tissue's resistance to being mangled with a joint lock. Defaults to 0. |  |
|  MAX_EDGE |  | How sharp the material is. Used in cutting calculations. Applying a value of at least 10000 to a stone will allow weapons to be made from that stone. Defaults to 10000. |  |
|  MATERIAL_VALUE | \ | Value modifier for the material. Defaults to 1. This number can be made negative by placing a "-" in front, resulting in things that you are paid to buy and must pay to sell. |  |
|  MULTIPLY_VALUE | \ | Multiplies the value of the material. **Not permitted in material template definitions.** |  |
|  SPEC_HEAT |  | Rate at which the material heats up or cools down (in J⋅kg−1⋅K−1.). If set to NONE, the temperature will be fixed at its initial value. See Temperature for more information. Defaults to NONE. |  |
|  HEATDAM_POINT | \ | Temperature above which the material takes damage from heat. May be set to NONE. If the material has an ignite point but no heatdam point, it will burn for a very long time (9 months and 16.8 days). Defaults to NONE. |  |
|  COLDDAM_POINT | \ | Temperature below which the material takes damage from cold. Defaults to NONE. |  |
|  IGNITE_POINT | \ | Temperature at which the material will catch fire. Defaults to NONE. |  |
|  MELTING_POINT | \ | Temperature at which the material melts. Defaults to NONE. |  |
|  BOILING_POINT | \ | Temperature at which the material boils. Defaults to NONE. |  |
|  MAT_FIXED_TEMP | \ | Items composed of this material will initially have this temperature. Used in conjunction with `[SPEC_HEAT:NONE]` to make material's temperature fixed at the specified value. Defaults to NONE. |  |
|  IF_EXISTS_SET_HEATDAM_POINT | \ | Changes a material's HEATDAM_POINT, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  IF_EXISTS_SET_COLDDAM_POINT | \ | Changes a material's COLDDAM_POINT, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  IF_EXISTS_SET_IGNITE_POINT | \ | Changes a material's IGNITE_POINT, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  IF_EXISTS_SET_MELTING_POINT | \ | Changes a material's MELTING_POINT, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  IF_EXISTS_SET_BOILING_POINT | \ | Changes a material's BOILING_POINT, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  IF_EXISTS_SET_MAT_FIXED_TEMP | \ | Changes a material's MAT_FIXED_TEMP, but only if it was not set to NONE. **Not permitted in material template definitions.** |  |
|  SOLID_DENSITY | \ | Specifies the density (in kg/m³) of the material when in solid form. Also affects combat calculations; affects blunt-force damage and ability of weak-in-impact-yield blunt attacks to pierce armor. Defaults to NONE. |  |
|  LIQUID_DENSITY | \ | Specifies the density of the material when in liquid form. Defaults to NONE. Also affects combat calculations; affects blunt force damage like SOLID_DENSITY, but only for attacks made by liquids (e.g. forgotten beasts made of water). |  |
|  MOLAR_MASS |  | Specifies (in kg/mol) the molar mass of the material in gaseous form. Only affects combat calculations like the densities, and only for attacks made by gases (e.g. forgotten beasts made of steam). |  |
|  EXTRACT_STORAGE | \* BARREL or FLASK | Specifies the type of container used to store the material. Used in conjunction with the \[EXTRACT_BARREL\], \[EXTRACT_VIAL\], or \[EXTRACT_STILL_VIAL\] plant tokens. Defaults to BARREL. |  |
|  BUTCHER_SPECIAL | \ | Specifies the item type used for butchering results made of this material. Stock raws use GLOB:NONE for fat and MEAT:NONE for other meat materials. |  |
|  MEAT_NAME |  | When a creature is butchered, meat yielded from organs made from this material will be named via this token. If this token is not specified, meat objects will be called "chops" instead. |  |
|  BLOCK_NAME |  | Specifies the name of blocks made from this material. |  |
|  MATERIAL_REACTION_PRODUCT | \ | Used with reaction raws to associate a reagent material with a product material. The first argument is used by HAS_MATERIAL_REACTION_PRODUCT and GET_MATERIAL_FROM_REAGENT in reaction raws. The remainder is a material reference, generally LOCAL_CREATURE_MAT:SUBTYPE or LOCAL_PLANT_MAT:SUBTYPE or INORGANIC:STONETYPE. / \[MATERIAL_REACTION_PRODUCT:TAN_MAT:LOCAL_CREATURE_MAT:LEATHER\] |  |
|  ITEM_REACTION_PRODUCT | \ / \ | Used with reaction raws to associate a reagent material with a complete item. The first argument is used by HAS_ITEM_REACTION_PRODUCT and GET_ITEM_DATA_FROM_REAGENT in reaction raws. The rest refers to the type of item, then its material. / \[ITEM_REACTION_PRODUCT:BAG_ITEM:PLANT_GROWTH:LEAVES:LOCAL_PLANT_MAT:LEAF\] |  |
|  REACTION_CLASS |  | Used to classify all items made of the material, so that reactions can use them as generic reagents. / In default raws, the following are used: / FAT, TALLOW, SOAP, PARCHMENT, PAPER_PLANT, PAPER_SLURRY, MILK, CHEESE, WAX / CAN_GLAZE - items made from this material can be glazed. / FLUX - can be used as / flux / in pig iron and steel making. / GYPSUM - can be processed into / gypsum plaster / . / CALCIUM_CARBONATE - can be used in production of / quicklime / . / The TALLOW reaction class also flags the material to be stored in "rendered fat" containers. Other default reaction classes might affect storage, too, but testing is needed. |  |
|  HARDENS_WITH_WATER | \ | Allows the material to be used to make casts. |  |
|  SOAP_LEVEL |  | Determines effectiveness of soap - if the amount of grime on a body part is more than 3-SOAP_LEVEL, it sets it to 3-SOAP_LEVEL; as such setting it above 3 is bad. Soap has \[SOAP_LEVEL:2\]. Defaults to 0. |  |
|  SYNDROME |  | Begins defining a syndrome applied by the material. Multiple syndromes can be specified. See Syndrome token. |  |
|  ANTLER |  | Found in the raws of several antler-wielding animals. It is used to show an antler as bodypart. |  |
|  HAIR |  | Probably used in graphics. |  |
|  FEATHER |  | Probably used in graphics. |  |
|  SCALE |  | Probably used in graphics. |  |
|  HOOF |  | Probably used in graphics. |  |
|  CHITIN |  | Probably used in graphics. |  |
|  CARTILAGE |  | Probably used in graphics. |  |
|  NERVOUS_TISSUE |  | Probably used in graphics. |  |
|  MEAT_CATEGORY | category | Probably used in graphics. The following values for "category" are used in the vanilla raws: STANDARD, EYE, LUNG, HEART, INTESTINES, LIVER, STOMACH, PANCREAS, SPLEEN, KIDNEY, BRAIN, GIZZARD. |  |

\

\

### Material states

The following is a list of valid material states:

|                                    |
|------------------------------------|
| **SOLID**                          |
| **LIQUID**                         |
| **GAS**                            |
| **POWDER** (or **SOLID_POWDER**)   |
| **PASTE** (or **SOLID_PASTE**)     |
| **PRESSED** (or **SOLID_PRESSED**) |

The following can be specified within tokens such as STATE_NAME, STATE_NAME_ADJ and STATE_ADJ to make them apply to several of the above material states simultaneously:

|               |                                                   |
|---------------|---------------------------------------------------|
| Value         | Description                                       |
| **ALL**       | Denotes all possible material states.             |
| **ALL_SOLID** | Denotes 'SOLID', 'POWDER', 'PASTE' and 'PRESSED'. |

## Material usage tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  IMPLIES_ANIMAL_KILL |  | Lets the game know that an animal was likely killed in the production of this item. Entities opposed to killing animals (Elves in vanilla) will refuse to accept these items in trade. |
|  ALCOHOL_PLANT |  | Classifies the material as plant-based alcohol, allowing its storage in food stockpiles under "Drink (Plant)". |
|  ALCOHOL_CREATURE |  | Classifies the material as animal-based alcohol, allowing its storage in food stockpiles under "Drink (Animal)". |
|  ALCOHOL |  | Classifies the material as generic alcohol. Implied by both ALCOHOL_PLANT and ALCOHOL_CREATURE. Exact behavior unknown, possibly vestigial. |
|  CHEESE_PLANT |  | Classifies the material as plant-based cheese, allowing its storage in food stockpiles under "Cheese (Plant)". |
|  CHEESE_CREATURE |  | Classifies the material as animal-based cheese, allowing its storage in food stockpiles under "Cheese (Animal)". |
|  CHEESE |  | Classifies the material as generic cheese. Implied by both CHEESE_PLANT and CHEESE_CREATURE. Exact behavior unknown, possibly vestigial. |
|  POWDER_MISC_PLANT |  | Classifies the material as plant powder, allowing its storage in food stockpiles under "Milled Plant". |
|  POWDER_MISC_CREATURE |  | Classifies the material as creature powder, allowing its storage in food stockpiles under "Bone Meal". Unlike milled plants, such as sugar and flour, "Bone Meal" barrels or pots may not contain bags. Custom reactions using this product better use buckets or jugs instead. |
|  POWDER_MISC |  | Classifies the material as generic powder. Implied by both POWDER_MISC_PLANT and POWDER_MISC_CREATURE. Exact behavior unknown, possibly vestigial. |
|  STOCKPILE_GLOB or  STOCKPILE_GLOB_SOLID |  | Permits globs of the material in solid form to be stored in food stockpiles under "Fat" - without it, dwarves will come by and "clean" the items, destroying them (unless \[DO_NOT_CLEAN_GLOB\] is also included). |
|  STOCKPILE_GLOB_PASTE |  | Classifies the material as milled paste, allowing its storage in food stockpiles under "Paste". |
|  STOCKPILE_GLOB_PRESSED |  | Classifies the material as pressed goods, allowing its storage in food stockpiles under "Pressed Material". |
|  STOCKPILE_PLANT_GROWTH |  | Classifies the material as a plant growth (e.g. fruits, leaves), allowing its storage in food stockpiles under Plant Growth/Fruit. |
|  LIQUID_MISC_PLANT |  | Classifies the material as a plant extract, allowing its storage in food stockpiles under "Extract (Plant)". |
|  LIQUID_MISC_CREATURE |  | Classifies the material as a creature extract, allowing its storage in food stockpiles under "Extract (Animal)". |
|  LIQUID_MISC_OTHER |  | Classifies the material as a miscellaneous liquid, allowing its storage in food stockpiles under "Misc. Liquid" along with lye. |
|  LIQUID_MISC |  | Classifies the material as a generic liquid. Implied by LIQUID_MISC_PLANT, LIQUID_MISC_CREATURE, and LIQUID_MISC_OTHER. Exact behavior unknown, possibly vestigial. |
|  STRUCTURAL_PLANT_MAT |  | Classifies the material as a plant, allowing its storage in food stockpiles under "Plants". |
|  SEED_MAT |  | Classifies the material as a plant seed, allowing its storage in food stockpiles under "Seeds". |
|  BONE |  | Classifies the material as bone, allowing its use for bone carvers and restriction from stockpiles by material. |
|  WOOD |  | Classifies the material as wood, allowing its use for carpenters and storage in wood stockpiles. Entities opposed to killing plants (i.e. Elves) will refuse to accept these items in trade. |
|  THREAD_PLANT |  | Classifies the material as plant fiber, allowing its use for clothiers and storage in cloth stockpiles under "Thread (Plant)" and "Cloth (Plant)". |
|  TOOTH |  | Classifies the material as tooth, allowing its use for bone carvers and restriction from stockpiles by material. |
|  HORN |  | Classifies the material as horn, allowing its use for bone carvers and restriction from stockpiles by material. |
|  HAIR |  | Classifies the material as hair, allowing for its use for spinners and restriction from refuse stockpiles by material. |
|  PEARL |  | Classifies the material as pearl, allowing its use for bone carvers and restriction from stockpiles by material. |
|  SHELL |  | Classifies the material as shell, allowing its use for bone carvers and restriction from stockpiles by material. |
|  LEATHER |  | Classifies the material as leather, allowing its use for leatherworkers and storage in leather stockpiles. |
|  SILK |  | Classifies the material as silk, allowing its use for clothiers and storage in cloth stockpiles under "Thread (Silk)" and "Cloth (Silk)". |
|  SOAP |  | Classifies the material as soap, allowing it to be used as a bath detergent and stored in bar/block stockpiles under "Bars: Other Materials".\[Verify\] |
|  GENERATES_MIASMA |  | Material generates miasma when it rots. |
|  MEAT |  | Classifies the material as edible meat.\[Verify\] |
|  ROTS |  | Material will rot if not stockpiled appropriately. Currently only affects food and refuse, other items made of this material will not rot. |
|  NERVOUS_TISSUE |  | In most living creatures, it controls many bodily functions and movements by sending signals around the body. See: Nervous tissue |
|  BLOOD_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "blood" in Adventurer mode tile descriptions ("Here we have a Dwarf in a slurry of blood."). |
|  ICHOR_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "ichor". |
|  GOO_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "goo". |
|  SLIME_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "slime". |
|  PUS_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "pus". |
|  SWEAT_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "sweat". |
|  TEARS_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "tears". |
|  SPIT_MAP_DESCRIPTOR |  | Tells the game to classify contaminants of this material as being "spit". |
|  EVAPORATES |  | Contaminants composed of this material evaporate over time, slowly disappearing from the map. Used internally by water. |
|  ENTERS_BLOOD |  | Used for materials which cause syndromes, causes it to enter the creature's blood instead of simply spattering on the surface. |
|  EDIBLE_VERMIN |  | Can be eaten by vermin. |
|  EDIBLE_RAW |  | Can be eaten raw. |
|  EDIBLE_COOKED |  | Can be cooked and then eaten. |
|  DO_NOT_CLEAN_GLOB |  | Prevents globs made of this material from being cleaned up and destroyed. |
|  NO_STONE_STOCKPILE |  | Prevents the material from showing up in Stone stockpile settings. |
|  ITEMS_METAL |  | The material can be made into minecarts, wheelbarrows, and stepladders at the metalsmith's forge. |
|  ITEMS_BARRED |  | Theoretically allows the item to be made into [`[BARRED]`](/index.php/Armor_token#BARRED "Armor token") armor, but doesn't actually work (game checks for [`[BONE]`](/index.php/Material_definition_token#BONE "Material definition token") instead). Given to bone. |
|  ITEMS_SCALED |  | Theoretically allows the item to be made into [`[SCALED]`](/index.php/Armor_token#SCALED "Armor token") armor, but doesn't actually work (game checks for [`[SHELL]`](/index.php/Material_definition_token#SHELL "Material definition token") instead). Given to shell. |
|  ITEMS_LEATHER |  | Theoretically allows the item to be made into [`[LEATHER]`](/index.php/Armor_token#LEATHER "Armor token") armor, but doesn't actually work (game checks for [`[LEATHER]`](/index.php/Material_definition_token#LEATHER "Material definition token") instead). Given to leather. |
|  ITEMS_SOFT |  | The material can be made into clothing, amulets, bracelets, earrings, backpacks, and quivers, contingent on which workshops accept the material. Given to plant fiber, silk and wool. |
|  ITEMS_HARD |  | The material can be made into furniture, crafts, mechanisms, and blocks, contingent on which workshops accept the material. Random crafts made from this material include all seven items. Given to stone, wood, bone, shell, chitin, claws, teeth, horns, hooves and beeswax. Hair, pearls and eggshells also have the tag. |
|  IS_STONE |  | Used to define that the material is a stone. Allows its usage in masonry and stonecrafting and storage in stone stockpiles, among other effects. |
|  UNDIGGABLE |  | Used for a stone that cannot be dug into. |
|  DISPLAY_UNGLAZED |  | Causes containers made of this material to be prefixed with "unglazed" if they have not yet been glazed. |
|  YARN |  | Classifies the material as yarn, allowing its use for clothiers and its storage in cloth stockpiles under "Thread (Yarn)" and "Cloth (Yarn)". |
|  STOCKPILE_THREAD_METAL |  | Classifies the material as metal thread, permitting thread and cloth to be stored in cloth stockpiles under "Thread (Metal)" and "Cloth (Metal)". |
|  IS_METAL |  | Defines the material as being metal, allowing it to be used at forges. |
|  IS_GLASS |  | Used internally by green glass, clear glass, and crystal glass. Appears to only affect the [\[GLASS_MATERIAL\]](/index.php/Reaction#GLASS_MATERIAL "Reaction") reaction token. Does not cause the game to treat the material like glass, i.e being referred to as "raw" instead of "rough" in its raw form or being displayed in the "glass" trade/embark category. |
|  IS_CERAMIC |  | Defines the material as a ceramic. Examples include CERAMIC_EARTHENWARE, CERAMIC_STONEWARE and CERAMIC_PORCELAIN. |
|  CRYSTAL_GLASSABLE |  | Can be used in the production of crystal glass. |
|  ITEMS_WEAPON |  | Melee weapons can be made out of this material. |
|  ITEMS_WEAPON_RANGED |  | Ranged weapons can be made out of this material. |
|  ITEMS_ANVIL |  | Anvils can be made out of this material. |
|  ITEMS_AMMO |  | Ammunition can be made out of this material. |
|  ITEMS_DIGGER |  | Picks can be made out of this material. |
|  ITEMS_ARMOR |  | Armor can be made out of this material. |
|  ITEMS_DELICATE |  | Used internally by amber and coral. Functionally equivalent to ITEMS_HARD. |
|  ITEMS_SIEGE_ENGINE |  | Theoretically, siege engine parts can be made out of this material. Does not appear to work (game checks for [`[WOOD]`](/index.php/Material_definition_token#WOOD "Material definition token") or [`[IS_METAL]`](/index.php/Material_definition_token#IS_METAL "Material definition token")+[`[ITEMS_SOFT]`](/index.php/Material_definition_token#ITEMS_SOFT "Material definition token") instead). |
|  ITEMS_QUERN |  | Theoretically, querns and millstones can be made out of this material. Does not appear to work (game checks for [`[ITEMS_HARD]`](/index.php/Material_definition_token#ITEMS_HARD "Material definition token") instead). |

## Syndrome tokens

Below is a table with some of the tokens you can use when declaring a \[SYNDROME\] token. For all the tokens you can use, see the Syndrome token page.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| SYN_NAME | text | Defines the name of the syndrome |
|  SYN_INJECTED |  | Syndrome can be contracted by injection (by a creature) |
|  SYN_CONTACT |  | Syndrome can be contracted on contact (e.g. poison dust or liquid) |
|  SYN_INHALED |  | Syndrome can be contracted by inhalation (e.g. poison vapor or gas) |
|  SYN_INGESTED |  | Syndrome can be contracted by ingestion (when the material is eaten in solid or liquid form) |
|  SYN_AFFECTED_CLASS | creature class name | Adds a class of creatures to those affected, such as CREATURE_CLASS:GENERAL_POISON |
|  SYN_IMMUNE_CLASS | creature class name | Makes the class of creatures immune to the syndrome |
|  SYN_AFFECTED_CREATURE | creature name / caste name or ALL | Adds a specific creature to those affected. |
|  SYN_IMMUNE_CREATURE | creature name / caste name or ALL | Makes the creature immune to the syndrome |
| CE_PAIN / CE_SWELLING / CE_OOZING / CE_BRUISING / CE_BLISTERS / CE_NUMBNESS / CE_PARALYSIS / CE_FEVER / CE_BLEEDING / CE_COUGH_BLOOD / CE_VOMIT_BLOOD / CE_NAUSEA / CE_UNCONSCIOUSNESS / CE_NECROSIS / CE_IMPAIR_FUNCTION / CE_DROWSINESS / CE_DIZZINESS | SEV: / (severity, higher is worse) / PROB: / (probability) / RESISTABLE (optional) allows resistance / SIZE_DILUTES (optional) lessens effect based on size / Place affected: / LOCALIZED (optional) / VASCULAR_ONLY (optional) / MUSCULAR_ONLY (optional) / BP:BY_CATEGORY:category:tissue (optional) / BP:BY_TYPE:type:tissue (optional) / BP:BY_TOKEN:token:tissue (optional) / Timeline: / Start:effect start time / Peak:effect peak time / End:effect end time | Specifies the way that a syndrome affects a creature -- more detail can be found on the Syndromes page |

## See also

- Inorganic material definition token
- Syndrome
- Hardcoded material
