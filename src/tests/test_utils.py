"""Test utils module."""

import pytest

from elf_name_generator.utils import parse_data
from tests.mock_data import (
    table2_line,
    table2_parsed_line,
    table3_line,
    table3_parsed_line,
)


@pytest.mark.parametrize(
    "row_input,expected",
    [
        [table3_line()[0], table3_parsed_line()[0]],
        [table3_line()[1], table3_parsed_line()[1]],
        [table3_line()[2], table3_parsed_line()[2]],
        [table3_line()[3], table3_parsed_line()[3]],
        [table3_line()[4], table3_parsed_line()[4]],
        [table3_line()[-3], table3_parsed_line()[-3]],
        [table3_line()[-2], table3_parsed_line()[-2]],
        [table3_line()[-1], table3_parsed_line()[-1]],
    ],
)
def test_parse_line_of_table3(row_input, expected):
    result = parse_data(row_input, True)
    assert result == expected


@pytest.mark.parametrize(
    "row_input,expected",
    [
        [table2_line()[0], table2_parsed_line()[0]],
        [table2_line()[1], table2_parsed_line()[1]],
        [table2_line()[2], table2_parsed_line()[2]],
        [table2_line()[3], table2_parsed_line()[3]],
        [table2_line()[4], table2_parsed_line()[4]],
        [table2_line()[-3], table2_parsed_line()[-3]],
        [table2_line()[-2], table2_parsed_line()[-2]],
        [table2_line()[-1], table2_parsed_line()[-1]],
    ],
)
def test_parse_line_of_table2(row_input, expected):
    result = parse_data(row_input, suffix_table=False)
    assert result == expected
