def calculate_purchase_price(purchase, set_to_dict=False):
    total = 0
    for book in purchase['books']:
        total += book['price']

    if set_to_dict is True:
        purchase['total'] = total

    return total

