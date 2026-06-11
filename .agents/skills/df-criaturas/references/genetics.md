# Genetics

> Fonte: [Genetics](https://dwarffortresswiki.org/index.php/Genetics) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Genetics** is the study of inheritance and genes, the ”things” that decide an organism’s innate traits. *Dwarf Fortress* sports a model of Mendelian genetics, deciding creature colors. According to Dwarf Fortress Talk #8, attributes (e.g. strength, speed and memory) and other appearance modifiers (e.g. nose length) are also affected by genetics, but more research is currently needed to either prove or disprove this.

Using knowledge of a creature’s genetics, breeding for specific traits can become easier.

Unlike real life, plants in *Dwarf Fortress* do not have genes.

## Simple color genetics

All possible combinations of black and brown alleles in a rabbit. Because black is dominant, it is represented by an upper-case 'B'; the recessive brown by a lower-case 'b'.

The model used for deciding creature colors is normally simple, but considerably more complicated when it comes to ”caste-specific” colors. For most creatures, including dwarves and all domestic animals but the blue peafowl, only the ”simple” model is used. Thus, only this section is needed to understand those; consider the ”caste based” section an advanced course.

It is unknown whether other traits than colors are inheritable. For the remainder of this tutorial, it will be assumed that only colors are.

To explain genetics, a couple of terms are generally used: gene, genotype, phenotype, allele, dominance (and recessiveness). Basically, *genes* are pieces of data that can be inherited from a creature to its offspring. Each creature has a double set of genes, one set from its mother and one set from its father. This set of genes are called the creature's *genotype*. As the genes interact, they affect the traits of the creature. This, the expressed traits, are called the creature's *phenotype*. Only the phenotype is ever visible in-game, so the genotype must be deduced from the former.

In *Dwarf Fortress*, all traits/colors are decided by one gene-pair each. This means each gene in a pair corresponds to a color. The variants of a gene are called *alleles*. Let's look at an example, here are the genotypes of four rabbits: black/black, black/brown, brown/black, brown/brown. The alleles involved here are black and brown, but often there are more than two. The phenotype is decided by the more *dominant* allele of the two. The opposite of dominant/dominance is *recessive*/*recessiveness*. In this case black is more dominant than brown, so all but the last rabbit will be black.

This means a black rabbit can have a genotype consisting of either two 'black' genes, or one 'black' gene and one 'hidden' gene of any allele more recessive than black (brown, white, grey etc.). This also means the offspring of two black rabbits may be not-black, if they both carry a 'hidden' recessive allele. Which of the genes in the gene-pair is passed down to each offspring is random.

Two black rabbits may have a brown child. A square diagram like this is called a Punnett square. Each sub-square has equal probability, 25%.

More than two alleles may come into question, even if there is only one phenotype. Here, a grey allele (represented by 'g') is more recessive than both black and brown. It will only show in the phenotype in later generations, if paired with another grey allele or one more recessive than grey.

Each gene corresponds to one trait/color, here's an example of dwarves, passing down both eye color (amethyst or aquamarine) and hair/beard color (black or brown). Amethyst eyes and black hair is dominant.

"Amethyst eyes = 'A', aquamarine eyes = 'a', black hair = 'B', brown hair = 'b'. Note that female dwarves in *Dwarf Fortress* normally don't have beards.

Of course, these mechanics apply to all breeding creatures, not only rabbits and dwarves, but the alleles may not be the same, and the order of dominance may vary from creature to creature, and from trait to trait. Whether a color is dominant or recessive is determined by the color's position in the list of possible colors, defined in the raw files. The first colors listed are dominant over the colors after them.

Dwarves don’t have human eye colors. The most dominant colors are amethyst and aquamarine, the most recessive are turquoise and gray.

## Caste based color genetics

Peafowl have colors defined at caste level. 'B' stands for both a blue and a brown allele. The two alleles never interact, as they are bound to specific castes. G1 stands for 'Generation 1', G2 for 'Generation 2'.

Not to be confused with the real-world social castes, castes in *Dwarf Fortress* are essentially the same as sexes; in vanilla, only ants (and their variants) and bees use the caste definitions for anything else, having queen, worker, and drone castes.

\

Color definitions can be declared both at the general creature (e.g. CASTE:ALL) level (this is what the 'Simple' tutorial detailed) and at caste level. In turn, creatures with color defined only at the caste level will have genetics bound to these. This means that a child of a certain caste will only inherit genes from a parent of the same caste, e.g. male children will only take after their father, and female children only their mother. How this works if no parent has the same caste as the child is as yet unknown. In any case, the way this works, is that one of the same-caste parents two genes is duplicated and given to the child. As creatures from off-map have random genotypes{confirm}, this means the first child bred in your fortress may have another color (if that allele was recessive) than its same-caste parent, but its children, grandchildren etc. will always remain the second generation's color.

Here, a modded peacock has a recessive black allele = 'b'. After one generation, no more blue children can be born. G1 stands for 'Generation 1' etc.

It is also possible to have a creature with colors defined at *both* creature and caste level. In this case, colors defined at the caste level for a certain part/descriptor will override those at the caste level visually (i.e. in the creature description), but the genes for the creature level color will still be inherited. Basically, the creature will have an extra pair of 'hidden' color genes in its genotype. For this example, a modded peafowl is used, where the male colors (dominant blue, recessive black) are defined at the creature level, and female colors (dominant brown, recessive buff) at the caste level for the FEMALE caste.

A male and a female peafowl. The female also have the 'male's' colors hidden in its genotype, shown in brackets. 'B' = blue or brown allele (dominant), 'b' = black or buff allele (recessive).

Note that the colors defined at caste level will still be inherited like they would without the creature level color. Below is an example showing it all in action. The example has the female's genes decide the caste/sex of the child, to correspond to the ZW chromosomes of real-life birds, but in all likelihood *Dwarf Fortress* uses no such system, instead using the POP_RATIO token and RNG.

'B' = blue or brown allele (dominant), 'b' = black or buff allele (recessive).

## Population genetics

Genetic information is saved for every historical figure, from which each culture derives a number of tissue colors and other appearance modifiers that are likely to be found on any given member of that culture. Abstract entity populations have a (currently mild?) impact on the histfig's genetic profile, drawing from 'subpopulations' which are the cause of eye and skin color being very similar or identical in any given region.

## Bugs

- Experiments conducted in V0.47.04 have shown that attributes are not inherited by the offspring of egg-layers. It is unknown whether this also affects inheritance of appearance modifiers.
