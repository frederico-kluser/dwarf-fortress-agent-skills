# Creature variation token

> Fonte: [Creature variation token](https://dwarffortresswiki.org/index.php/Creature_variation_token) — Dwarf Fortress Wiki (GFDL/MIT)

Creature variations are templates for creatures. In conjunction with they may be used to create creatures which are derived from another already-existing creature, thus the name, though their use-case is broader than that, in vanilla also covering gaits and attacks. They may either be embedded inside creatures (when using ) or be defined as CREATURE_VARIATION objects. The default variations are defined in c_variation_default.txt

Creature variations can be contrasted with the other types of templates for creatures: tissue templates, material templates, and body detail plans. Creature variations are the newest of the four (from 2009) and also the most advanced.

Creature variations can add/convert almost all tokens, but is an exception, so you can’t nest creature variations.

[TABLE]

## Application

The two ways of applying creature variations are and . APPLY_CURRENT_CREATURE_VARIATION takes all creature variation tokens before it in the creature raws (and after previous APPLY_CURRENT_CREATURE_VARIATION tokens, if they exist) and applies them. When tokens are added through APPLY_CURRENT_CREATURE_VARIATION, they are added in the place of APPLY_CURRENT_CREATURE_VARIATION.

Creature variations have an unusual order of application. First, remove tokens are applied (bottom-up according to Toady in c_variation_default.txt, though this should never matter). Then, convert tokens are applied bottom-up (in "reverse" order). Finally, add tokens are applied from the top. This means that won't remove any token added by the same creature variation. It is also why more general conversions can (must) be higher up when overlapping s are used. If they were not read bottom-up, e.g.

`[CV_CONVERT_TAG]`\
`   [CVCT_MASTER:BODY]`\
`   [CVCT_TARGET:QUADRUPED]`\
`   [CVCT_REPLACEMENT:HUMANOID]`

would convert \[BODY:QUADRUPED_FRONT_GRASP:...\] and \[BODY:QUADRUPED_NECK:...\] into \[BODY:HUMANOID_FRONT_GRASP:...\] and \[BODY:HUMANOID_NECK:...\] respectively, before

`[CV_CONVERT_TAG]`\
`   [CVCT_MASTER:BODY]`\
`   [CVCT_TARGET:QUADRUPED_FRONT_GRASP]`\
`   [CVCT_REPLACEMENT:HUMANOID]`\
`[CV_CONVERT_TAG]`\
`   [CVCT_MASTER:BODY]`\
`   [CVCT_TARGET:QUADRUPED_NECK]`\
`   [CVCT_REPLACEMENT:HUMANOID_NECK:3FINGERS]`

could convert them into the expected \[BODY:HUMANOID:...\] and \[BODY:HUMANOID_NECK:3_FINGERS:...\], as should be.

## Arguments and conditional tokens

may be given arguments (in addition to the required creature variation ID). These arguments will replace instances of "!ARG*n*", where *n* is the index of the argument given to APPLY_CREATURE_VARIATION; the first argument will replace any "!ARG1", the second any "!ARG2" and so on. You may use any number of arguments¹. If you have an "!ARG*n*" of a higher number than the argument given the replacements will act oddly, depending on if *n* has more digits than the number of arguments given. E.g. \[APPLY_CREATURE_VARIATION:EXAMPLE_CV:one:two:three\], which has three arguments given, will leave all "!ARG5" in EXAMPLE_CV intact as "!ARG5", but "!ARG10" will become "one0".

The pipe character "\|" is turned into ":" when inserted, so single arguments in APPLY_CREATURE_VARIATION may be turned into multi-argument segments in the output. E.g. given

`[CREATURE_VARIATION:DIMORPHIC_FEATHER_COLORS]`\
`   [CV_NEW_``TAG:SELECT_CASTE:FEMALE``]`\
`       [CV_NEW_``TAG:SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER``]`\
`           [CV_NEW_``TAG:TL_COLOR_MODIFIER``:!ARG1]`\
`               [CV_NEW_``TAG:TLCM_NOUN:feathers:PLURAL``]`\
`   [CV_NEW_``TAG:SELECT_CASTE:MALE``]`\
`       [CV_NEW_``TAG:SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER``]`\
`           [CV_NEW_``TAG:TL_COLOR_MODIFIER``:!ARG2]`\
`               [CV_NEW_``TAG:TLCM_NOUN:feathers:PLURAL``]`\
`   [CV_NEW_``TAG:SELECT_CASTE:ALL``]`

and \[APPLY_CREATURE_VARIATION:DIMORPHIC_FEATHER_COLORS:BROWN\|1:BLUE\|10\|GREEN\|1\|BLACK\|1\] we get

`[SELECT_CASTE:FEMALE]`\
`   [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]`\
`       [TL_COLOR_MODIFIER:BROWN:1]`\
`           [TLCM_NOUN:feathers:PLURAL]`\
`[SELECT_CASTE:MALE]`\
`   [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]`\
`       [TL_COLOR_MODIFIER:BLUE:10:GREEN:1:BLACK:1]`\
`           [TLCM_NOUN:feathers:PLURAL]`\
`[SELECT_CASTE:ALL]`

as the tokens added to the target creature.

The conditional tags (/, and ) are copies of CV_NEW_TAG/CV_ADD_TAG, CV_REMOVE_TAG and CV_CONVERT_TAG, except they only work if a numbered argument of APPLY_CREATURE_VARIATION has an arbitrary value. E.g. \[CV_ADD_CTAG:2:HUMANOID:CAN_SPEAK\] will only add \[CAN_SPEAK\] if argument number two is "HUMANOID".

¹Functionally. Up to 65537=2¹⁶+1 arguments have been tested, with no problems other than a long load time.

### Example

The following is an example of a creature variation, demonstrating most of the tokens and arguments mentioned above; with an explanation of how you would use it to change the properties of a cow.

`[CREATURE_VARIATION:CREATURE_EDIT]`\
`    [CV_CONVERT_CTAG:1:NAME]`\
`        [CVCT_MASTER:NAME]`\
`        [CVCT_TARGET:!ARG3:!ARG3s:!ARG4]`\
`        [CVCT_REPLACEMENT:!ARG5:!ARG5s:!ARG6]`\
`    [CV_CONVERT_CTAG:2:CNAME]`\
`        [CVCT_MASTER:CASTE_NAME]`\
`        [CVCT_TARGET:!ARG3:!ARG3s:!ARG4]`\
`        [CVCT_REPLACEMENT:!ARG5:!ARG5s:!ARG6]`\
`    [CV_NEW_CTAG:7:FC:SELECT_CASTE:FEMALE]`\
`    [CV_NEW_CTAG:7:FC:COLOR:!ARG8]`\
`    [CV_CONVERT_TAG]`\
`        [CVCT_MASTER:STATE_NAME:LIQUID]`\
`        [CVCT_TARGET:!ARG3's milk]`\
`        [CVCT_REPLACEMENT:!ARG5's milk]`\
`    [CV_CONVERT_TAG]`\
`        [CVCT_MASTER:STATE_ADJ:LIQUID]`\
`        [CVCT_TARGET:!ARG3's milk]`\
`        [CVCT_REPLACEMENT:!ARG5's milk]`\
`    [CV_NEW_CTAG:9:MRED:SELECT_CASTE:MALE]`\
`    [CV_NEW_CTAG:9:MREL:CASTE_COLOR:4:0:0]`\
`    [CV_NEW_CTAG:9:MYEL:SELECT_CASTE:MALE]`\
`    [CV_NEW_CTAG:9:MYEL:CASTE_COLOR:6:0:1]`

We add the following to a creature file.

`    [SELECT_CREATURE:COW]`\
`        [APPLY_CREATURE_VARIATION:CREATURE_EDIT:X:CNAME:cow:bovine:super-cow:cowtastic:FC:7|0|1:MYEL]`

This will change the cow creature file so that the cows are now called "super-cows", which can be described as "cowtastic", are white colored and produce "super-cow's milk", and it will also change the color of the bulls to yellow.

Here is a step-by-step explanation of what is happening in order of the arguments:

- "X" doesn't match the first CTAG argument of "NAME", so we have decided not to change the overall name of the creature.
- "CNAME" does match the second CTAG so we are changing the name of a caste which matches arguments !ARG3 & !ARG4, as well as looking for specific liquids with state names that contain !ARG3 followed by the characters "'s milk".
- Using arguments 3 & 4 we look for a caste name that matches "cow:cows:bovine" and any liquid name or adjective that matches "cow's milk".
- The caste name and liquids do exist, so !ARG5 & !ARG6 now declare what we want to change these names to; in this case the caste name "super-cow:super-cows:cowtastic" and liquid name and adjective "super-cow's milk".
- Now we declare that we want CTAG argument 7 to match "FC" which means we will select the \[FEMALE\] caste and add a color to it which is decided by the next argument !ARG8.
- We need to choose three digits but they need to be separated by ":". Using this character here will move us onto the next argument, so we separate the digits with "\|" instead choosing "7\|0\|1" (white), for a white cow (not necessarily represented by the graphics).
- The next argument has multiple CTAGs numbered "9", but with different arguments. Either option will use \[SELECT_CASTE:MALE\] but we can choose between the argument MRED or MYEL. We have chosen MYEL which adds the tag \[CASTE_COLOR:6:0:1\] (yellow) for us, giving the male caste (in this case a bull) yellow as a caste color.

## See Also

- Creature token
- Tissue definition token
- Material definition token
- Body detail plan token
