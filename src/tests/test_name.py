"""Test name module."""

import pytest

from elf_name_generator import ElfNameGenerator
from tests.mock_data import elf_name1, elf_name2


def _make_test_name(elf_name):
    """Mock Factory for ElvenName object."""
    en = ElfNameGenerator(elf_name.first_part, elf_name.last_part)
    en._t2_data = elf_name.t2_data
    en._t3_data = elf_name.t3_data
    return en


def _make_test_full_name():
    """Data with full name."""
    return _make_test_name(elf_name1)


def _make_test_first_name():
    """Data with only first name given."""
    return _make_test_name(elf_name2)


def test_first_name():
    """Create first name based on full and first part only."""
    en1 = _make_test_full_name()
    name1 = en1._make_a_word(en1._first_part)
    expected1 = "Shelian"
    assert expected1 == name1

    en2 = _make_test_first_name()
    name2 = en2._make_a_word(en2._first_part)
    expected2 = "Eilrah"
    assert expected2 == name2


def test_full_name():
    """Create full name based on full and first part only."""
    en1 = _make_test_full_name()
    first_name1 = en1._make_a_word(en1._first_part)
    last_name1 = en1._make_a_word(en1._last_part)
    expected1 = "Shelian Zathusro"
    assert expected1 == first_name1 + " " + last_name1

    en2 = _make_test_first_name()
    first_name2 = en2._make_a_word(en2._first_part)
    last_name2 = en2._make_a_word(en2._last_part)
    expected2 = "Eilrah"
    assert expected2 == first_name2 + last_name2


def test_first_name_definition():
    en2 = ElfNameGenerator(elf_name2.first_part, elf_name2.last_part)
    with pytest.raises(NameError) as exc:
        en2.get_definition()
    assert "Run name generator to retrieve its definition." in str(exc.value)

    name2 = en2.get_name()
    expected2 = "Eilrah"
    assert expected2 == name2

    def2 = en2.get_definition()
    expected = "Azure/blue beast"
    assert expected == def2


def test_full_name_definition():
    en1 = ElfNameGenerator(elf_name1.first_part, elf_name1.last_part)
    with pytest.raises(NameError) as exc:
        en1.get_definition()
    assert "Run name generator to retrieve its definition." in str(exc.value)

    name1 = en1.get_name()
    expected1 = "Shelian Zathusro"
    assert expected1 == name1

    def1 = en1.get_definition()
    expected = "Age/time master/mistress Royal"
    assert expected == def1


def test_alternative_first_name():
    en2 = _make_test_first_name()
    with pytest.raises(NotImplementedError) as exc:
        en2.get_alternatives()
    assert "Make a method!" in str(exc.value)
    # TODO: make a method
    # expected = 'Eilrae, Eilraee'
    # assert expected == alt2


def test_alternative_full_name():
    en1 = _make_test_full_name()
    with pytest.raises(NotImplementedError) as exc:
        en1.get_alternatives()
    assert "Make a method!" in str(exc.value)
    # TODO: make a method!
    # expected = 'Shelia Zarithas, Shelia Zaronaethus, Shelia Zaroaethas'
    # assert expected == alt1


def test_name_9():
    """Test name that fits dice 8-9."""
    elf_name_numbers = ([79, 49], [99, [85, 70]])
    en = ElfNameGenerator(*elf_name_numbers)
    expected_name = "Shelian Zathusro"
    assert expected_name == en.get_name()
    expected_definition = "Age/time master/mistress Royal"
    assert expected_definition == en.get_definition()


def test_name_10():
    """Test name that fits dice 10, name with apostrophe."""
    elf_name_numbers = (["'", 18], [62, [21, 7]])
    en = ElfNameGenerator(*elf_name_numbers)
    expected_name = "Dar'Naidrimal"
    assert expected_name == en.get_name()
    expected_definition = "World Oak"
    assert expected_definition == en.get_definition()


if __name__ == "__main__":
    retcode = pytest.main(["-x"])
    print(retcode)
