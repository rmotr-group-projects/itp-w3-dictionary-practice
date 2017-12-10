def eldest_customer_per_state(customers_dict):
    newdict = {}
    for state, customers in customers_dict.items():
        oldest = None
        for customer in customers:
            if oldest == None or customer['age'] > oldest['age']:
                oldest = customer
        newdict[state] = oldest
    return newdict
