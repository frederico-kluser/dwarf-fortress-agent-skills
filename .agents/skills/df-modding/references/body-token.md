# Body token

> Fonte: [Body token](https://dwarffortresswiki.org/index.php/Body_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Body tokens** are one of the fundamental parts of creatures, and determine their bodily structure. There are two major types of body tokens: *body templates* (BODY) and *body parts* (BP).

A creature uses the [`[BODY]`](/index.php/Creature_token#BODY "Creature token") creature token to list all of the body templates it includes. Each part listed in each template is then included in the creature. In other words: a creature lists the *body templates* it is made of, and each *body template* contains a set of *body parts*. Each *body part* specifies which other body part it is attached to.

Body parts can connect specifically to another body part, or generally to any body part of a certain category. These connections are handled by the CON and CONTYPE body part tokens respectively.

Body parts can be renamed with a bodygloss, allowing someone to reuse an existing template instead of defining a similar template with only the names of the body parts changed.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  BP | ID / name / pluralized name | Begin the definition of a body part with the given ID, name, and plural name. If the plural form would just add an 's' then it can be replaced with 'STP' (which stands for "Standard Plural"). |
|  APERTURE |  | Marks the body part as an opening in the body. If it is [`[EMBEDDED]`](/index.php/Body_token#EMBEDDED "Body token"), it cannot be gouged. |
|  BREATHE |  | Body part is used to breathe. If all body parts with \[BREATHE\] are damaged or destroyed, the creature will suffocate unless it has the [`[NOBREATHE]`](/index.php/Creature_token#NOBREATHE "Creature token") tag. Note that bruising counts as (fast-healing) damage. |
|  CATEGORY | ID | Assigns the body part to a user-defined category. Used by [`[CON_CAT]`](/index.php/Body_token#CON_CAT "Body token") to attach to other body parts. |
|  CON | value | Connects the body part to a specific other body part. |
|  CON_CAT | value | Connects the body part to all other body parts having the specified [`[CATEGORY]`](/index.php/Body_token#CATEGORY "Body token"). |
|  CONTYPE | value | Connects the body part to all other body parts having the specified type token. Valid values are UPPERBODY, LOWERBODY, HEAD, GRASP, or STANCE. |
|  CIRCULATION |  | Body part is responsible for blood circulation. Exact effects not known. |
|  CONNECTOR |  | Body part is used to connect other body parts together. Used for the neck and lower spine. |
|  DEFAULT_RELSIZE | Size | This command establishes the relative size of body parts within a creature. The numbers have no absolute meaning or units. |
|  DIGIT |  | Defines part as a digit. Body parts that are digits, or have them as direct sub-parts, can perform gouging attacks within a wrestling hold. |
|  EMBEDDED |  | Body part with this tag is embedded on the surface of parent body part. i.e.: eyes and mouth on head. It cannot be chopped off, can't be used to wrestle enemies and can't be grabbed by them. |
|  FLIER |  | Flags the body part as being needed for flight. Damage to a certain number of FLIER body parts will prevent the creature from flying. Note that a creature can only fly if the creature has the [`[FLIER]`](/index.php/Creature_token#FLIER "Creature token") tag in its creature definition, and that a flying creature does not actually need any FLIER body parts. This tag's only purpose is to identify body parts which will cause a creature to **lose** the ability to fly when damaged. |
|  GELDABLE |  | Creatures with a body part containing this token may be / gelded / , creating a sterile creature that is typically marked with / x♂x / . Gelding may also occur during combat if this body part is damaged sufficiently. / Despite its name, GELDABLE does not need to be combined with / MALE / . A modded / FEMALE / creature with a GELDABLE body part can be "gelded" through the regular gelding interface or through combat damage, resulting in a sterile creature marked / x♀x / . |
|  GRASP |  | Creature can wield a picked-up weapon with the body part, and can use the part to initiate almost all wrestling moves. When creatures are spawned with a weapon and shield, one GRASP part will hold a weapon while **all others** will hold shields. A grasp-able bodypart is needed for Grasp-attacks, which are in turn needed to start a fist fight. Creatures throwing a tantrum, but missing a bodypart with the grasp-property, will be cancelling their fist fight, due to being 'too injured'. |
|  GUTS |  | Body part is susceptible to low blows. Used for guts. Damage to this body part causes nausea and may make the creature lose turns, vomiting uncontrollably. |
|  HEAD |  | Flags the body part as being able to wear head clothing like hats, helms, etc. If all heads are chopped off, the creature dies. Multiple heads **are** redundant - for example, hydras can survive with several missing heads. |
|  HEAR |  | Body part is used to hear. May be a requirement for the body part to wear earrings. |
|  INDIVIDUAL_NAME | name / plural | Adding individual names tells the game what to call each individual part in a NUMBERed bodypart. This command replaces "first upper front tooth" for example. |
|  INTERNAL |  | Marks the body part as being inside the body. It is behind all the other tissues of the body part, cannot be severed, nor used for wrestling. It cannot be targeted directly in combat, but can be damaged by attacks to the parent body part. |
|  JOINT |  | Body part is a joint. If the limb it's in is grabbed in a wrestling hold, it can be broken with bending force, disabling the parent limb. If the joint is modded to sit outside the body, grabbing and breaking it snaps the entire limb right off. |
|  LIMB |  | Body part is a limb. It can be used to initiate most wrestling moves. If it is located between an [`[UPPERBODY]`](/index.php/Body_token#UPPERBODY "Body token") part and a [`[GRASP]`](/index.php/Body_token#GRASP "Body token") body part, it is eligible to be covered by certain types of armor (body armors and gauntlets). If it is located between a [`[LOWERBODY]`](/index.php/Body_token#LOWERBODY "Body token") part and a [`[STANCE]`](/index.php/Body_token#STANCE "Body token") body part, it is eligible to be covered by other types of armor (Leg armors like pants, etc.; trailing body armors like mail shirts and robes; and high boots). |
|  LOWERBODY |  | Flags the body part as being able to wear lower body clothing like skirts, pants, etc. If all parts with this token are chopped off or pulped, the creature dies. If the creature has multiple parts with this token, they will not die until all parts with this token have been pulped or severed. No such creature exists in the base game, however. |
|  LEFT |  | Marks body part as on the left side of the body and vulnerable to attacks from the left. Used in conjunction with tags in the b_detail_plan_default raw. |
|  MOUTH |  | Body part is a mouth. Implication unknown. |
|  NUMBER | value | The number lets you stack identical body parts. These can be individually damaged by wounds, but you don't have to define them explicitly one by one. If you don't give them individual names (see teeth) they'll be preceded by ordinal numbers (first, second, etc.). In practice, though, they cannot be individually damaged - if you knock out one tooth, the entire group will be knocked out at once (and will be scattered across the area). Butchering doesn't respect this and produces only a single body part per group. The value is capped at 32. |
|  NERVOUS |  | Body part is the hub of nervous function. Used for the parts of the spine. Damage disables everything in the parent bodypart and what's below it, causing death by suffocation in most cases. |
|  PREVENTS_PARENT_COLLAPSE |  | Body part must be destroyed in order for the attached parent object to be considered destroyed. Found on skulls and spinal columns. |
|  RIGHT |  | Marks body part as on the right side of the body and vulnerable to attacks from the right. Used in conjunction with tags in the b_detail_plan_default raw. |
|  SKELETON |  | Body part is part of the creature's skeleton. |
|  STANCE |  | Allows the creature to stand. Damage or loss of these body parts will cause the creature to fall over - loss of one STANCE part can be substituted with a crutch. Does not give the body part an ability to initiate wrestling moves, unlike [`[GRASP]`](/index.php/Body_token#GRASP "Body token") or [`[LIMB]`](/index.php/Body_token#LIMB "Body token"). |
|  SIGHT |  | Body part is used to see. If the creature has no SIGHT body parts, or if all its sight body parts are damaged or destroyed, it can't see unless it has the [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token") tag in its creature definition. |
|  SMELL |  | Body part is used to smell. Currently unused. |
|  SMALL |  | "SMALL means that the part isn't displayed as part of the overall displayed body part lists, and can't be splinted. They are more often targeted for torture (although those situations might not occur anymore). They are removed in skeletons if they aren't specifically skeletons/joints/digits/apertures. They are more easily lost in world gen duels. They are the only gougable/pinchable parts *(note: at least this is no longer the case.)*. SMALL is an old tag, so it has accumulated some weird functions which'll get split off over time. " --Toady |
|  SOCKET |  | Body part breaks off and goes flying if broken, even with blunt force. Used on teeth to make them easy to knock out - rendered invalid by [`[INTERNAL]`](/index.php/Body_token#INTERNAL "Body token"). |
|  THROAT |  | Body part can be strangled - latching bites that hit the head have a chance to target this instead. Note: this tag doesn't control any bleeding behavior. |
|  THOUGHT |  | The central core of the body, used with the brain. Damage causes instant death, unless the creature has / \[NO_THOUGHT_CENTER_FOR_MOVEMENT\] / \[NOTHOUGHT\] / . / \[ / Verify / \] / If no body part has this token (and none of the above exclusions are specified), the creature will spawn injured and will be unable to stand or fly. If the creature is a / \[FLIER\] / , this can result in it spawning in mid-air, immediately plummeting to the ground, and dying of fall damage. |
|  TOTEMABLE |  | This bodypart can be turned into a totem by craftsmen. Always drops from slaughtered creatures, no matter how small. |
|  UPPERBODY |  | Flags the body part as being able to wear upper body clothing like coats, breastplates etc. If all parts with this token are pulped or chopped off, the creature dies. Multiple UPPERBODY parts are redundant, but no such creatures exist in the base game. All default creatures with bodies have the upper body as the root of the body tree, making it impossible to chop off. |
|  UNDER_PRESSURE |  | Makes the body part pop out of the body when cut through - used on guts. Body part shows up as "~" and drags behind the victim when spilled. |
|  VERMIN_BUTCHER_ITEM |  | Allows the item to be obtained from butchered or rotted vermin - used with shells. |

## Example

The following example creates an arrangement of spike parts that emerge from spike bases arranged along the upper and lower back. The parts are attached together in a flexible way that allows the creature definition to choose how many spikes bases are arranged on the body, how thick the spike bases are, and how many spikes emerge from each individual base.

    defines spikes that are intended to looking something like this:
          /\          <-SPIKE
          ||
         _||_         <-SPIKE_BASE
    ____/    \____    <-SPIKE_LAYOUT (flush with existing skin)

    [BODY:SPIKE_LAYOUT_8]    arranges 8 spikes along the back
        [BP:UBACK_SPIKE_AREA_UL:left upper back:STP][CONTYPE:UPPERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT] the SPIKE_LAYOUT category marks where our spike bases will grow out of the body later
            [DEFAULT_RELSIZE:80]
        [BP:UBACK_SPIKE_AREA_UR:right upper back:STP][CONTYPE:UPPERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:UBACK_SPIKE_AREA_LL:left upper middle back:STP][CONTYPE:UPPERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:UBACK_SPIKE_AREA_LR:right upper middle back:STP][CONTYPE:UPPERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_UL:left lower middle back:STP][CONTYPE:LOWERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_UR:right lower middle back:STP][CONTYPE:LOWERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_LL:left lower back:STP][CONTYPE:LOWERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_LR:right lower back:STP][CONTYPE:LOWERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]

    [BODY:SPIKE_LAYOUT_4]    arranges 4 spikes in the middle of the back
        [BP:UBACK_SPIKE_AREA_LL:left upper middle back:STP][CONTYPE:UPPERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:UBACK_SPIKE_AREA_LR:right upper middle back:STP][CONTYPE:UPPERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_UL:left lower middle back:STP][CONTYPE:LOWERBODY][EMBEDDED][LEFT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]
        [BP:LBACK_SPIKE_AREA_UR:right lower middle back:STP][CONTYPE:LOWERBODY][EMBEDDED][RIGHT][CATEGORY:SPIKE_LAYOUT]
            [DEFAULT_RELSIZE:80]

    [BODY:SPIKE_BASE_THIN]   a small base for spike(s)
        [BP:SB_THIN:thin spike base:STP][CON_CAT:SPIKE_LAYOUT][CATEGORY:SPIKE_BASE]    a SB_THIN will grow out of every SPIKE_LAYOUT part we have added to the body
            [DEFAULT_RELSIZE:20]

    [BODY:SPIKE_BASE_MED]    a medium base for spike(s)
        [BP:SB_MED:spike base:STP][CON_CAT:SPIKE_LAYOUT][CATEGORY:SPIKE_BASE]   a SB_MED will grow out of every SPIKE_LAYOUT part
            [DEFAULT_RELSIZE:30]

    [BODY:SPIKE_BASE_THICK]  a large base for spike(s)
        [BP:SB_THICK:thick spike base:STP][CON_CAT:SPIKE_LAYOUT][CATEGORY:SPIKE_BASE]  a SB_THICK will grow out of every SPIKE_LAYOUT part
            [DEFAULT_RELSIZE:40]

    [BODY:SPIKE_1]   a single spike
        [BP:S1:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]    a S1 will grow out of every SPIKE_BASE part we have added to the body
            [DEFAULT_RELSIZE:30]

    [BODY:SPIKE_2]   a pair of spikes
        [BP:S1:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]    a S1 and S2 will grow out of every SPIKE_BASE part
            [DEFAULT_RELSIZE:30]
        [BP:S2:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]
            [DEFAULT_RELSIZE:30]

    [BODY:SPIKE_3]   a trio of spikes
        [BP:S1:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]    a S1, S2, and S3 will grow out of every SPIKE_BASE part
            [DEFAULT_RELSIZE:30]
        [BP:S2:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]
            [DEFAULT_RELSIZE:30]
        [BP:S2:spike:STP][CON_CAT:SPIKE_BASE][CATEGORY:SPIKE]
            [DEFAULT_RELSIZE:30]

Usage:

`[BODY:QUADRUPED_NECK:SPIKE_LAYOUT_8:SPIKE_BASE_THICK:SPIKE_2]` would create a creature with 8 thick spike bases that each hold 2 spikes.

`[BODY:QUADRUPED_NECK:SPIKE_LAYOUT_4:SPIKE_BASE_THIN:SPIKE_1]` would create a creature with 4 thin spike bases that each hold a single spike.
