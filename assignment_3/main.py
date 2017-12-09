def number_of_customers_per_state(customers):
    results = {}
    for state, state_customers in customers.items():
        if state_customers is None:
            results[state] = 0
        else:
            results[state] = len(state_customers)
    return results
