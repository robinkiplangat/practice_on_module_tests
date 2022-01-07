import pytest
import sys
sys.path.insert(0, './src')
from scripts.preprocessing_helpers import convert_to_int, row_to_list


class TestRowToList(object):
    def test_on_no_tab_no_missing_value(self):  # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_no_missing_value(self):  # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_one_tab_with_missing_value(self):  # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_no_tab_with_missing_value(self):  # (0, 1) case
        # Assign to the actual return value for the argument "\n"
        actual = row_to_list("\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_with_missing_value(self):  # (2, 1) case
        # Assign to the actual return value for the argument "123\t\t89\n"
        actual = row_to_list("123\t\t89\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        # Fill in with the expected return value for the argument "123\t4,567\n"
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        # Write the assert statement along with a failure message
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

class TestConvertToInt(object):
    def test_convert_to_int(self):
        return_value = convert_to_int("2,081")
        assert isinstance(return_value, int)
        assert return_value == 2081

    def test_with_no_comma(self):
        actual = convert_to_int("756")
        assert actual == 756, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        assert actual == 1034891, "Expected: 2081, Actual: {0}".format(actual)

    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_incorrectly_placed_comma(self):
        actual = convert_to_int("12,72,891")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_one_comma(self):
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
