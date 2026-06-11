# Reaction (parte 2/2)

|  MAGMA_BUILD_SAFE |  | Reagent modifier | Currently broken - Reagent must be considered magma-safe (stable temperature below 12000 °U  ). |
|  MAX_MULTIPLIER | Integer |  | Sets the maximum number of times a reaction is allowed to run when using stacked reagents. This can be used to ensure that the reaction doesn't repeat until the entire stack is depleted. |
|  METAL_ORE | Inorganic material | Reagent modifier | Reagent material must be an ore of the specified metal. |
|  MIN_DIMENSION | Integer | Reagent modifier | Requires that the reagent have a size of at least *integer*. Only effective with BAR, POWDER_MISC, LIQUID_MISC, DRINK, THREAD, CLOTH, and GLOB items. |
|  NAME | Name |  | Defines the name used by the reaction in-game. |
|  NO_EDGE_ALLOWED |  | Reagent modifier | Reagent must not have an edge, so must be blunt. Sharp stones (produced using knapping) and most types of weapon/ammo can not be used with this token. |
|  NOT_ARTIFACT\[Verify\] |  | Reagent modifier | Reagent item must not be an artifact. |
|  NOT_CONTAIN_BARREL_ITEM |  | Reagent modifier | If the reagent is a Barrel, it must not contain an item that has to reside in a barrel. Barrel items appear to be lye and milk. Alcohol appears to be covered as part of \[EMPTY\]. A reaction which places an item in a barrel should probably have both tags. |
|  NOT_ENGRAVED |  | Reagent modifier | Reagent has not been engraved i.e. a blank memorial slab. |
|  NOT_IMPROVED |  | Reagent modifier | Reagent has not been decorated. |
|  NOT_PRESSED |  | Reagent modifier | Reagent must not be in the SOLID_PRESSED state. |
|  NOT_WEB |  | Reagent modifier | Reagent must be "collected" - used with THREAD:NONE to exclude webs. |
|  ON_GROUND |  | Reagent modifier | Reagent must be on the ground. Grabs from stockpiles. Does not grab from bins in stockpiles, nor inventories (workshops, wagon). Causes infinite collection of items if reaction is in workshop, as reagents are no longer on ground when brought to workshop. Untested in adventure mode; possibly more useful for adv. mode reactions. |
|  POTASHABLE (Deprecated) |  | Reagent modifier | Alias for \[CONTAINS_LYE\]. |
|  PRESERVE_REAGENT |  | Reagent modifier | Reagent is not destroyed, which is the normal effect, at the completion of the reaction. Typically used for containers. |
|  PRODUCT | Probability of success (%) / Quantity / Item token:subtype / Material token:subtype |  | Defines a thing that comes out of the reaction. GET_MATERIAL_FROM_REAGENT and GET_ITEM_DATA_FROM_REAGENT can be used to defer the choice of material and/or item to the appropriate tag in a given reagent's material - the former comes in place of the material token, the latter replaces both the item and material tokens. See above for detailed information on how the hooks work. |
|  PRODUCT_DIMENSION | Size | Product modifier | Specifies the amount of the product for those items that use dimension. For items of type BAR, DRINK, GLOB, LIQUID_MISC, and POWDER_MISC, one item is dimension 150; one item of CLOTH or SHEET is dimension 10000; and one item of THREAD is dimension 15000. Has no effect on any other item types. Note: this is not the actual storage volume of the product, which is hard-coded by the item token. |
|  PRODUCT_PASTE |  | Product modifier | Product is created in the SOLID_PASTE state. |
|  PRODUCT_PRESSED |  | Product modifier | Product is created in the SOLID_PRESSED state. |
|  PRODUCT_TO_CONTAINER | Reagent name | Product modifier | Places the product in a container; reagent name must be the name of a reagent with the \[PRESERVE_REAGENT\] token and a container item type. |
|  PRODUCT_TOKEN | Name | Product modifier | Allows the product to be referred to by the given name, for the purpose of being passed down as argument in other tokens in the same fashion as reagent names. |
|  REACTION | Identifier |  | Defines a new reaction. |
|  REACTION_CLASS | CLASS_ID (custom) | Reagent modifier | Requires the reagent's material to have a matching REACTION_CLASS entry. Intended for reactions which accept a variety of materials but where the input material does not determine the output material, such as FLUX (for making pig iron and steel) and GYPSUM (for producing plaster powder). |
|  REAGENT | Reagent name / Quantity / Item token / Material token |  | Specifies a given reagent as an input for a reaction. |
|  SKILL | Skill token |  | Skill used by the reaction. |
|  SKILL_IP | Integer | Skill modifier | Amount of skill given per product made. Default is 30. |
|  SKILL_ROLL_RANGE | Range / Multiplier | Skill modifier | Determines how skill level affects quality of the reaction product. The skill roll is random(range) + random((skill level \* multipler)/2 + 1) + random((skill level \* multipler)/2 + 1). random(x) returns a number between 0 and x-1, so range is always 1 or more. The default is 11. The default multiplier is 5. Higher skill rolls give better results. |
|  TRANSFER_ARTIFACT_STATUS |  | Product modifier | Transfers artifact status from the reagent to the product. |
|  UNROTTEN |  | Reagent modifier | Reagent must not be rotten, mainly for organic materials. |
|  USE_BODY_COMPONENT |  | Reagent modifier | Reagent material must come off a creature's body. |
|  WEB_ONLY |  | Reagent modifier | Reagent must be "undisturbed" - used with THREAD:NONE to gather webs. |
|  WORTHLESS_STONE_ONLY |  | Reagent modifier | Reagent is not made of an economic stone. |
|  WOVEN_ITEM |  | Reagent modifier | Reagent material must be a woven material, eg. plant cloth, silk, yarn. This *excludes* CLOTH or THREAD items. |

## Examples

*Main articles: Reaction examples*


---
*Parte 2 de 2 de «Reaction». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Reaction*
