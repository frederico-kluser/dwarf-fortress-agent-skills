# Kobold language

> Fonte: [Kobold language](https://dwarffortresswiki.org/index.php/Kobold_language) — Dwarf Fortress Wiki (GFDL/MIT)

The **Kobold language** is one of the languages the player will come across. This language is used in-game for the names, groups, and civilizations of kobolds.

Kobold is governed by rules different from the four main languages. Kobolds have the UTTERANCES creature token, which means their language has no pre-defined vocabulary. Instead, the language consists entirely of proper names built by hard-coded rules, which are detailed below.

Kobold-language words do not actually have a proper English translation *(due to not quite being based on any particular language - see Inspiration)* ; however, Kobold-language objects and individual kobolds will maintain the same name over time.

## Alphabet and Graphemics

The letters of the Kobold alphabet are:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| **Majuscule forms** (also called **uppercase** or **capital letters**) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | R | S | T | U | Y |
| **Minuscule forms** (also called **lowercase** or **small letters**) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | r | s | t | u | y |

Of these 21 letters, six (A, E, I, O, U, and Y) represent vowels, while the other fifteen represent consonants.

Peculiarities:

- The letter *h* only appears in the digraphs *sh*, *th*, and *ch*.
- The letter *n* only appears in the digraphs *ng*, *nk*, and *in*, and the trigraph *rsn*.
- The letter *y* only appears in the digraph *ay*.

The letters Q, V, W, X, and Z of the ISO basic Latin alphabet do not occur in the Kobold alphabet.

### Letter Frequency

Based on a sample of 120 kobold names, the approximate letter frequencies can be established:

| Letter | Frequency |
|--------|-----------|
| a      | 7.8%      |
| b      | 4.7%      |
| c      | 0.9%      |
| d      | 3.6%      |
| e      | 4.2%      |
| f      | 2.4%      |
| g      | 4.3%      |
| h      | 3.6%      |
| i      | 8.6%      |
| j      | 1.5%      |
| k      | 2.9%      |
| l      | 10.8%     |
| m      | 1.9%      |
| n      | 2.7%      |
| o      | 4.9%      |
| p      | 1.3%      |
| r      | 8.1%      |
| s      | 11.4%     |
| t      | 3.6%      |
| u      | 9%        |
| y      | 1.9%      |

## Phonotactics

The Kobold language has 16 distinguishable consonant phonemes, forming the phonological consonant inventory:

|  | Labial | Dental | Alveolar | Post-alveolar | Velar |
|----|----|----|----|----|----|
| Nasal | *m* \[m\] |  | *n* \[n\*\] |  |  |
| Plosive | *p* \[p\], *b* \[b\] |  | *t* \[t\], *d* \[d\] |  | *k* \[k\], *g* \[g\] |
| Affricate |  |  |  | *ch* \[t͡ʃ\], *j* \[d͡ʒ\] |  |
| Fricative | *f* \[f\] | *th* \[θ\] | *s* \[s\] | *sh* \[ʃ\] |  |
| Approximant |  |  | *r* \[r\] |  |  |
| Lateral |  |  | *l* \[l\] |  |  |

\*The phoneme represented by *n* likely has the allophone \[ŋ\] before *g* and *k.*

### Syllables

Kobold has three kinds of syllables, *primary,* *secondary,* and *final.* Every word is composed of one or two primary syllables, zero to two secondary syllables, and one final syllable. Words must begin with a primary syllable, end with a final syllable, the penultimate syllable must be a primary syllable, and all others must be secondary syllables. Therefore, the following structures are allowed:

| No. of syllables | Structure |
|------------------|-----------|
| 2 syllables      | 1-F       |
| 3 syllables      | 1-1-F     |
| 4 syllables      | 1-2-1-F   |
| 5 syllables      | 1-2-2-1-F |

#### Primary Syllables

Every primary syllable is of the syllable structure C₁(C₂)V. C₁ is mandatory, and can be one of many consonants; C₂ is an optional approximant, which can be either *r* or *l*; and V is a vowel.

- The allowed consonants for C₁ are: *b*, *d*, *st*, *sh*, *s*, *t*, *th*, *ch*, *l*, *f*, *g*, *k*, *p*, and *j*.
- The allowed consonants for C₂ are: *r*, *l*, or nothing.
  - **Exception**: The consonant cluster *ll* is forbidden.
- The allowed vowels for V are: *a*, *o*, *u*, *ay*, *ee*, and *i*.
  - **Exception**: The digraph vowels *ay* and *ee* can only be present in the penultimate syllable of a word (if this is also the initial syllable, it is still allowed).

#### Secondary Syllables

Every secondary syllable is of the simple form CV. C is one of a handful of consonants, and V is a vowel.

- The allowed consonants for C are: *b*, *d*, *l*, *f*, *g*, and *k*.
- The allowed vowels for V are: *a*, *i*, *o*, and *u*.
  - **Note**: All secondary syllables use the same vowel as the first syllable.

#### Final Syllables

Every final syllable is of the structure CR. C is one of several consonants or consonant clusters, while R is a rime that is limited to one of the four endings *-is*, *-us*, *-er*, or *-in*.

- The allowed consonants for C are: *m*, *r*, *ng*, *b*, *rb*, *mb*, *g*, *lg*, *l*, *lb*, *lm*, *k*, *nk*, *ld*, *d*, and *rsn*.
- The allowed rimes for R are: *is*, *us*, *er*, and *in*.
  - **Exception:** The rimes *er* and *in* are not allowed if the penultimate syllable's vowel is *ee* or *i*.

Note that the consonant C is likely not meant to actually begin the final syllable, but rather to be appended to the penultimate syllable. For example, the kobold name *Krudulugrilgus* would be enunciated as *Kru-du-lu-**gril**-gus*, not *Kru-du-lu-gri-**lgus.***

## Vocabulary

As mentioned above, Kobold has no set vocabulary, being formed entirely of procedurally generated proper names. The shortest possible words would be 5 letters and 2 syllables, like *[Sober*, and the longest possible words would be 18 letters and 5 syllables, such as *Stribikistreersnis*.

You can generate Kobold names outside of *Dwarf Fortress*, that follow *most* of the rules above ("all secondary syllables use the same vowel as the first syllable" is not enforced), with the online program GenGo. After clicking the link, copy the following into the appropriate boxes (overwriting any default already there), and click generate.

[TABLE]

## Inspiration

Toady has said in an interview that the kobold language was created in imitation of his and Threetoe's childhood language developed to speak to cats. (BlindIRL interview, 2020/06/11, 1 )
