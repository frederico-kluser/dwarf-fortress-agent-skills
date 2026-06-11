# Night troll/script

> Fonte: [Night troll/script](https://dwarffortresswiki.org/index.php/Night_troll/script) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

night_troll_names={
        {name="troll",names="trolls",name_adj="troll",cond=function(options) return true end},
        {name="man",names="men",name_adj="man",cond=function(options) return adj_exploitable_check(options.fadj) and options.is_male_version end},
        {name="woman",names="women",name_adj="woman",cond=function(options) return adj_exploitable_check(options.fadj) and not options.is_male_version end},
        {name="brute",names="brutes",name_adj="brutish",cond=function(options) return options.is_male_version and options.night_creature_strength_pref and adj_exploitable_check(options.fadj) end},
        {name="hag",names="hags",name_adj="hag",cond=function(options) return not options.is_male_version end},
        {name="crone",names="crones",name_adj="crone",cond=function(options) return not options.is_male_version end},
        {name="monster",names="monsters",name_adj="monster",cond=function(options) return true end},
        {name="creature",names="creatures",name_adj="creature",cond=function(options) return true end},
        {name="ogre",names="ogres",name_adj="ogre",cond=function(options) return options.night_creature_strength_pref and options.is_male_version end},
        {name="ogress",names="ogresses",name_adj="ogress",cond=function(options) return options.night_creature_strength_pref and not options.is_male_version end},
        {name="freak",names="freak",name_adj="freak",cond=function(options) return adj_exploitable_check(options.fadj) end},
        {name="horror",names="horrors",name_adj="horror",cond=function(options) return true end},
    }

    night_troll_flavor_adjs={
        "night",
        "dark",
        "shadow",
        "midnight",
        "dusk",
        "vile",
        "wicked",
        "twilight",
        "moon",
        "gloom",
        "bleak",
    }

    night_troll_flavor={
        {
            add="it mutters to itself as it moves aimlessly",
            flavor_adj={"muttering","grumbling","whispering","brooding"}
        },
        {
            add="it groans from time to time",
            flavor_adj={"groaning","moaning","whispering","brooding"}
        },
        {
            add="it howls into high winds",
            flavor_adj={"screaming","howling","baying","bellowing","shrieking","wailing"}
        },
    }
    night_troll_strength_flavor={
        {
            add="it shambles sluggishly",
            flavor_adj={}
        },
        {
            add="it stamps the ground and snorts",
            flavor_adj={}
        },
        {
            add="it has a bloated body",
            flavor_adj={"bloated"}
        },
        {
            add="it lumbers along steadily from place to place",
            flavor_adj={}
        },
    }
    night_troll_agile_flavor={
        {
            add="its joints are backward",
            flavor_adj={"backward"}
        },
        {
            add="it moves with uneven jerking motions",
            flavor_adj={}
        },
        {
            add="its limbs jut out at asymmetric angles",
            flavor_adj={"crooked","twisted"}
        },
        {
            add="it lopes quickly along the ground",
            flavor_adj={}
        },
        {
            add="it strides in silence with purpose",
            flavor_adj={}
        },
    }

    night_troll_smells={
        "bug innards",
        "cooked flesh",
        "death"
    }

    creatures.night_creature.troll.default=function(tok)
        local lines={}
        local options={
            spheres={
                NIGHT=true,
                DEATH=true
            },
            fallback_pref_str="macabre ways",
            token=tok
        }
        options.is_male_version=one_in(2)
        if one_in(2) then
            options.night_creature_strength_pref=true
        else
            options.night_creature_agile_pref=true
        end
        night_creature_universals(lines,options)
        -- partially I started feeling split_to_lines is ugly,
        -- partially I want to show there's no one right way to do it
        -- hopefully my caprice isn't too aggravating
        lines[#lines+1]="[NIGHT_CREATURE_HUNTER]"
        lines[#lines+1]="[BIOME:ANY_FOREST]"
        lines[#lines+1]="[BIOME:ANY_SHRUBLAND]"
        lines[#lines+1]="[BIOME:ANY_SAVANNA]"
        lines[#lines+1]="[BIOME:ANY_GRASSLAND]"
        lines[#lines+1]="[BIOME:ANY_WETLAND]"
        lines[#lines+1]="[BIOME:TUNDRA]"
        if options.is_male_version then
            lines[#lines+1]="[CASTE:MALE]"
            lines[#lines+1]="[MALE]"
            lines[#lines+1]="[SPOUSE_CONVERTER]"
            lines[#lines+1]="[ORIENTATION:MALE:1:0:0]"
            lines[#lines+1]="[ORIENTATION:FEMALE:0:0:1]"
        lines[#lines+1]="[CASTE:FEMALE]"
            lines[#lines+1]="[FEMALE]"
            lines[#lines+1]="[CONVERTED_SPOUSE]"
        else
            lines[#lines+1]="[CASTE:FEMALE]"
            lines[#lines+1]="[FEMALE]"
            lines[#lines+1]="[SPOUSE_CONVERTER]"
            lines[#lines+1]="[ORIENTATION:MALE:0:0:1]"
            lines[#lines+1]="[ORIENTATION:FEMALE:1:0:0]"
        lines[#lines+1]="[CASTE:MALE]"
            lines[#lines+1]="[MALE]"
            lines[#lines+1]="[CONVERTED_SPOUSE]"
        end
        lines[#lines+1]="[SELECT_CASTE:ALL]"

        lines[#lines+1]="[CAN_LEARN]"
        if one_in(2) then lines[#lines+1]="[SLOW_LEARNER]" end
        lines[#lines+1]="[CAN_SPEAK]"
        lines[#lines+1]="[SENSE_CREATURE_CLASS:GENERAL_POISON:15:4:0:1]"
        if options.night_creature_strength_pref then
            lines[#lines+1]="[PHYS_ATT_RANGE:STRENGTH:1000:1250:1500:2000:2250:2500:3000]"
            lines[#lines+1]="[PHYS_ATT_RANGE:AGILITY:450:550:700:750:800:850:900]"
            lines[#lines+1]="[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"
            lines[#lines+1]="[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"
            options.special_walk_speed=1000
        elseif options.night_creature_agile_pref then
            lines[#lines+1]="[PHYS_ATT_RANGE:STRENGTH:450:550:700:750:800:850:900]"
            lines[#lines+1]="[PHYS_ATT_RANGE:AGILITY:1000:1250:1500:2000:2250:2500:3000]"
            lines[#lines+1]="[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"
            lines[#lines+1]="[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"
            options.special_walk_speed=800;
        elseif options.night_creature_strength_agile_pref then
            lines[#lines+1]="[PHYS_ATT_RANGE:STRENGTH:1000:1150:1250:1500:2000:2250:2500]"
            lines[#lines+1]="[PHYS_ATT_RANGE:AGILITY:1000:1150:1250:1500:2000:2250:2500]"
            lines[#lines+1]="[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"
            lines[#lines+1]="[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"
            options.special_walk_speed=850;
        end
        lines[#lines+1]="[PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]"
        lines[#lines+1]="[PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]"
        lines[#lines+1]="[MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]"
        lines[#lines+1]="[MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]"
        lines[#lines+1]="[MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]"
        --[[
    MENTAL_ATTRIBUTE_CREATIVITY,
    MENTAL_ATTRIBUTE_INTUITION,
    MENTAL_ATTRIBUTE_SPATIAL_SENSE,
    MENTAL_ATTRIBUTE_KINESTHETIC_SENSE,
    MENTAL_ATTRIBUTE_EMPATHY,
        ]]
        --lines[#lines+1]="[PERSONALITY:ANXIETY_PROPENSITY:0:0:0]"
        --lines[#lines+1]="[PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:BASHFUL:0:0:0]"
        lines[#lines+1]="[PERSONALITY:STRESS_VULNERABILITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:FRIENDLINESS:0:0:0]"
        --lines[#lines+1]="[PERSONALITY:ASSERTIVENESS:100:100:100]"
        lines[#lines+1]="[PERSONALITY:DISDAIN_ADVICE:100:100:100]"
        lines[#lines+1]="[PERSONALITY:CHEER_PROPENSITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:GRATITUDE:0:0:0]"
        lines[#lines+1]="[PERSONALITY:TRUST:0:0:0]"
        lines[#lines+1]="[PERSONALITY:ALTRUISM:0:0:0]"
        --lines[#lines+1]="[PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]"
        lines[#lines+1]="[PERSONALITY:CRUELTY:100:100:100]"
        --lines[#lines+1]="[PERSONALITY:PRIDE:100:100:100]"

        add_regular_tokens(lines,options)
        populate_sphere_info(lines,options)
        local rcp={
            name_string="humanoid",
            tile='H',
            body_base="HUMANOID",
            c_class="AMPHIBIAN", -- FOR SKIN/ORGANS AND NO HAIR/FEATHERS AT FIRST
            min_size=1,
            cannot_have_shell=true
        }
        lines[#lines+1]="[NATURAL_SKILL:WRESTLING:6]"
        lines[#lines+1]="[NATURAL_SKILL:BITE:6]"
        lines[#lines+1]="[NATURAL_SKILL:GRASP_STRIKE:6]"
        lines[#lines+1]="[NATURAL_SKILL:STANCE_STRIKE:6]"
        lines[#lines+1]="[NATURAL_SKILL:MELEE_COMBAT:6]"
        lines[#lines+1]="[NATURAL_SKILL:DODGING:6]"
        lines[#lines+1]="[NATURAL_SKILL:SITUATIONAL_AWARENESS:6]"

        lines[#lines+1]="[DIFFICULTY:3]"
        lines[#lines+1]="[LAIR:SIMPLE_MOUND:50]"
        lines[#lines+1]="[LAIR:SIMPLE_BURROW:50]"
        lines[#lines+1]="[LAIR_CHARACTERISTIC:HAS_DOORS:100]"
        lines[#lines+1]="[HABIT_NUM:TEST_ALL]"
        lines[#lines+1]="[HABIT:GRIND_BONE_MEAL:50]"
        lines[#lines+1]="[HABIT:COOK_BLOOD:50]"
        lines[#lines+1]="[HABIT:GRIND_VERMIN:50]"
        lines[#lines+1]="[HABIT:COOK_VERMIN:50]"
        lines[#lines+1]="[HABIT:COOK_PEOPLE:50]"
        lines[#lines+1]="[HABIT:COLLECT_TROPHIES:50]"
        lines[#lines+1]="[ODOR_STRING:"..pick_random(night_troll_smells).."]"
        lines[#lines+1]="[ODOR_LEVEL:90]"
        local body_size=70000+trandom(8)*10000+trandom(11)*1000
        options.body_size=body_size
        lines[#lines+1]="[SELECT_CASTE:"..(options.is_male_version and "MALE" or "FEMALE").."]"
        lines[#lines+1]="[BODY_SIZE:0:0:"..tostring(math.floor(body_size/20)).."]"
        lines[#lines+1]="[BODY_SIZE:2:0:"..tostring(math.floor(body_size/4)).."]"
        lines[#lines+1]="[BODY_SIZE:12:0:"..tostring(math.floor(body_size)).."]"
        body_size_properties(lines,body_size)
        local spouse_size=math.floor(body_size*(trandom(51)+50)/100)
        lines[#lines+1]="[SELECT_CASTE:"..(options.is_male_version and "FEMALE" or "MALE").."]"
        add_body_size(lines,spouse_size)
        lines[#lines+1]="[SELECT_CASTE:ALL]"
        lines[#lines+1]="[BABY:1]"
        lines[#lines+1]="[CHILD:18]"
        lines[#lines+1]="[CREATURE_TILE:165]" --Ñ
        options.custom_desc_func=function(options)
            local add_tbl={}
            options.flavor_adj = options.flavor_adj or {}
            if one_in(4) then
                add_tbl=pick_random(night_troll_flavor)
            elseif options.night_creature_strength_pref then
                add_tbl=pick_random(night_troll_strength_flavor)
                options.flavor_adj[#options.flavor_adj+1]="lumbering"
                options.flavor_adj[#options.flavor_adj+1]="hulking"
            elseif options.night_creature_agile_pref then
                add_tbl=pick_random(night_troll_agile_flavor)
                options.flavor_adj[#options.flavor_adj+1]="narrow"
                options.flavor_adj[#options.flavor_adj+1]="starved"
                options.flavor_adj[#options.flavor_adj+1]="emaciated"
            end
            table_merge(options.flavor_adj,add_tbl.flavor_adj)
            return add_tbl.add
        end
        options.flavor_adj=options.flavor_adj or {}
        build_procgen_creature(rcp,lines,options)
        table_merge(options.flavor_adj,night_troll_flavor_adjs)
        night_troll_end_phrases=night_troll_end_phrases or {
            " of the night",
            " of evil",
            " of twilight",
            " of shadow",
        }
        options.potential_end_phrase = options.potential_end_phrase or {}
        table_merge(options.potential_end_phrase,night_troll_end_phrases)
        local name_str=""
        local used_ending=false
        local name={}
        if trandom(#options.flavor_adj + #options.potential_end_phrase) >= #options.flavor_adj then
            options.eadj=pick_random(options.potential_end_phrase)
            name=pick_random_conditional(night_troll_names,"cond",options)
            name_str=name.name..options.eadj..":"..name.names..options.eadj..":"..name.name_adj..options.eadj
            used_ending=true
        else
            options.fadj=pick_random(options.flavor_adj)
            name=pick_random_conditional(night_troll_names,"cond",options)
            name_str=options.fadj.." "..name.name..":"..options.fadj.." "..name.names..":"..options.fadj.." "..name.name_adj
        end
        night_troll_wife_names=night_troll_wife_names or {
            {"spouse","spouses"},
            {"mate","mates"},
            {"consort","consorts"},
            {"wife","wives"},
            {"bride","brides"},
        }
        night_troll_husband_names=night_troll_husband_names or {
            {"spouse","spouses"},
            {"mate","mates"},
            {"consort","consorts"},
            {"husband","husbands"},
            {"bridegroom","bridegrooms"},
            {"groom","grooms"}
        }
        local sn,sns="",""
        if options.is_male_version then
            sn,sns=table.unpack(pick_random(night_troll_wife_names))
            lines[#lines+1]="[SELECT_CASTE:MALE]"
        else
            sn,sns=table.unpack(pick_random(night_troll_husband_names))
            lines[#lines+1]="[SELECT_CASTE:FEMALE]"
        end
        local cstr=""
        if used_ending then
            cstr=name.name.." "..sn..options.eadj..":"..name.name.." "..sns..options.eadj..":"..name.name_adj.." "..sn..options.eadj
        elseif one_in(2) then
            cstr=options.fadj.." "..name.name.." "..sn..":"..options.fadj.." "..name.name.." "..sns..":"..options.fadj.." "..name.name.." "..sn
        else
            cstr=sn.." of the "..options.fadj.." "..name.name..":"..sns.." of the "..options.fadj.." "..name.name..":"..sn.." of the "..options.fadj.." "..name.name_adj
        end
        lines[#lines+1]="[CASTE_NAME:"..name_str.."]"
        if options.is_male_version then lines[#lines+1]="[SELECT_CASTE:FEMALE]"
        else lines[#lines+1] = "[SELECT_CASTE:MALE]" end
        lines[#lines+1]="[CASTE_NAME:"..cstr.."]"
        lines[#lines+1]="[GO_TO_START]"
        lines[#lines+1]="[NAME:"..name_str.."]"
        return {raws=lines,weight=1}
    end
