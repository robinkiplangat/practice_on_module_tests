[![Build Status](https://app.travis-ci.com/robinkiplangat/practice_on_module_tests.svg?branch=main)](https://app.travis-ci.com/robinkiplangat/practice_on_module_tests)
[![codecov](https://codecov.io/gh/robinkiplangat/practice_on_module_tests/branch/main/graph/badge.svg?token=TIJ0A0XAMY)](https://codecov.io/gh/robinkiplangat/practice_on_module_tests)

# Practice Module Tests



Sample scripts to aid in understanding the Theoretical structure for Unit Testing for Data Science
on a Univariate linear regression of housing price against housing area.

## Project Structure

```
src/        #All application code
|-- data/ 
|   |-- __init__.py
|   |-- example_clean_data.txt # Sample Text file
|-- features/ # Package for feature generation from preprocessed data
|   |-- __init__.py
|   |-- as_numpy.py # Contains get_data_as_numpy_array()
|-- models/ # Package for training/testing linear regression model
|   |-- __init__.py
|   |-- train.py
|--scripts/   # Package for data preprocessing
|   |-- __init__.py
|   |-- preprocessing_helpers.py # Contains row_to_list(), convert_to_int()
|
test/ # Test suite: all tests are found here
|-- data/
|   |-- __init__.py
|-- features/
|   |-- __init__.py
|   |-- test_as_numpy.py
|-- models/
|   |-- __init__.py
|   |-- test_train.py
|-- scripts/
|   |-- test_preprocessing_helpers.py
```
