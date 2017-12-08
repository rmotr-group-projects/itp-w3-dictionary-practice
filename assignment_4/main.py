def eldest_customer_per_state(customers_dict):
    eldest_customer = None
    for customer in customers_list:
        if eldest_customer is None:
            eldest_customer = customer

        else:
            customer_age = customer['age']
            eldest_customer_age = eldest_customer['age']
            if customer_age >= eldest_customer_age:
                eldest_customer = customer

    return eldest_customer
