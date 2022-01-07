import pytest
from scripts.preprocessing_helpers import convert_to_int


def test_convert_to_int():
    return_value = convert_to_int("2,081")
    assert isinstance(return_value, int)
    assert return_value == 2081
      
    
