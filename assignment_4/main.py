def eldest_customer_per_state(customers_dict):
    results = {}
    for state, customers in customers_dict.items():
        eldest = None
        for customer in customers:
            if eldest is None or customer['age'] > eldest['age']:
                eldest = customer
        results[state] = eldest
    return results
