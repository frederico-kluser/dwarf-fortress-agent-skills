# Inorganic material definition token

> Fonte: [Inorganic material definition token](https://dwarffortresswiki.org/index.php/Inorganic_material_definition_token) — Dwarf Fortress Wiki (GFDL/MIT)

The following tokens can be used in inorganic material definitions, generally for stones, gems, and metals, but not with materials attached to plants or creatures.

[TABLE]

## ENVIRONMENT and ENVIRONMENT_SPEC

Format:

- \[ENVIRONMENT:\:\:\\]

Possible values for class:

[TABLE]

Possible values for inclusion type:

[TABLE]

An inclusion may be contained within a larger inclusion. For example, diamond small clusters are found within kimberlite veins.

The frequency number varies from 1 to 100 and determines the relative frequency at which the stone will be chosen to appear - if all frequency values are the same, then all stones will be equally likely to appear.

ENVIRONMENT_SPEC follows much the same format, but takes a specific stone material ID where ENVIRONMENT would take a class token. What you can use will depend on what inorganic raws are around.

## See also

- Material definition token
