import pytest
from src.scripts.preprocessing_helpers import convert_to_int, row_to_list


def test_with_no_comma():
    actual = convert_to_int("756")
    assert actual == 756, "Expected: 756, Actual: {0}".format(actual)


def test_with_one_comma():
    actual = convert_to_int("2,081")
    assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)


def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    assert actual == 1034891, "Expected: 2081, Actual: {0}".format(actual)


def test_on_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_string_with_incorrectly_placed_comma():
    actual = convert_to_int("12,72,891")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(
        actual
    )
    # Write the assert statement which prints message opytn failure
    assert isinstance(expected, int)
    assert actual == expected, message
