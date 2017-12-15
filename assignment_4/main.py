def eldest_customer_in_list(customers_list):
    eldest_customer = None # {'age': 1, 'name': 'Empty Customer'}
    for customer in customers_list:
        if eldest_customer is None or customer['age'] >= eldest_customer['age']:
            eldest_customer = customer
    return eldest_customer

def eldest_customer_per_state(customers):
    result = {}
    for state, state_customers in customers.items():
        eldest_customer = eldest_customer_in_list(state_customers)
        result[state] = eldest_customer
    return result
