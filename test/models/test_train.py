import sys
import os

sys.path.insert(0, "./src")
import pytest
import numpy as np
from models.train import split_into_training_and_testing_sets, model_test


class TestSplitIntoTrainingAndTestingSets(object):
    def test_on_six_rows(self):
        example_argument = np.array(
            [
                [2081.0, 314942.0],
                [1059.0, 186606.0],
                [1148.0, 206186.0],
                [1506.0, 248419.0],
                [1210.0, 214114.0],
                [1697.0, 277794.0],
            ]
        )
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 4
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = (
            example_argument.shape[0] - expected_training_array_num_rows
        )
        actual = split_into_training_and_testing_sets(example_argument)
        # Write the assert statement checking training array's number of rows
        assert (
            actual[0].shape[0] == expected_training_array_num_rows
        ), "The actual number of rows in the training array is not {}".format(
            expected_training_array_num_rows
        )
        # Write the assert statement checking testing array's number of rows
        assert (
            actual[1].shape[0] == expected_testing_array_num_rows
        ), "The actual number of rows in the testing array is not {}".format(
            expected_testing_array_num_rows
        )


@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_perfect_fit(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(
            expected, actual
        )

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)

    def test_on_circular_data(self):
        theta = pi / 4.0
        test_argument = np.array(
            [
                [0.0, 1.0],
                [cos(theta), sin(theta)],
                [1.0, 0.0],
                [cos(3 * theta), sin(3 * theta)],
                [0.0, -1.0],
                [cos(5 * theta), sin(5 * theta)],
                [-1.0, 0.0],
                [cos(7 * theta), sin(7 * theta)],
            ]
        )
        actual = model_test(test_argument, 0.0, 0.0)
        assert actual == pytest.approx(0.0)
