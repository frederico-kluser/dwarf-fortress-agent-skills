# Bogeyman/script

> Fonte: [Bogeyman/script](https://dwarffortresswiki.org/index.php/Bogeyman/script) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

creatures.night_creature.bogeyman.default=function(tok)
        local lines={}
        local options={
            can_bogey_polymorph=true,
            spheres={
                NIGHT=true,
                NIGHTMARES=true,
                MISERY=true
            },
            forced_color={
                f=0,
                b=0,
                br=1
            },
            no_general_poison=true,
            blood_color=function(cl)
                -- DARKER MAGENTA COLORS
                return cl.h>=260 and cl.h = 0.1
            end,
            fallback_pref_str="terror-inspiring antics",
            token=tok
        }
        night_creature_universals(lines,options)
        options.cannot_have_antennae=false
        if one_in(10) then options.glowing_eyes=true end
        lines[#lines+1]="[NIGHT_CREATURE_BOGEYMAN]"

        lines[#lines+1]="[NATURAL_SKILL:WRESTLING:6]"
        lines[#lines+1]="[NATURAL_SKILL:BITE:6]"
        lines[#lines+1]="[NATURAL_SKILL:MELEE_COMBAT:6]"
        lines[#lines+1]="[NATURAL_SKILL:GRASP_STRIKE:6]"
        lines[#lines+1]="[NATURAL_SKILL:STANCE_STRIKE:6]"
        lines[#lines+1]="[NATURAL_SKILL:DODGING:6]"
        lines[#lines+1]="[NATURAL_SKILL:SITUATIONAL_AWARENESS:6]"

        lines[#lines+1]="[CAN_LEARN][CAN_SPEAK]"
        options.can_learn=true;
        lines[#lines+1]="[NO_GENDER]"
        lines[#lines+1]="[CLUSTER_NUMBER:4:6]"
        --[[******************************* BOGEY
            --atts
        lines[#lines+1]="[PHYS_ATT_RANGE:STRENGTH:450:1050:1150:1250:1350:1550:2250]"
        lines[#lines+1]="[PHYS_ATT_RANGE:TOUGHNESS:450:1050:1150:1250:1350:1550:2250]"
        lines[#lines+1]="[PHYS_ATT_RANGE:ENDURANCE:450:1050:1150:1250:1350:1550:2250]"
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
    MENTAL_ATTRIBUTE_CREATIVITY,
    MENTAL_ATTRIBUTE_INTUITION,
    MENTAL_ATTRIBUTE_SPATIAL_SENSE,
    MENTAL_ATTRIBUTE_KINESTHETIC_SENSE,
    MENTAL_ATTRIBUTE_EMPATHY,
        ]]
        lines[#lines+1]="[PERSONALITY:ANXIETY_PROPENSITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:BASHFUL:0:0:0]"
        lines[#lines+1]="[PERSONALITY:STRESS_VULNERABILITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:FRIENDLINESS:0:0:0]"
        lines[#lines+1]="[PERSONALITY:ASSERTIVENESS:100:100:100]"
        lines[#lines+1]="[PERSONALITY:DISDAIN_ADVICE:100:100:100]"
        lines[#lines+1]="[PERSONALITY:CHEER_PROPENSITY:0:0:0]"
        lines[#lines+1]="[PERSONALITY:GRATITUDE:0:0:0]"
        lines[#lines+1]="[PERSONALITY:TRUST:0:0:0]"
        lines[#lines+1]="[PERSONALITY:ALTRUISM:0:0:0]"
        lines[#lines+1]="[PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]"
        lines[#lines+1]="[PERSONALITY:CRUELTY:100:100:100]"
        --lines[#lines+1]="[PERSONALITY:PRIDE:100:100:100]"
        lines[#lines+1]="[PERSONALITY:HUMOR:100:100:100]"
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
        add_body_size(lines,10000+trandom(11)*1000,options)
        lines[#lines+1]="[CREATURE_TILE:164]" --ñ
        options.custom_desc_func=function(options)
            return "it hurls vicious insults constantly"
        end
        build_procgen_creature(rcp,lines,options)
        lines[#lines+1]="[GO_TO_START]"
        local name_str="bogeyman:bogeymen:bogeyman]"
        lines[#lines+1]="[NAME:"..name_str
        lines[#lines+1]="[CASTE_NAME:"..name_str
        return {raws=lines,weight=1}
    end
