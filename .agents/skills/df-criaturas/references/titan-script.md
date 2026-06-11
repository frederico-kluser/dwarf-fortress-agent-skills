# Titan/script

> Fonte: [Titan/script](https://dwarffortresswiki.org/index.php/Titan/script) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

creatures.titan.default=function(subregion,tok)
        local tbl={}
        local options={
            pick_sphere_rcm=true,
            strong_attack_tweak=true,
            sickness_name="titan sickness",
            token=tok
        }
        local atp = tostring(world.param.titan_attack_trigger_population)
        local atew = tostring(world.param.titan_attack_trigger_exported_wealth)
        local atcw = tostring(world.param.titan_attack_trigger_created_wealth)
        split_to_lines(tbl,[[
        [TITAN]
        [ATTACK_TRIGGER:]]..atp..":"..atew..":"..atcw..[[]
        [NO_GENDER]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [DIFFICULTY:10]
        [LAIR:SHRINE:100]

        [NATURAL_SKILL:WRESTLING:6]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:15]
        ]])
        add_regular_tokens(tbl,options)
        options.spheres={}
        if subregion then
            map_merge(options.spheres,regiontypes[subregion.type].spheres)
            if subregion.is_evil then
                options.spheres[pick_random(evil_spheres)]=true
                options.is_evil = true
            elseif subregion.is_good then
                options.spheres[pick_random(good_spheres)]=true
                options.is_good = true
            end
        end
        populate_sphere_info(tbl,options)
        local rcp=get_random_creature_profile(options)
        add_body_size(tbl,math.max(10000000,rcp.min_size),options)
        tbl[#tbl+1]="[CREATURE_TILE:"..tile_string(rcp.tile).."]"
        if options.is_good then
            tbl[#tbl+1]="[BENIGN]"
        else
            tbl[#tbl+1]="[LARGE_PREDATOR]"
        end
        build_procgen_creature(rcp,tbl,options)
        tbl[#tbl+1]="[GO_TO_START]"
        local subreg_name=subregion and regiontypes[subregion.type].name(subregion) or "buggy"
        local name_str = subreg_name.." titan:"..subreg_name.." titans:"..subreg_name.."-titan]"
        tbl[#tbl+1]="[NAME:"..name_str
        tbl[#tbl+1]="[CASTE_NAME:"..name_str
        return {creature=tbl,weight=1}
    end
