"""Test number module."""

import random

import pytest

from elf_name_generator.number import _roll_dice_d100, roll_dice


def test_roll_dice():
    number = roll_dice()
    assert number >= 1
    assert number <= 10

    number = roll_dice(15)
    assert number >= 1
    assert number <= 10


def test_roll_dice_100():
    number = roll_dice(100)
    assert number >= 1
    assert number <= 100


def test_roll_dice_d100():
    random_int = random.randint(0, 2)
    name_numbers = _roll_dice_d100(random_int)
    print(name_numbers)
    if random_int == 2:
        assert isinstance(name_numbers, list)
    else:
        assert isinstance(name_numbers, int)


if __name__ == "__main__":
    retcode = pytest.main(["-x"])
    print(retcode)
