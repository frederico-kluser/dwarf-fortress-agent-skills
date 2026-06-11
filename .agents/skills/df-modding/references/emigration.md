# Emigration

> Fonte: [Emigration](https://dwarffortresswiki.org/index.php/Emigration) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This article is about people migrating from your fortress, for the opposite see immigration.*

Emigration or **exile** from your fortress currently happens when you order one of your dwarves to leave. If your fortress has any holdings, you may send them there - otherwise, they will travel to the nearest site of your civilization. Nobles (elected or otherwise) can never be expelled, presumably because they're in charge of the emigration orders in the first place. If you want to get rid of nobles, consider sending them on a mission to occupy a site instead.

Dwarves don't take expulsion orders very well; expect the emigrant's entire family to be upset at your decision. Upset enough, in fact, that their immediate family (and pets) will willingly follow them. To expel a dwarf, click on them, choose  and then "Expel".

## Emigration to holdings

You may choose a specific holding if you have several, and the dwarf's family will reside there, as historical figures. Dwarves sent to a holding can never return in subsequent migrant waves, but if you happen to request workers from the same holding you sent them off to, they may come back. Note that there is no guarantee that they will remain there, as world activities are often tumultuous and they may choose to migrate again, or be killed.

## Expulsion

Dwarves who are expelled from your fortress will settle in the nearest site of your parent civilization and cannot be recalled or return in migrant waves for the current fortress.

## Emigration in DFHack

This DFHack script implements an emigration mechanism, which allows unhappy dwarves to emigrate from the fortress, emigrants may choose to leave with a caravan, diplomat or even on their own. Like with the immigration‎‎ mechanic, the process is entirely outside the control of the player.

A check is run once a month, and the dwarves whose desire to stay (which is directly dependent on their stress level) fails a roll leave the fortress if a diplomat or caravan is present. Roll requirements are harder if they are to leave alone. Contrary to standard emigration, dwarves who leave this way do not take their family with them, and no stress penalty is incurred onto their relatives (apart from the standard "being away from family").

## Bugs

- Any children, including ones out in the world, prevents the exiling of parentsBug:10848
- Expelled dwarves affected by loyalty cascade are not leaving fortressBug:10994
- Expelled citizens leave with hauled items, trigger "thief has stolen" announcementsBug:11038
