# Historical figure

> Fonte: [Historical figure](https://dwarffortresswiki.org/index.php/Historical_figure) — Dwarf Fortress Wiki (GFDL/MIT)

In world generation, due to memory constraints, most population numbers have to be treated abstractly. However, a small percentage of the population is treated explicitly, i.e. the game keeps track of all of their history. These people are called **historical figures**, or *histfig* for short.

Historical figures mainly relate to what is abstractly offloaded (i.e. forgotten) or explicitly tracked by the game. The game can't keep track of every single creature in the world, but it has to keep things interesting for your fortress, adventurer, or legends; as such, there are a number of rules that define who gets to become a historical figure and who doesn't. These rules are mostly there to guarantee a consistency of gameplay experience, so that people you encounter don't suddenly disappear from the game as they are offloaded. In other words, the game generates everything for you as you explore the world - *except* for historical figures, artifacts and what pertains to them; and vanishes everything as you leave a site - *except* for that which is related to historical figures and artifacts, including newly-generated ones.

## In world generation (and after)

In each site, a percentage of the actual population is tracked: this includes nobility and their entourage. Their family relationships, titles and heroic feats (e.g. kill lists) are stored for you to discover. All (semi-)")megabeasts, unique demons, forgotten beasts, titans and other such creatures are historical figures, as are other villainous creatures such as necromancers, vampires, werebeasts, night trolls, or bosses of criminal organisations (along with all their families and other such relationships). Likewise, animals that somehow become enemies of a civilization (usually for killing a few members) become historical figures.

## In fortress mode

Your seven starting dwarves are generated *ex nihilo* (out of nothing - "void dwarves"). However, all fortress citizens become historical figures as they appear, and the game will keep track of them if they leave the site, or you retire or abandon your fortress. The game attempts to pull subsequent migrants from actual histfig populations, but it will continue to generate 'void dwarves' as necessary. Caravans and invasions can instantiate non-historical populations, though those generated creatures may become historical figures during their time on site. Nobles (including diplomats and liaisons), workers requested from holdings, and visitors will generally only be selected from existing historical figures.

Wildlife is abstracted away, except if an animal gets a name for some reason (e.g. killing one of your dwarves), in which case they also become a historical figure. If a creature's hist_figure_id is not equal to -1, then by definition it is a historical figure. It's possible that the act of training a creature makes it into a histfig, perhaps in order to assign entity/site membership to it.

## In adventure mode

Similarly to fortress mode's starting seven, your adventurer is also generated *ex nihilo*, but becomes a historical figure upon entering the game. Every time the local map is offloaded, all units, including your adventurer, are also offloaded and re-initialized from historical figure data. This is why, whenever sleeping/waiting, fast-traveling, composing, crafting, or site-building, all non-permanent wounds are healed (though some are converted to scars) and stomach fullness and intoxication is reset.

Anyone with a name who the adventurer encounters also becomes a historical figure, if they weren't already. This includes companions, the people you take quests from, the people in your kill list, and people (or animals) you talk to. It should also be noted that anyone you encounter that wasn't a historical figure already is going to be a complete blank slate, with almost no knowledge of anything--for example, they won't know about any of the enemies or beasts you've slain (even the most basic animals such as cats and dogs) if you don't tell them. This leaves the impression that no one cares about your achievements you brag about - they would if they had any idea who you were talking about.

## In legends mode

You may browse the history of every single histfig in the world, as well as their relationships with other histfigs. Special objects of note (namely artifacts and other such objects that have gotten a name from one of your dwarves or adventurers) also have their history tracked.
