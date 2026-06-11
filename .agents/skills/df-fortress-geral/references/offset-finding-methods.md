# Offset Finding Methods

> Fonte: [Offset Finding Methods](https://dwarffortresswiki.org/index.php/Offset_Finding_Methods) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Tools

- Process Table Access (i.e. Win32::Process::List in Perl)
- Memory Access (i.e. Win32::Process::Memory in Perl; ReadProcessMemory in C++)
- Cheat Engine: http://www.cheatengine.org/

## how to identify version

The PE header timestamp is set each time the executable is compiled and is thus unique for each release. It can be consistently found with a few simple steps and thus is far superior in version identification than any other attribute of the DF executable. The steps are as follows:

- get process table, find DF process
- get executable path from process table
- open DF executable in binary mode, confirm first two bytes are "MZ"
- read long at offset 0x3C, this is the PE header offset
- read 2 bytes at PE header offset, confirm they are "PE"
- read long at PE header offset + 0x08, this is the compilation timestamp

## map offset

- start on map with boulder in top left corner
- note distance to top and left. offset of this tile in tile type block is ( 2 \* ( ( x_dist \* 16 ) + y_dist ) )
- find all 2 byte values with 0x0192 in Cheat Engine
- channel out boulder
- click next scan to find all those that changed to 0x0020, should return 1 result; that is offset of type of tile that was just channeled out
- subtract offset of tile in tile type block from overall offset of tile type; this is offset of tile type in tile data block
- subtract 0x007A from that; this is offset of tile data block (if not, first 4-byte offset before the "FF FF 00 00" block in the tile data header)

!!NOT COMPLETE!!

Next step: Identify start and end of the array of tile data blocks in the chosen vertical column.

## Economy status

Find the function using the string "Stocks". It should look like that:

    mov ebx, offset "Stocks"
    mov eax, offset
    call something
    cmp offset_economy, 0
