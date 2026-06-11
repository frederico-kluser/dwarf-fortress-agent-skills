# Stress

> Fonte: [Stress](https://dwarffortresswiki.org/index.php/Stress) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

At least it wasn't blood rain...\
*Art by theRealOdieman*

**Stress** is a condition that is similar to unhappiness in earlier versions. It will cause the dwarf to flash with a downward red arrow, and Over the long term, Urist McStressed has been under a great deal of stress. will show on their thoughts and preferences tab.

Dwarves under stress for long periods of time will develop worse symptoms of stress, e.g: Urist McStressed has become haggard and drawn due to the tremendous stresses placed on him.. In the short term, excessive levels of stress will lead to temporary **emotional breakdowns** – throwing tantrums, slipping into depression, or stumbling around obliviously. If they're under stress for prolonged periods of time, dwarves will become Harrowed, their thoughts and preferences tab reading: Urist McStressed has been utterly harrowed by the nightmare that is his tragic life. If a harrowed dwarf experiences a stressful event like observing death, it will lead to **insanity**.

Animals can also be stressed, which seems to happen when an animal has been constrained for a long time.

\

## Technical details

Internally, stress level is tracked by two numbers, where a negative number is good and a positive number is bad – it is not possible to view these numbers without third-party utilities.

**Short-term stress** ranges from -100000 to 100000, it is affected by emotions and directly correlates with a creature's mood: the happy or angry emojis which are labelled "stress level" in game and range from escatic to miserable.

**Long-term stress** ranges from -50000 to 120000, it is a gradual accumulation of short-term stress, the only indication of a dwarf's long term stress are statuses: stressed at +25000, haggard at +50,000 and harrowed at +100,000.

Only if both short-term and long-term stress are high does a creature become prone to **emotional breakdowns**.

Under "ideal" circumstances, long term stress can increase by at most 20,160 per year, and decrease by at most 43,564 per year [1], this means it takes several years for a dwarf to become haggard, even if the dwarf is in a very bad mood, but a full recovery also takes several years, even if the dwarf is in an excellent mood - but in the meantime the good mood does protect against breakdowns.

Despite the nomenclature "short-term stress" it can take several years to improve a dwarf's short-term stress level from miserable to ecstatic.

## Detailed mechanics

### How stress works

First, to bust a myth: discipline is not an indicator of how well a dwarf copes with stressful situations, but there is a correlation that will be explained below.

When a dwarf experiences an emotion, whether from an immediate experience or from revisiting a long-term memory, a certain number of points, which will be called "stress points", are added to that dwarf's "stress score". The dwarf keeps a running tally of their stress points, determining their mood. Unhappy thoughts add to the stress score, happy thoughts subtract from the stress score. It is confirmed that there are only two things that affect stress: the emotions that a dwarf experiences, each of which is shown on the thoughts and preferences screen, and a return towards a neutral point over time.

There are three key personality traits which determine a dwarf's propensity to experience stress: bravery, which determines how fast a dwarf accumulates stress; stress vulnerability, which determines how much stress a dwarf can experience before breaking \[note 4\]; and anxiety, which determines how fast a dwarf dissipates stress. A fourth trait, depression propensity, seems to be related to the difficulty of recovering an unhappy dwarf, but requires additional testing.

There are some experiences which have a constant and predictable effect across all dwarves and others that are much more variable. In assessing the impact of an experience on a dwarf's stress score, a key measure is whether or not the resulting emotion was promoted to a dwarf's long term memory, as these tend to be the stronger emotions and are those that are revisited.

The results below are taken from a sample of 300 dwarves across 3 fortresses, where all dwarves had been in their fortress for more than 2 years. The fortresses were designed to "molly-coddle" the dwarves, shielding them as much as possible from rain, death, corpses and miasma, and promoting happy thoughts as much as possible (after year 2, because it took 2 years and 5 migrant waves to reach that point with the infrastructure). The fortresses each had 150+ dwarves and had been run for 7 years. The overall mood of the fortresses after 7 years was 45% happy to ecstatic, 55% fine, less than 1% unhappy (4 dwarves in total).

### Stress reducers

#### Bedrooms

More than 99% of dwarves had short-term memories of feeling blissful sleeping in a bedroom like a personal palace, 89% were also experiencing long-term memories of remembering feeling blissful about their bedroom. This was achieved by giving them a 3x3 engraved bedroom.

#### Dining room

88% of dwarves had short-term memories of feeling blissful eating in a legendary dining room, 70% were also experiencing long term memories of remembering feeling blissful about their dining room. This was achieved by digging out a 15 x 20 room and designating it as a dining room; it doesn't take much to impress them in this regard, but to force them to eat there, you have to restrict placing unallocated tables anywhere else in the fortress.

#### Meaningful work

93% of dwarves were satisfied at work, 62% had long term memories of being satisfied at work. Curiously, a number of dwarves had two memories of being satisfied at work. Satisfaction is a low-strength emotion, so it is suspected that this is the result of a long-term memory being overwritten by a stronger short-term memory of a different group, then cycling back in again because it was a frequent experience always ready to be promoted back from short-term memory. From what was seen, hauling is not a satisfying job, but any job which enables a skill increase can be satisfying work, so long as it doesn't conflict with a dwarf's personality (for example, a butcher will get unhappy thoughts if they have a deep respect for nature).

#### Military training

Military training is HUGE. After year 2 in each fortress, all dwarves were put into squads (no armor, no weapons), with each squad scheduled for one or two months of military training per year. 93% of dwarves had happy long-term memories of something relating to their military training, with 34% having more than one positive long-term memory. Gratitude or pleasure from sparring was the most common, with interest in improving a military skill (wrestling, dodging, biting, kicking, etc.) and pride in teaching a military skill also widely present. Additionally several dwarves were satisfied remembering improving discipline and/or observation. The effect of military training in clogging long-term memory with happy thoughts correlates with an increase in discipline, which is a common association between high-discipline dwarves suffering from low stress. No dwarves had negative long-term memories, despite some not liking warfare or not respecting military skills. A fairly reliable method to turn around unhappy dwarves using military training was noted, which will be discussed further below.

#### Other things

All dwarves had access to masterwork clothing, walked past an indoor waterfall frequently, were able to acquire an item, read books, and walked past fine furniture frequently, but less than 25% of dwarves retained their thoughts about these things in long-term memory. Spending time with family and pets will do quite a lot to help reduce a dwarf's stress.

### Stress increasers

The median number of unhappy long-term memories across the sample of dwarves was only 1; most of the things that they were unhappy about in the long-term were things that would eventually be promoted to core memory: death, miasma, trauma, etc. Their other stress increasers were less than 1% of dwarves: being annoyed or irritated remembering being accosted by vermin; 1 dwarf was uneasy remembering becoming a parent; 1 dwarf was annoyed remembering drinking without a mug, which is suspected to have been a lingering long-term memory clogging their thoughts for several years; another was worried dwelling on not being able to help somebody and another was frustrated remembering the lack of traditions.

### Mixed and/or variable effects on stress

#### Praying

77% had long-term memories of wonder or enrapture from praying, 10% had negative long-term memories from being unable to pray, some dwarves had both positive and negative long term memories about praying. All dwarves had multiple positive and negative short-term thoughts about praying and not being able to pray. The balance of positive to negative long-term memories shows the effect of dwarves being unable to hold more than one thought of the same group in their short-term memory. As long as they get to pray more than once a year, they'll have a strong positive short-term memory about a deity and won't have room in their short-term memory to retain the negative thoughts from not being able to pray to the multiple gods that they wanted to.

#### Performances

All dwarves had multiple short-term memories about watching a performance or performing. However, a minority of thoughts were negative (about 5% were bored or embarrassed). Only a few dwarves had long-term memories related to performances/performing, all of them positive.

#### Arguments

Short-term memories about being upset getting into an argument were ubiquitous, and most dwarves had multiple short-term memories about arguing. However, only 3 dwarves were angry remembering getting into an argument (although 1 dwarf was exhilarated remembering this).

### Things that didn't matter

Some things were ubiquitous in dwarves' short-term memories, but didn't appear at all in long-term memories. These are often the things that worry players seemingly more than the dwarves themselves. These were: being away from family; being away from friends; being sad at being separated from a loved one; not having decent meals; being unable to craft an item; and being unable to wander.

### Recovering unhappy dwarves

From time to time, some dwarves would get stressed. In one test, an accident with a "malfunctioning" atom smasher occurred, which rained rotten body parts and gore all over the farmers. A dwarf in a strange mood was accidentally made to go berserk after the misapplication of a burrow command, several dwarves and their pets died of old age – usually in the middle of high-traffic corridors, and there were the usual unavoidable mishaps with visitors turning werebeast, trying to stage a coup, etc. Typically, around 10% of dwarves registered positive stress scores, with around 3% being so unhappy that they would be actively made to recover.

The first approach to trying to recover the stressed-out dwarves was to give them special attention and try to satisfy any unmet needs, in an attempt to overwrite some low-strength unhappy memories with happy memories. This had mixed results, was slow and took a lot of micromanagement. It would typically take about 2 years to turn around a mildly stressed dwarf.

During testing, a far more reliable and quick method to turn around stressed-out dwarves was found, using military training, in the form of a special "Therapy" military squad which was assigned to train all year round, and the squad was set to active/training on the squad menu. However, the squad was not assigned any barracks to train in. Any dwarf that was getting a bit down about things would be put into the Therapy Squad for a while. When a dwarf is scheduled to train, but has nowhere to train, they will actively seek to satisfy any needs. Rather than hang around with the "no job" label, they'll dash off to the tavern to socialise, the library to learn, the temple to pray or guildhall to increase their skills. It is far more effective, and easier to manage, than removing all of their tasks and hoping that they'll do something to cheer themselves up. It seems that they replace their duty to train with a duty to fulfill their needs.

After deploying this method and expanding it so that all dwarves got one month a year in which they were scheduled to train, but had no barracks, positive stress scores dropped to around 5%, with only 1 dwarf ever reaching the point of being unhappy (that particular dwarf being subjected to quite a lot of cycling up and down the stress levels to see what happened).

Of the 4 dwarves that became unhappy enough to be seemingly unrecoverable (3 from before the Therapy Squad method was discovered), all 4 dwarves had a depression propensity stat that was extremely low, meaning that they "were often sad and dejected". There were other dwarves in the fortresses with extreme depression propensities that didn't become unhappy, so it is unknown if this was a coincidence or whether it's just hard to turn around these dwarves once they reach an unhappy state.

### Combat hardness and immunity to corpses/stress

There is a very old piece of code which measures the "combat hardness value" of a dwarf. This value is listed as "detachment" in Dwarf Therapist, although it doesn't appear in the default grid views. Toady said that when a dwarf sees guts and stuff, including seeing people die, it increases their combat hardness, which will eventually lead them to become immune to seeing corpses. This code predates the current stress system and is still active. Anecdotal reports of dwarves becoming immune to seeing corpses due to constant combat exist, which is why it was brought to question. It was attempted to bring some dwarves to the maximum state of "doesn't really care about anything anymore", but after 10 years of running a fortress with one squad dedicated to fighting goblins released from cages, only the intermediate level of "is a hardened individual" was reached. There was fighting indoors, so it required frequent breaks to remove corpses to prevent miasma. There was an attempt at discovering which aspects of the stress system would be overridden by combat hardness – which things would a dwarf become immune to? Would it be everything? Do they not feel happiness or unhappiness about anything anymore? Can a dwarf still go berserk? Trying to test that concurrently with the rest of the experiment didn't sit well alongside the molly-coddle approach, so it was not pursued further, but knowing the effect on all aspects of stress would be interesting.\[Verify\]

Anecdotal evidence [2] from version 0.47.05 seems to indicate that dwarves gain combat hardness much more quickly than they did in previous versions. Even without taking any special measures, it seems common for most of the adult population to have some level of combat hardness, and it's not unusual for civilians who have never been in combat to reach the highest level of "doesn't really care about anything anymore".

### Conclusion

To keep stress down, keep the things that end up in core memory to a minimum, or at least restrict the variety of strong unhappy memory groups that dwarves are exposed to in any particular year – in particular, seeing corpses, sentient things die, being exposed to miasma and rain and vomiting because of the sun. If you plan on fighting rather than turtling, plan to battle underground so that the dwarves aren't exposed to sun and rain at the same time as death and corpses. If a dwarf sees a corpse, get them hauling all of the corpses, as they'll only remember the first one. If they're exposed to rain, get them to do all of the outdoor work quickly and keep the rest of the dwarves dry. If you have to pick somebody to do unsavory work, choose the dwarf(s) with the best mix of bravery, stress vulnerability and anxiety.

Clog a dwarf's long-term memory slots with happy thoughts that can't be promoted. Give them a big room to dine in very early on; even if they only have one table and chair to eat on, it'll still count, but get them enough chairs and tables as soon as possible. Give them a wide variety of things to have happy thoughts about, as multiple low-strength short-term memories have a chance at cycling out low-strength unhappy memories and preventing them from sticking. Put everybody in a military squad as soon as you can afford the labor – don't worry about weapons and armor; just get them training in any old dirt hole of a barracks for at least one month of the year (you might want to make sure that your mayor and trader are training over winter when there are no caravans or delegations). As soon as you can give everybody a 3x3 engraved bedroom, that's a sure-fire mood enhancer. Make sure that you have at least one temple and that the dwarves have a bit of downtime to pray.

## Stress factors

Stress is affected by the emotions a dwarf experiences upon encountering certain circumstances; these encounters are temporarily shown as thoughts in the dwarf's profile, though the resulting stress can linger long after the thoughts are gone. The strength of the emotions (and the resulting stress values) vary based on the dwarf's personality. Controlled testing has shown that these sources of stress build up less in dwarves with high \[BRAVERY\] and low \[STRESS_VULNERABILITY\]. \[ANXIETY_PROPENSITY\] affects the rate at which dwarves dissipate stress. For example, being out in the sun seems to affect dwarves quite strongly in terms of stress.

Emotions and the level of stress or stress relief they cause are detailed in the table of emotions. Note that one event may cause different emotions for different dwarves (and, occasionally, for the same dwarf). The exact mechanisms of how it's decided what emotions are to follow are as of yet unclear, but there's a general consensus that it depends on both severity of factors and the personality of the dwarf in question.

Here is a partial table of emotions and what they can be caused by:

|  |  |
|----|----|
| Emotion | Cause |
| adoration | Giving birth to a baby, becoming a parent |
| admiration | Being next to completely sublime furniture, watching a performance |
| affection | Interacting with a pet, adopting a new pet, forming a bond with the trained animal, talking with a friend, making a new friend |
| aroused | Talking with the spouse, watching a performance |
| caring | Giving somebody food |
| empathy | Being yelled at/cried on by an unhappy citizen |
| enraptured | Communing with deity |
| fondness | Making a new friend, talking with a friend or a sibling, interacting with a pet |
| gratitude | Being rescued, receiving water or food, being granted residency, being elected as mayor, sparring |
| lustful | Talking with the spouse |
| love | Talking with a parent, spouse, or child, gaining a sibling |
| passionate | Talking with the spouse |
| pleasure | Being next to fine/very fine/splendid/completely sublime furniture, acquiring well-crafted items, putting on a well-crafted/exceptional item, performing, viewing something on display |
| proud | Owning a high quality furniture, being elected as a mayor, bringing somebody to rest in bed |
| repentant | Being confined |
| sympathy | Giving somebody water or food, bringing somebody to rest in bed |
| tenderness | Talking with the spouse, bringing somebody to rest in bed |
| amused | Watching a performance |
| blissful | Dining in a legendary dining room, sleeping in a good bedroom/great bedroom/bedroom like a personal palace, having a bath, becoming a parent, performing |
| content | Being able to rest and recuperate, eating a fine/pretty decent meal, having a fine/pretty decent drink, putting on a well-crafted/finely-crafted/superior item, sleeping in a bedroom like a personal palace, having a bath, being near to a waterfall, discussing or pondering a topic |
| delighted | Eating a truly decent/legendary meal, putting on an exceptional item, being near to a waterfall, watching a performance |
| elated | Having punishment delayed, being elected |
| enjoyment | Being near to favourite animal in a cage, performing, watching a performance, playing with toys, playing make believe |
| euphoric | Drinking |
| expectant | Discussing or pondering {topic} |
| free | Being released from confinement |
| gaiety | Performing |
| happy | Adopting a new pet, being granted residency |
| hope | Being released from confinement |
| jovial | Having a mandate deadline met |
| joy | Performing |
| relieved | Being rescued, bringing somebody to rest in bed, eating vermin to survive, having punishment delayed, being near to a waterfall, being released from confinement, yelling at/crying on somebody in charge |
| satisfied | Receiving water or food, being successful at work, mastering a skill, teaching a skill, producing a masterwork, creating an artifact, improving a skill, reading a book, learning a book, felling a tree, slaughtering an animal, getting into an argument, caging a creature, being granted residency, realizing the value of leisure time, realizing the value of nature, realizing nuances of independence, realizing nuances of fairness, realizing nuances of loyalty, realizing nuances of law, realizing nuances of leisure time, realizing nuances of friendship, realizing the value of knowledge, realizing the worthlessness of eloquence, realizing the worthlessness of power |
| triumph | Killing somebody, being elected/re-elected |
| optimistic | Being able to rest and recuperate, having a mandate deadline met |
| astonished | Having punishment reduced, having punishment delayed, being elected |
| awe | Being next to completely sublime furniture |
| excited | Performing |
| eager | Being elected/re-elected |
| exhilarated | Being attacked, getting into an argument, a sparring session, performing |
| interested | Being next to fine/very fine/splendid/completely sublime furniture, learning the secrets of life and death, watching a performance, being taught a skill, reading a book, learning a book, realizing the value of nature, realizing nuances of perseverance, realizing nuances of craftsmanship, realizing the worthlessness of fairness, viewing something on display |
| wonder | Being taught a skill, learning a book, communing with {deity}, realizing the worthlessness of perseverance, realizing the value of family, realizing the value of competition, realizing the value of cooperation, realizing the value of loyalty |
| accepting | Seeing somebody's dead body, having a mandate ignored, being caught in the rain, being forced to drink vomit, being forced to endure the decay of a pet, retching on a miasma, having to conduct an official meeting in a bedroom (many negative memories may change to acceptance as a result of the personality-change system) |
| ambivalent | Delayed punishment of a criminal, putting on a well-crafted/finely-crafted item |
| grim satisfaction | Seeing somebody's death |
| suspicious | Having a mandate ignored |
| aggravated | Being pestered by flies |
| agitated | Being utterly sleep-deprived |
| annoyed | Being caught in the rain, being caught in a snow storm, being out in the sun, eating without a table or chair, eating without a proper dining room, sleeping on dirt/rocks/cave floor/in the grass, drinking water without a well, suffering a minor injury, choking on cave-in dust, choking on smoke, being accosted by hated vermin, being pestered by flies, drinking without a goblet, cup or mug |
| anxious | Discussing/pondering (topic) |
| bitter | Wearing tattered clothes, getting into an argument |
| bored | Watching a performance, being unoccupied, being unable to practice a craft, being unable to practice a martial art, not learning anything, being unable to use abstract thinking, being unable to wander, being unable to fight, being unable to hear eloquent speech, lack of trouble-making, doing nothing creative, generally leading an unexciting life |
| confused | Being knocked out during a cave-in |
| contemptuous | Getting into an argument |
| dejected | Being caught in the rain, being caught in a snow storm, wearing tattered clothes, lack of decent meals, being unable to pray to {deity}, being kept from alcohol, being unable to admire art, being unable to acquire something, being unable to be extravagant, lack of introspection, generally being unable to take it easy |
| disappointed | Having a mandate deadline missed |
| disillusioned | An animal was convicted of a crime |
| dislike | Talking to somebody annoying |
| embarrassed | Sleeping without a proper zone, sleeping on a dirt/rocks/cave floor/in the grass, wearing tattered clothes, having no shirt, having no shoes, being uncovered, watching a performance, having to conduct an official meeting in a dining room |
| exasperated | Being caught in the rain, being caught in a snow storm, getting into an argument |
| frustrated | Considering the scarcity of cages and chains, having a mandate ignored, nobody could be punished for a mandate failure, getting into an argument, lack of decent meals, being unable to practice a skill, being unable to practice a craft, being unable to practice a martial art, being unable to pray to {deity}, being kept from alcohol, being unable to acquire something, being unable to wander, being unable to fight, being unable to admire art, lack of abstract thinking, lack of trouble-making, generally leading an unexciting life |
| gloomy | Being out in the sun |
| glum | Getting into an argument |
| grouchy | Being caught in the rain, being caught in a snow storm, being out in the sun, eating the same old food, drinking the same old booze |
| guilty | Being confined, being able to rest and recuperate, being rescued |
| indignant | Being forced to endure the decay of a (dead) friend, delayed punishment of a criminal |
| insulted | Being forced to endure the decay of a (dead) friend, getting into an argument |
| irritated | Being out in the sun, being hungry/thirsty/drowsy, eating at crowded table, wearing old/tattered clothes, sleeping uneasily due to noise |
| isolated | Being unable to find somebody in charge to yell at |
| lonely | Being away from family, being away from friends, being away from people, being unable to make merry, being unable to make romance |
| regretful | Toppling something over, starting a fist fight, throwing something, becoming a parent |
| resentful | Giving somebody water, experiencing trauma, getting into an argument |
| restless | Being able to rest and recuperate, being unable to practice a craft, being unable to practice a martial art, being unable to learn, being unable to use abstract thinking, being unable to argue, lack of trouble-making, doing nothing creative, generally leading an unexciting life |
| self-pity | Being away from family, being away from friends, being unable to argue, being unable to fight, being unable to make merry, being unable to practice a craft, being unable to practice a martial art, being unable to wander, lack of abstract thinking, being unoccupied, doing nothing creative, not learning anything, generally leading an unexciting life |
| uneasy | Being near to hated vermin in a cage, being caught in freakish weather, seeing somebody's dead body, being uncovered, retching on a miasma, being attacked, being attacked by the dead, giving birth to a baby, being unable to pray to {deity}, lack of decent meals, being kept from alcohol, being unable to be extravagant, being unable to help anybody, being unable to admire art, being unable to acquire something, generally being unable to take it easy |
| worried | Lack of decent meals, being kept from alcohol, being unable to pray to {deity}, being unable to be extravagant |
| anguish | Experiencing a miscarriage |
| ashamed | Eating without a chair |
| despair | Being caught in freakish weather |
| disgusted | Retching on a miasma, being nauseated by the sun, drinking water from murky pool, being caught in freakish weather, being forced to eat vermin, being forced to drink vomit, being forced to endure the decay of a (dead) pet, being accosted by hated vermin |
| distressed | Being pestered by flies |
| empty | Having a masterwork destroyed |
| existential crisis | Being unable to advance the study of topic |
| frightened | Being haunted by the dead |
| grieved | Unexpected death of somebody |
| hopeless | Suffering a major injury, being nauseated by the sun |
| humiliated | Eating without a table or chair, wearing tattered clothes, being uncovered, not having any rooms, having a mandate ignored |
| mortified | Being forced to eat vermin |
| panicked | Being attacked, being starving/dehydrated |
| sad | Being separated from a loved one/loved ones, retching on a miasma |
| shaken | Suffering a major injury, being knocked out during cave-in, being forced to endure the decay of a (dead) friend |
| shocked | Being attacked, unexpected death of somebody, having a masterwork destroyed or stolen |
| alarmed | Seeing somebody's dead body |
| afraid | Experiencing trauma |
| angry | Getting into an argument, being forced to endure the decay of a (dead) friend |
| ferocity | Being attacked |
| horrified | Seeing somebody die, seeing somebody's dead body, being caught in a freakish weather, being haunted by the dead, being attacked by the dead |
| loathing | Being out in the sun, being beaten up in the course of dwarven justice or otherwise |
| outraged | Being forced to endure the decay of a (dead) child/spouse |
| terrified | Being in conflict |
| vengeful | Joining an existing conflict |
