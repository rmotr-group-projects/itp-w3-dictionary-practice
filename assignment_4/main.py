def eldest_customer_per_state(customers):
    result = {}
    for state, state_customers in customers.items():
        eldest_customer = None
        for customer in customers:
            if eldest_customer is None or customer['age'] >= eldest_customer['age']:
                eldest_customer = customer
        result[state] = eldest_customer
    return result
