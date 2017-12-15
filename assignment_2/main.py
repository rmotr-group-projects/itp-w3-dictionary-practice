def calculate_purchase_price(purchase, set_to_dict=False):
    total = 0
    for book in purchase['books']:
        price = book['price']
        total += price

    if set_to_dict is True:
        purchase['total'] = total
    return total
