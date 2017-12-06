def eldest_customer_per_state(customers_dict):
    eldest_customers = {}
    
    for state, customers in customers_dict.items():
        age = 0
        eldest = None
        for customer in customers:
            if customer.get('age') > age:
                age = customer.get('age')
                eldest = customer
        eldest_customers[state] = eldest
    return eldest_customers

    
 
