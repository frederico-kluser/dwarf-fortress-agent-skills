# Emotion

> Fonte: [Emotion](https://dwarffortresswiki.org/index.php/Emotion) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Certain circumstances can evoke a wide range of **emotions**, both negative and positive, affecting dwarves' stress levels. Emotional reactions can result from immediate experience, or from revisiting a long-term memory, and are affected by dwarves' personalities and values, resulting in different reactions to the same circumstances. Recent emotions experienced by dwarves (listed along with their circumstance pairs) are listed in the Thoughts and Preferences screen.

Different thoughts can have different "strength", denoting the effect the emotion has on a dwarf's stress levels (negative numbers reduce stress, while positive numbers increase it) and depends on time elapsed and dwarven personality. This thought strength is then divided by the 'Divider' numbers given in the table. The thought strength is loosely color-coded, with positive thoughts being in blue or green and strong negative thoughts being in red or yellow. Brown thoughts are mildly to moderately negative, and purple and grey ones are pretty much neutral.

Note that positive thoughts have a *negative* number, as they *reduce* stress. Numbers closer to 1 or -1 have the strongest effect on stress.

Many examples of a dwarf feeling emotions are as follows:\

Syndromes can cause a creature to feel particular emotions using the CE_FEEL_EMOTION tag. When a creature's stress level is high enough, certain negative emotions may create additional effects. These emotions will display a string in the dwarf's General status screen.

A total of 170 emotions are defined within the code, but only 130 of them are currently implemented:

|  |  |  |  |
|----|----|----|----|
| ID | Emotion | Divider | Additional text / Effects at high stress |
| -1 | Anything | 0 |  |
| 0 | Acceptance | -8 |  |
| 1 | Adoration | -1 |  |
| 2 | Affection | -2 |  |
| 3 | Agitation | 4 |  |
| 4 | Aggravation | 4 |  |
| 5 | Agony | 1 | "Writhing in agony!" |
| 6 | Alarm | 4 |  |
| 7 | Alienation | 8 |  |
| 8 | Amazement | 0 |  |
| 9 | Ambivalence | 0 |  |
| 10 | Amusement | -4 |  |
| 11 | Anger | 2 |  |
| 12 | Angst | 1 | "In existential crisis!" Creature will lie on the ground, pondering the meaning of life, and will not move. |
| 13 | Anguish | 1 | "Anguished!" Creature will lie on the ground crying and will not move. |
| 14 | Annoyance | 8 |  |
| 16 | Anxiety | 4 |  |
| 17 | Apathy | 0 |  |
| 19 | Arousal | -8 |  |
| 20 | Astonishment | 0 |  |
| 22 | Aversion | 4 |  |
| 23 | Awe | 0 |  |
| 24 | Bitterness | 2 |  |
| 25 | Bliss | -1 |  |
| 26 | Boredom | 8 |  |
| 27 | Caring | -2 |  |
| 29 | Confusion | 8 |  |
| 30 | Contempt | 4 |  |
| 31 | Contentment | -8 |  |
| 34 | Defeat | 2 |  |
| 35 | Dejection | 4 |  |
| 36 | Delight | -1 |  |
| 39 | Despair | 1 |  |
| 40 | Disappointment | 8 |  |
| 41 | Disgust | 4 |  |
| 42 | Disillusionment | 8 |  |
| 43 | Dislike | 8 |  |
| 44 | Dismay | 2 |  |
| 45 | Displeasure | 8 |  |
| 46 | Distress | 2 |  |
| 47 | Doubt | 8 |  |
| 49 | Eagerness | -4 |  |
| 51 | Elation | -2 |  |
| 52 | Embarrassment | 8 |  |
| 53 | Empathy | -2 |  |
| 54 | Emptiness | 4 |  |
| 55 | Enjoyment | -8 |  |
| 57 | Enthusiasm | -8 |  |
| 59 | Euphoria | -1 |  |
| 60 | Exasperation | 8 |  |
| 61 | Excitement | -2 |  |
| 62 | Exhilaration | -2 |  |
| 63 | Expectancy | -8 |  |
| 64 | Fear | 1 | "Experiencing mortal fear!" |
| 65 | Ferocity | 2 |  |
| 66 | Fondness | -8 |  |
| 67 | Freedom | -4 |  |
| 68 | Fright | 2 |  |
| 69 | Frustration | 8 |  |
| 71 | Gaiety | -2 |  |
| 73 | Glee | -2 |  |
| 74 | Gloom | 4 |  |
| 75 | Glumness | 8 |  |
| 76 | Gratitude | -4 |  |
| 78 | Grief | 2 |  |
| 79 | Grim Satisfaction | 0 |  |
| 80 | Grouchiness | 8 |  |
| 81 | Grumpiness | 8 |  |
| 82 | Guilt | 4 |  |
| 83 | Happiness | -2 |  |
| 84 | Hatred | 2 |  |
| 86 | Hope | -2 |  |
| 87 | Hopelessness | 2 |  |
| 88 | Horror | 1 | "Overwhelmed by horror!" |
| 90 | Humiliation | 4 |  |
| 95 | Insult | 4 |  |
| 96 | Interest | -8 |  |
| 97 | Irritation | 8 |  |
| 98 | Isolation | 4 |  |
| 100 | Jolliness | -4 |  |
| 101 | Joviality | -2 |  |
| 102 | Joy | -1 |  |
| 103 | Jubilation | -1 |  |
| 104 | Loathing | 2 |  |
| 105 | Loneliness | 4 |  |
| 107 | Love | -1 |  |
| 109 | Lust | -8 |  |
| 111 | Misery | 1 | "Wallowing in misery!" Creature will lie on the ground crying and will not move. |
| 112 | Mortification | 2 |  |
| 114 | Nervousness | 8 |  |
| 115 | Nostalgia | -8 |  |
| 116 | Optimism | -4 |  |
| 117 | Outrage | 2 |  |
| 118 | Panic | 1 |  |
| 119 | Patience | -8 |  |
| 120 | Passion | -2 |  |
| 121 | Pessimism | 8 |  |
| 123 | Pleasure | -4 |  |
| 124 | Pride | -4 |  |
| 125 | Rage | 1 | "Enraged at all enemies!" Causes Enraged. |
| 126 | Rapture | -1 |  |
| 127 | Rejection | 4 |  |
| 128 | Relief | -2 |  |
| 129 | Regret | 8 |  |
| 130 | Remorse | 4 |  |
| 131 | Repentance | -2 |  |
| 132 | Resentment | 8 |  |
| 134 | Righteous Indignation | 8 |  |
| 135 | Sadness | 4 |  |
| 136 | Satisfaction | -8 |  |
| 138 | Self Pity | 8 |  |
| 140 | Servile | 0 |  |
| 141 | Shaken | 1 | "Shaken to the core!" |
| 142 | Shame | 4 |  |
| 143 | Shock | 1 | "In emotional shock!" |
| 148 | Suspicion | 8 |  |
| 149 | Sympathy | -8 |  |
| 150 | Tenderness | -2 |  |
| 152 | Terror | 1 | "Overcome by terror!" Creature will flee from enemies. / Default behavior when experiencing high stress in combat. |
| 153 | Thrill | -2 |  |
| 155 | Triumph | -2 |  |
| 156 | Uneasiness | 8 |  |
| 157 | Unhappiness | 4 |  |
| 158 | Vengefulness | 4 |  |
| 160 | Wonder | -8 |  |
| 161 | Worry | 8 |  |
| 162 | Wrath | 1 |  |
| 163 | Zeal | -4 |  |
| 167 | Restless | 8 |  |
| 168 | Admiration | -8 |  |
