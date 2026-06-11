# Sphere

> Fonte: [Sphere](https://dwarffortresswiki.org/index.php/Sphere) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A graph showing the connections between all the spheres. A thin line represents a friendship, a thick line a parent/child-relationship, and a red line preclusion.

A **sphere**, or **cosmic principle**, is an aspect where a being has influence. Deities, forces, angels, demons, megabeasts, semi-megabeasts, forgotten beasts and titans may be associated with one or more spheres, and civilizations may prefer certain spheres when selecting creatures to worship. There are currently a total of 130 spheres.

Ancient artifacts known as primordial remnants are connected to spheres, taking a unique form and granting powers depending on the sphere they're connected to.

## Understanding spheres

A being such as a deity, demon or megabeast may come to represent or epitomize certain things like emotions, qualities, terrain types, and items, which are called "spheres". As an example from real-world mythology, the Greek goddess Athena is goddess in the "spheres" of wisdom, warfare, handicrafts and reason.

Gods and adored megabeasts can grant secrets related to their spheres. In unmodded *Dwarf Fortress*, this means that death gods can teach the secret of life and death to their worshipers, turning them into necromancers. If those gods also happen to be associated with nightmares, they can grant the ability to summon bogeymen and nightmares as well.

Dwarves and other creatures will come to worship certain "powerful beings" and, as such, will follow the "religion", and have a relationship with its "deity".

A historical figure with associated spheres that generates in the wild, or as a god, will be named after its spheres. So a death-aligned demon will be able to raise dead, and should they rule an entity, they will convert the surrounding regions into evil-aligned undead-raising biomes. Nightmare-aligned demons can summon bogeymen and nightmares. The symbols associated with the sphere will be used to generate first names, compound names, and titles. If an interaction from a deity creates an artifact, then that artifact will be named using the spheres of the god who gave the blessing.

## Creatures with pre-determined spheres

While many procedurally generated creatures in *Dwarf Fortress* are given random spheres upon creation, there are others who have static spheres, which remain constant across all save files:

- Bogeyman: Misery, night, nightmares
- Bronze colossus: Metals, strength, war
- Cyclops: Light, longevity, minerals, strength, thunder
- Dragon: Fire, wealth
- Ettin: Speech, strength
- Experiment: Deformity, night
- Giant: Food, strength
- Hydra: Muck, rebirth, strength
- Minotaur: Caverns, chaos, darkness, deformity, strength
- Nightmare: Misery, night, nightmares
- Roc: Hunting, sky, wind
- Werebeast: Animals, chaos, moon, night
- Night troll: Death, Night

## Sphere tokens

\
According to Toady: "*Spheres have a parent/child list, a friend list, and a preclude list. A deity has either one or two base spheres, and then they pick friends of those spheres, while never choosing a precluded or parent/child sphere of any of the spheres they already have. I tried to be pretty lax with the preclude list so that interesting relationships could pop up.*"

Creatures and inorganic materials can be assigned spheres with the \[SPHERE:\] token.

A secret uses any number of \[IS_SPHERE\] tokens to determine what spheres it is available to.

Available sphere tokens are:

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| Sphere | Parent spheres | Child spheres | Friend spheres | Precluded spheres | Associated string and properties | Symbols |
| AGRICULTURE |  |  | FOOD, FERTILITY, RAIN |  | it looks constantly to the sky for rain | FOOD, NATURE |
| ANIMALS | NATURE | FISH | PLANTS |  | it growls, buzzes, clicks and generally makes a varied racket | NATURE, PRIMITIVE |
| ART |  | DANCE, MUSIC, PAINTING, / POETRY, SONG | INSPIRATION, BEAUTY |  | it is decorated with intricate patterns | FLOWERY, THOUGHT |
| BALANCE |  |  |  |  | it is perfectly symmetric | BALANCE |
| BEAUTY |  |  | ART | BLIGHT, DEFORMITY, DISEASE, MUCK | it is strikingly beautiful | FLOWERY |
| BIRTH |  |  | CHILDREN, CREATION, FAMILY, MARRIAGE, / PREGNANCY, REBIRTH, YOUTH |  | it is covered with a filmy sac | NEW |
| BLIGHT |  |  | DISEASE, DEATH | BEAUTY, FOOD, FERTILITY, HEALING | nearby vegetation seem(sic) to shrink away from it | DEATH, UGLY |
| BOUNDARIES |  | COASTS |  |  | the pieces of its body are carefully separated by markings | BOUNDARY |
| CAVERNS |  |  | MOUNTAINS, EARTH |  | its moans seem to echo no matter where it resides | NAME_CAVE |
| CHAOS |  |  | WAR | DISCIPLINE, ORDER, LAWS | it spins wildly, lurching and howling | VIOLENT, WILD |
| CHARITY |  |  | GENEROSITY, SACRIFICE | JEALOUSY | it seems very pleasant | GOOD |
| CHILDREN |  |  | BIRTH, FAMILY, YOUTH, PREGNANCY |  | it never misses an opportunity to jump in puddles | NEW |
| COASTS | BOUNDARIES |  | LAKES, OCEANS |  | it appears to be covered with rocky crags | AQUATIC |
| CONSOLATION |  |  |  | MISERY | it radiates a sad kindness | GOOD, PEACE |
| COURAGE |  | VALOR |  |  | it makes those around it feel brave | ASSERTIVE |
| CRAFTS |  |  | CREATION, LABOR, METALS |  | it appears constructed | ARTIFICE |
| CREATION |  |  | CRAFTS, BIRTH, PREGNANCY, REBIRTH |  | small objects seem to pop into existence around it | NEW |
| DANCE | ART |  | FESTIVALS, MUSIC, REVELRY |  | it whirls, skips and jumps whenever it moves | DANCE, FLOWERY |
| DARKNESS |  |  | NIGHT | DAWN, DAY, LIGHT, TWILIGHT, SUN | it is difficult to see clearly even in bright light | DARKNESS, MYSTERY |
| DAWN |  |  | SUN, TWILIGHT | NIGHT, DAY, DARKNESS | it always turns to welcome the rise of the sun | NEW, COLOR, LIGHT |
| DAY |  |  | LIGHT, SUN | DARKNESS, NIGHT, DAWN, DUSK / DREAMS, NIGHTMARES, TWILIGHT | it hums pleasantly when the sun is high in the sky | LIGHT |
| DEATH |  |  | BLIGHT, DISEASE, MURDER, / REBIRTH, SUICIDE, WAR | HEALING, LONGEVITY, YOUTH | it has a rattling exhale | DEATH |
| DEFORMITY |  |  | DISEASE | BEAUTY | its body is bent and misshapen | UGLY |
| DEPRAVITY |  |  | LUST | LAWS | it slavers uncontrollably | EVIL, WILD, UGLY |
| DISCIPLINE |  |  | LAWS, ORDER | CHAOS | it moves with great focus | LEADER, ORDER |
| DISEASE |  |  | BLIGHT, DEATH, DEFORMITY | BEAUTY, HEALING | it bears malodorous pustules / \[ODOR_STRING:death\]\[ODOR_LEVEL:100\] | DEATH, UGLY |
| DREAMS |  |  | NIGHT, NIGHTMARES | DAY | the details of its form are easily forgotten without deliberate concentration | MYSTERY |
| DUSK |  |  | TWILIGHT | NIGHT, DAY | it never looks toward the sun | DARKNESS, MYSTERY |
| DUTY |  |  | ORDER |  | it is utterly still when not taking deliberate action | LEADER |
| EARTH |  | METALS, MINERALS, SALT | CAVERNS, MOUNTAINS, VOLCANOS |  | it looks very solid and stocky | EARTH |
| FAMILY |  |  | BIRTH, CHILDREN, MARRIAGE, PREGNANCY |  | it appears to be closely related to every other of its kind | DOMESTIC, FAMILY |
| FAME |  |  | RUMORS | SILENCE | Fanfare follows it wherever it goes | ASSERTIVE, LEADER |
| FATE |  |  |  | LUCK | it never appears to be perturbed or surprised by any happening | MYSTERY, MYTHIC |
| FERTILITY |  |  | AGRICULTURE, FOOD, RAIN | BLIGHT | it appears to be very healthy | NEW |
| FESTIVALS |  |  | DANCE, MUSIC, REVELRY, SONG | MISERY | it skips and twirls as it moves | DOMESTIC, FESTIVAL |
| FIRE |  |  | METALS, SUN, VOLCANOS | WATER, OCEANS, LAKES, RIVERS | a sheen around it always seems to rise upward | FIRE |
| FISH | ANIMALS |  | OCEANS, LAKES, RIVERS, WATER, FISHING |  | it only looks comfortable when it is in the water | AQUATIC, NATURE |
| FISHING |  |  | FISH, HUNTING |  | it always moves carefully around water | AQUATIC, NATURE |
| FOOD |  |  | AGRICULTURE, FERTILITY | BLIGHT | it has the delicious smell of freshly-baked goods / \[ODOR_STRING:freshly-baked goods\]\[ODOR_LEVEL:100\] | FOOD |
| FORGIVENESS |  |  | MERCY | REVENGE | it is impossible to hold a grudge near it | GOOD |
| FORTRESSES |  |  | WAR |  | it is very sturdy-looking | PROTECT |
| FREEDOM |  |  |  | ORDER | it eagerly moves from place to place | FREEDOM |
| GAMBLING |  |  | GAMES, LUCK |  | it changes between two colors intermittently | GAMES, LUCK, WEALTH |
| GAMES |  |  | GAMBLING, LUCK |  | it giggles at random | GAMES |
| GENEROSITY |  |  | CHARITY, SACRIFICE |  | it makes those around it want to give up their possessions | GOOD |
| HAPPINESS |  |  | REVELRY | MISERY | it seems to smile constantly | GOOD |
| HEALING |  |  |  | DISEASE, BLIGHT, DEATH | it is surrounded by a gentle atmosphere | GOOD, PEACE |
| HOSPITALITY |  |  |  |  | it radiates an aura of welcoming | DOMESTIC, GOOD, PEACE |
| HUNTING |  |  | FISHING |  | it inspects the ground intently as it moves | NATURE, PRIMITIVE, WILD |
| INSPIRATION |  |  | ART, PAINTING, POETRY |  | flashes of energy pulse across its surface intermittently | THOUGHT |
| JEALOUSY |  |  |  | CHARITY | it appears to be a very bitter creature | EVIL, SUBORDINATE |
| JEWELS |  |  | MINERALS, WEALTH |  | its whole body appears to be faceted in a symmetric fashion | COLOR, EARTH |
| JUSTICE |  |  | LAWS |  | it seems eager to pronounce judgment on others | GOOD, PROTECT |
| LABOR |  |  | CRAFTS |  | it appears very deliberate in its actions | ARTIFICE, DOMESTIC |
| LAKES | WATER |  | COASTS, FISH, OCEANS, RIVERS | FIRE | it moves ponderously | AQUATIC, NAME_LAKE |
| LAWS |  |  | DISCIPLINE, JUSTICE, OATHS, ORDER | CHAOS, DEPRAVITY, MURDER, THEFT | it has a very stark look about it | ORDER, PROTECT, RESTRAIN |
| LIES |  |  | TREACHERY, TRICKERY | TRUTH | it seems unerringly honest if one does not concentrate | EVIL, MYSTERY |
| LIGHT |  |  | DAY, RAINBOWS, SUN | DARKNESS, TWILIGHT | it returns surrounding light with a new vibrance and intensity | COLOR, LIGHT |
| LIGHTNING | WEATHER |  | RAIN, STORMS, THUNDER |  | it crackles with energy | ASSERTIVE, LIGHT, WILD |
| LONGEVITY |  |  | YOUTH | DEATH | it always seems to be looking far into the distance | OLD |
| LOVE |  |  |  |  | it stares longingly at those nearby | FLOWERY, ROMANTIC |
| LOYALTY |  |  | OATHS | TREACHERY | it never abandons its companions | GOOD, PROTECT |
| LUCK |  |  | GAMBLING, GAMES | FATE | it changes direction suddenly at times | LUCK |
| LUST |  |  | DEPRAVITY |  | it has an unnerving stare | PRIMITIVE, ROMANTIC |
| MARRIAGE |  |  | BIRTH, FAMILY, OATHS, PREGNANCY |  | it heckles those it meets that are not married | FLOWERY, ROMANTIC |
| MERCY |  |  | FORGIVENESS | REVENGE | it always seems like it is on the verge of crying | GOOD, PROTECT |
| METALS | EARTH |  | CRAFTS, FIRE, MINERALS |  | it appears to have sharp shimmering edges on many parts of its body | EARTH |
| MINERALS | EARTH |  | JEWELS, METALS |  | it has an angular appearance | EARTH |
| MISERY |  |  | TORTURE | CONSOLATION, FESTIVALS, REVELRY, HAPPINESS | it has a distinctly depressing moan | NEGATIVE |
| MIST |  |  |  |  | it is difficult to see clearly | MYSTERY |
| MOON |  |  | NIGHT, SKY |  | it changes color with the phases of the moon | DARKNESS, LIGHT, MYSTERY |
| MOUNTAINS |  |  | CAVERNS, EARTH, VOLCANOS |  | it is very solidly built | EARTH, NAME_MOUNTAINS |
| MUCK |  |  |  | BEAUTY | there is a foul reek about it | PRIMITIVE, UGLY |
| MURDER |  |  | DEATH | LAWS | it cannot abide anything that lives | DEATH, EVIL |
| MUSIC | ART |  | DANCE, FESTIVALS, REVELRY, SONG | SILENCE | it sounds clear tones as its body moves in time | FLOWERY, MUSIC, '*not* SILENCE |
| NATURE |  | ANIMALS, PLANTS | RAIN, SUN, WATER, WEATHER |  | it seems most at ease when it is outdoors | NATURE |
| NIGHT |  |  | DARKNESS, DREAMS, MOON, NIGHTMARES, STARS | DAY, DAWN, DUSK, TWILIGHT | it eerily reflects the light of the stars and moon | DARKNESS |
| NIGHTMARES |  |  | DREAMS, NIGHT | DAY | it reminds those that look upon it of their most unpleasant memories | DARKNESS, DEATH, EVIL, MYSTERY, UGLY, VIOLENT |
| OATHS |  |  | LAWS, LOYALTY, MARRIAGE | TREACHERY | it cannot look directly at somebody that has broken an oath | ORDER, PROTECT |
| OCEANS | WATER |  | COASTS, FISH, LAKES, RIVERS, SALT | FIRE | it always raises a part of its body toward the moon | AQUATIC, NAME_OCEAN |
| ORDER |  |  | DISCIPLINE, DUTY, LAWS | CHAOS, FREEDOM | it moves very stiffly | ORDER |
| PAINTING | ART |  | INSPIRATION |  | its surface is always enlivened with a refreshing play of color | COLOR, FLOWERY |
| PEACE |  |  |  |  | it has an incredibly calm demeanor | PEACE |
| PERSUASION |  |  | POETRY, SPEECH |  | it rocks back and forth whenever somebody changes their mind in its presence | ASSERTIVE |
| PLANTS | NATURE | TREES | ANIMALS, RAIN |  | it always seems to point toward the sun when it is in the sky | NATURE |
| POETRY | ART |  | INSPIRATION, PERSUASION, SONG, WRITING |  | it recites verses in a strange language on occasion | FLOWERY, THOUGHT |
| PREGNANCY |  |  | BIRTH, CHILDREN, CREATION, FAMILY, MARRIAGE |  | it appears to be expecting | NEW, ROMANTIC |
| RAIN | WATER, WEATHER |  | AGRICULTURE, FERTILITY, LIGHTNING, / NATURE, PLANTS, RAINBOWS, / STORMS, THUNDER, TREES |  | it leaves water wherever it goes | AQUATIC, SKY |
| RAINBOWS | WEATHER |  | LIGHT, RAIN, SKY |  | it is strikingly colored | COLOR, SKY |
| REBIRTH |  |  | BIRTH, CREATION, DEATH |  | it alternates from instant to instant between sluggishness and extreme vibrancy | NEW |
| REVELRY |  |  | DANCE, FESTIVALS, HAPPINESS, MUSIC, SONG | MISERY | it moves with a bouncing rhythm | FESTIVAL, GOOD, WILD |
| REVENGE |  |  |  | FORGIVENESS, MERCY | it has a fixed and unblinking gaze when interacting | VIOLENT |
| RIVERS | WATER |  | FISH, LAKES, OCEANS | FIRE | its outer surface seems to flow about its body | AQUATIC |
| RULERSHIP |  |  |  |  | it is hard to disobey | LEADER |
| RUMORS |  |  | FAME |  | it always nods eagerly when somebody is speaking | MYSTERY |
| SACRIFICE |  |  | CHARITY, GENEROSITY | WEALTH | it inspires those around it to acts of great sacrifice | PROTECT |
| SALT | EARTH |  | OCEANS |  | it makes nearby water undrinkable | NAME_OCEAN |
| SCHOLARSHIP |  |  | WISDOM, WRITING |  | it always seems to be deep in thought | THOUGHT |
| SEASONS |  |  |  |  | its form is ever-changing | NATURE |
| SILENCE |  |  |  | FAME, MUSIC | it makes absolutely no sound | SILENCE, PEACE, **not** MUSIC |
| SKY |  |  | MOON, RAINBOWS, SUN, STARS, WEATHER, WIND |  | it has a slowly shifting pattern on its surface | SKY |
| SONG | ART |  | FESTIVALS, MUSIC, POETRY, REVELRY |  | it sings beautiful songs endlessly | FLOWERY, MUSIC |
| SPEECH |  |  | PERSUASION |  | it pays attention carefully to anybody that is speaking | FLOWERY, THOUGHT |
| STARS |  |  | NIGHT, SKY |  | it appears to sparkle after night falls | SKY, MYSTERY |
| STORMS | WEATHER |  | LIGHTNING, RAIN, THUNDER |  | its movement is the sound of wind and rain | ASSERTIVE, SKY, WILD |
| STRENGTH |  |  |  |  | it looks solidly built | ASSERTIVE |
| SUICIDE |  |  | DEATH |  | it mutters to itself about death | DEATH |
| SUN |  |  | DAWN, DAY, FIRE, LIGHT, NATURE, SKY | DARKNESS | it is difficult to look at directly | ASSERTIVE, LIGHT, SKY |
| THEFT |  |  |  | LAWS, TRADE | it always seems to have its attention on the most valuable object in the area | EVIL, MYSTERY |
| THRALLDOM |  |  |  |  | its movements sound like the rattling of chains | LEADER, SUBORDINATE |
| THUNDER | WEATHER |  | LIGHTNING, RAIN, STORMS |  | it is incredibly noisy | ASSERTIVE, SKY, WILD |
| TORTURE |  |  | MISERY |  | it appears to be covered with sharp hooks and barbs | EVIL |
| TRADE |  |  | WEALTH | THEFT | it seems most content when a fair wind is blowing | TRADE, TRAVEL |
| TRAVELERS |  |  |  |  | it never stops moving completely | TRADE, TRAVEL |
| TREACHERY |  |  | LIES, TRICKERY | LOYALTY, OATHS | it is unsettling to be around | EVIL, MYSTERY |
| TREES | PLANTS |  | RAIN |  | it is top-heavy | NATURE, NAME_FOREST |
| TRICKERY |  |  | LIES, TREACHERY | TRUTH | it has a tendency to laugh quietly to itself every so often | MYSTERY |
| TRUTH |  |  |  | LIES, TRICKERY | it tenses up throughout its entire body whenever somebody tells a falsehood in its presence | GOOD, TRUTH |
| TWILIGHT |  |  | DAWN, DUSK | LIGHT, DARKNESS, DAY, NIGHT | it chitters briefly before sunrise and just after nightfall | DARKNESS, MYSTERY |
| VALOR | COURAGE |  | WAR |  | it always tries to embolden any fighting in its presence with exhortations of bravery, even its foes | ASSERTIVE, VIOLENT |
| VICTORY |  |  | WAR |  | it looks very proud of itself | ASSERTIVE, LEADER |
| VOLCANOS |  |  | EARTH, FIRE, MOUNTAINS |  | it seems to glow brightly from within | FIRE, NAME_VOLCANO |
| WAR |  |  | CHAOS, DEATH, FORTRESSES, VALOR, VICTORY |  | it bellows and cheers without pause | ASSERTIVE, LEADER, VIOLENT |
| WATER |  | LAKES, OCEANS, RIVERS, RAIN | FISH, NATURE | FIRE | it seems to flow as it moves | AQUATIC |
| WEALTH |  |  | JEWELS, TRADE | SACRIFICE | it always seems to be counting something | WEALTH |
| WEATHER |  | LIGHTNING, RAIN, RAINBOWS, / STORMS, THUNDER, WIND | NATURE, SKY |  | it changes appearance based on the clouds and precipitation above | SKY |
| WIND | WEATHER |  | SKY |  | it is surrounded by an everpresent rush of wind | ASSERTIVE, SKY, WILD |
| WISDOM |  |  | SCHOLARSHIP |  | it acts with unwavering calm | THOUGHT |
| WRITING |  |  | POETRY, SCHOLARSHIP |  | it is covered with divine writing | THOUGHT |
| YOUTH |  |  | BIRTH, CHILDREN, LONGEVITY | DEATH | it appears spry and vigorous | ASSERTIVE, NEW |
