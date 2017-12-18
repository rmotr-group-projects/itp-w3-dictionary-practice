def eldest_customer_per_state(customers_dict):
    eldest_customer = {}
    
    for state, customers in customers_dict.items():
        age = 0
        eldest = None
        for customer in customers:
            if customer.get('age') > age:
                age = customer.get('age')
                eldest = customer
        eldest_customer[state] = eldest
    
    return eldest_customer