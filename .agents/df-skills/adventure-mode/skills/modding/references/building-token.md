# Building token

> Fonte: [Building token](https://dwarffortresswiki.org/index.php/Building_token) — Dwarf Fortress Wiki (GFDL/MIT)

**Building tokens** control the functionality of custom buildings.

All custom buildings are defined as objects of type BUILDING_WORKSHOP or BUILDING_FURNACE; workshops show up in the Build \> Workshops (-) menu, while furnaces show up in the Build \> Workshops \> Furnaces (--) menu.

You also must add any new custom buildings to the civilization that you want to use it.

Additionally, furnaces must be designed by an mason before being constructed (and will gain quality accordingly), though they will always use the labor(s) specified in the building definition, rather than ones based on the materials being used.

[TABLE]

## Item Modifiers

Building items have many of the same modifiers as reagents in custom reactions.

| Token | Meaning |
|----|----|
| \[\] | Item material must have the \[BONE\] token. |
| \[\] | Item material must have the \[HORN\] token. |
| \[\] | Item material must have the \[LEATHER\] token. |
| \[\] | Item material must have the \[PEARL\] token. |
| \[\] | Item material must be subordinate to a PLANT object. |
| \[\] | Item material must have the \[SHELL\] token. |
| \[\] | Item material must have the \[SILK\] token. |
| \[\] | Item material must have the \[SOAP\] token. |
| \[\] | Item is made of a tissue having \[TISSUE_SHAPE:STRANDS\], intended for matching hair and wool. Must be used with \[USE_BODY_COMPONENT\]. |
| \[\] | Item material must have the \[TOOTH\] token. |
| \[\] | Item material must have the \[YARN\] token. |
| \[\] | Item must be a bag - that is, a BOX made of plant fiber, silk, yarn, or leather. |
| \[\] | Item must be a general building material - BAR, BLOCKS, BOULDER, or WOOD. |
| \[\] | Item can be an Artifact. |
| \[\] | Item must be a BARREL or TOOL which contains at least one item of type LIQUID_MISC made of LYE. |
| \[\] | If the item is a container, it must be empty. |
| \[\] | Item material must be stable at temperatures below 11000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| \[\] | Item material must have the \[IS_GLASS\] token. All 3 types of glass have this token hardcoded. |
| \[:X\] | Item's material has a \[MATERIAL_REACTION_PRODUCT\] token with the appropriate ID. |
| \[:X\] | Item must be a tool with the specific TOOL_USE value. The item type must be  for this to make any sense. |
| \[\] | Item material must be stable at temperatures below 12000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| \[:X\] | Item material must be an ore of the specified metal. |
| \[:X\] | Item's dimension must be at least this large. The item type must be BAR, POWDER_MISC, LIQUID_MISC, DRINK, THREAD, or CLOTH for this to work. |
| \[\] | Item must not have an edge, so must be blunt. Sharp stones (produced using knapping) and most types of weapon/ammo can not be used with this token. |
| \[\] | If the item is a container, it must not contain lye or milk. Not necessary if specifying \[EMPTY\]. |
| \[\] | Item can not be engraved. For example, a memorial slab can not be engraved. |
| \[\] | Item must be collected (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| \[\] (Deprecated) | Alias for \[CONTAINS_LYE\]. |
| \[:X\] | Item's material has a \[REACTION_CLASS\] token with the appropriate ID. |
| \[\] | Item must not be rotten, mainly for organic materials. |
| \[\] | Item must be a body part (CORPSE or CORPSEPIECE). |
| \[\] | Item must be undisturbed (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| \[\] | Item material must be non-economic. |
