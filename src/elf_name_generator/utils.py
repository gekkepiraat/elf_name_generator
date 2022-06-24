"""Utils module."""

import os
import re
from typing import Tuple

from .typing_ import List, ListStrInt, OptionalStrInt

BASE_DIR = os.path.join(os.path.dirname(__file__))
FILE_T2 = '../names/t2.txt'
FILE_T3 = '../names/t3.txt'


def parse_data(row: str, suffix_table: bool) -> dict:
    """Parse str line."""
    str_list = re.findall(r'[A-Za-z\-]+', row)
    word_part, meaning = [], []
    key = 'prefix' if not suffix_table else 'suffix'
    for char in str_list:
        if char.startswith('-'):
            word_part.append(char[1:])
        elif char.istitle():
            word_part.append(char)
        else:
            meaning.append(char)

    return {word_part[0]: {key: word_part[1:], 'meaning': meaning}}


def _read_from_file(file_name: str,
                    diced_numbers: List[int],
                    t3=False) -> dict:
    """Read data from a file."""
    output = {}
    with open(file_name, 'r', encoding='utf-8') as rows:
        for row in rows:
            line_number = re.search(r'\d+', row).group()
            if line_number in diced_numbers:
                output[int(line_number)] = parse_data(row, t3)
    return output


def full_path(file_name: str) -> str:
    """Make an absolute path to a file."""
    return os.path.join(BASE_DIR, file_name)


def get_table_data(first_part: ListStrInt,
                   last_pref: OptionalStrInt,
                   last_suf: OptionalStrInt) -> Tuple[dict, dict]:
    """Retrieve table data from a file."""
    def sorted_(input_):
        # List of numbers for a name prefix and suffix
        return sorted(re.findall(r'\d+', str(input_)))

    file2 = full_path(FILE_T2)
    file3 = full_path(FILE_T3)

    if not os.path.exists(file2) or not os.path.exists(file3):
        raise FileNotFoundError(f'{FILE_T2} and/or {FILE_T3} is not found.')

    return (_read_from_file(file2, sorted_([first_part[0], last_pref])),
            _read_from_file(file3, sorted_([first_part[1], last_suf]), True))
