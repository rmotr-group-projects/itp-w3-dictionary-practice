def number_of_customers_per_state(customers_dict):
  result = {}
  
  for state, state_customer in customers_dict.items():
    if state_customer is None:
      result[state] = 0
      
    else: 
      result[state] = len(state_customer)
      
  return result