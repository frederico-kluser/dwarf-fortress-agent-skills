# Topic

> Fonte: [Topic](https://dwarffortresswiki.org/index.php/Topic) — Dwarf Fortress Wiki (GFDL/MIT)

**Topics** (also **Tech** or **Innovations**) are part of knowledge.

There are around 300 innovations that can be discovered. Many of them have requirements, and many do not, so it's kind of a tech forest/grassland rather than a tree. Notably missing are innovations related to practical labors in the game (which will be added later in development). Only the discovery of literary form topics has any effect on gameplay, as it allows scholars to write new types of books.

Several innovations require innovations from other branches, and since all knowledge is individually tracked, that implies some investigators will need to be at least well-read if not skilled in various topics (there aren't currently joint research projects). There are some old and new mechanisms in place to ensure this happens.

There are 9 "branches" of the knowledge system. Each branch is further divided into categories of topics, such as methodologies, theories, etc.

## Discovering Topics

According to a Future of the Fortress reply:

> Fortress scholars do activity cycles, the length of which is 1-2 days (whether they are pondering or discussing etc.) Once they get through 50 cycles, it rolls 0-50 vs. the number of completed cycles minus 50 to see if they get "breakthrough credit." So at 51, they have a 2% chance, and at 100, they have a 100% chance. Then, it resets the cycle number to zero and gives them breakthrough credit, based on a skill roll plus 100 (for discuss, the other researchers contribute half of their summed skill rolls.) Based on the difficulty (1-4) of the topic, total lifetime breakthrough credit is then assigned a number of 50-sided dice. An easy topic is dice=credit/2500, then /5000, then /10000, then /20000 for level 4 topics. The number of dice cannot exceed 10. Then roll these dice -- if you get a 50 on any of them, discovery! This is a bit archaic, and I'm not suggesting it works particularly well. But that is how it works. Also: if they fail to get the breakthrough after the 50-sided rolls, they have a 2% chance of switching topics, or if their credit exceeds 100000, they always switch topics (though they keep the credit, so returning to the topic later gives them a decent chance at breakthrough.)

For unskilled roles, some initial back-of-the-envelope calculations and some rough estimates observed through dfHack gives a basic idea of just how long research can take. Note that player testing had found that the skill roll contributes a lot to the breakthrough credit. Even dabbling dwarfs can gain over 2000 breakthrough credit at once and may average around 1000 breakthrough credit. Additionally the formula for the skill roll seems to have a very large spread, players have reported as low as 3000 breakthrough credit and as high as 25000 breakthrough credit awarded to a dwarf with legendary skill. Analytically calculating from the algorithm Toady gave, it takes an average of 58.54 cycles to get a breakthrough credit. Player testing has confirmed breakthrough credits typically take 55-65 cycles, so this calculation seems plausible. Likewise, player testing has not shown any correlation between skill level and number of cycles to get breakthrough credit. An unskilled dwarf might average around 120+ cycles to get their first breakthrough die for a level 1 topic. With only a single research die, it would take an average of 2528 cycles to get a breakthrough. Pondering takes slightly over 2 days per cycle, so this would be around 14 years. In a real fortress, the research dice and skill level will be increasing during the process. However, in a real fortress, the scholars will also need to take breaks to eat, drink, and meet other needs. A more reasonable estimate is around 5-10 years for a breakthrough starting with no skills. In short, research takes an unreasonably long time with an unskilled dwarf.

To optimize for research, there are several ideas worth considering. Discussion is faster, taking only a single day, but requires at least 2 dwarves. Player testing has found discussion also awards more XP, (0-5 for pondering vs. 15-30 for discussion). So to optimize research, dwarves should be separated by topic/skill, with unskilled dwarves paired with skilled dwarves. This way, discussions will be equally divided between increasing the skilled dwarf's cycle count and the unskilled dwarf's cycle count. Only half the cycles will go to the skilled dwarf's cycle count, but discussion only takes a single day, so this is at net the same speed for the skilled dwarf with the additional bonus of the unskilled dwarf's cycle count also being increased. Both dwarves benefit from the increased XP gain.

Note that several topics benefit from skills that can be trained through faster means. Diagnostician and Wound Dresser can be trained through intentionally causing injuries or simply engaging in dangerous activities that require regular dwarf healthcare. Organizer can be trained through assigning make work to the manager, or Mechanic can be trained by spamming the creation of mechanisms. Skill level will increase much faster through these activities than through pondering or discussion. Thus, to optimize for producing breakthroughs in engineering topics, mechanics could first be quickly trained to a legendary within a year or two at only the cost of the stones for the mechanisms, and then assigned as a scholar.

Player testing has also found that visitors can come with research credits already done, thus, for forts aiming to maximize research, it makes sense to prioritize attracting wandering scholars.

## Astronomy

These topics are relevant to astronomers.

## Chemistry

These topics are relevant to chemists.

## Engineering

These topics are relevant to engineers.

## Geography

These topics are relevant to geographers.

## History

These topics are relevant to critical thinkers.

## Mathematics

These topics are relevant to mathematicians.

## Medicine

These topics are relevant to many medical professions, including doctors and diagnosticians.

## Nature

These topics are relevant to naturalists and trackers.

## Philosophy

These topics are relevant to logicians.

If visitor scholars are allowed in a library, one should regularly check all books for nature-related value agenda to prevent fortress citizens from wandering off to start a dwarven forest retreat.

 Ru:Topic
