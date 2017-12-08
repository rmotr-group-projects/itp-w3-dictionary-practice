def eldest_customer_per_state(customers_dict):
    name = ''
    age = 0
    state_eldest = {}
    
    for state, customers_list in customers_dict.items():
        for customers in customers_list:
            if customers['age'] > age:
                name = customers['name']
                age = customers['age']
                
        if age != 0:
            state_eldest.update({state : {'name' : name, 'age' : age}})
        else:
            state_eldest.update({state : None})
        age = 0
        
    return state_eldest