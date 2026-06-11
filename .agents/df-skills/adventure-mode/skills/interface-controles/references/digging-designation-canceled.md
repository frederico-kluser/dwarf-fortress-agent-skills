# Digging designation canceled

> Fonte: [Digging designation canceled](https://dwarffortresswiki.org/index.php/Digging_designation_canceled) — Dwarf Fortress Wiki (GFDL/MIT)

This error message pauses the game and zooms to the location where the warm or damp stone was located.

Warm or damp stone is very dangerous, as it indicates the presence of nearby magma or water, respectively. However, the stone could be warm/damp because the magma/water is beside the tile, directly above the tile, or directly below the tile - and, most of the time, *you don't know which*. You will only know if you are near the surface and find the damp stone below a known murky pool or river.

The safest thing to do is back off several tiles, mine up a z-level then approach the location again. Rinse and repeat until you emerge above the surface of the magma/water. Note that you will not receive warnings when digging staircases upward. If you plan on digging a staircase to a higher z-level, make sure there are no heavy aquifers or magma in your way!

`Side Profile: `\

`   Below tile   Beside tile  Above tile            Key`\

`     #######     #######      #######          # Unmined stone`\
` ↑   __o``#``#``##     ###``##``##      ###``##``##          ``#`` Warm stone`\
` z   ##``#~~#``#     _o``#``~~#``#      ##``#~~#``#          ``#`` Square that was just canceled`\
`axis ##``#~~#``#     ##``#~~#``#      ##``#~~#``#          ``~`` Magma`\
` ↓   ###``##``##     ###``##``##      __o``#``#``##          _ Floor of the tunnel`\
`     #######     #######      #######          o Miner`

Only in the middle case would it be unsafe to mine out the square that had just been canceled: In the first and last cases, there would be a floor between your miner and the fluid.

If the damp stone is due to a light aquifer, the tiles around the damp stone will eventually (but slowly) get filled with water.

The obnoxious recentering and pausing can be stopped by editing announcements.txt and removing `:P:R` from the lines concerning the announcement, so they read:

`[DIG_CANCEL_WARM:A_D:D_D]`\
`[DIG_CANCEL_DAMP:A_D:D_D]`

The job cancellations can be disabled with the utility on  . Note that this can be fun. (This utility no longer works in recent versions, as the addresses it relies on have changed.)

Alternatively, there is a DFhack script to reveal designated tiles which will prevent those designations from being cancelled (since the tiles will already be revealed). This may reduce fun if it reveals water or magma that you actually didn't know was there, so please use responsibly.
