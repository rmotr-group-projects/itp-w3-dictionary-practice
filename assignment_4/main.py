def eldest_customer_per_state(customers_dict):
    answer = {}
    for state, value in customers_dict.items():
        if value == None:
            answer[state] = None
        else:
            oldest = None
            for customer in value:
                name = customer['name']
                age = customer['age']
                
                if oldest is None:
                    oldest = customer
                else:
                    oldest_age = oldest['age']
                    if age >= oldest_age:
                        oldest = customer
            answer[state] = oldest
    print(answer)
    return answer