# Spit

> Fonte: [Spit](https://dwarffortresswiki.org/index.php/Spit) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

**Spit** is a kind of contaminant, like blood or vomit, that results from the action of spitting, treated as a "natural ability" by most creatures. Spitting mostly occurs in Adventure mode, when NPCs encounter people that they hate, typically due to a bad reputation (as e.g. a murderer) or belonging to different factions without being outright hostile (e.g. criminal organizations in towns).

As an adventurer you can spit on anyone or anything you want, aiming it just like you would with a projectile. This is done in the abilities menu (X). If you get spit on, you can also drink it in an attempt to slake your thirst, but it will have little (if any) effect, and won't add to fullness.

Note that some creatures like magma crabs have very dangerous spit indeed; appropriate modding can turn this mostly harmless expression of spite into a deadly weapon.

\

    [MATERIAL_TEMPLATE:SPIT_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:CLEAR]
        [STATE_NAME:ALL_SOLID:frozen spit]
        [STATE_ADJ:ALL_SOLID:frozen spit]
        [STATE_COLOR:LIQUID:CLEAR]
        [STATE_NAME:LIQUID:spit]
        [STATE_ADJ:LIQUID:spit]
        [STATE_COLOR:GAS:CLEAR]
        [STATE_NAME:GAS:boiling spit]
        [STATE_ADJ:GAS:boiling spit]
        [DISPLAY_COLOR:7:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10508]
        [MELTING_POINT:10000]
        [BOILING_POINT:10180]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:6600] used high salinity ice
        [SHEAR_FRACTURE:6600]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:500]
        [ABSORPTION:100]
        [SPIT_MAP_DESCRIPTOR]
        [EVAPORATES]
