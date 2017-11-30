# Dictionary Practice

Each assignment under `assignment_1`, `assignment_2`, `assignment_3` and `assignment_4` contains detailed instructions. This readme contains a summary of how to run the tests.

## Running tests
_(make sure the virtual environment is active before running tests)_

##### Running all tests

```bash
(my-virtualenv) $ py.test assignment_1/tests.py
```

![image](https://user-images.githubusercontent.com/872296/33446165-fbfda988-d5dd-11e7-98eb-fe838d6ac888.png)


##### Running a single test function

```bash
(my-virtualenv) $ py.test assignment_1/tests.py -k default_price
```

![image](https://user-images.githubusercontent.com/872296/33446227-271cbfdc-d5de-11e7-942f-db1de36c4837.png)

##### Controlling test output

You can control the way errors are shown with the `--tb` argument. For example, for shorter error details:

```bash
(my-virtualenv) $ py.test assignment_1/tests.py --tb=short 
```

![image](https://user-images.githubusercontent.com/872296/33446290-55b04350-d5de-11e7-9327-43a8c10df284.png)
