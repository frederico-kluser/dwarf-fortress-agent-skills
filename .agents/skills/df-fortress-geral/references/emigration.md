# Emigration

> Fonte: [Emigration](https://dwarffortresswiki.org/index.php/Emigration) — Dwarf Fortress Wiki (GFDL/MIT)

*This article is about people migrating from your fortress, for the opposite see immigration.*

Emigration or **exile** from your fortress currently happens when you order one of your dwarves to leave. If your fortress has any holdings, you may send them there - otherwise, they will be sent into the wilderness. Nobles (elected or otherwise) can never be expelled, presumably because they're in charge of the emigration orders in the first place. If you want to get rid of nobles, consider sending them on a mission to occupy a site instead.

Dwarves don't take expulsion orders very well; expect the emigrant's entire family to be upset at your decision. Upset enough, in fact, that their immediate family will willingly follow them into exile. To expel a dwarf, iew their rofessions, and choose xpel.

## Emigration to holdings

You may choose a specific holding if you have several, and the dwarf's family will reside there, as historical figures. Dwarves sent into exile can never return in subsequent migrant waves, but if you happen to request workers from the same holding you sent them off to, they may come back. Note that there is no guarantee that they will remain there, as world activities are often tumultuous and they may choose to migrate again, or be killed.

## Emigration to the wild

Dwarves sent off to the wild are supposed to never return, so beware in future versions. This option is always available, even if you don't have any holdings. Dwarves who are expelled may return; this is a known bug which will be fixed in future versions.

## Emigration in DFHack

This DFHack script implements an emigration mechanism, which allows unhappy dwarves to emigrate from the fortress, emigrants may choose to leave with a caravan, diplomat or even on their own. Like with the immigration‎‎ mechanic, the process is entirely outside the control of the player.

A check is run once a month, and the dwarves whose desire to stay (which is directly dependent on their stress level) fails a roll leave the fortress if a diplomat or caravan is present. Roll requirements are harder if they are to leave alone. Contrary to standard emigration, dwarves who leave this way do not take their family with them, and no stress penalty is incurred onto their relatives (apart from the standard "being away from family").

## Bugs

- Any children, including ones out in the world, prevents the exiling of parents
- Expelled dwarves affected by loyalty cascade are not leaving fortress
- Expelled citizens leave with hauled items, trigger "thief has stolen" announcements
