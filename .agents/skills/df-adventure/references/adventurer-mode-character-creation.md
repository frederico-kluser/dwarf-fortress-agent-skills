# Adventurer mode character creation

> Fonte: [Adventurer mode character creation](https://dwarffortresswiki.org/index.php/Adventurer_mode_character_creation) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\
**Main menu:** Adventure mode; Gameplay; FAQ

With the addition of adventuring parties, you can now have multiple adventurers - to add another adventurer, press N on the (Mounts and pets) page, when creating the current one.

## Race and civilization

Race selection menu

Civilization selection menu

Any race from an [`[ALL_MAIN_POPS_CONTROLLABLE]`](/index.php/Entity_token#ALL_MAIN_POPS_CONTROLLABLE "Entity token") civilization is playable in adventure mode. In most standard games, this includes dwarves, elves, and humans - all three races can complete the same quests. If an `[ALL_MAIN_POPS_CONTROLLABLE]` civilization never existed in the world, however, adventure mode cannot be played.

- **Dwarves** have the advantage of being able to go into a martial trance when fighting multiple foes at once, giving them many combat bonuses, which aids their survival greatly. They are the only race that can start with steel weapons, but they wear "small"-sized clothing which means that they're unable to wear human clothes and armor. Goblin armor fits them, making dark fortresses (if your computer can handle them) and dark pits a viable source of armor; if you're up for it, you could also just rob some dwarves or a dwarven fortress. They can start with almost the same weapon skills as civilized humans. Many larger weapons must be wielded two-handed by dwarves, due to their size.
- **Elves** start with very weak wooden weapons, and have a more limited list of weapon skills during character creation. They have the advantage that they have higher natural speed. Elves are [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Entity_token#AT_PEACE_WITH_WILDLIFE "Entity token"), which makes all wildlife passive towards them. They also have a notably better sense of smell compared to the other races with a [`[SMELL_TRIGGER]`](/index.php/Creature_token#SMELL_TRIGGER "Creature token") of 10 instead of 90, which means they can sense smells over much larger distances. Like dwarves, they wear small-sized clothing.
- **Humans** begin with bronze, copper, or iron weapons, and the widest variety of weapon skills. Humans are larger than the other main races, meaning armor from other civilizations is too small to be worn. Human-sized clothes and armor are commonly found in hamlets and towns.
- **Goblins** are only playable when a goblin population is present in an `[ALL_MAIN_POPS_CONTROLLABLE]` civilization. They possess the same body size as dwarves and elves, and can wear whatever weapons and armor the civilization which adopted/conquered them allows. They require no food or water to live.
- **Kobolds** are playable by modding. They are very weak in combat, and a huge challenge compared to other races - even smaller than the other main races, and it is next-to-impossible to find properly-fitting armor for them, unless you are absurdly lucky and run into armored kobolds.\[Verify\]
- **Intelligent Wilderness Creatures** are playable wild animals - any creature with [`[LOCAL_POPS_CONTROLLABLE]`](/index.php/Creature_token#LOCAL_POPS_CONTROLLABLE "Creature token") fits into this category. A wilderness creature can be played as long as a particular population of them exists in an `[ALL_MAIN_POPS_CONTROLLABLE]` civilization. Most wilderness creatures are animal people - they come in various sizes, shapes and abilities, and as such, a short description cannot be given. You can choose the items you start with, including armor, but animal people still have the problem of finding appropriate armor during gameplay, making Dodger and Shield User more important as defensive skills. Some useful features will be copied from the species to your character, such as the ability to fly, a poisonous bite, extravision, large size, various immunities (e.g. pain, stunning, exertion, traps, fear, dizziness, fevers, fire, poison, or drowning), special abilities (e.g. shooting webs, hurling fireballs), intrinsic starting skills, or the absence of vulnerable internal organs. Some features can also be uselessly amusing (e.g. snakemen talk with a [`[LISP]`](/index.php/Creature_token#LISP "Creature token")) or more crippling: plump helmet men can't talk, and characters from a [`[MEANDERER]`](/index.php/Creature_token#MEANDERER "Creature token") species stroll very slowly in lieu of normal movement. Here you can read more.

### Outsider

Outsiders are adventurers that aren't from a civilization - they can begin at any site and are strangers to all. Only humans can currently be outsiders in vanilla by default - other races can be played as outsiders if [`[OUTSIDER_CONTROLLABLE]`](/index.php/Creature_token#OUTSIDER_CONTROLLABLE "Creature token") is added to the creature's raws. At least one `[ALL_MAIN_POPS_CONTROLLABLE]` civilization must have existed in the world in order to play as an outsider, though the civilization does not need to be alive. A human (or in this case, dwarven) civilization is not strictly required.

The game will always try to start Outsiders in a populated site - caves, and even lairs with megabeasts, will be chosen when there are no occupied civ sites. When starting from a lair, be sure to escape from the site **immediately**, as soon as the game starts, to avoid an instant death.

Playing as an outsider has many initial limitations - they possess no pre-existing relationships or knowledge of various events and wildlife. Also, because they lack a cultural identity or (supposedly) knowledge of laws, outsiders cannot worship deities, name items, or claim sites, and are unable to perform dance, music, or poetry due to having no held art forms. When selecting skills for outsiders during creation, many more skills may be available than would otherwise be, if they were part of a civilization.

An outsider may become a member of a civilization: retire your outsider in a civilized area, causing them to be "reformed" the next time you unretire the character. You can also join a civ if you can get a site leader to accept you as a hearthperson (or maybe, entertainer). You can make people like you by giving them gifts, especially named gifts. E.g.: carve some bones into trinkets, name them, give them to some lord or lady, then ask them to make you a hearthperson.

## Status

Determines the number of starting skill, attribute points, and equipment points which do not change based on race:

- **Peasant:** 15 attribute, 35 skill, 55 equipment
- **Hero:** 35 attribute, 95 skill, 255 equipment
- **Demigod:** 105 attribute, 161 skill, 1255 equipment

The number of skill points is less significant than the number of attribute points, because the time it takes to go from Peasant to Demigod in skill terms is much less than what it would take to go from Peasant to Demigod in attribute terms.

## Background

Home, occupation and beliefs choosing menu

You can choose the town you start at, your occupation (affects skills) and religious beliefs, if any.

### Home

This decides where you start the game at, and what local government you initially belong to. Generally, this is not very important, as you can always make your way to "better" sites later, but there are advantages and disadvantages to certain site types. For example, mountain halls and fortresses can prove difficult to get out of, so they are not recommended to the new player. When creating multiple adventurers, party members can start at different sites (and even from different civilizations). The last screen of party creation has an option to choose which of their homes the party starts at.

The available site types depend on civilization type (e.g. dwarven, human or elven), but, all in all, there are: hamlet, town, castle, fort, hillock, fortress, mountain halls, forest retreat, camp.

This also affects your "childhood friends" (what people your adventurers already know by the start of the game). If you start in an important (well-populated) site, your friends may very well encompass royalty or semi-important priests.

Note: As you have already selected a civilization in the previous screen, all sites you will be able to choose from will be of that civilization, and that civilization only. If you want other sites to choose from, you have to go back.

### Occupation

The occupation selection might seem glamorous, but most of the occupations are presently only there for flavor - they do grant skills, however most of these are not currently usable in adventurer mode.

The available occupations are dependent on civilization, with elven civilizations having only a few of the occupations available to humans and dwarves. Outsiders can't choose any occupation at all.

Notable occupations are **hearthperson**, **fortress guard**, and **soldier**, which grant you a position as the vassal of a local noble (lord/lady, captain of the guard or mercenary/bandit leader) instead of any skills. The **Hunter** occupation also has several skills usable in adventurer mode.

The level of skill granted is dependent on your adventurer status (peasant, hero, or demigod), with the greater statuses getting more skill levels. For this reason, the list below doesn't include any set skill levels, instead using the terms "Low-level", "Mid-level" and "High-level". To see what those correspond to, see the table below.

|         |           |            |              |
|---------|-----------|------------|--------------|
| Status  | Low-level | Mid-level  | High-level   |
| Peasant | Novice    | Competent  | Talented     |
| Hero    | Adequate  | Proficient | Professional |
| Demigod | Competent | Adept      | Master       |

Occupations and skills:

- **Hearthperson**, **Fortress Guard** or **Soldier**: None, see above.
- **Miner**: Mid-level miner (Potentially useful, since miner is the combat skill for picks)
- **Woodworker**: Mid-level carpenter, wood cutter and bowyer
- **Carpenter**: High-level carpenter
- **Bowyer**: High-level bowyer
- **Woodcutter**: High-level wood cutter
- **Stoneworker**: Mid-level mason and engraver
- **Engraver**: Mid-level engraver
- **Mason**: Mid-level mason
- **Ranger**: Mid-level ambusher, animal trainer, animal caretaker, animal dissector and Trapper; Low-level marksdwarf and dodger
- **Animal Caretaker**: High-level animal caretaker
- **Animal Trainer**: High-level animal trainer
- **Hunter**: High-level ambusher; Skilled marksdwarf and dodger
- **Trapper**: High-level trapper
- **Animal Dissector**: High-level animal dissector
- **Metalsmith**: Mid-level weaponsmith, armorsmith, metalsmith, metal crafter and furnace operator
- **Furnace Operator**: High-level furnace operator
- **Weaponsmith**: High-level weaponsmith
- **Armorer**: High-level armorsmith
- **Blacksmith**: High-level blacksmith
- **Metal Crafter**: High-level metal crafter
- **Jeweler**: Mid-level gem setter and gem cutter
- **Gem Cutter**: High-level gem cutter
- **Gem Setter**: High-level gem setter
- **Craftsdwarf**: Mid-level bone carver, glassmaker, weaver, stone crafter, wood crafter, potter, wax worker, glazer, leatherworker, clothier, papermaker and bookbinder
- **Woodcrafter**: High-level wood crafter
- **Stonecrafter**: High-level stone crafter
- **Leatherworker**: High-level leatherworker
- **Bone Carver**: High-level bone carver
- **Weaver**: High-level weaver
- **Clothier**: High-level clothier
- **Glassmaker**: High-level glassmaker
- **Potter**: High-level potter
- **Glazer**: High-level glazer
- **Wax Worker**: High-level wax worker
- **Strand Extractor**: High-level strand extractor
- **Fishery Worker**: Mid-level fisherman, fish dissector and fish cleaner
- **Fisherman**: High-level fisherman
- **Fish Dissector**: High-level fish dissector
- **Fish Cleaner**: High-level fish cleaner
- **Farmer**: Mid-level butcher, grower, milker, gelder, shearer, spinner, cheese maker, tanner, dyer, herbalist, brewer, thresher, cook, miller, presser and beekeeper
- **Cheese Maker**: High-level cheese maker
- **Milker**: High-level milker
- **Cook**: High-level cook
- **Thresher**: High-level thresher
- **Miller**: High-level miller
- **Butcher**: High-level butcher
- **Tanner**: High-level tanner
- **Dyer**: High-level dyer
- **Planter**: High-level grower
- **Herbalist**: High-level herbalist
- **Brewer**: High-level brewer
- **Soap Maker**: High-level soaper
- **Potash Maker**: High-level potash maker
- **Lye Maker**: High-level lye maker
- **Wood Burner**: High-level wood burner
- **Shearer**: High-level shearer
- **Spinner**: High-level spinner
- **Presser**: High-level presser
- **Beekeeper**: High-level beekeeper
- **Engineer**: Mid-level mechanic, pump operator, siege engineer, siege operator, optics engineer, fluid engineer and student; Low-level reader, wordsmith and writer
- **Mechanic**: High-level mechanic
- **Siege Engineer**: High-level siege engineer
- **Siege Operator**: High-level siege operator
- **Pump Operator**: High-level pump operator
- **Clerk**: Mid-level record keeper
- **Administrator**: Mid-level organizer
- **Trader**: Mid-level appraiser
- **Architect**: Mid-level building designer
- **Doctor**: Mid-level diagnostician, surgeon, bone doctor and suturer; Low-level reader, wordsmith, writer and wound dresser
- **Diagnoser**: High-level diagnostician; Mid-level(-1) wound dresser
- **Bone Doctor**: High-level bone doctor; Mid-level(-1) wound dresser
- **Suturer**: High-level suturer; Mid-level(-1) wound dresser
- **Surgeon**: High-level surgeon; Mid-level(-1) wound dresser
- **Gelder**: High-level gelder
- **Papermaker**: High-level papermaker
- **Bookbinder**: High-level bookbinder

### Belief

This decides what deity or religion you put your faith in. You may also be atheist/have no faith, and sometimes this is the only option given to you. With w and q you control how ardent your faith is. The stronger your faith, the more likely you will get the need to Pray to your deity.

## Starting attributes

Attributes and skills choosing menu

Attributes are divided into Body and Soul attributes. This section provides some guidance for allocating attributes as it relates to adventurer mode.

### Body

- **Strength**: Contributes to melee attack momentum, adding velocity and force, and leg strength to movement velocity. Strength determines encumbrance limits, and higher capacity reduces the speed penalty of carrying burdens. Increases to muscle layer mass proportionately improves damage resistance but also reduces speed; proportionately larger characters benefit more from the extra layer thickness and suffer more from the speed penalty.
- **Agility**: This attribute is directly related to a character's Speed. All combat skills, especially defensive ones, rely on it. Increases attack velocity and potential attack rate.
- **Toughness**: Reduces physical damage inflicted on you. Also relates to defensive combat skills.
- **Endurance**: Reduces the rate at which the adventurer becomes exhausted. Exhaustion progressively penalizes physical skills and rate of movement to the point of immobility and unconsciousness.
- **Recuperation**: Increases the rate of wound healing.
- **Disease Resistance**: Reduces risk of contracting syndromes (including infection) and the negative effects when active (including alcohol-induced.)

### Soul

Some of these are demonstrably useful for adventure-mode-applicable skills, but the effects of the attributes aren't clearly understood. For ideas on how they may be applied, see a list of skills organized by attributes..

- **Analytical Ability**: Useful for Tracker, Knapping and Student. Analytical Ability seems to have an influence on the quality of written creations, such as poems, as well as ability to speak about ideals.
- **Focus**: Affects Archer, Ambusher, Observer.
- **Willpower**: Affects Fighter, Crutch Walker and Swimmer. Willpower helps resist the negative effects of status ailments such as Pain, Stunned, Unconscious, and all states of exhaustion and food/drink/sleep deprivation.
- **Creativity**: This influences quality of poems, songs, dances and crafts. It may also influence "make believe", now able to be performed by children.
- **Intuition**: Helps with Observer, which aids in spotting concealed enemies, ambushes, and identifying attacks from opponents.
- **Patience**: May have some effect on dealings with others as a result of the new conversation system.\[Verify\]
- **Memory**: Memory is applied to the Student and Reading skills. Higher Student skill improves the ability to learn from demonstrations in fortress mode, but it isn't certain whether it has any application in adventurer mode. It's also unknown what benefits come from higher Reading capability.
- **Linguistic Ability**: Affects any speaking and writing ability, improves the ability to communicate thoughts and feelings to listeners/readers. Verbal ability can form a positive impression depending on how the listener values eloquence, and responses to stories and poetry relies on delivery.
- **Spatial Sense**: Important. Affects combat skills, Ambusher, Crutch Walker, Swimmer, Observer, Knapping. Also, prevents/reduces the chance of stumbling during a dance.
- **Musicality**: Influences the adventurer's ability to perform music and song well. This, so far, works for all instruments; one can play a flute, guitar, or any other instrument equally well, given that the adventurer has equal skills in all instrument fields.
- **Kinesthetic Sense**: Affects most combat skills, walking with crutches, swimming and dancing.
- **Empathy**: Affects social skills such as Persuader, Flatterer, Judge of Intent, and other Social skills that may not be applied in adventurer mode.
- **Social Awareness**: Increases the number of followers you can have at a given fame level. Normally, you start with a limit of two. Increasing this stat by one level raises that to three, etc. Your fame still plays a big part in whether you can recruit followers or not. This attribute also helps with Persuader and Judge of Intent.

### Attribute advancement cap

Adventure mode attributes are capped at double starting value, or starting value plus the racial average, whichever is greater. Humans, for example, have a racial average strength of 1,000. If a human adventurer started with an *above average* strength of 1,100, then their strength would ultimately be capped at 2,200. Had this human started with a *below average* strength of 900, then their strength would be capped at 1,900 instead. For the purpose of maximizing final attributes, this makes it important to start with as many attributes in the *superior* range as possible (more attributes per point allocated), while avoiding taking any penalties to even remotely-important attributes (big attribute deductions per point recovered). As a consequence of the attribute cap, demigod adventurers will always have a much higher potential for advancement than mere peasants and heroes (unless you become a night creature, that is).

## Starting skills

Not all races have the same sets of skills available at character creation time, but keep in mind that (almost - an exception would seem to currently be Reader skill) all starting skills, as well as ones not available at character creation, can be improved through use in-game.

This section will specifically address starting skills as they relate to adventure mode. For a full description of combat skills see Combat skill. Other skills that you can't start with, but which can be increased in-game (such as Butchery) are described elsewhere.

### Weapon

Weapons may be chosen on the embark screen before starting an adventure. The weapons available to a given adventurer are decided in their civilization's entity raws: humans will be able to start with a whip, while the same will not be available to a dwarf, and so on. Outsiders will have a wide array of weapons to choose from, some of which may be made of non-weapon grade material.

Not all races/civilizations can start with all of the skills - dwarves can't start with Bowman, Pikeman, or Lasher, while elves can only use Swordsman, Bowman, and Spearman. Of the other playable races, only humans have access to Pikeman and Lasher. Strangely, only outsiders can start with Knife User.

Note that different races have different names for their weapon skills. Axegoblin, Axedwarf etc. These names are defined in the creature raws, as can be seen in the dwarf raws, but Crossbowman is an exception - dwarves call this skill Marksdwarf, although bow skill is referred to as Bowdwarf, as you'd expect. Elite Axe and Hammerdwarves are referred to as Lords.

- **Axeman**: allows characters to use axes, great axes, and halberds more effectively. Useful for cleaving off limbs.
- **Bowman**: skill allows characters to use bows more effectively. Useful for taking down enemies at a distance.
- **Crossbowman**: allows characters to use crossbows more effectively. Useful for taking down enemies at a distance.
- **Hammerman**: allows characters to use crossbows, mauls, and war hammers more effectively in melee. Useful for breaking limbs.
- **Knife user**: allows characters to use large daggers and knives more effectively. Useful for stabbing things.
- **Lasher**: allows characters to use whips and scourges more effectively. Very deadly weapons.
- **Maceman**: allows characters to use flails, maces, and morningstars more effectively. Similar to hammers.
- **Pikeman**: allows characters to use pikes more effectively - like spears, but much bigger.
- **Spearman**: allows characters to use spears more effectively. Useful for stabbing things.
- **Swordsman**: allows characters to use blowguns and bows in melee, long swords, scimitars, short swords, and two-handed swords more effectively. Useful for cutting, stabbing, and whacking, but less effective than more dedicated weapons.

### General combat

These skills form the basis for combat effectiveness. There is no maximum value to their utility, so if you begin with a rank equal or higher to your chosen weapon you'll become better able to benefit from other weapons when necessity or strategic advantage requires. Starting versatility can pay off early; you may choose your starting weapon, but the *best* available weapon is beyond your control or prediction.

- **Fighter**: This increases with, and contributes to, melee combat, whether armed or unarmed. It appears that the purpose of it is to allow melee experience to contribute to melee combat in general regardless of weapon type. Repeatedly wrestling (grabbing and releasing) even a small creature will raise this skill.
- **Archer**: This increases with, and contributes to, ranged combat including throwing. It works similarly to Fighter except for ranged attacks. It can be easily raised by repeatedly throwing rocks, making it advisable for archers to practice their marksmanship with rock throwing before using up the more finite and expensive forms of ammunition. Shooting at a wall with adjacent upward ramp one level below and picking back projectiles is also a good idea (such places often happen to be in keeps and fortresses). See the FAQ section on increasing your skills and attributes for information on raising bowman/marksman skills.

### Defensive

These skills are critical for survival. Starting out with good ability in one (especially Shield User or Armor User) if not all is strongly advised.

- **Shield user**: Ability to block attacks with shields. Starting with even novice skill in this means that the adventurer will start with a shield. This is a no-brainer unless you're creating a two handed weapon user, and lack a broadness or height modifier on your character - necessary for one-handing any two-handed weapon, without penalty.
- **Armor user**: A higher level of this skill reduces the encumbrance penalties of armor, allowing you to move faster when wearing it. It also affects how well armor protects you, and this makes a huge difference. Unskilled armor users gain little protection. This is noticeable, as you'll begin seeing far more combat reports about hits either striking you though armor, (you managed to use your armor to lessen the force of the blow) or being deflected by your armor (you used your armor to avoid the hit entirely) as your skill rises, and you learn to actually use your armor to deflect hits. It is highly advised to train your armor skill before entering battle with it, as the speed penalties of lower levels can be a serious handicap.
- **Dodger**: Ability to dodge out of the way of attacks. Dodger is incredibly important and will allow you to avoid many, many hits that would have otherwise injured you. Especially important when you are fighting unarmored and can't afford a battle axe in the chest. Boost this to talented, or at least close to it.

### Unarmed combat and improvised weapons

While some of them come in handy at times, they can generally be raised fairly easily in-game, especially Wrestler and Thrower.

- **Wrestler**: Ability to grapple, restrain, take-down, throw opponents, etc. Higher skill means all of these moves succeed more often - see \#Wrestling and Unarmed Attacks for details.
- **Striker**: Punching ability - comes in handy when weapons get stuck, and there is no time to wrest them back.
- **Kicker**: Kicking ability,same as Striker. Kicks are slower but more deadly than punches; heavy kicks are particularly good at crushing and exploding heads.
- **Biter**: Biting ability; surprisingly effective even with non-animal races, as, after biting, you can shake opponents around by your teeth, causing great damage and possibly ripping off body parts, although with sapient races, this tends to lean more towards fingers or toes, perhaps the occasional hand or foot.
- **Thrower**: Throwing any miscellaneous object - rocks, knives, axes, swords, heads, etc. Skill affects accuracy and damage caused.
- **Miscellaneous object user**: Ability to beat things to death with anything that comes to hand, from bags to coins to their own severed body parts. Also somewhat more commonly used for shield bashing. This skill affects combat with any object, from a rock to a beehive. There are no separate skills for different items - items actually intended to be weapons, like swords or axes, are unaffected by this skill.

### Movement and awareness

- **Observer**: Helps one to notice things like ambushes, enemies who are "sneaking" (stealth movement), and traps. Detection range increases with skill, up to a maximum of 3 tiles away. Higher levels give more information regarding opponents. Hard to train - adding some points here is advisable.
- **Swimmer**: Allows movement through water without drowning. A Novice swimmer can swim, but will revert to being unable to swim if stunned, which happens when falling even 1 z-level into the water, or possibly after an unfriendly encounter with a creature *in* the water. An Adequate swimmer can swim normally (not drown) while stunned. For this reason, *starting out as an Adequate swimmer is advisable.* If you don't, at least start as Novice and go get some swimming practice right away.
- **Ambusher**: The skill of Sneaking around unobserved. This can be raised fairly easily by sneaking around while travelling from place to place when speed is not important. Enemies will have "sight ranges" from where they can detect a sneaking adventurer. The red zone of sight is where they will see you immediately and begin chasing you; the yellow is where they might see you. Staying out of sight will allow you to silently assassinate your foes, as they rarely seem to notice a knife in the back in time.
- **Climber**: The skill of climbing up walls, into trees, and around the edges of gorges. Higher levels reduce the chance of falling and increase the speed of a climbing character.
- **Tracker**: The skill of tracking your quarry, whether it be animals or goblins. Higher levels will let you spot more tracks and help you distinguish different tracks.
- **Crutch-walker**: The skill of standing and walking with a crutch for support. This skill only becomes available when attempting to move with a crutch in inventory, and can be developed with or without legs. At Legendary levels, a crutch walker walks with no speed reduction, and simply keeping it in hand will continue to increase attributes.

### Crafting

These allow your character to create things:

- **Knapper**: The fine art of sharpening rocks by banging them together in a clever manner. The resulting rocks become sharp rocks which do more damage when thrown and can be used for things requiring a sharp edge like butchering. Easy to make in-game, and doing so helps with Kinesthetic/Spatial Sense.
- **Bone carver**: The art of making knick-knacks and other items by carving bones. A skilled bone carver adventurer can make items of the same quality as fortress mode dwarves, including "☼Masterpiece☼". Bone carving adventurers can also make bone figurines, and customize their appearance.
- **Writer**: Your adventurer's ability to craft/write upon books and scrolls, you can choose the topic as well. It is hard to acquire the writing materials, however - checking in libraries and old dwarven fortresses may prove profitable.
- **Carpenter**: Your adventurer's ability to craft wooden objects and create wooden buildings and displays.

### Social

Almost all of these are only used in arguments.

- **Persuader**: Increases your ability to convince people of your view.
- **Judge of intent**: Allows you to tell how the opponent is arguing, unknown if higher levels change anything.
- **Flatterer**: Increases your ability to flatter your way out of the argument.

### General performance skills

These are your general performance skills, similar to fighter skill, in that they enhance rolls for many different skills and can be leveled easily.

- **Musician**: Increases quality of all instrument-based performances, this is your all-around instrument skill, very similar to speaker and fighter, except with instruments.
- **Speaker**: Your all-around speaking skill increases quality of all performances that involve speaking out loud, includes reading poetry, singing etc. Very similar to "Fighter" skill, except it's with performance rolls, not fighting rolls. May also effect arguments\[Verify\].

### Performance skills

Skills that affect your character's ability to pull off performances. These skills can be used to play as a bard.

- **Poet**: Increases the quality of poems you create and read out loud.
- **Singer**: Increases quality of all songs your character sings.
- **Dancer**: Increases quality of dances you choreograph and perform.
- **Stringed Instrumentalist**: Increases quality of all performances using stringed instruments.
- **Wind Instrumentalist**: Increases quality of all performances using wind-based instruments.
- **Percussionist**: Increases quality of all performances using percussion instruments.
- **Keyboardist**: Increases quality of all performances using keyboard instruments. (NB, shows up far less often in character generation than any of the others)

**Note: if your civilization does not have access to a type of instrument, you will not be able to choose that skill at character generation time.**

There are also procedural skills for every different kind of instrument, dance and poetic form, these will vary from world to world and by civilization, and cannot be chosen at character generation, but can be leveled in play.

### Other

- **Reader**: Allows you to read books, signs, and writing in Adventurer mode. Novice level is required in order to become a Necromancer. Can be trained slowly by reading books (if you can read). Adding more points is a waste, as novice allows you to read anything.
- **Butcher**: The art of turning corpses into piles of delicious prepared meat for food. Butchering also makes corpses and body parts less useful to enemy necromancers (*assuming the character has the zombie-making faculty to begin with*). You can allocate points here during character creation, but doing so is a waste because the skill doesn't really affect anything, anyway - except the taste, of course.
- **Wordsmith**: It is unknown exactly what this skill affects, but likely it affects the quality of books, poems, and other written materials.

## Character appearance and preferences

Appearance choosing menu

Personality overview menu

You are able to customize your adventurer's appearance, needs and preferences. Appearance does not seem to affect anything.\[Verify\] Just like with any citizen in fortress mode, their needs will have to be fulfilled, or else the character suffers from distraction. However, a few unmet needs do not matter as long as a character has more satisfied needs and/or their more intense needs are fulfilled.

As needs are fulfilled, your character's total level of focus goes up, gaining you bonuses to accuracy and other skill rolls. When your focus level is high or low, the following will be displayed on the status bar: Focused, Focused!, or Distracted. The focus level can also be seen in the last paragraph of the current adventurer's description, which can be viewed with z-d.

In the current version, some needs are unable to be fulfilled in adventurer mode. Be with family is an example, as adventurers start without any, and cannot start a family. Others include: Eat good meal, Admire art, Make romance, Be with friends, Uphold tradition, and Take it easy.\[Verify\]Some easy-to-fulfill needs (with the way many people play) include: Cause trouble, Be extravagant, Wander, Excitement, and Fight. With f it is possible to adjust their personality to eliminate unsatisfiable needs, or even all needs entirely.

For example, the Be with family need can be eliminated by setting the Family to N/A or lower. To eliminate all needs, set all values to N/A, the Flatterer personality to \>, and all the following personalities to \: Greedy, Intemperate, Avoid fights, Harmony, Austere, Incurious, Altruistic, Loner, Leisurely, Excitement-seeking, Inclined to abstract, and Inclined to create art. Their personality also determines what dream they might have - some of these are also not currently attainable, like raising a family. They can currently only have one dream, but if their personality enables more than one, you can swap between them with g. Achieving their dream seems to only give them a good thought, which generally has no effect until they are retired.

Adventurers can have the need to Pray to their deity. This is the one possible need that is not determined by their personality - depending on their beliefs, it will be added automatically - also one of the easiest needs to fulfill, assuming they can talk.

## Equipment, mounts, and pets

Equipment menu

All equipment, mounts, and pets you start with have a cost, which is paid from a single pool of points. Any points left unspent will be converted to coins, if your civilization has produced any. (It might be more useful to spend remaining points on gems, since coins currently have less value in other civilizations.) The amount of starting points depends on your status.

### Equipment

The items available are those which are available to your civilization. Outsiders only have access to weapons, armor, and shields made of any metal available in that world. There is no weight, volume, or count limit on what equipment you can take; however, if you take more than you can easily carry, you will be slowed down. (You could get a pack animal pet to help with that.) The item selection screen only shows items which you can currently afford. You can further filter the list by just typing what you are looking for.

Once an item has been added to your inventory, you can change the quantity with - and +; to remove an item reduce the quantity to zero. You can also change the quality of an item with q and w, for the cost shown on those options. Note that handwear and footwear do not come in pairs, so you will want to add as many as you need. For example, a spider man will want six lines of gauntlet and two of boot.

Unless you are similar in size to one of the main races, this may be the only way to get armor and clothing that you can wear - another way is to make equipment for your race in fortress mode first, then go get it in adventurer mode.

There are some items that currently have no use - other than for trading - in (unmodded) adventurer mode. For example, splints cannot be used to set broken bones, and thread cannot be used to suture wounds (no matter what skill levels a character has). Note, crutches **can** be used for walking. Also, a pick can be used as a weapon, but not for digging, nor can the dice you add here yet be rolled in-game. Another thing to consider is that not all creatures you can play as are omnivores; some may be carnivores or herbivores.

Items that can have a shape (gems, figurines, dice, etc.) will get a random shape when added. For items made from multiple materials (instruments), the additional materials will be random from those available to the civilization.

### Mounts and pets

Mounts are pets you can ride. Some pets can be used as pack animals to carry stuff. The smallest pets can ride you (you carry them as an item). Unfortunately, there is no indication on this screen as to which is which. You can check the wiki page for an animal to see if it has the [`[MOUNT]`](/index.php/Creature_token#MOUNT "Creature token"), [`[MOUNT_EXOTIC]`](/index.php/Creature_token#MOUNT_EXOTIC "Creature token"), [`[PACK_ANIMAL]`](/index.php/Creature_token#PACK_ANIMAL "Creature token"), or VERMIN tokens. Pets may also fight for you - and some can be rather formidable - or they may get scared and run away.

When an animal is added as a pet, it will be given a random name. You can then select it, and rename it with n, or remove it with r. There is no known limit - other than cost and sanity - to how many you can take.

Getting to this page enables a new option at the top of the screen: N: Add a new character to the party.

## Party summary

Party summary

The final screen of character creation is a list of the party members. You can choose which character's home the party will start at with 82, with the general location shown on the map and the name of the site below. Pressing ESC will take you back to modifying the party, where you can cycle through existing party members with TAB or add another with N.

Once the party is ready to go, press y to start the adventure.
