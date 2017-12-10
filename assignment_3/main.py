def number_of_customers_per_state(customers_dict):
    newdict = {}
    for key, value in customers_dict.items():
        if value != None:
            newdict[key] = len(value)
        else:
            newdict[key] = 0
    return newdict
        
