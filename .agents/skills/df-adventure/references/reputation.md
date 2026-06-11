# Reputation

> Fonte: [Reputation](https://dwarffortresswiki.org/index.php/Reputation) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Reputation, or **fame**, is an invisible metric that tracks how well-known or fearsome your adventurer is. Reputation directly impacts the quality and difficulty of quests you will receive, the number of companions willing to join you, or whether bandits will directly attempt to target you. A certain level of reputation also allows you to get tavern services for a lower (or free) price and vice-versa.

## Increasing your reputation

### Quests/Rumors

The most straightforward way to increase reputation is to perform quests, and report back to whoever sent you off; which can range from killing some mundane animal (like a dingo), to neutralizing a bandit camp, or outing a vampire in hiding. As your reputation increases, you will be tasked to complete more serious quests, such as slaying a megabeast on the other side of the world. If you are a hearthperson or a subordinate to some kind of lord, you may repeatedly ask your superior for quests and build up a reputation as a loyal soldier. Or, if you are not a subordinate to anybody and don't wish to be, you can simply use rumors to brag about your feats - slay some beast, bandit or night creature and bring up the incident in a conversation, and let the rumor system do the work. Alternatively, you may tell the story of your feats in a performance, and spectators will spread the story for you.

## Types of reputation

There are currently 32 sorts of reputation, with corresponding titles, EG. "Preserver of Knowledge" for returning a book to a library, but they aren't equal or even necessarily numeric. (It's all handled dynamically based on incident/rumor/entity-membership knowledge, so it can be slippery to pin things down, especially in cases where somebody has died, since people can go a few levels deep to ascertain what they think about that, and still too often end up with nothing). Once events/etc. go stale, a simple numeric reputation is captured for those events, and that lives inside entities and historical figures that are thinking about a given person (some events are entity-level, some histfig-level, some both.) The utterances are shifted in ranges 1-24, 25-49, 50-74, 75-99, 100+ oftentimes, so, many reputations have five verbal levels. So for example, you get 25 hero points for reuniting two people if the thinker has a positive feeling about either of them, or positive entity affiliation with either - you get 100 hero points from either of the reunited people regardless of affiliation, whereas an entity itself gives you a hero rep for reuniting people with positions, and that is felt by all members.

Depending on the feats you've accomplished, your type of reputation may differ: slaying bandits will earn you the title of "protector of the weak", while doing your hearthperson duty will make you known as a "loyal soldier", or retrieving artifacts for claimants will make you known as a "Treasure Hunter". On the other hand, if you become known as a thief or a murderer who indiscriminately massacres citizens, people will refuse to speak to you and spit on you. Therefore, it may be desirable to avoid, or at least control, rumor-spreading. The scale goes from 0 to 100: for instance, in the "hero" scale, you will be known as a "Famous Hero" between 75 and 99, and a "Legendary Hero" at 100.

The 32 sorts are:

|  |  |
|----|----|
| Reputation type | Obtained through |
| Hero | Ending an unjust situation. This varies a lot between people, as stated in the example of reuniting people. |
| Friend | Unobtainable in adventure mode, but can be obtained in fort mode. Tracks friendships. |
| Grudge | Unobtainable in adventure mode, but can be obtained in fort mode. Tracks grudges. |
| Bonded | Reserved for trainers/animal training partners. Can be obtained by training animals in fort mode. |
| Brawler | Starting a battle with a person at brawl escalation level. |
| Psychotic/Villain | Starting a battle with a person at no-quarter escalation level. |
| Good for Business | Make a successful transaction with a trader. |
| Friendly Terms | Have a conversation with a figure. It is unknown if quarreller or flatterer rep has any effect on this. |
| Killer | Killing any sentient creature. |
| Murderer | Killing an innocent. |
| Comrade | Defines the bond between a person and their liege-lord, or of two oathsworn of the same lord. |
| Member of Respected Group/Member of Hated Group | Reserved for members of entities that are, respectively, considered 'worthy of respect' or 'unfit to rule'. Related to the insurrection mechanic. |
| Enemy Fighter | Reserved for fighters of an enemy group. You get this when asking what people think of you during a conflict, or when you attacked a member of the same group. |
| Friendly Fighter | Corresponds to 'on my side' utterance, implies that the figure considers you someone who they otherwise are unconnected to, but is the enemy of their enemy.\[Verify\] |
| Bully | Making someone successfully yield in adventure mode. |
| Brigand | Demanding items in exchange (will be labelled as robbery). |
| Loyal Soldier | Finishing hearthperson assignments. |
| Monster | Reserved for megabeasts and other named animals, not possible to obtain in unmodded DF.\[Verify\] |
| Storyteller/Poet/Bard/Dancer | Telling a story, reciting poetry, performing a piece of music, or performing a dance in front of a person. |
| Quarreler | Unknown, presumably obtained by pressing or arguing when a disagreement is reached through a value statement Bug:11193. |
| Flatterer | Obtainable by failing to flatter a figure repeatedly. Bug:11193. |
| Hunter | Slaying a named animal, or a megabeast. |
| Protector of the Weak | Standing up to bandits. This includes attacking them (and failing...), brawling with them, or slaying them outright. |
| Treasure Hunter | Retrieving an artifact for a claimant. |
| Thief | Seems unobtainable right now Bug:6391. |
| Information source | This is reserved for spies who form false friendships; they will think of their 'friend' this way. Unknown how to obtain this in adventure mode. |
| Preserver of Knowledge | Returning a book to a library. |
| Intruder | Obtained by not identifying yourself to people that ask you to identify yourself, marking the whole entity as hostile to you. |
| Preacher | Obtained by performing sermons. |

## Controlling your reputation

You may assume multiple identities as an adventurer. Starting over with a fresh identity will reset your reputation if people don't know you under your previous name. Alternatively, if witnesses see you murder someone, you may try to kill all of them before the site is offloaded (which is a requirement for the rumor system to start working). Or you may move to another civilizational entity entirely, where your reputation does not follow you. So if you ask after a goblin agent using their true name or an identity used in a previous town, people in the current town the agent is infiltrating will properly say that they don't know who you are talking about, even if they have a lot of information about the agent under their current alias -- or they might have an opinion about the old identity if they heard a rumor about it. People can give different answers for the true historical figure and each identity, as well as what they think on sight (which may or may not involve any names -- they keep track of which identities they associate with the physical appearance).

## Trivia

- If your reputation becomes exceptionally high ("Famous Hero", so above 75), bandits trying to ambush you will say "Ha-ha-halt!" instead of the normal announcement message, presumably stammering in front of such a supposedly-fearsome figure. An exception is if they have [`[NOFEAR]`](/index.php/Creature_token#NOFEAR "Creature token").
