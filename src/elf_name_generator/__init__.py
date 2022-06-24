"""Import functions."""

from .message import display_d10 as roll_dice_message
from .name import ElfNameGenerator
from .number import get_pair_numbers, roll_dice

__all__ = [
    'ElfNameGenerator',
    'get_pair_numbers',
    'roll_dice_message',
    'roll_dice'
]
