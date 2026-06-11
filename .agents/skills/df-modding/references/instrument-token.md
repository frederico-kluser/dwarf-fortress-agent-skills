# Instrument token

> Fonte: [Instrument token](https://dwarffortresswiki.org/index.php/Instrument_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

Instruments are procedurally generated for each world, but if so desired, it is still possible to define custom instruments in the raws by using an \[ITEM_INSTRUMENT\] token. Most tool tokens can be used, but there are also a few instrument-specific tokens, as listed in the table below.

The information on this page is sourced from the file `raw/objects/examples and notes/item_instrument_example.txt`, which also includes useful example instrument definitions.

## Tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  PLACED_AS_BUILDING |  | Makes the instrument stationary. |
|  DOMINANT_MATERIAL_PIECE | instrument piece | Sets a piece as the central part of the instrument. |
|  INSTRUMENT_PIECE | token / tool token / singular / plural / STANDARD / ALWAYS_PLURAL / ALWAYS_SINGULAR | Defines an instrument piece. / token / is the identifier that can be used in other raw tags to refer to this instrument piece. / tool token / is the tool which is required (and consumed) during the construction process to create this instrument piece. / If an instrument does not have any pieces, SELF can be used for any argument which needs to be an instrument piece. |
|  VOLUME_mB | min / max | The instrument's volume range, in millibels (100 mB = 1 dB). |
|  SOUND_PRODUCTION | various tokens | Defines how a musician can produce sound when using this instrument. Can be used multiple times. Valid tokens and their required additional arguments are: / PLUCKED_BY_BP, PLUCKED (requires two tokens, actor then target) / BOWED (two tokens) / STRUCK_BY_BP, STRUCK (two tokens) / VIBRATE_BP_AGAINST_OPENING / BLOW_AGAINST_FIPPLE, BLOW_OVER_OPENING_SIDE, BLOW_OVER_OPENING_END, BLOW_OVER_SINGLE_REED, BLOW_OVER_DOUBLE_REED, BLOW_OVER_FREE_REED / STRUCK_TOGETHER, SHAKEN / SCRAPED (two tokens), FRICTION (two tokens) / RESONATOR / BAG_OVER_REED (two tokens), AIR_OVER_REED (two tokens), AIR_OVER_FREE_REED (two tokens), AIR_AGAINST_FIPPLE (two tokens) |
|  PITCH_CHOICE | method | Defines how the pitch can be varied by the musician. Can be used multiple times. Valid methods are: / MEMBRANE_POSITION / SUBPART_CHOICE / KEYBOARD / STOPPING_FRET (requires two tokens, first for "string" second for "neck" -- or whatever is being pressed against what), STOPPING_AGAINST_BODY (two tokens), STOPPING_HOLE, STOPPING_HOLE_KEY / SLIDE / HARMONIC_SERIES / VALVE_ROUTES_AIR / BP_IN_BELL / FOOT_PEDALS (two token, first is what is being changed e.g. "strings", second is "body" which has pedalboard -- or whatever piece is being stepped on) |
|  TUNING | method / instrument piece | Can be used multiple times. Valid methods are: PEGS, ADJUSTABLE_BRIDGES, CROOKS, TIGHTENING, LEVERS. |
|  PITCH_RANGE | min pitch / max pitch | From the example file: / Pitch is / : / in cents with middle C at zero. There are 1200 cents in an octave. The game verbally differentiates values from -4200 to 4200, but you can go outside that if you like. The in-game generated instruments will range from roughly C0 to C8 (-4800 to 4800), sometimes beyond for really unusual ones. / You can also use INDEFINITE_PITCH. |
|  INDEFINITE_PITCH |  | May replace [`[PITCH_RANGE]`](/index.php/Instrument_token#PITCH_RANGE "Instrument token"). |
|  TIMBRE | any number of timbre words | Valid timbre words are: CLEAR, NOISY, FULL, THIN, ROUND, SHARP, SMOOTH, CHOPPY, STEADY, EVOLVING, STRONG, DELICATE, BRIGHT, GRACEFUL, SPARSE, BREATHY, STRAINED, BROAD, LIGHT, MELLOW, WOBBLING, FOCUSED, EVEN, FLUID, VIBRATING, QUAVERING, EERIE, FRAGILE, BRITTLE, PURE, PIERCING, STRIDENT, WAVERING, HARSH, REEDY, NASAL, BUZZY, ROUGH, WARM, RUGGED, HEAVY, FLAT, DARK, CRISP, SONOROUS, WATERY, GENTLE, SLICING, LIQUID, RAUCOUS, BREEZY, RASPY, WISPY, SHRILL, MUDDY, RICH, DULL, FLOATING, RINGING, RESONANT, SWEET, RIPPLING, SPARKLING. |
|  REGISTER | min pitch / max pitch / any number of timbre words | See PITCH_RANGE and TIMBRE for possible values. The pitch range overrides the global pitch for a register, but the register timbres are added to the global ones. |
|  MUSIC_SKILL | skill token | Which skill should be trained by playing the instrument. Any skill token is valid, but the in-game generated instruments only use PLAY_KEYBOARD_INSTRUMENT, PLAY_STRINGED_INSTRUMENT, PLAY_WIND_INSTRUMENT, or PLAY_PERCUSSION_INSTRUMENT. Levels in this skill do not seem to have any effect on the quality of music produced. Can only be used once. |
|  DESCRIPTION | description | A general description of the completed instrument. Multiple \[DESCRIPTION\] tokens can be used in the same definition, with each appearing on a new line. |
