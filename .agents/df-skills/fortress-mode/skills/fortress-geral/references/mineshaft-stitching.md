# Mineshaft stitching

> Fonte: [Mineshaft stitching](https://dwarffortresswiki.org/index.php/Mineshaft_stitching) — Dwarf Fortress Wiki (GFDL/MIT)

When using mine shafts, dwarves will prefer to dig all of one level before moving on to the next. This can result in a lot of time spent moving, as miners go up and down mine shafts. If you have a large number of relatively-unskilled miners, this is unlikely to be a problem: digging time will dominate in any case. If you have one or two legendary miners, this is quite annoying. As a solution, you can create a single path that forces the dwarves to finish one shaft before moving on to the next. To do so, connect shafts alternately at the top and bottom layers, so the shaft snakes through the area. For example, the top, middle, and bottom layers could look like:

▒▒▒▒▒▒▒▒▒ .X▒▒X..X▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒ ▒X..X▒▒X▒ ▒▒▒▒▒▒▒▒▒

▒▒▒▒▒▒▒▒▒ ▒X▒▒X▒▒X▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒ ▒X▒▒X▒▒X▒ ▒▒▒▒▒▒▒▒▒

▒▒▒▒▒▒▒▒▒ ▒X▒▒X▒▒X▒ ▒.▒▒.▒▒.▒ ▒.▒▒.▒▒.▒ ▒X▒▒X▒▒X▒ ▒▒▒▒▒▒▒▒▒

Clearly you can repeat the middle layer as often as you want: I recommend at least 5-10 levels to really make this worthwhile. Note that this pattern creates a very long walkway back to the start of the mineshafts. If you do not excavate routinely, consider connecting the top-level paths of areas you have already explored.

### AHK script

An AHK script to construct such a pattern is provided below, based on this script, but using many fewer keystrokes, constructing only necessary stairs at the top and bottom, and capable of being cancelled at any time.

In the previous version of DF, there was an alternate version here. It has not been tested for 2010, but there is no reason it shouldn't work.

     ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
     ; stitching.ahk                       ;
     ; this is an ahk script to place exploratory mine shafts. ;
     ; press d and place the cursor                ;
     ; in the top left corner of the area to be explored       ;
     ;                                     ;
     ; Alt+Shift+c to change parameters            ;
     ; Alt+Shift+s to run                          ;
     ; Ctrl+c cancel anytime                   ;
     ;                             ;
     ; NOTE:                               ;
     ; Author: Seth Fogarty                        ;
     ; Based on a script by StrawberryBunny            ;
     ; Bug fix from Corey Amend                ;
     ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    x = 4
    y = 4
    depth = 3
    wait =  100
    spacing = 1

    DropShaft(vertdir, depth, wait)
    {
            if (vertdir = ">")
        {
            Send j
        }
        else
        {
            Send u
        }
        Send {Enter 2}i
        tmp := depth -1
        Loop %tmp%
        {
            Send %vertdir%{Enter 2}
            Sleep %wait%
        }
            if (vertdir = ">")
        {
            Send %vertdir%u{Enter 2}
        }
        else
        {
            Send %vertdir%j{Enter 2}
        }
    }

    $+!c::
    inputbox x, Input Length, Vertical pattern length: x-axis
    inputbox y, Input Width, Horizontal pattern width: y-axis
    inputbox depth, Input Depth, Mineshaft depth: z-axis
    inputbox spacing, Input Spacing, Spacing multiplier (1 for complete visiblity)
    inputbox wait, Input Delay, Delay in miliseconds (100 recommended)
    return

    $^c::
      Critical
      ExitApp
      return

    $+!s::
    shafts := (x * y) -1
    vdir = >
    i := x-1
    hdir = {Down}
    next = {Up}

    Loop %shafts%
    {
        DropShaft(vdir, depth, wait)
            if (vdir = ">")
        {
            vdir =
        }
        k := spacing-1
        Send d%hdir%{Enter}
        Loop %k%
        {
            Send %hdir%{Enter}%hdir%{Enter}%hdir%
            Sleep %wait%
        }
        Send %hdir%{Enter}%hdir%
        Sleep %wait%
        i--
        if (i = 0)
        {
            if (hdir = "{Down}")
            {
                hdir = {Right}
                next = {Up}
                i=1
            }
            else if (hdir = "{Right}")
            {
                hdir = %next%
                i := x-1
            }
            else if (hdir = "{Up}")
            {
                hdir = {Right}
                next = {Down}
                i=1
            }
        }
    }
    DropShaft(vdir, depth, wait)
    if (vdir = ">")
    {
        Loop %depth%
        {
            Send <
        }
    }
    return

\]\] \]\]
