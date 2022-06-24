# Elf Name Generator

## About
I searched for a name generator on the Internet and found a source
[Aérithaéné](https://www.angelfire.com/rpg2/vortexshadow/arethanehome2.html?) specifically for elven. I found the tables
with a name generator pretty interesting (especially if you're a D&D/RPG gamer) and decided to automate it. Just for fun.

It is important that names represent and reflect the race’s special attitudes and philosophies. The elven name generator
below has been presented to assist with this daunting task. Although this could not possibly represent all the possible
names for a race as old and diverse as the elves, this list can serve as a starting point and quick reference to create
a large and consistent list of names.
Inspired by [Aérithaéné project](https://www.angelfire.com/rpg2/vortexshadow/names.html?).

## How it Works
Each elven name consists of a prefix (from Table 2) and one or more suffixes (from Table 3).
Definitions have been included in these tables to help determine what a name means once it has been generated.
In the case of suffixes, male and female endings have been included where appropriate. Alternate spellings have also
been provided in some cases. In Some Cases a formal house name can be generated as well by rolling randomly on Optional
Table 1B. These formal House names would be used for ancient noble houses, usually of Grey or Gold Elf Descent.

You may randomly generate an elven name by rolling on Table 1. If you prefer, it is also possible to pick a set of
definitions you like and assemble the name that matches them. If your character is a ranger who is fond of bears,
you might decide her name should reflect this. Looking at the definitions, you decide her name will mean “Bear-Friend.”
This results in the name “Rethar,” “Reethar,” or “Reithar.”


## How to Use
Example of a code

```python

from elf_name_generator import ElfNameGenerator, get_pair_numbers, roll_dice

args = list()
## Option 1 - w/o arguments
## Option 2 - args = get_pair_numbers(roll_dice())

elf = ElfNameGenerator(*args)

print(f'>>> "{elf.dice_number}":', elf.roll_dice_message())
print(f'>>> "{elf.dice_number}":', elf.get_name())
print(f'>>> "{elf.dice_number}":', elf.get_definition())
```

And output will be
```bash
$ python main.py
>>> "1": Roll once on T2 and once on T3.
>>> "1": Caellar
>>> "1": Archer/arrow shine
```

## Development
Currently, two tables are in use (Table 2 - Prefixes (D100) and Table 3 - Suffixes (D100)). Table 1 (D10) is used to
get the rule of what flow to use to generate an elven name.

### Check and test
```bash
  $ pre-commit run --all-files
  $ pytest
```

### Todo
1. Separate male and female names where it is possible.
2. The list of alternative names is in the process.
3. Optional Table 1B (D10) (that would work with extra tables Table 4 -
   House Name Prefixes(D100) and Table 5 - House Name Suffixes (D100))
