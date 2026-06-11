# Justice

> Fonte: [Justice](https://dwarffortresswiki.org/index.php/Justice) — Dwarf Fortress Wiki (GFDL/MIT)

The **justice** system is present to punish criminals. Justice is administered by a sheriff or captain of the guard, and is used to deal with criminal acts committed in the fortress by citizens or visitors, for example dwarves disobeying their betters, breaking furniture, starting fights, etc.

## Screen

To get to the justice screen, click the Justice menu button or press

### Open cases tab

The Open cases tab has a list of the open cases on the left from oldest to most recent. On the right, details about the selected case are provided, including the injured party (if applicable), the case status (), and the witnesses who reported the crime. There are two buttons which allow the player to interrogate or convict a creature.

### Closed cases tab

The Closed cases tab, similarly to the Open cases tab, has a list of the closed cases on the left from oldest to most recent, with details on the right. However, there are no buttons, and the case status is described as

### Cold cases tab

The Cold cases Tab is the same as the Open cases tab, but only includes cases older than one year.

### Fortress guard tab

The Fortress guard tab contains information on the fortress guard if it exists. At the top is shown the total number of combined cages plus restraints in the dungeon out of the number requested by the fortress guard (approximately one tenth the population). Note that chains includes both ropes and chains.

The rest of the tab is a list of members of the fortress guard, including the cases assigned to each member.

### Convicts tab

The Convicts tab contains of a list on the left of everybody who has been convicted of a crime. On the right, pending sentence(s) for the selected creature are displayed, along with all the crimes they have ever been convicted of.

### Intelligence tab

The Intelligence tab shows information gathered about hostile plots via interrogation.

## Crimes

- **Violation of Production Order** - failing to produce items mandated by a noble.
- **Violation of Export Prohibition** - selling items to a caravan which a noble forbade the export of.
- **Violation of Job Order** - failing to complete guild jobs mandated by the mayor (currently does not happen).
- **Conspiracy to Slow Labor** - deliberately slowing down the workflow of the fortress by delaying jobs (currently does not happen)
- **Murder** - killing a fellow dwarf or tame animal; alternatively, being caught sucking blood out of another dwarf.
- **Disorderly Conduct**, **Building destruction**, **Vandalism** - attacking another dwarf, destroying a building, or toppling furniture or doors during a tantrum.
- **Theft** - a dwarf stole an artifact
- **Espionage** - an agent infiltrated your fortress as a visitor as part of a larger plot (for example, to steal an artifact, or to corrupt a noble).

If a vampire is caught feeding on another dwarf, even if the victim survives, it is still considered a murder. The vampire will typically make a false report, to try to frame another dwarf. Witnesses will also sometimes make false reports to try and frame dwarves they have grudges against.

In some cases, the player has to convict a criminal or suspect, in others, criminals are convicted without player input. In case of mandate infractions, the player is generally not asked for input, while murderers must be convicted by the player. Practically anybody can be blamed for a murder, including tame animals and long-dead persons. However, the populace will feel affronted at particularly nonsensical convictions.

"Violating an export ban" happens when a banned item is sold to a merchant and a merchant leaves the map with it. In this case, the criminal is NOT the trader who authorized the sale, but the hapless hauler who brought the good to the trade depot. It can happens when a noble decides to ban an export **after** you've already traded away a relevant item. Yeah, that's lame, but one way to mitigate it is to not perform trades unless there is an active mandate, and then obey it. You'll have a lower risk of the noble making a NEW mandate between the time merchants arrive and depart if one is already in place. If you've sold an item that subsequently becomes banned, but the merchants haven't left yet, you can also eat your pride and pay to buy it back.

If your dwarves start throwing tantrums, then you'll see the harsher crimes, as they let off steam by throwing items around, breaking furniture, toppling doors, and punching fellow dwarves who are just trying to clean up the mess - instead of punches, sometimes, they may use the weapons they're carrying. Suddenly, keeping those axe lords happy seems a bit more high priority, eh?

Dwarves and others are also variously tempted by e.g. the opportunity to embezzle or accept bribes using the power of their positions. If their personality and values aren't up to the challenge, they may eventually fall to temptation and undertake corrupt activities in an ongoing fashion, which will make them a target for both law enforcement and blackmail.

## Interrogation

Dwarves and friendly visitors can also be interrogated as the suspects of crimes, in which case they are escorted by the Captain of the Guard to their office and questioned. If the interrogation is successful (which is determined by the Captain's various social skills against the target's) the target will confess what they know, whether that is a crime they themselves have committed or their membership of a particular scheming or other villainous organisation, and possibly the names of other members of said organisations; the results are detailed in a report and the target is listed in the Actors tab of the justice menu. Interrogating an innocent dwarf does not have any negative effects, so if you're unsure of a culprit, you could interrogate the entire fort without any repercussions other than lost work time.

You can (and probably should) investigate all new arrivals (immigrants and visitors), as some of them may be there to commit a crime (espionage, theft, etc) or may be under a false name that is guilty of another crime. To do so, there needs to be at least one Open case in the Justice \> Open cases menu. You can click "Interrogate" and then scroll down to the target of investigation. This may result in newly reported crimes in the Open cases tab, and it will result in new data in the Intelligence tab.

## Punishments

Dwarves who misbehave can receive punishments if a sheriff has been assigned. In increasing order of severity (at least that's what the dwarves think):

1.  Beating by a fortress guard (more dangerous than it sounds, see below)
2.  Imprisonment for a period of time.
3.  Hammering by the Hammerer.

The punishment for a crime, or series of crimes, will be issued by the sheriff or by a member of the fortress guard. If the crime calls for imprisonment, then the guard will try to put the prisoner in jail; if no jails are available, the guard will "downgrade" the punishment to a beating, giving the criminal an unhappy thought and the injured party (i.e. the dwarf injured by the criminal, if one exists) a happy thought. If the crime calls for hammer strikes, then the Hammerer will attach the prisoner to a restraint before carrying out the sentence; if no justice restraints are available, the punishment will be downgraded to a beating. All punishments will give the criminal an unhappy thought (and the guard/Hammerer a happy thought).

Note that it is usually not a good idea to train your guards to physical perfection if you want your dwarves to survive beatings: Punches to the head have a very high fatality rate, possibly due to a bug . Therefore it is wise to ensure that any criminals scheduled for beating are fitted with a metal helm as quickly as possible (if you want them to live). Even without headstrikes, beatings can easily result in broken bones or organ damage, making prison sentences a less risky option.

Punishments are performed sequentially; a criminal who has been sentenced to jail time *and* a hammering will not be hammered until the entire jail term has been served.

The level of punishment is determined by the civilisation's Ethics. PUNISH_SERIOUS will result in either a beating or a month in prison PUNISH_CAPITAL will result in either 8 months in prison or 50 hammerstrikes

## Cages and Chains

Metal cages, metal chains, and ropes can be built and designated as jails (uery -\> make a oom -\> use for ustice), where dwarves can be imprisoned for a time as part of their punishment. A dwarf throwing a tantrum may destroy restraints (even metal ones) and escape, leading to further punishment (for building destruction).

Designate a new Dungeon by going to ones, select Dungeon, and then highlight the area of your future dungeon/prison. Once designated, The ustice \> Fortress guard screen will show you how many metal cages and chains are available in the dungeon.

It is also strongly recommended to use chains, not cages, for imprisonment: dwarves on chains are still free to move one step in any direction, allowing them to keep themselves fed and hydrated when food and booze stockpiles or wells are placed adjacent to the chain. Dwarves in cages are entirely dependent on the assistance of others.

## Happiness management

A dwarf that is carelessly tied up in a dank dungeon is subject to several unhappy thoughts. Most can be avoided or offset with some care:

Putting food and booze stockpiles right next to the chain allows for happy thoughts from both instead of having to drink water when (if) someone finally brings some. Don't forget that all civilized dwarves like using a mug/goblet. Decorating your jail with numerous valuable engravings and furniture is helpful too. This includes the chain itself -- prisoners will be happier being shackled with a shiny diamond-encrusted gold chain than tied up with a boring old pig tail rope. Finally, with a bed and a table next to a chair all within a square of the chain itself, negative thoughts approach zero. You can even add a beautiful water well and a soap stockpile so the dwarf can bathe and drink water if necessary.

## Backlog

Crimes do not seem to lapse, so if you've delayed appointing the "executive" nobles for some time, there might be a long list of delinquents and open sentences pending. The law will swiftly proceed to chaining up all delinquents and, once all chains are occupied, beating up any remaining free "criminals". Therefore, beatings are avoided only by constructing restraints first, and possibly way more than recommended in the z-screen.

## Exemption

Creatures are exempt from the justice system if they are any of the following:

- Dead
- Insane
- In a strange mood
- A child or a baby
- Non-humanoid (animals are exempt)
- A local position holder with

In the Dwarven justice system, the Dwarves are oppressed by two separate yet equally obstinate nobles: the sheriff, who investigates crimes, and the hammerer, who beats the living %#(\* out of the offenders. These are their stories.

"Thank god I only got assigned a long-term jail time followed by a hammering. My partner in crime was assigned to a guard beating, poor bastard's head got pulped after one punch." -Urist Mc. Murderhobo.
