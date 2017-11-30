# Dictionary Practice

Each assignment under `assignment_1`, `assignment_2`, `assignment_3` and `assignment_4` contains detailed instructions. This readme contains a summary of how to run the tests.

## Running tests
_(make sure the virtual environment is active before running tests)_

##### Running all tests

```bash
(my-virtualenv) $ py.test assignment_1/tests.py
```

##### Running a single test function

```bash
(my-virtualenv) $ py.test assignment_1/tests.py -k test_add_book_to_purchase
```

##### Controlling test output

You can control the way errors are shown with the `--tb` argument. For example, for shorter error details:

```bash
(my-virtualenv) $ py.test assignment_1/tests.py --tb=short 
```
