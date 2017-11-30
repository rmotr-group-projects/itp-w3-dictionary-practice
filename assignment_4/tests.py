from main import eldest_customer_per_state


def test_eldest_customer_per_state_basic_use_case():
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',  # Eldest
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': [{
            'name': 'Linda',  # Eldest (only customer)
            'age': 71
        }],
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }, {
            'name': 'Helen',  # Eldest
            'age': 29
        }]
    }
    expected_result = {
        'UT': {
            'name': 'John',
            'age': 31
        },
        'NY': {
            'name': 'Linda',
            'age': 71
        },
        'CA': {
            'name': 'Helen',
            'age': 29
        }
    }

    assert eldest_customer_per_state(customers) == expected_result


def test_eldest_customer_per_state_with_empty_states():
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',  # Eldest
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': [],
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }, {
            'name': 'Helen',  # Eldest
            'age': 29
        }]
    }
    expected_result = {
        'UT': {
            'name': 'John',
            'age': 31
        },
        'NY': None,
        'CA': {
            'name': 'Helen',
            'age': 29
        }
    }

    assert eldest_customer_per_state(customers) == expected_result

