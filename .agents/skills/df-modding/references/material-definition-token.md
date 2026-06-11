# Material definition token

> Fonte: [Material definition token](https://dwarffortresswiki.org/index.php/Material_definition_token) — Dwarf Fortress Wiki (GFDL/MIT)

The following tokens can be used in material definitions (whether for inorganics or those within plants and creatures) as well as in material templates.

## Material properties

[TABLE]

### Material states

The following is a list of valid material states:

|                                    |
|------------------------------------|
| **SOLID**                          |
| **LIQUID**                         |
| **GAS**                            |
| **POWDER** (or **SOLID_POWDER**)   |
| **PASTE** (or **SOLID_PASTE**)     |
| **PRESSED** (or **SOLID_PRESSED**) |

The following can be specified within tokens such as STATE_NAME, STATE_NAME_ADJ and STATE_ADJ to make them apply to several of the above material states simultaneously:

| Value         | Description                                       |
|---------------|---------------------------------------------------|
| **ALL**       | Denotes all possible material states.             |
| **ALL_SOLID** | Denotes 'SOLID', 'POWDER', 'PASTE' and 'PRESSED'. |

## Material usage tokens

[TABLE]

## Syndrome tokens

Below is a table with some of the tokens you can use when declaring a \[SYNDROME\] token. For all the tokens you can use, see the Syndrome token page.

[TABLE]

## See also

- Inorganic material definition token
- Syndrome
- Hardcoded material
