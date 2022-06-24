"""Generate prefix and suffix numbers."""

import random
from typing import Tuple

from .typing_ import ListStrInt, OptionalStrInt, StrInt


def roll_dice(number=10) -> int:
    """Roll dice 10 or 100."""
    if number not in (10, 100):
        number = 10
    return random.randint(1, number)


def get_pair_numbers(dice_number: int) -> Tuple[ListStrInt, OptionalStrInt]:
    """Map dice number to 1, 2 or 0 and generate pare numbers.

    Map dice number to define whether only first part should be or the
    part name and a last part.
    Generate number for a prefix and a suffix for the first and last parts.
    E.g.:
        "4" -  Roll once on T2 and once on T3. (Output is a first part)
        "4" - ([77, 39], [0, 0])

        "5" -  Roll once on T2 and twice on T3. (Output is a first part)
        "5" - ([12, [37, 4]], [0, 0])

        "10" - Roll once on T3, add an apostrophe, then roll once on T2 and
                twice on T3. (Output is a first part and a last part)
        "10" - (["'", 32], [43, [16, 99]])

    t2 - first part prefix, data taken from Table 2
    t3 - first part suffix, data taken from Table 3
    t2_ - last part prefix, data taken from Table 2
    t3_ - last part suffix, data taken from Table 3
    """
    dn = str(dice_number)
    t2, t3, t2_, t3_ = 1, 1, 0, 0
    if dn in "1234":
        pass
    elif dn in "567":
        t3 = 2
    elif dn in "89":
        t2_, t3_ = 1, 2
    elif dn in "10":
        t2, t3, t2_, t3_ = "'", 1, 1, 2

    first_part_number = list(map(_roll_dice_d100, (t2, t3)))
    last_part_number = list(map(_roll_dice_d100, (t2_, t3_)))
    if last_part_number[0] == 0:  # last part might be absent ~ [0, 0]
        last_part_number = None
    return first_part_number, last_part_number


def _roll_dice_d100(number: int) -> StrInt:
    """Generate number from 1 to 100 based on D100.

    Note: number should be 0, 1 or 2
    """
    if number == 0 or isinstance(number, str):
        return number

    output = []
    for _ in range(0, number):
        output.append(roll_dice(100))
    return output if len(output) > 1 else output[0]
