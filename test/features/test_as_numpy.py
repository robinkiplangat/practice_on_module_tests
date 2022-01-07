import numpy as np
import pytest
import sys
sys.path.insert(0, './src')
from features.as_numpy import get_data_as_numpy_array

filePath = "src/data/example_clean_data.txt"
class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info < (2, 7), reason="Works only on Python 2.7 or higher")
    def test_on_clean_file(self):

        expected = np.array(
            [[2081.0, 314942.0], [1059.0, 186606.0], [1148.0, 206186.0]]
        )
        actual = get_data_as_numpy_array(filePath, num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(
            expected, actual
        )
        # Complete the assert statement
        assert actual == pytest.approx(expected), message
