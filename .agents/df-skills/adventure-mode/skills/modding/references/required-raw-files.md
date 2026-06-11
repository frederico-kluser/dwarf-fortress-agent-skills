# Required Raw Files

> Fonte: [Required Raw Files](https://dwarffortresswiki.org/index.php/Required_Raw_Files) — Dwarf Fortress Wiki (GFDL/MIT)

*This article is based on version 0.43.05. It may not be accurate to the latest release.*

The following is a list of files in the raw/objects/ folder necessary for *Dwarf Fortress* version 43.05; removing them causes unpredictable behavior, mostly crashing, in different parts of the game because they provide definitions for tokens hard-coded into the executable:

- b_detail_plan.txt - provides required body detail plan tokens for the object testing arena and world generation
- body_default.txt - provides the body part tokens used to define creatures
- body_rcp.txt - provides the body part tokens used to randomly generate creatures
- c_variation_default.txt - provides creature variation tokens required by the object testing arena and world generation
- creature_standard.txt - defines dwarves and standard creatures.
- descriptor_color_standard.txt - provides color definitions required by the object testing arena and world generation
- descriptor_pattern_iris_eye.txt - provides descriptions for creature irises
- descriptor_pattern_pupil_eye.txt - provides descriptions for creature pupils.
- descriptor_shape_standard.txt - provides descriptions for shapes required by the testing arena and world generation.
- entity_default.txt - defines various civilizations
- inorganic_metal.txt - allows dwarves to dig and defines various metals for the dwarves to dig.
- inorganic_stone_layer.txt - required for world generation
- interaction_standard.txt - defines interactions required for world generation.
- item_ammo.txt - defines ammo used by dwarves
- item_armor.txt - defines armor used by dwarves
- item_gloves.txt - defines gloves used by dwarves
- item_helm.txt - defines helmets used by dwarves
- item_pants.txt - defines pants used by dwarves
- item_shield.txt - defines shield items used by dwarves
- item_shoes.txt - defines shoes used by dwarves
- item_seigeammo.txt - defines siege ammo used by dwarves
- item_tool.txt - defines tools used by dwarves
- item_toy.txt - defines toys used by dwarves
- item_trapcomp.txt - defines trap components used by dwarves.
- item_weapon.txt - defines weapons used by dwarves
- language_DWARF.txt - defines the dwarf language
- language_SYM.txt - defines the grammar of different words
- language_words.txt - defnes words used by the system
- material_template_default.txt - defines materials required by object testing and dwarves
- plant_standard.txt - defines standard plants required for dwarves
- tissue_template_default.txt - defines tissue tokens used to define body parts.

Additionally, the following files in the raw/objects/text/ folder are required to play *Dwarf Fortress* because the relative file paths are hard-coded into the executable.

- secret_death.txt
- book_instruction.txt
- book_art.txt

Note that these files are required, but their contents seem meaningless; the game will crash if they are not found or if they are empty.

inorganic_stone_layer.txt is required for fortress mode. The ability to dig is provided by inorganic_metal, probably because inorganic_metal defines metals that can be used to create picks.

A github repository exists that contains these files and incomplete documentation on what they do.
