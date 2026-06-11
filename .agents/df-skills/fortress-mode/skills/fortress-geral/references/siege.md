# Siege

> Fonte: [Siege](https://dwarffortresswiki.org/index.php/Siege) — Dwarf Fortress Wiki (GFDL/MIT)

*For catapults and ballistae, see Siege engine.*

**Sieges** are large-scale assaults on your fortress by other civilizations, and a step beyond ambushes. Sieges are drawn from moving units advancing towards the fortress, whether from an army, a bandit group, or a necromancer's tower "tower"). They are announced with a full-screen message that differs depending on the attacking race, and the main screen showing the tag at the top for the duration of the siege. A siege's objective is to exterminate every dwarf in your fortress, or die trying. It is possible to be sieged by all civilized races, with the exception of kobolds (who never go beyond ambushes) and subterranean animal people (who just don't attack at all). Enemy civilizations will begin to send sieges against your fortress once its population reaches 80 members, with the exception of the undead, who may attack at any time.

Caravans will not arrive at a besieged fortress. They will arrive, though, if a siege is not broken quickly enough - it is possible to miss out entirely on a civilization's caravan for the year this way. Even if they do arrive before the siege, the attackers may kill them or chase them off if they can reach them. Consider this when deciding how you set up your trade depot and how heavily reliant your economy is on imported goods.

A civilization will be unable to lay siege if it can't *reach* your fortress site. Armies need to physically move to the location of your fortress; they are normally allowed a 30-tile radius of interaction (towers have 10 tiles), beyond which sieges are impossible. You will never get sieges if you embark on an island, or in a valley which is completely surrounded by mountains. If you want to make sure that a certain civilization will be capable of laying siege to you, then look at the "neighbors" view of the embark site finder when selecting your fortress site.

## Structure of a siege

- Siege forces usually consist of several 'squads'. Using the goblins as an example, each squad consists of several goblins of one military class (swordsman, lasher, etc.), and often one 'squad leader' (typically an Elite or better, which need not be the same class as the squad being led).
- Occasionally, a squad will be mounted - this means each of its members will be riding a suitable creature, though the creatures typically vary between members. The squad leader can be mounted, even if their squad is not. These mounts can change the combat dynamics, since some can fly, are building destroyers, or have substantially different combat traits than their riders. For more info on mounted units, and the fun they can unleash upon an ill-prepared defender, see: Mount.
- Invaders can climb walls and pits. This can be quite fun, if your fort defense relies on the same kind of walls and pits as previous versions.
- In the pause menu, your retiring option will change from "retire your fortress" to "succumb to the invasion". Choosing this option will lead to the siege succeeding and the dwarves being killed.
- After being sufficiently "successful" at defending against the siege (killing sufficient attackers, waiting them out, or some combination thereof), the attackers will retreat. All of the remaining squads and groups will head for the map edges and leave, typically favoring the edge they entered from. Once all of the remaining attackers have decided to retreat, the tag will go away.
- It is possible to have multiple sieges at the same time. If the attacking civilizations are at war with each other, they will start to fight with each other as well.
- Different races will favor different styles of attack during sieges. The following attack styles were observed in .40d; it remains to be seen if these traits are still present in current releases.
- By default, a max of 120 soldiers and 40 monsters can attack your fortress during a siege. This number can be adjusted in the d_init.txt file.
- You can turn off sieges and forgotten beasts altogether by editing the d_init.txt file to change \[INVADERS:YES\] to \[INVADERS:NO\].
- Depending on how your fortress is set up, winter can be the worst time for a siege due to any outside water being frozen. If your fortress is surrounded by a moat, or is meant to be blocked off by water in some way, your enemies will simply walk over the ice and climb over any walls into your fortress.

## Goblin sieges

Usually, the tactics used by the goblins are no more sophisticated than charging in an open march toward your fortress and attempting to kill your dwarves. Goblin sieges often include groups of trolls and beak dogs, but may also include things like ogres, or cave dragons, that can break buildings and smash workshops. Unlike the squads, however, these 'groups' usually enter the map in a single tile, somewhat akin to arriving migrants. These war creatures usually possess random civilian classes, and show little of the organized behavior of the squads. Goblins may also bring fighters belonging to other races (previously kidnapped by snatchers), and if you're really lucky, they may be commanded by something particularly fun. Goblin sieges usually involve mounted squads, some of which can fly over whatever defenses you might have set up to stop them.

Interestingly, the goblin civilization lacks the token, while large-scale attacks by them nevertheless activate the state. This suggests that the token doesn't regulate the overall ability to send out sieging forces, but merely enables large attacking forces to set up camp and try to wait out a fort, instead of charging in blindly like a pack of fools - the behaviour described in the paragraph on human sieges. Goblins are also the only race who can siege your fortress without their civilization being explicitly at war with your own, presumably because their evil nature makes them disregard diplomacy entirely.

## Elven sieges

It is possible to have elven attacks as well, but that usually requires some effort on the part of the player, or for your starting civilization to have a pre-existing conflict with a nearby elven one. You can check this when you embark while looking at nearby civilizations, where it will read next to the elf civilization, though it seems to be entirely dependent on how world gen plays out and embarking at a time when a war is happening. Another, possibly simpler (and more amusing) way to elven siege is to blatantly provoke them. If you don't want to be attacked by elves you should not offer them wooden goods or goods stored in wooden barrels or bins. You might also avoid clearing too much woodland, as elves will be offended if you do so. Unless you want to be attacked by them, don't send squads to raid their sites in the civilization screen.

Elves use stealth squads, *à la* goblin ambushes, to hide their numbers and locations. It should be noted, however, that unlike goblin ambushes which cap at four squads, elves can come in **massive** numbers, atop mighty (and tasty) unicorns or other exotic beasts. Fortunately, unlike goblins and humans, who wear heavy armor and wield metal weapons that can cause considerable damage, the elves are very weak in battle - their weapons and arrows are made of wood, which will simply bounce off any standard metal armor, and they march into battle wearing easily breakable wooden armor, or even nothing but cloth robes and trousers.

## Human sieges

Humans may also siege you if you let their diplomat die while visiting your fortress; if too many of their trade wagons get destroyed, if you trade with an elven nation the humans are at war with or if you raid their sites. Humans sometimes set up a camp near the map edge they arrived on, harassing wandering dwarves and waiting for you to come to them instead of blindly charging toward your fortress.

Humans often ride rather mundane animals, such as horses, camels (of both varieties), or war grizzly bears, and may bring along further war animals like trained cheetahs. Be aware that human siegers know of all traps that their diplomats have seen before, even their war animals are immune to those traps. If you had a human diplomat in your fort, best assume that your traps are useless against the invaders unless they were built after his last visit. A removed and rebuilt trap counts as "new", even if it's the same type of trap in the same tile.

## Necromancer sieges

Necromancers will only be able to siege you if you embark in an area near a tower "tower"). If no tower is present in the neighbors list, no necromancers will ever besiege your fortress unless you attack them first.

Necromancers will besiege your fortress by sending undead to your fort or even coming themselves. Either way, undead sieges are a guaranteed source of Fun. The undead units will arrive from all sides of the map, slowly meandering towards your fortress. Undead sieges may arrive with as few as one zombie to as many as fifty or more—and if a necromancer is present with them, every dwarf that dies in battle is likely to be revived as a new zombie, complete with all the skills, attributes, and equipment it had in life. The undead in general are serious enemies that one cannot treat like goblin garbage. A legendary squad can take down unarmed zombies in equal numbers, but the large numbers that necromancers can bring are unmatchable. To make things worse, "elite" zombie fighters may carry *weapons and armour*, a truly terrifying thought were there ever one.

While normally human, goblin and elven invaders usually do not have access to steel (with elves not using metal weapons/armour at all), if the original necromancer of the group (the one who was given the slab during worldgen) was a dwarf, it is not uncommon for the undead invaders to use steel. Yes, that means being invaded by steel clad elven zombies with steel swords, for example.

It is recommended that you have many traps every single trap with the best available materials you could possibly build set in advance, and when the undead legions arrive, **shut down everything**. Be sure to shut down all of your butcher's shops, crypts, and refuse stockpiles, as necromancers can reanimate armies of body parts to destroy your fortress from the inside. Be also careful with fishery workshops, as reports of mussel shells rising from the dead are fairly common. Necromancers will raise any corpse or corpse part that they see, and simple proximity to undead can cause things like skin and hair to rise and attack the unfortunate butcher. It doesn't really matter how many zombies arrive; if you are not prepared, you will probably get slaughtered, as one zombie can easily become two zombies, then four, then eight and so on. If the zombies cannot attack your dwarves immediately, they will simply mill about on the surface until something living (wild animals included) comes too close or until they are all destroyed. Like other sieges, it is also possible to wait out necromancer sieges, though this can take a year or more. When fighting zombies that used to be your own dwarves, be sure not to let anyone who knew that dwarf fight them—it generates a strong negative thought on top of the reduction to sanity caused by fighting the living dead. Use blunt weapons whenever possible—a mangled corpse is one that will stay dead, and with no functioning organs to damage, the only other way to stop them is through decapitation or bisection.

Undead sieges can attack your fortress at any time, including before the second spring's elven caravan arrives, or even before the first dwarven caravan arrives in the fall of your first year (thus preventing its arrival). The number of undead sent will depend on your wealth and population, and early sieges tend to have as few as 3 undead—but can cause very much cheesy fun if a lone necromancer accompanies them (which isn't uncommon).

If experiments are brought along, the latter message will be shown. Sometimes these "sieges" of experiments will be very small, consisting of only a few experiments and no necromancer.

## Dwarven sieges

Dwarves of a different entity from yours will normally not interact with your fortress. However, should the player raid the sites of another dwarven civilization, or refuse to give a petitioned legendary artifact if requested, the other dwarves may declare war on yours, leading to dwarven sieges. It isn't possible to be attacked by dwarves of your own entity.

Dwarves employ tactics similar to those of humans during sieges, and employ war beasts and cavalry equivalent to their own or to those used by goblins, as they have access both to above-ground and subterranean resources. Enemy dwarves can be particularly fun to face due to them possessing access to everything the player has, including the likes of steel equipment, and due to being able to enter martial trances much like your own dwarves.

## Bandit sieges

Roving bandit groups nearby your fortress may also besiege it, happening potentially as early as *the first year*, making them an excellent source of surprise fun.

Bandit groups are drawn from any entity with the and tokens. In unmodded games, these are goblins, humans and kobolds, though other races (even dwarves) have been reported. Their announcement messages are the same as the messages for regular sieges of their race. Bandit sieges are generally smaller than a later-game full-blown siege, more similar to goblin ambushes in size, as there are fewer units from which to draw combatants. Bandits tend to be poorly equipped and skilled, some being recruits with no weapons or armour.

## Bugs

- Amphibian invader mounts drown their riders.
- Occasionally sieges will not end with all invaders being dealt with. In such cases the siege seems to end after several months by itself.
