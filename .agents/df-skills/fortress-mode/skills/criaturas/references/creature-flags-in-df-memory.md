# Creature flags in DF memory

> Fonte: [Creature flags in DF memory](https://dwarffortresswiki.org/index.php/Creature_flags_in_DF_memory) — Dwarf Fortress Wiki (GFDL/MIT)

## Creature or Unit flags

Thanks to ToadyOne for explaining what these bits do.

Checkbox labels

### Flags Word 0 (32 bits)

| Bit | Integer Value (hex) | DwarfCompanion | Meaning |
|----|----|----|----|
| 0 | 0x00000001 | 0x1 | Can the dwarf move or are they waiting for their movement timer |
| 1 | 0x00000002 | dead? | Dead (might also be set for incoming/leaving critters that are alive) |
| 2 | 0x00000004 | 0x4 | Currently in mood |
| 3 | 0x00000008 | artifact | Had a mood |
| 4 | 0x00000010 | 0x10 | "marauder" -- wide class of invader/inside creature attackers |
| 5 | 0x00000020 | 0x20 | Drowning |
| 6 | 0x00000040 | merch1? | Active merchant |
| 7 | 0x00000080 | caravan guard? | "forest" (used for units no longer linked to merchant/diplomacy, they just try to leave mostly) |
| 8 | 0x00000100 | 0x100 | Left (left the map) |
| 9 | 0x00000200 | 0x200 | Rider |
| 10 | 0x00000400 | !unitlist | Incoming |
| 11 | 0x00000800 | liaison? | Diplomat |
| 12 | 0x00001000 | zombie | Zombie |
| 13 | 0x00002000 | skel | Skeleton |
| 14 | 0x00004000 | working? | Can swap tiles during movement (prevents multiple swaps) |
| 15 | 0x00008000 | prone | On the ground (can be conscious) |
| 16 | 0x00010000 | 0x1.4 | Projectile |
| 17 | 0x00020000 | inv1 | Active invader (for organized ones) |
| 18 | 0x00040000 | hidden | Hidden in ambush |
| 19 | 0x00080000 | inv2 | Invader origin (could be inactive and fleeing) |
| 20 | 0x00100000 | 0x1.5 | Will flee if invasion turns around |
| 21 | 0x00200000 | 0x2.5 | Active marauder/invader moving inward |
| 22 | 0x00400000 | 0x4.5 | Marauder resident/invader moving in all the way |
| 23 | 0x00800000 | 0x8.5 | Check against flows next time you get a chance |
| 24 | 0x01000000 | 0x1.6 | Ridden |
| 25 | 0x02000000 | 0x2.6 | Caged |
| 26 | 0x04000000 | tame | Tame |
| 27 | 0x08000000 | 0x8.6 | Chained |
| 28 | 0x10000000 | r.guard | Royal guard |
| 29 | 0x20000000 | f.guard | Fortress guard |
| 30 | 0x40000000 | 0x4.7 | Suppress wield for beatings/etc |
| 31 | 0x80000000 | 0x8.7 | Is an important historical figure |

### Flags Word 1 (32 bits)

| Bit | Integer Value (hex) | DwarfCompanion | Meaning |
|----|----|----|----|
| 0 | 0x00000001 | 0x1b | Swimming |
| 1 | 0x00000002 | 0x2b | Play combat for sparring |
| 2 | 0x00000004 | 0x4b | Do not notify about level gains (for embark etc) |
| 3 | 0x00000008 | 0x8b | Unused |
| 4 | 0x00000010 | 0x10b | Nerves calculated |
| 5 | 0x00000020 | 0x20b | Body part info calculated |
| 6 | 0x00000040 | 0x4b | Is important historical figure (slight variation) |
| 7 | 0x00000080 | dead | Has been killed by kill function (slightly different from dead, not necessarily violent death) |
| 8 | 0x00000100 | vanish | Must be forgotten by forget function (just cleanup) |
| 9 | 0x00000200 | 0x200b | Must be deleted (cleanup) |
| 10 | 0x00000400 | 0x400b | Recently forgotten (cleanup) |
| 11 | 0x00000800 | 0x800b | Offered for trade |
| 12 | 0x00001000 | 0x1000b | Trade resolved |
| 13 | 0x00002000 | winded? | Has breaks |
| 14 | 0x00004000 | 0x4000b | Gutted |
| 15 | 0x00008000 | ground | Circulatory spray |
| 16 | 0x00010000 | flying | Locked in for trading (it's a projectile on the other set of flags, might be what the flying was) |
| 17 | 0x00020000 | slaughter | Marked for slaughter |
| 18 | 0x00040000 | underwrld | Underworld creature |
| 19 | 0x00080000 | can't eat | Current resident |
| 20 | 0x00100000 | 0x1.5b | Marked for special cleanup as unused load from unit block on disk |
| 21 | 0x00200000 | 0x2.5b | Insulation from clothing calculated |
| 22 | 0x00400000 | 0x4.5b | Uninvited guest |
| 23 | 0x00800000 | visitor? | Visitor |
| 24 | 0x01000000 | 0x1.6b | Inventory order calculated |
| 25 | 0x02000000 | 0x2.6b | Vision -- have good part |
| 26 | 0x04000000 | 0x4.6b | Vision -- have damaged part |
| 27 | 0x08000000 | 0x8.6b | Vision -- have missing part |
| 28 | 0x10000000 | 0x1.7b | Breathing -- have good part |
| 29 | 0x20000000 | winded? | Breathing -- having a problem |
| 30 | 0x40000000 | 0x4.7b | Roaming wilderness population source |
| 31 | 0x80000000 | tame2 | Roaming wilderness population source -- not a map feature |

\]\]
