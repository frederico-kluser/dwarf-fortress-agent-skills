# Creature token (parte 3/3)

|  UNDERGROUND_DEPTH | Creature | mindepth / maxdepth | Depth that the creature appears underground. Numbers can be from 0 to 5. 0 is actually 'above ground' and can be used if the creature is to appear both above and below ground. Values from 1-3 are the respective cavern levels, 4 is the magma sea and 5 is the HFS. A single argument may be used instead of min and max. Demons use only 5:5; user-defined creatures with both this depth and [`[FLIER]`](/index.php/Creature_token#FLIER "Creature token") will take part in the initial wave from the HFS alongside generated demons, but without [`[FLIER]`](/index.php/Creature_token#FLIER "Creature token") they will only spawn from the map edges. Civilizations that can use underground plants or animals will only export (via the embark screen or caravans) things that are available at depth 1. |
|  UNDERSWIM | Caste |  | The creature is displayed as blue when in 7/7 water. Used on fish and amphibious creatures which swim under the water. |
|  UNIQUE_DEMON | Caste |  | Found on generated demons; causes the game to create a single named instance of the demon which will emerge from the underworld and take over civilizations during worldgen. |
|  USE_CASTE | Creature | new caste token / old caste token | Defines a new caste derived directly from a previous caste. The new caste inherits all properties of the old one. The effect of this tag is automatic if one has not yet defined any castes: "Any caste-level tag that occurs before castes are explicitly declared is saved up and placed on any caste that is declared later, unless the caste is explicitly derived from another caste." / Roostre: "When DF detects duplicate tokens in the raws of the same object, a failsafe seems to kick in; it takes the bottom-most of the duplicates, and disregards the others. In the case of tokens added by a mod, it prioritizes the duplicate in the mod." This means that if a tag is defined in the base-caste and redefined in the derived caste, the derived tag overwrites the base tag. |
|  USE_MATERIAL | Creature | new material ID / old material ID | Defines a new local creature material and populates it with all properties defined in the specified local creature material. A maximum of 200 materials can be defined on any given creature. |
|  USE_MATERIAL_TEMPLATE | Creature | new material token / material template | Defines a new local creature material and populates it with all properties defined in the specified template. A maximum of 200 materials can be defined on any given creature. |
|  USE_TISSUE | Creature | new tissue token / old tissue id | Defines a new local creature tissue and populates it with all properties defined in the local tissue specified in the second argument. |
|  USE_TISSUE_TEMPLATE | Creature | new tissue token / tissue template | Loads a tissue template listed in OBJECT:TISSUE_TEMPLATE files, such as tissue_template_default.txt. |
|  UTTERANCES | Creature |  | Changes the language of the creature into unintelligible 'kobold-speak', which creatures of other species will be unable to understand. If a civilized creature has this and is not part of a [`[SKULKING]`](/index.php/Entity_token#SKULKING "Entity token") civ, it will tend to start wars with all nearby civilizations and will be unable to make peace treaties due to 'inability to communicate'. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## V

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  VEGETATION | Caste |  | Like [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Creature_token#AT_PEACE_WITH_WILDLIFE "Creature token"), but also makes the creature more valued in artwork by civilisations with the PLANT sphere. [5] Used by grimelings in the vanilla game. |
|  VERMIN_BITE | Caste | chance of occurrence / \[ / Verify / \] / verb (bitten, stung, etc.) / material token / material state | Enables vermin to bite other creatures, injecting the specified material. See [`[SPECIALATTACK_INJECT_EXTRACT]`](/index.php/Creature_token#SPECIALATTACK_INJECT_EXTRACT "Creature token") for details about injection - this token presumably works in a similar manner.\[Verify\] |
|  VERMIN_EATER | Creature |  | The vermin creature will attempt to eat exposed food. See [`[PENETRATEPOWER]`](/index.php/Creature_token#PENETRATEPOWER "Creature token"). Distinct from [`[VERMIN_ROTTER]`](/index.php/Creature_token#VERMIN_ROTTER "Creature token"). |
|  VERMIN_FISH | Creature |  | The vermin appears in water and will attempt to swim around. Required to catch the vermin with fishing or capturing a live fish. |
|  VERMIN_GROUNDER | Creature |  | The creature appears in "general" surface ground locations. Note that this doesn't stop the creature from flying if it can (most vermin birds have this tag). |
|  VERMIN_HATEABLE | Caste |  | Some dwarves will hate the creature and get unhappy thoughts when around it. See the list of hateable vermin for details. |
|  VERMIN_MICRO | Caste |  | This makes the creature move in a swarm of creatures of the same race as it (e.g. swarm of flies, swarm of ants). |
|  VERMIN_NOFISH | Caste |  | The creature cannot be caught by fishing. |
|  VERMIN_NOROAM | Caste |  | The creature will not be observed randomly roaming about the map. |
|  VERMIN_NOTRAP | Caste |  | The creature cannot be caught in baited animal traps; however, a "catch live land animal" task may still be able to capture one if a dwarf finds one roaming around. |
|  VERMIN_ROTTER | Creature |  | The vermin are attracted to rotting stuff and loose food left in the open and cause unhappy thoughts to dwarves who encounter them. Present on flies, knuckle worms, acorn flies, and blood gnats. |
|  VERMIN_SOIL | Creature |  | The creature randomly appears near dirt or mud, and may be uncovered by creatures that have the [`[ROOT_AROUND]`](/index.php/Creature_token#ROOT_AROUND "Creature token") interaction such as geese and chickens. Dwarves will ignore the creature when given the "Capture live land animal" task. |
|  VERMIN_SOIL_COLONY | Creature |  | The vermin will appear in a single tile cluster of many vermin, such as a colony of ants. |
|  VERMINHUNTER | Caste |  | Old shorthand for "does cat stuff". Contains [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Creature_token#AT_PEACE_WITH_WILDLIFE "Creature token") + [`[RETURNS_VERMIN_KILLS_TO_OWNER]`](/index.php/Creature_token#RETURNS_VERMIN_KILLS_TO_OWNER "Creature token") + [`[HUNTS_VERMIN]`](/index.php/Creature_token#HUNTS_VERMIN "Creature token") + [`[ADOPTS_OWNER]`](/index.php/Creature_token#ADOPTS_OWNER "Creature token"). |
|  VESPERTINE | Caste |  | When set, the creature will only appear in the evening (between 8:00 PM and 10:05 PM) in Adventurer mode. |
|  VIEWRANGE | Caste | value | Value should determine how close you have to get to a critter before it attacks (or prevents adv mode travel etc.) Default is 20. |
|  VISION_ARC | Caste | binocular vision arc / non-binocular vision arc | The width of the creature's vision arcs, in degrees (i.e. 0 to 360). The first number is binocular vision, the second is non-binocular vision. Binocular vision has a minimum of about 10 degrees, monocular, a maximum of about 350 degrees. Values past these limits will be accepted, but will default to ~10 degrees and ~350 degrees respectively. Defaults are 60:120. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## W

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  WAGON_PULLER | Caste |  | Allows the creature to pull caravan wagons. If a civilization doesn't have access to any, it is restricted to trading with pack animals. |
|  WEBBER | Caste | material token | Allows the creature to create webs, and defines what the webs are made of. |
|  WEBIMMUNE | Caste |  | The creature will not get caught in thick webs. Used by creatures who can shoot thick webs (such as giant cave spiders) in order to make them immune to their own attacks. |

## Attack Tokens

Attacks can use four different part selection criteria. Except for TISSUE_LAYER, the base game makes use of all of these in its attacks.

|  |  |  |
|----|----|----|
| Part type token | Arguments | Description |
|  BODYPART | BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category | This attack uses a particular body part; for example, ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP will make it use any part that can hold onto an object. |
|  TISSUE_LAYER | BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category / tissue layer | This attack uses a specific tissue layer on a specific body part; ATTACK:SCRATCH:TISSUE_LAYER:BY_TYPE:GRASP:BONE will make it use the bone of the hands. |
|  CHILD_BODYPART_GROUP | BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category / BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category | Uses a body part that is subordinate to another; ATTACK:SLAP:CHILD_BODYPART_GROUP:BY_CATEGORY:ARM_LOWER:BY_TYPE:GRASP will make it use every hand attached to each lower arm (so it will generate one attack per lower arm, each of which will use every hand on that arm, assuming there are multiple hands per arm). |
|  CHILD_TISSUE_LAYER_GROUP | BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category / BY_TYPE / BY_TOKEN / BY_CATEGORY / type / token / category / tissue layer | As CHILD_BODYPART_GROUP, but specifying a tissue, too; ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH |

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  ATTACK_SKILL | Caste | Skill token | Defines the skill used by the attack. |
|  ATTACK_VERB | Caste | 2nd person / 3rd person | Descriptive text for the attack. |
|  ATTACK_CONTACT_PERC | Caste | % value | The contact area of the attack, measured in % of the body part's volume. Note that all attack percentages can be more than 100%. |
|  ATTACK_PENETRATION_PERC | Caste | % value | The penetration value of the attack, measured in % of the body part's volume. Requires ATTACK_FLAG_EDGE. Maximum value: 15000. |
|  ATTACK_PRIORITY | Caste | MAIN or SECOND | Usage frequency. MAIN attacks are 100 times more frequently chosen than SECOND. Opportunity attacks ignore this preference. |
|  ATTACK_VELOCITY_MODIFIER | Caste | number | The velocity multiplier of the attack, multiplied by 1000. |
|  ATTACK_FLAG_CANLATCH | Caste |  | Attacks that damage tissue have the chance to latch on in a wrestling hold. The grabbing bodypart can then use the "shake around" wrestling move, causing severe, armor-bypassing tensile damage according to the attacker's body volume. |
|  ATTACK_FLAG_WITH | Caste |  | Displays the name of the body part used to perform an attack while announcing it, e.g. "The weaver punches the bugbat with his right hand". |
|  ATTACK_FLAG_EDGE | Caste |  | The attack is edged, with all the effects on physical resistance and contact area that it entails. |
|  ATTACK_PREPARE_AND_RECOVER | Caste | Preparation time / Recovery time | Determines the length of time to prepare this attack and until one can perform this attack again. Values appear to be calculated in adventure mode ticks. |
|  ATTACK_FLAG_BAD_MULTIATTACK | Caste |  | Multiple strikes with this attack cannot be performed effectively. |
|  ATTACK_FLAG_INDEPENDENT_MULTIATTACK | Caste |  | Multiple strikes with this attack can be performed with no penalty. The creature will use all attacks with this token at once. |
|  SPECIALATTACK_INJECT_EXTRACT | Caste | \ / \ | When added to an attack, causes the attack to inject the specified material into the victim's bloodstream. Once injected, the material will participate in thermal exchange within the creature - injecting something like molten iron (INORGANIC:IRON:LIQUID) would cause most unmodded creatures to melt (note that some of the injected material also splatters over the bodypart used to carry out the attack, so it should be protected appropriately). If the injected material has an associated syndrome with the [\[SYN_INJECTED\]](/index.php/Syndrome#SYN_INJECTED "Syndrome") token, it will be transmitted to the victim. If the attack is blunt, the injected material lacks the [\[ENTERS_BLOOD\]](/index.php/Material_definition_token#ENTERS_BLOOD "Material definition token") token, the attacked bodypart has no [\[VASCULAR\]](/index.php/Tissue_definition_token#VASCULAR "Tissue definition token") tissues, or the victim is bloodless, the material will splatter over the attacked body part instead. |
|  SPECIALATTACK_INTERACTION | Caste | interaction | When this attack lands successfully, a specified interaction will take effect on the target creature. The attack must break the target creature's skin in order to work. This will take effect in worldgen as well. If the attack would break skin, the interaction will occur **before the attack actually lands**. |
|  SPECIALATTACK_SUCK_BLOOD | Caste | min / max | Successful attack draws out an amount of blood randomized between the min and max value. Beware that this **will** trigger any ingestion syndromes attached to the target creature's blood - for example, using this attack on a vampire will turn you into one too. |

## Tissue Layer Tokens

Tissue layers are added to a creature's body parts by the creature tokens TISSUE_LAYER, TISSUE_LAYER_OVER, TISSUE_LAYER_UNDER, and the body detail plan token TL_LAYERS.

These tissue layers are not the same thing as tissues, which are defined at creature level, but rather applications of the tissues. If the SKIN tissue of a creature is the more general and abstract notion of what skin is for that creature, then a tissue layer may be the "actual" skin on the creature's nose, head, or second toe. As most creatures have more than one body part, tissue layers are normally selected en masse.

Some tissue layer tokens are analogous to tissue definition tokens, e.g. TL_CONNECTS to CONNECTS.

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  SELECT_TISSUE_LAYER | Caste | TISSUE / BY_CATEGORY, BY_TYPE, BY_TOKEN / Location - category, type, or token \| Selects a tissue at a location / (optional) FRONT, BACK, LEFT, RIGHT, TOP, BOTTOM, AROUND. | Begins a selection of tissue layers. / \[SELECT_TISSUE_LAYER:HEART:BY_TYPE:HEART\] |
|  PLUS_TISSUE_LAYER | Caste | TISSUE / BY_CATEGORY, BY_TYPE, BY_TOKEN / Location - category, type, or token | Adds tissue layers to those selected. |
|  SET_TL_GROUP | Caste | TISSUE / BY_CATEGORY, BY_TYPE, BY_TOKEN / Location - category, type, or token / tissue | Begins a selection of tissue layers. Only usable for descriptor and cosmetic purposes. / Research has implied it may be redundant with SELECT_TISSUE_LAYER, as the latter allows for cosmetics as well as "functional" tokens such as TL_MAJOR_ARTERIES. Vanilla raws still use SET_TL_GROUP though, for all cosmetic purposes. More research is needed on this subject. |
|  PLUS_TL_GROUP | Caste | BY_CATEGORY, BY_TYPE, BY_TOKEN / Location - category, type, or token / tissue | Adds tissue layers to those selected. Like SET_TL_GROUP, it may be redundant even if used in the vanilla raws. |
|  SET_LAYER_TISSUE | Caste | TISSUE | Sets a selected tissue layer to be made of a different tissue. |
|  SHEARABLE_TISSUE_LAYER | Caste | tissue modifier / required value | Tissue layer can be sheared for its component material. The specified modifier must be at least of the desired value for shearing to be possible (for example, a llama's wool must have a LENGTH of 300 before it is shearable). |
|  TISSUE_LAYER_APPEARANCE_MODIFIER | Caste | QUALITY / lowest / lower / low / median / high / higher / highest | Sets the range of qualities, including LENGTH, DENSE, HIGH_POSITION, CURLY, GREASY, WRINKLY |
|  TISSUE_STYLE_UNIT | Caste | tissue style unit ID / shaping | Sets tissue layer to be the target of TISSUE_STYLE token specified for an entity, works only on entity members. Mostly used with tissues HAIR, BEARD, MOUSTACHE, SIDEBURNS. |
|  TL_COLOR_MODIFIER | Caste | COLOR / freq / COLOR / freq etc. | Creates a list of colors/color patterns, giving each a relative frequency. If the given color or pattern does not exist, the tissue is described as being "transparent". |
|  TLCM_GENETIC_MODEL | Caste |  | The way the color modifier is passed on to offspring. May or may not work right now.\[Verify\] |
|  TLCM_IMPORTANCE | Caste | number | Presumably modifies the importance of the tissue layer color modifier, for description purposes. / HOWEVER using this appears to remove all mention of colour from creature descriptions. It does not appear in any default creatures. |
|  TLCM_NOUN | Caste | name / SINGULAR or PLURAL | Names the tissue layer color modifier, and determines the noun. Also used by Stonesense for colouring body parts. |
|  TLCM_TIMING | Caste | ROOT / start change window years / days / end change window years / days | Determines the point in the creature's life when the color change begins and ends. |
|  TL_CONNECTS | Caste |  | Gives the CONNECTS attribute to selected layers. |
|  TL_HEALING_RATE | Caste | value | Changes the HEALING_RATE of the selected tissue layers. |
|  TL_MAJOR_ARTERIES | Caste |  | Gives the "major arteries" attribute to selected layers. Used to add massive bleeding properties to the throat, made from skin. |
|  TL_PAIN_RECEPTORS | Caste | value | Changes the number of pain receptors for selected tissue layers. |
|  TL_RELATIVE_THICKNESS | Caste | value | Changes the relative thickness for selected tissue layers. |
|  TL_VASCULAR | Caste | value | Sets a new VASCULAR value (which modulates bleeding) for selected tissue layers. |

## See Also

- Body detail plan token
- Body token
- Material definition token
- Syndrome
- Tissue definition token
- Creature examples


---
*Parte 3 de 3 de «Creature token». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Creature_token*
