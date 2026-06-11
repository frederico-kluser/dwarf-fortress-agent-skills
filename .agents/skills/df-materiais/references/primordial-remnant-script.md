# Primordial remnant/script

> Fonte: [Primordial remnant/script](https://dwarffortresswiki.org/index.php/Primordial_remnant/script) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

mythical_remnant_adjectives={
        "primordial",
        "elder",
        "cosmic",
        "primal",
        "elemental",
        "primeval"
    }

    mythical_remnant_spheres={}

    mythical_remnant_spheres.MOUNTAINS={
        name="stone",
        color="4:0:1",
        state_color="GRAY"
    }

    mythical_remnant_spheres.MINERALS=mythical_remnant_spheres.MOUNTAINS
    mythical_remnant_spheres.CAVERNS=mythical_remnant_spheres.MOUNTAINS
    mythical_remnant_spheres.EARTH=mythical_remnant_spheres.MOUNTAINS

    mythical_remnant_spheres.JEWELS={
        name="crystal",
        color="7:0:1",
        state_color="WHITE"
    }

    mythical_remnant_spheres.CHAOS={
        name="chaos",
        color="4:0:1",
        state_color="RED"
    }

    mythical_remnant_spheres.DARKNESS={
        name="darkness",
        color="0:0:1",
        state_color="BLACK"
    }

    mythical_remnant_spheres.DEATH=mythical_remnant_spheres.DARKNESS
    mythical_remnant_spheres.NIGHTMARES=mythical_remnant_spheres.DARKNESS

    mythical_remnant_spheres.DREAMS={
        name="dreamstuff",
        color="2:0:1",
        state_color="GREEN"
    }

    mythical_remnant_spheres.FIRE={
        name="fire",
        color="4:0:1",
        state_color="RED"
    }

    mythical_remnant_spheres.LIGHT={
        name="light",
        color="6:0:1",
        state_color="YELLOW"
    }

    mythical_remnant_spheres.LIGHTNING={
        name="lightning",
        color="6:0:1",
        state_color="YELLOW"
    }

    mythical_remnant_spheres.METALS={
        name="metal",
        color="7:0:1",
        state_color="SILVER"
    }

    mythical_remnant_spheres.MOON={
        name="moonstone",
        color="7:0:1",
        state_color="WHITE"
    }

    mythical_remnant_spheres.DARKNESS={
        name="mudstone",
        color="6:0:0",
        state_color="BROWN"
    }

    mythical_remnant_spheres.OCEANS={
        name="ice",
        color="1:0:1",
        state_color="BLUE"
    }

    mythical_remnant_spheres.WATER=mythical_remnant_spheres.OCEANS

    mythical_remnant_spheres.PLANTS={
        name="leaf",
        color="2:0:1",
        state_color="GREEN"
    }

    mythical_remnant_spheres.SALT={
        name="salt",
        color="7:0:1",
        state_color="WHITE"
    }

    mythical_remnant_spheres.MIST={
        name="cloudstuff",
        color="7:0:1",
        state_color="WHITE"
    }

    mythical_remnant_spheres.SKY=mythical_remnant_spheres.MIST
    mythical_remnant_spheres.STORMS=mythical_remnant_spheres.MIST
    mythical_remnant_spheres.WIND=mythical_remnant_spheres.MIST

    mythical_remnant_spheres.STARS={
        name="stardust",
        color="6:0:1",
        state_color="YELLOW"
    }

    mythical_remnant_spheres.SUN={
        name="sunstone",
        color="6:0:1",
        state_color="YELLOW"
    }

    mythical_remnant_spheres.TREES={
        name="wood",
        color="6:0:0",
        state_color="BROWN"
    }

    mythical_remnant_spheres.VOLCANOS={
        name="obsidian",
        color="4:0:1",
        state_color="RED"
    }

    materials.mythical_remnant.default=function(sph)
        local lines={}
        lines[#lines+1]="[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"
        local sph_info = mythical_remnant_spheres[sph] or {name="glitchstuff", color="0:0:1", state_color="BLACK"}
        lines[#lines+1]="[DISPLAY_COLOR:"..sph_info.color.."]"
        lines[#lines+1]="[BUILD_COLOR:"..sph_info.color.."]"
        lines[#lines+1]="[STATE_COLOR:ALL:"..sph_info.state_color.."]"
        lines[#lines+1]="[STATE_NAME_ADJ:ALL_SOLID:"..pick_random(mythical_remnant_adjectives).." "..sph_info.name.."]"
        lines[#lines+1]="[MATERIAL_VALUE:200]"
        lines[#lines+1]="[SPEC_HEAT:7500]"
        lines[#lines+1]="[MELTING_POINT:NONE]"
        lines[#lines+1]="[BOILING_POINT:NONE]"
        lines[#lines+1]="[ITEMS_HARD]"
        if(sph=="METALS") then lines[#lines+1]="[ITEMS_METAL]" end
        lines[#lines+1]="[SOLID_DENSITY:1000]"
        lines[#lines+1]="[LIQUID_DENSITY:1000]"
        lines[#lines+1]="[MOLAR_MASS:20000]"
        lines[#lines+1]="[IMPACT_YIELD:1000000]"
        lines[#lines+1]="[IMPACT_FRACTURE:2000000]"
        lines[#lines+1]="[IMPACT_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[COMPRESSIVE_YIELD:1000000]"
        lines[#lines+1]="[COMPRESSIVE_FRACTURE:2000000]"
        lines[#lines+1]="[COMPRESSIVE_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[TENSILE_YIELD:1000000]"
        lines[#lines+1]="[TENSILE_FRACTURE:2000000]"
        lines[#lines+1]="[TENSILE_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[TORSION_YIELD:1000000]"
        lines[#lines+1]="[TORSION_FRACTURE:2000000]"
        lines[#lines+1]="[TORSION_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[SHEAR_YIELD:1000000]"
        lines[#lines+1]="[SHEAR_FRACTURE:2000000]"
        lines[#lines+1]="[SHEAR_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[BENDING_YIELD:1000000]"
        lines[#lines+1]="[BENDING_FRACTURE:2000000]"
        lines[#lines+1]="[BENDING_STRAIN_AT_YIELD:0]"
        lines[#lines+1]="[MAX_EDGE:12000]"
        return {mat=lines,weight=1}
    end
