# Interaction token

> Fonte: [Interaction token](https://dwarffortresswiki.org/index.php/Interaction_token) — Dwarf Fortress Wiki (GFDL/MIT)

The following tokens can be used to define and use interactions. (*It appears that, at least in order to make the big list make a little more sense, some examples of those may be necessary.*)

## Definitions

[TABLE]

## Usage

To enable a particular type of creature to use an interaction directly, the creature token [`CAN_DO_INTERACTION:``]` should be added to its creature raws (replacing '\' with the ID of the desired interaction; for an interaction called `[INTERACTION:CLEANING]` in the raws, the ID would be "CLEANING"), followed by a series of \[CDI:...\] tokens as detailed below.

Interactions can also be granted to individual creatures via syndromes using the syndrome effect token [`CE_CAN_DO_INTERACTION``]` followed by [`CDI:INTERACTION:``]` and additional CDI tokens as required.

The following is a list of valid CDI tokens. Precede them with "CDI:" in the style of `[CDI:ADV_NAME:Clean]`, for example.

[TABLE]

## Breath attacks

Breath attacks are controlled by the MATERIAL_EMISSION interaction, like so:

` [CAN_DO_INTERACTION:MATERIAL_EMISSION]`\
`       [CDI:ADV_NAME:Breath custom material]`\
`       [CDI:USAGE_HINT:ATTACK]`\
`       [CDI:BP_REQUIRED:BY_CATEGORY:MOUTH]`\
`       [CDI:MATERIAL:LOCAL_CREATURE_MAT:CUSTOMMATERIAL:TRAILING_VAPOR_FLOW]`\
`       [CDI:TARGET:C:LINE_OF_SIGHT]`\
`       [CDI:TARGET_RANGE:C:15]`\
`       [CDI:MAX_TARGET_NUMBER:C:1]`\
`       [CDI:WAIT_PERIOD:50]`

The most important part is this line:

` [CDI:MATERIAL:LOCAL_CREATURE_MAT:CUSTOMMATERIAL:TRAILING_VAPOR_FLOW]`

The CDI refers to CAN_DO_INTERACTION; the MATERIAL states that this line shows what the material is. LOCAL_CREATURE_MAT:CUSTOMMATERIAL is your material, and TRAILING_VAPOR_FLOW refers to the breath attack type. Other types are seen below. Also important is this line:

` [CDI:TARGET:C:LINE_OF_SIGHT]`

LINE_OF_SIGHT refers to where the target C may be; others include SELF_ALLOWED (presumably like LINE_OF_SIGHT, but with the creature allowed to target itself), SELF_ONLY (preferable for undirected attacks and TOUCHABLE (for up-close attacks, as trailing flows tend to be).

### Breath Attack Types

`   `**`[CDI:MATERIAL::]`**

Is used to emit a specific material in a specific manner. A list of valid emission types can be found below.

Examples:

`   [CDI:MATERIAL:INORGANIC:GABBRO:``SHARP_ROCK``]`

shoots a sharp gabbro rock

`   [CDI:MATERIAL:PLANT_MAT:GRASS_CAVE_WHEAT:MILL:``UNDIRECTED_DUST``]`

releases a cloud of dwarven wheat flour

`   [CDI:MATERIAL:CREATURE_MAT:DWARF:TEARS:``SPATTER_LIQUID``]`

creates a pool of dwarven tears

`   `**`[CDI:FLOW:]`**

Is used to emit one of the special hardcoded flow types (FIREBALL, FIREJET or DRAGONFIRE).

Example:

`   [CDI:FLOW:``DRAGONFIRE``]`

[TABLE]

Keep in mind that you can give a creature multiple breath attacks, which appears to make the creature choose between them at random. Creatures cannot use the WEATHER effects, these being reserved for regional interactions.

One major difference between GAS, VAPOR, and DUST is that if the material cannot exist in the specified state at the current temperature, it will automatically be created at a temperature allowing it to exist. So if you create a vapor spray that uses rock or metal as a material, that spray will be created at the material's melting point, setting everything it touches on fire. You can also create a freezing spray by using a custom material that has extremely low melting and/or boiling points.

If you give a creature a material breath attack, be aware that it will be caught in the attack more frequently than its targets. Make sure to make your creatures immune to their own breath weapons!

## Creature and Caste Flags

Certain interaction and syndrome effects (currently limited to [\IE_SUMMON_UNIT\] and [\CE_BODY_TRANSFORMATION\]) permit modders to specify the required/forbidden creature and caste flags of the desired creature(s). These are a collection of internal flags which are derived from creature tokens but are not necessarily identical to them. The following lists contain creature and caste flag names as provided by Toady One in a FotF reply 4 (valid as of 0.47.04).

## See Also

- Syndrome
- Interaction examples
