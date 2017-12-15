def number_of_customers_per_state(customers_dict):
    answer = {}
    for state, value in customers_dict.items():
        if value == None:
            answer[state] = 0
        else:
            answer[state] = len(value)
        
    print(answer)
    return answer
        