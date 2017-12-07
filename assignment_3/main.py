def number_of_customers_per_state(customers_dict):
    number_of_customers = {state: len(customers) if customers else 0 
                for state, customers in customers_dict.items()}
    return number_of_customers
