# Topic

> Fonte: [Topic](https://dwarffortresswiki.org/index.php/Topic) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A diagram of all knowledge topics.

 **Topics** (also **Tech** or **Innovations**) are part of knowledge.

There are 312 innovations that can be discovered. Many of them have requirements, and many do not, so it's kind of a tech forest/grassland rather than a tree. Notably missing are innovations related to practical labors in the game (which will be added later in development). Only the discovery of literary form topics has any effect on gameplay, as it allows scholars to write new types of books.

Several innovations require innovations from other branches, and since all knowledge is individually tracked, that implies some investigators will need to be at least well-read if not skilled in various topics (there aren't currently joint research projects). There are some old and new mechanisms in place to ensure this happens.

There are 9 "branches" of the knowledge system. Each branch is further divided into categories of topics, such as methodologies, theories, etc.

## Discovering Topics

According to a Future of the Fortress reply:

> Fortress scholars do activity cycles, the length of which is 1-2 days (whether they are pondering or discussing etc.) Once they get through 50 cycles, it rolls 0-50 vs. the number of completed cycles minus 50 to see if they get "breakthrough credit." So at 51, they have a 2% chance, and at 100, they have a 100% chance. Then, it resets the cycle number to zero and gives them breakthrough credit, based on a skill roll plus 100 (for discuss, the other researchers contribute half of their summed skill rolls.) Based on the difficulty (1-4) of the topic, total lifetime breakthrough credit is then assigned a number of 50-sided dice. An easy topic is dice=credit/2500, then /5000, then /10000, then /20000 for level 4 topics. The number of dice cannot exceed 10. Then roll these dice -- if you get a 50 on any of them, discovery! This is a bit archaic, and I'm not suggesting it works particularly well. But that is how it works. Also: if they fail to get the breakthrough after the 50-sided rolls, they have a 2% chance of switching topics, or if their credit exceeds 100000, they always switch topics (though they keep the credit, so returning to the topic later gives them a decent chance at breakthrough.)

For unskilled roles, some initial back-of-the-envelope calculations and some rough estimates observed through dfHack gives a basic idea of just how long research can take. Note that player testing had found that the skill roll contributes a lot to the breakthrough credit. Even dabbling dwarves can gain over 2000 breakthrough credit at once and may average around 1000 breakthrough credit. Additionally the formula for the skill roll seems to have a very large spread, players have reported as low as 3000 breakthrough credit and as high as 25000 breakthrough credit awarded to a dwarf with legendary skill. Analytically calculating from the algorithm Toady gave, it takes an average of 58.54 cycles to get a breakthrough credit. Player testing has confirmed breakthrough credits typically take 55-65 cycles, so this calculation seems plausible. Likewise, player testing has not shown any correlation between skill level and number of cycles to get breakthrough credit. An unskilled dwarf might average around 120+ cycles to get their first breakthrough die for a level 1 topic. With only a single research die, it would take an average of 2528 cycles to get a breakthrough. Pondering takes slightly over 2 days per cycle, so this would be around 14 years. In a real fortress, the research dice and skill level will be increasing during the process. However, in a real fortress, the scholars will also need to take breaks to eat, drink, and meet other needs. A more reasonable estimate is around 5-10 years for a breakthrough starting with no skills. In short, research takes an unreasonably long time with an unskilled dwarf.

To optimize for research, there are several ideas worth considering. Discussion is faster, taking only a single day, but requires at least 2 dwarves. Player testing has found discussion also awards more XP, (0-5 for pondering vs. 15-30 for discussion). So to optimize research, dwarves should be separated by topic/skill, with unskilled dwarves paired with skilled dwarves. This way, discussions will be equally divided between increasing the skilled dwarf's cycle count and the unskilled dwarf's cycle count. Only half the cycles will go to the skilled dwarf's cycle count, but discussion only takes a single day, so this is at net the same speed for the skilled dwarf with the additional bonus of the unskilled dwarf's cycle count also being increased. Both dwarves benefit from the increased XP gain.

Note that several topics benefit from skills that can be trained through faster means. Diagnostician and Wound Dresser can be trained through intentionally causing injuries or simply engaging in dangerous activities that require regular dwarf healthcare. Organizer can be trained through assigning make work to the manager, or Mechanic can be trained by spamming the creation of mechanisms. Skill level will increase much faster through these activities than through pondering or discussion. Thus, to optimize for producing breakthroughs in engineering topics, mechanics could first be quickly trained to a legendary within a year or two at only the cost of the stones for the mechanisms, and then assigned as a scholar.

Player testing has also found that visitors can come with research credits already done, thus, for forts aiming to maximize research, it makes sense to prioritize attracting wandering scholars.

## Astronomy

These topics are relevant to astronomers.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Empirical observation | Methods of empirical observation in astronomy | Empirical evidence | Method | Astronomer |
| Path models | The method of forming precise models for the paths of astronomical objects | Orbit modeling | Method | Astronomer |
| Astrography | The creation of star charts | Star chart | *n/a* | Astronomer, Record keeper |
| Dates of lunar and solar eclipses | The dates of lunar and solar eclipses | Saros (astronomy) | *n/a* | Astronomer, Record keeper |
| Daylight variation with solar year | The variation of daylight with the seasons | Daytime § Daytime variations with latitude and seasons | *n/a* | Astronomer |
| Geocentrism | The theory that the sun moves around the world | Geocentric model | *n/a* | Astronomer |
| Height of tides vs moon and sun | The height of the tides, the moon and the sun | Pytheas § Pytheas on the tides and Tide | *n/a* | Astronomer |
| Heliocentrism | The theory that the world moves around the sun | Heliocentric model | *n/a* | Astronomer |
| Path of the moon | The path of the moon | Orbit of the Moon | *n/a* | Astronomer |
| Phases of the moon | The phases of the moon | Lunar phase | *n/a* | Astronomer |
| Precession of equinoxes | The precession of equinoxes over great periods of time | Axial precession | *n/a* | Astronomer, Record keeper |
| Relationship between lunar/solar year | The relationship between the lunar and solar year | Lunisolar calendar | *n/a* | Astronomer, Record keeper |
| Shape of the world | The shape of the world | Spherical Earth | *n/a* | Astronomer |
| Star catalogues 100 | The compilation of information about stars | Star catalogue | *n/a* | Astronomer, Record keeper |
| Star catalogues 1000 | The precise compilation of information about stars | Star catalogue | *n/a* | Astronomer, Record keeper |
| Star magnitude classification | The classification of stars according to brightness | Magnitude (astronomy) | *n/a* | Astronomer, Record keeper |
| Stellar Spectroscopy | The classification of stars according to color | Astronomical spectroscopy | *n/a* | Astronomer, Record keeper |
| Summer/winter moon | The rise of the moon according to the season | Lunar calendar | *n/a* | Astronomer |
| Summer/winter sun | The rise of the sun according to the season | Solar calendar | *n/a* | Astronomer |
| Tides and the moon | The relationship between the moon and the tides | Seleucus of Seleucia § Tides and Tide | *n/a* | Astronomer |

\

## Chemistry

These topics are relevant to chemists.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Adhesives | The preparation and use of adhesive materials | Adhesive | Chemicals | Chemist |
| Aqua regia | The preparation of aqua regia | Aqua regia | Chemicals | Chemist |
| Oil of vitriol | The preparation of oil of vitriol | Sulfuric acid | Chemicals | Chemist |
| Spirit of niter | The preparation of spirit of niter | Nitric acid | Chemicals | Chemist |
| Alkali and acids | The classification of alkali and acids | pH | Classification | Chemist, Record keeper |
| Combustibles | The classification of combustible materials | Combustibility | Classification | Chemist, Record keeper |
| Elemental theory | The classification of materials based on which elemental materials might form them | Classical element or Atomic theory | Classification | Chemist |
| Ores | The classification of ores | Ore | Classification | Chemist |
| Scratch test | A method of classifying the hardness of materials by scratching them against each other | Scratch hardness | Classification | Chemist, Record keeper |
| Alembic | The construction and use of the alembic | Alembic | Laboratory | Chemist |
| Blast furnace | The construction and use of the blast furnace | Blast furnace | Laboratory | Chemist |
| Crucible | The construction and use of the crucible | Crucible | Laboratory | Chemist |
| Lab ovens | The construction and use of laboratory ovens | Laboratory oven | Laboratory | Chemist |
| Systematic experiments | Methods for performing experiments systematically in the laboratory | Scientific method | Laboratory | Chemist, Record keeper |
| Theory of distillation | The theory and methods involved in distillation | Distillation | Laboratory | Chemist |
| Theory of evaporation | The theory and methods involved in evaporation | Evaporation | Laboratory | Chemist |
| Theory of liquid-liquid extraction | The theory and methods involved in the extraction of a constituent liquid from one solution to another | Liquid–liquid extraction | Laboratory | Chemist |
| Ampoule | The construction and use of the ampoule | Ampoule | Laboratory (glass) | Chemist |
| Beaker | The construction and use of the beaker | Beaker | Laboratory (glass) | Chemist |
| Flask | The construction and use of the flask | Flask | Laboratory (glass) | Chemist |
| Funnel | The construction and use of the funnel | Funnel | Laboratory (glass) | Chemist |
| Retort | The construction and use of the retort | Retort | Laboratory (glass) | Chemist |
| Vial | The construction and use of the vial | Vial | Laboratory (glass) | Chemist |
| Alloys | The mixing of metals to produce alloys | Alloy | Metallurgy | Chemist |

\

## Engineering

These topics are relevant to engineers.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Armillary sphere | The construction and use of armillary spheres | Armillary sphere | Astronomy | Mechanic |
| Astrolabe | The construction and use of the astrolabe | Astrolabe | Astronomy | Mechanic |
| Dioptra | The construction and use of the dioptra | Dioptra | Astronomy | Mechanic |
| Mural instrument | The construction and use of a mural instrument or **mural quadrant** | Mural instrument | Astronomy | Mechanic |
| Orrery | The construction and use of the orrery | Orrery | Astronomy | Mechanic |
| Spherical astrolabe | The construction and use of the spherical astrolabe | Astrolabe | Astronomy | Mechanic |
| Wood lamination | The use of lamination | Lamination | Construction | Mechanic |
| Models and templates | The use of models and templates in engineering | Prototype and Stencil | Design | Mechanic |
| Archimedes principle | The law of fluid displacement | Archimedes' principle | Fluid | Fluid engineer |
| Force pump | The construction and use of the force pump | Piston pump § Force pump | Fluid | Fluid engineer |
| Theory of siphon | The action of the siphon | Siphon | Fluid | Fluid engineer |
| Valves | The construction and use of valves | Valve | Fluid | Fluid engineer |
| Astrarium | The construction and use of the astrarium | Astrarium | Horology | Mechanic |
| Conical water clock | The use of conical shapes in water-based clocks to improve their accuracy | Water clock | Horology | Fluid engineer |
| Hourglass | The construction and use of the hourglass | Hourglass | Horology | Mechanic |
| Mechanical clock | The construction and use of mechanical clocks | Clock § Early mechanical clocks | Horology | Mechanic |
| Shadow clock | The use of shadows to tell direction and time | Sundial | Horology | Mechanic |
| Water clock | The use of water-based devices to tell time | Water clock | Horology | Fluid engineer |
| Water clock reservoir | The use of reservoirs in water-based clocks to improve their accuracy | Zhang Heng § Extra tank for inflow clepsydra | Horology | Fluid engineer |
| Balance wheel | The construction and use of the balance wheel. | Balance wheel | Machine | Mechanic |
| Bellows | The construction and use of the bellows | Bellows | Machine | Mechanic |
| Camshaft | The construction and use of the camshaft | Camshaft | Machine | Mechanic |
| Chain drive | The construction and use of chain drives | Chain drive | Machine | Mechanic |
| Chariot odometer | The construction and use of the chariot odometer | Odometer | Machine | Mechanic |
| Combination lock | The construction and use of the combination lock | Combination lock | Machine | Mechanic |
| Crank | The construction and use of the crank | Crank (mechanism) | Machine | Mechanic |
| Crankshaft | The construction and use of the crankshaft | Crankshaft | Machine | Mechanic |
| Differential gear | The construction and use of the differential gear | Differential (mechanical device) | Machine | Mechanic |
| Double acting piston bellows | The construction and use of the double-acting piston bellows | Bellows | Machine | Mechanic |
| Lever | The construction and use of the lever | Lever | Machine | Mechanic |
| Mechanical compass | The construction and use of the mechanical compass | Compass | Machine | Mechanic |
| Padlock | The construction and use of the padlock | Padlock | Machine | Mechanic |
| Piston | The construction and use of the piston. | Piston pump § Force pump | Machine | Mechanic |
| Pulley | The construction and use of the pulley | Pulley | Machine | Mechanic |
| Screw | The construction and use of the screw | Screw | Machine | Mechanic |
| Straight beam balance | The construction and use of the straight-beam balance | Weighing scale § Mechanical balances | Machine | Mechanic |
| Theory of gears | The reasons why gears are effective | Gear | Machine | Mechanic |
| Theory of lever | The reasons why the lever is effective | Lever | Machine | Mechanic |
| Theory of pulley | The reasons why pulleys are effective | Pulley | Machine | Mechanic |
| Theory of screw | The reasons why screws are effective | Screw | Machine | Mechanic |
| Theory of wedge | The reasons why the wedge is effective | Wedge | Machine | Mechanic |
| Theory of wheel and axle | The reasons why the wheel-and-axle construction is effective | Wheel and axle | Machine | Mechanic |
| Trip hammer | The construction and use of the trip-hammer. | Trip hammer | Machine | Mechanic |
| Tumbler lock | The construction and use of the tumbler lock | Pin tumbler lock | Machine | Mechanic |
| Verge escapement | The construction and use of the verge escapement | Verge escapement | Machine | Mechanic |
| Warded lock | The construction and use of the warded lock | Warded lock | Machine | Mechanic |
| Water-powered piston bellows | The construction and use of the water-powered piston bellows. | Du Shi § The Water-Powered Blast Furnace | Machine | Mechanic |
| Water-powered sawmill | The construction and use of the water-powered sawmill. | Watermill | Machine | Mechanic |
| Water-powered trip hammer | The construction and use of the water-powered trip hammer | Trip hammer and Water wheel | Machine | Mechanic |
| Water wheel | The construction and use of the water wheel. | Water wheel | Machine | Mechanic |
| Windlass | The construction and use of the windlass | Windlass | Machine | Mechanic |
| Atmospheric refraction | atmospheric refraction | Atmospheric refraction | Optics | Optics engineer |
| Camera obscura | The construction and use of the camera obscura | Camera obscura | Optics | Optics engineer |
| Cause of twilight | a precise explanation of the cause of twilight involving atmospheric refraction | Atmospheric optics | Optics | Optics engineer |
| Crystal lens | The construction and use of the crystal lens | Lens (optics) and Crystal | Optics | Optics engineer |
| Glass lens | The construction and use of the glass lens | Lens (optics) and Glass | Optics | Optics engineer |
| Height of atmosphere | The calculation of the height of the atmosphere based on atmospheric refraction | Atmosphere of Earth | Optics | Optics engineer |
| Law of refraction | The relation between refraction and the half chord | Snell's law | Optics | Mechanic |
| Parabolic mirror | The construction and use of the parabolic mirror. | Parabolic reflector | Optics | Optics engineer |
| Theory of color | The theory of light and color | Color theory | Optics | Optics engineer |
| Theory of rainbows | The appearance of rainbows based on optical theories | Rainbows | Optics | Optics engineer |
| Water-filled spheres | The construction and use of water-filled spheres as lenses | Lens (optics) and History of optics § Early history of optics | Optics | Optics engineer |

\

## Geography

These topics are relevant to geographers.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Accurate maps | The creation of accurate maps | Map | Cartography | Geographer |
| Cartography | The process involved in creating maps | Cartography | Cartography | Geographer |
| Distance scale | The use of distance scale in the creation of maps | Scale (map) | Cartography | Geographer |
| Economic | The placement of economic information on maps | Economic geography | Cartography | Geographer, Record keeper |
| Geological | The placement of geological information on maps | Geologic map | Cartography | Geographer |
| Grid system | The use of a grid system in the creation of maps | Grid reference | Cartography | Geographer |
| Height measurements | The measurement of the height of land features. | Topographic map and Levelling | Cartography | Geographer, Record keeper |
| Map projections | Methods of adjusting maps to account for the shape of the world | Map projection | Cartography | Geographer |
| Atlases | The collection of maps and other information together into a single text | Atlas | Form | Geographer, Record keeper |
| Econometrics | The process of economic data collection | Econometrics | Method | Geographer, Record keeper |
| Cartographical surveying | Surveying by triangulation for the purpose of creating maps | Cartography and Surveying | Surveying | Geographer |
| Engineering surveying | Surveying by triangulation for engineering projects | Construction surveying | Surveying | Geographer |
| Land surveying | Surveying by triangulation for the purpose of allocating land | Cadastral surveying | Surveying | Geographer |
| Military surveying | Surveying by triangulation for military purposes | Construction surveying and Military engineering | Surveying | Geographer |
| Surveying | The process of surveying land | Surveying | Surveying | Geographer |
| Surveying staff | The construction and use of the surveying staff | Level staff | Surveying | Geographer |
| Triangulation | Surveying by triangulation | Triangulation | Surveying | Geographer |
| Anemology | The forces that govern wind patterns | Global wind patterns | Theory | Geographer |
| Delta formation | The process of the formation of deltas at the mouths of rivers | River delta § Formation | Theory | Geographer |
| Latitude climate zones | The division of the world into climate zones | Clime | Theory | Geographer |
| Origin of rainfall from evap condense | The origin of rainfall through evaporation and condensation | Evaporation and Condensation | Theory | Geographer |
| Water cycle | A world-wide cycle involving precipitation, oceans, rivers, and other forms of water | Water cycle | Theory | Geographer |

\

## History

These topics are relevant to critical thinkers.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Alternate history | The exploration of how history would be different if some key past events had transpired differently | Alternate history | Form | Critical thinker |
| Autobiographical adventure | The method of writing a biography of oneself, particularly as it concerns a military campaign or adventure | Autobiography | Form | Critical thinker |
| Biographical dictionaries | The compilation of brief biographies into one large collection | Biographical dictionary | Form | Critical thinker |
| Biography | The method of writing the history of a single individual | Biography | Form | Critical thinker |
| Comparative anthropology | The method of comparing and contrasting different cultures | Cross-cultural studies | Form | Critical thinker |
| Comparative biography | The method of compiling several biographies to compare and contrast the subjects' character and to gain insight into history | Biography | Form | Critical thinker |
| Cultural history | The method of accurately and comprehensively describing cultures and civilizations | Cultural history | Form | Critical thinker |
| Encyclopedia | The compilation of many summaries into a single text. | Encyclopedia | Form | Critical thinker, Record keeper |
| Genealogy | The compilation of family lineages and methods of displaying them artfully | Genealogy | Form | Critical thinker, Record keeper |
| Treatise on tech evolution | The method of examining artifacts to determine how methods have changed over time. | Technological evolution | Form | Critical thinker |
| Archaeology | The method of collecting and evaluating artifacts to learn about history and culture | Archaeology | Sourcing | Critical thinker |
| Personal interviews | Using personal interviews as sources | Interview | Sourcing | Critical thinker, Organizer |
| Role of cultural differences | The role of cultural differences in source reliability and interpretation | Cultural relativism | Sourcing | Critical thinker |
| Role of state bias and propaganda | The role of state bias and propaganda in sources | Propaganda | Sourcing | Critical thinker |
| Role of systemic bias | The role of systemic bias in sources | Systemic bias | Sourcing | Critical thinker |
| Source reliability | The reliability of sources | Source criticism | Sourcing | Critical thinker |
| Historical causation | The causes of historical events | Causality § History | Theory | Critical thinker |
| Historical cycles | The notion of historical, governmental and social cycles | Cyclic history | Theory | Critical thinker |
| Social conflict | Conflict between members of a community | Social conflict | Theory | Critical thinker |
| Sociology | The notion of bonds between members of a community | Sociology | Theory | Critical thinker |

\

## Mathematics

These topics are relevant to mathematicians.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Divergence of harmonic series | The divergence of the harmonic series | Harmonic series (mathematics) | Algebra | Mathematician |
| Equations | The technique of balancing and completion for solving equations | The Compendious Book on Calculation by Completion and Balancing, Algebra, and Equation | Algebra | Mathematician |
| Large sums | Simple formulas for certain arbitrarily large sums | Summation | Algebra | Mathematician |
| Pascal's triangle | A triangular configuration of numbers relating to the successive powers of any sum | Pascal's triangle | Algebra | Mathematician |
| Quadratic by completing square | The solving of quadratic equations by completion of the square | Completing the square | Algebra | Mathematician |
| Quadratic formula | A formula which solves quadratic equations | Quadratic formula | Algebra | Mathematician |
| Solving higher order polynomials | Methods for solving certain equations involving powers higher than the quadratic | Galois theory | Algebra | Mathematician |
| Systems of equations | Methods of solving systems of equations | Linear system | Algebra | Mathematician |
| Area enclosed by line and parabola | The area enclosed by a parabola and a line | The Quadrature of the Parabola | Geometry | Mathematician |
| Area of circle |  | Area of a disk | Geometry | Mathematician |
| Area of triangle from side lengths | The computation of the area of a triangle from its three side lengths alone | Heron's formula | Geometry | Mathematician |
| Basic geometry | Geometric objects: points, lines, circles, triangles, and so on | Geometry | Geometry | Mathematician |
| Chords | The properties of chords | Chord (geometry) | Geometry | Mathematician |
| Chord tables | A table of chord lengths indexed by angle | Ptolemy's table of chords | Geometry | Mathematician |
| Conic sections | The categorization and properties of conic sections | Conic section | Geometry | Mathematician |
| Existence of pi | The relationship between the area of a circle and its radius, involving the ratio of the circumference of the circle to its diameter | Pi | Geometry | Mathematician |
| Geometric mean | The relationship between the length of the altitude of a right triangle and the lengths of the segments into which it divides the hypotenuse | Geometric mean theorem | Geometry | Mathematician |
| Inscribed triangle on diameter is right | The angles of triangles inscribed in a circle with one edge on the diameter | Thales' theorem | Geometry | Mathematician |
| Irrational numbers | The existence of incommensurable ratios | Irrational number | Geometry | Mathematician |
| Isosceles base angles equal | The equality of the base angle of isosceles triangles | Pons asinorum | Geometry | Mathematician |
| Law of sines | The relatonship between the half chords of lengths and the diameter of the triangle’s circumscribed circle. | Law of sines | Geometry | Mathematician |
| Pi to 6 digits |  | Zu Chongzhi § Mathematics and Milü | Geometry | Mathematician |
| Pythagorean theorem | The relationship between the lengths of the hypotenuse of a right triangle and the other two sides | Pythagorean theorem | Geometry | Mathematician |
| Pythagorean triples 3 digit | Examples of triples of large whole numbers which, when taken together, are the lengths of the sides of a right triangle | Pythagorean triples | Geometry | Mathematician |
| Pythagorean triples 4 digit | Examples of triples of very large whole numbers which, when taken together, are the lengths of the sides of a right triangle | Pythagorean triples | Geometry | Mathematician |
| Pythagorean triples small | Examples of triples of small whole numbers which, when taken together, are the lengths of the sides of a right triangle | Pythagorean triples | Geometry | Mathematician |
| Similar and congruent triangles | The properties of similar and congruent triangles | Similarity (geometry) and Congruence (geometry) | Geometry | Mathematician |
| Sum-difference trig identities | Trigonometric identities relating to the sums and differences of angles | List of trigonometric identities § Angle sum and difference identities | Geometry | Mathematician |
| Surface area of sphere | The computation of the surface area of a sphere | Sphere § Surface area | Geometry | Mathematician |
| Volume of cone | The computation of the volume of a cone | Cone § Volume | Geometry | Mathematician |
| Volume of pyramid | The computation of the volume of different pyramids | Pyramid (geometry) § Volume | Geometry | Mathematician |
| Volume of sphere | The computation of the volume of a sphere | Sphere § Volume | Geometry | Mathematician |
| Axioms | Axiomatic reasoning | Axiomatic system | Method | Logician |
| Method of exhaustion | An approximation of the ratio of a circumference of a circle to its diameter, using the area of polygons and the method of exhaustion | Method of exhaustion | Method | Logician |
| Proof by contradiction | The method of proof by contradiction | Proof by contradiction | Method | Logician |
| Algebra | Notation for abbreviating the unknown and other elements of an equation in a systematic and useful fashion | Algebra | Notation | Logician |
| Negative numbers | Notation for negative quantities | Negative number | Notation | Logician |
| Place values | Positional notation | Positional notation | Notation | Logician |
| Scientific notation | Notation for very large numbers | Scientific notation | Notation | Logician |
| Symbol for addition | The idea of using symbolic notation for addition | Plus and minus signs § Plus sign | Notation | Logician |
| Zero | A symbol for nothingness | 0 (number) | Notation | Logician |
| Approximation of root 2 | An approximation for the length of the diagonal of a square | Square root of 2 § History | Numbers | Mathematician |
| Chinese remainder algorithm | An algorithm for computing a number which has given remainders when divided by several given primes | Chinese remainder theorem | Numbers | Mathematician |
| Division | An algorithm for dividing one number into another, possibly yielding a remainder | Euclidean division | Numbers | Mathematician |
| Euclid's Theorem | A proof that there are infinitely many prime numbers | Euclid's theorem | Numbers | Mathematician |
| Euclidean Algorithm | An algorithm for computing the greatest common divisor of two numbers | Euclidean algorithm | Numbers | Mathematician |
| Irrationality of root 2 | A proof that the length of a diagonal of a square is incommensurable with its edge | Square root of 2 § Proofs of irrationality | Numbers | Mathematician |
| Sieve algorithm for primes | An algorithm for calculating prime numbers | Sieve of Eratosthenes | Numbers | Mathematician |
| Unique prime factorization | The unique decomposition of a number into products of its prime divisors | Fundamental theorem of arithmetic | Numbers | Mathematician |

\

## Medicine

These topics are relevant to many medical professions, including doctors and diagnosticians.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Anesthesia | Anesthesia | Anesthesia | Method | Diagnostician |
| Asylum for mentally ill | The creation of asylums for the mentally ill. | Psychiatric hospital | Method | Critical thinker |
| Autopsy | The method of autopsy | Autopsy | Method | Diagnostician |
| Cataract surgery | Cataract surgery | Cataract surgery | Method | Surgeon |
| Cauterization | Cauterization | Cauterization | Method | Surgeon |
| Fracture immobilization | The method of fracture immobilization | Bone fracture § Immobilization | Method | Bone doctor |
| Fracture treatment | The treatment of fractures | Bone fracture § Treatment | Method | Bone doctor |
| Hernia surgery | Hernia surgery | Hernia § Surgery | Method | Surgeon |
| Hospital lab | The use of a laboratory for preparation of remedies in a hospital | Medical laboratory | Method | Critical thinker |
| Lithotomy surgery | The lithotomy surgery | Lithotomy | Method | Surgeon |
| Medical school | Schools of medicine | Medical school | Method | Critical thinker |
| Physical examination | The method of physical examination in diagnosing illness | Physical examination | Method | Diagnostician |
| Professional hospital staff | The use of professional hospital staff | Surgeon and Physician | Method | Critical thinker |
| Specialized wards | The use of specialized wards in hospitals | Hospital § Departments or wards | Method | Critical thinker |
| Tracheotomy surgery | The tracheotomy surgery | Tracheotomy | Method | Surgeon |
| Traumatic injuries | The treatment of traumatic injuries | Major trauma | Method | Diagnostician |
| Draining | The surgical method of draining | Drain (surgery) | Method (surgery) | Surgeon |
| Excision | The surgical method of excision | Surgery § Types of surgery | Method (surgery) | Surgeon |
| Incision | The surgical method of incision | Surgical incision | Method (surgery) | Surgeon |
| Ligature | The surgical method of ligature | Ligature (medicine) | Method (surgery) | Suturer |
| Probing | The surgical method of probing | Surgical instrument § Classification | Method (surgery) | Surgeon |
| Scraping | The surgical method of scraping | Surgical instrument § Classification | Method (surgery) | Surgeon |
| Suturing | The surgical method of suturing | Surgical suture | Method (surgery) | Suturer |
| Acute and chronic conditions | The distinction between acute and chronic conditions | Acute (medicine) and Chronic condition | Theory | Diagnostician |
| Anatomical studies | Anatomical studies for medical edification | Human body | Theory | Surgeon |
| Blood vessels | The distinction between veins and arteries | Blood vessel | Theory | Surgeon |
| Classification of bodily fluids | The classification of bodily fluids | Body fluid or Humorism | Theory | Surgeon |
| Classification of mental illnesses | The classification of mental illnesses | Mental disorder | Theory | Critical thinker, Diagnostician |
| Classification of muscles | The classification of muscles | Muscle | Theory | Surgeon |
| Comparative anatomy | Comparative anatomical studies for the use in medicine | Comparative anatomy | Theory | Surgeon |
| Convalescence | The theory of convalescence | Convalescence | Theory | Diagnostician |
| Disease and fouled water | The connection between disease and fouled water | Waterborne diseases | Theory | Critical thinker |
| Endemic disease | The theory of endemic disease | Endemic (epidemiology) | Theory | Diagnostician |
| Epidemic disease | The theory of epidemic disease | Epidemic | Theory | Diagnostician |
| Exacerbation | The notion of the exacerbation of a patient's condition | Exacerbation | Theory | Diagnostician |
| Eye anatomy | The anatomy of the eye | Human eye | Theory | Surgeon |
| Fracture classification | The classification of fractures | Bone fracture § Classification | Theory | Bone doctor |
| Motor vs sensory nerves | The distinction between motor and sensory nerves | Motor nerve and Sensory nerve | Theory | Surgeon |
| Nervous system function | The function of the nervous system | Nervous system | Theory | Diagnostician |
| Paroxysm | The notion of paroxysm | Paroxysmal attack | Theory | Diagnostician |
| Pathology | The classification of disease | Nosology | Theory | Diagnostician |
| Prognosis | Determining the likely outcome of a disease given a patient's current status | Prognosis | Theory | Diagnostician |
| Pulmonary circulation | Pulmonary circulation | Pulmonary circulation | Theory | Surgeon |
| Pulmonary medicine | Pulmonary medicine | Pulmonology | Theory | Diagnostician |
| Reaction time | The study of reaction time | Mental chronometry | Theory | Diagnostician |
| Relapse | The notion of relapse | Relapse | Theory | Diagnostician |
| Specialized surgical instruments | The use of specialized surgical instruments | Surgical instrument | Theory | Surgeon |
| Surgical models | The use of practice models in surgery | Anatomical model | Theory | Surgeon |
| The voice | The source of the voice | Phonation | Theory | Surgeon |
| Toxicology | The classification of toxic substances | Toxicology | Theory | Diagnostician |
| Treatment of mental illnesses | The treatment of mental illnesses | Treatment of mental disorders | Theory | Diagnostician |
| Animals as surgical models | The use of animals as surgical models | Vivisection | Tool | Surgeon |
| Animal remedies | Remedies prepared from animals | Traditional Chinese medicine § Animal substances | Tool | Diagnostician |
| Bandages | The method of bandaging wounds | Bandage | Tool | Wound dresser |
| Dedicated hospitals | The preparation and use of dedicated hospitals | Hospital | Tool | Critical thinker |
| Forceps | The construction and use of forceps | Forceps | Tool | Surgeon |
| Herbal remedies | Herbal remedies | Herbalism | Tool | Diagnostician |
| Mineral remedies | Mineral remedies | List of traditional Chinese medicines § Minerals | Tool | Diagnostician |
| Mud bags as surgical models | The use of mud bags as surgical models | Anatomical model | Tool | Surgeon |
| Needles | The construction and use of surgical needles | Surgical suture § Needles | Tool | Surgeon |
| Orthopedic cast | The creation and use of the orthopedic cast | Orthopedic cast | Tool | Bone doctor |
| Plants as surgical models | The use of plants as surgical models | Anatomical model | Tool | Surgeon |
| Scalpel | The construction and use of the scalpel | Scalpel | Tool | Surgeon |
| Surgical scissors | The construction and use of surgical sissors | Surgical scissors | Tool | Surgeon |
| Traction bench | The construction and use of the traction bench | Hippocratic bench | Tool | Bone doctor |

\

## Nature

These topics are relevant to naturalists and trackers.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Dissection | The dissection of creatures | Dissection | Method | Critical thinker |
| Anatomy | The anatomical study of creatures | Anatomy | Observation | Critical thinker, Tracker |
| Embryology | The embryological development of creatures | Embryology | Observation | Observer |
| Foraging behavior | The foraging behavior and diet of creatures | Foraging | Observation | Tracker, Record keeper, Observer |
| Migration | The migratory patterns of creatures | Animal migration | Observation | Tracker, Record keeper, Observer |
| Reproductive behavior | The reproductive behavior of creatures | Reproduction | Observation | Tracker, Record keeper, Observer |
| Social behavior | The social behavior of creatures | Social behavior | Observation | Tracker, Record keeper, Observer |
| Veterinary medicine | The diseases of creatures | Veterinary medicine | Observation | Tracker, Record keeper, Observer |
| Climactic adaptation | The way that creatures are suited to the climates in which they live | Climatic adaptation | Theory | Critical thinker |
| Comparative anatomy | The comparison of the anatomy of creatures | Comparative anatomy | Theory | Critical thinker |
| Food chain | The links between the diets of different creatures. | Food chain | Theory | Critical thinker |
| Physical taxonomy | The classification of creatures by their physical features | Aristotle's biology § Classification | Theory | Critical thinker |
| Struggle for existence | The struggle for survival among creatures | Struggle for existence | Theory | Critical thinker |

\

## Philosophy

These topics are relevant to logicians.

|  |  |  |  |  |
|----|----|----|----|----|
| Topic | Description | Wikipedia link | Subdivision | Skills used in research |
| Nature of beauty | Discourse on the nature of beauty | Beauty (ancient thought) | Aesthetics | Critical thinker |
| Value of art | Discourse on the value of art | Aesthetics | Aesthetics | Critical thinker |
| Belief | Discourse on the nature of belief | Epistemology § Belief | Epistemology | Critical thinker |
| Justification | Discourse on the nature of justification | Epistemology § Justification | Epistemology | Critical thinker |
| Perception | Discourse on the nature of perception | Philosophy of perception | Epistemology | Critical thinker |
| Truth | Discourse on the nature of truth | Epistemology § Truth | Epistemology | Critical thinker |
| Individual value | Discourse on the meaning of individual happiness | Value (ethics) § Personal values | Ethics | Critical thinker |
| State consequentialism | Discourse on ethics as applied to the benefit of the state | State consequentialism | Ethics | Critical thinker |
| Interpersonal conduct | Discourse on ethics as applied to interpersonal conduct | Value (ethics) § Cultural values | Ethics (applied) | Critical thinker |
| Medical | Discourse on medical ethics | Medical ethics | Ethics (applied) | Critical thinker |
| Military | Discourse on ethics as applied to war | Ethics § Military ethics | Ethics (applied) | Critical thinker |
| Analogical inference | Analogical inference | Argument from analogy | Logic | Logician |
| Deductive reasoning | Deductive reasoning | Deductive reasoning | Logic | Logician |
| Dialectic reasoning | Dialectic reasoning. Books on this topic will instead talk about using the dialogue, as this opens up the dialogue literary form. | Dialectic | Logic | Logician |
| Direct inference | Direct inference | Statistical syllogism | Logic | Logician |
| Formal reasoning | Formal reasoning | Reason | Logic | Logician |
| Hypothetical syllogisms | Hypothetical syllogisms | Hypothetical syllogism | Logic | Logician |
| Inductive reasoning | Inductive reasoning | Inductive reasoning | Logic | Logician |
| Propositional logic |  | Propositional calculus | Logic |  |
| Syllogistic logic | Syllogistic logic | Syllogism | Logic | Logician |
| Causation | The nature of causation | Causality | Metaphysics | Critical thinker |
| Events | Discourse on the nature of events | Event (philosophy) | Metaphysics | Critical thinker |
| Existence | The nature of existence. | Existence | Metaphysics | Critical thinker |
| Mind body | Discourse on the nature of mind and body | Mind–body problem | Metaphysics | Critical thinker |
| Objects and properties | The relationship between objects and their properties | Essence | Metaphysics | Critical thinker |
| Processes | The nature of processes | Process philosophy | Metaphysics | Critical thinker |
| Time | Discourse on the nature of time | Time | Metaphysics | Critical thinker |
| Wholes and parts | The relationship between wholes and parts | Mereology | Metaphysics | Critical thinker |
| Education | Education, its forms and recommendations | Education | Specialized | Critical thinker |
| Law | Discourse on law | Law | Specialized | Critical thinker |
| Dictionary | Dictionaries | Dictionary | Specialized (language) | Critical thinker |
| Etymology | The notion of etymology | Etymology | Specialized (language) | Critical thinker |
| Grammar | Grammar | Grammar | Specialized (language) | Critical thinker |
| Diplomacy | Discourse on diplomacy | Diplomacy | Specialized (politics) | Critical thinker |
| Economic policy | Discourse on economic policy | Economic policy | Specialized (politics) | Critical thinker |
| Government forms | Discourse on government | Government | Specialized (politics) | Critical thinker |
| Social welfare | Discourse on social welfare | Welfare | Specialized (politics) | Critical thinker |
| Value agendas | The philosopher will choose a belief that they have and write about the "worthlessness/nuances/value of (belief)". Reading these books will result in a dwarf's (or adventurer's) values changing. [1] [2] | Propaganda | *n/a* |  |

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
If visitor scholars are allowed in a library, one should regularly check all books for nature-related value agenda to prevent fortress citizens from wandering off to start a dwarven forest retreat.
