def calculate_purchase_price(purchase, set_to_dict=False):
    total = 0
    for item in purchase['books']:
        total += item['price']
    if set_to_dict:
        purchase['total'] = total 
    return total
    
