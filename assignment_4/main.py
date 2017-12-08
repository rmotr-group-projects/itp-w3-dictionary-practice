def eldest_customer_in_list(customer_list) :
  eldest = None
  
  for customer in customer_list:
    if eldest is None or customer["age"] >= eldest["age"]:
      eldest = customer
  
  return eldest
  
def eldest_customer_per_state(customer_list):  
  #the main thing
  result = {}
  
  for state, state_customer in customer_list.items():
    eldest_customer_in_state = eldest_customer_in_list(state_customer)
    
    result[state] = eldest_customer_in_state
  
  return result
