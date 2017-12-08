def number_of_customers_per_state(customers_dict):
    state_count = {}
    
    for state, customer_list in customers_dict.items():
        if customer_list == None:
            customer_sum = 0
        else:
            customer_sum = len(customer_list)
        
        state_count.update({state : customer_sum })
        
    return state_count