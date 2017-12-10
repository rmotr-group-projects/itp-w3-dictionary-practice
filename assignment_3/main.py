def number_of_customers_per_state(customers_dict):
    result = {}
    for state in customers_dict.keys():
        customers_in_this_state = customers_dict[state]
        if customers_in_this_state:
            n = len(customers_in_this_state)
        else:
            n = 0
        result[state] = n
    print(result)
    return result 
