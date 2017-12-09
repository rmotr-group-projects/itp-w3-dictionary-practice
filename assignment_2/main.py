def calculate_purchase_price(purchase, set_to_dict=False):

    total = 0
    for each in purchase['books']:
        for k, v in each.items():
            if k == 'price':
                total += v
    if set_to_dict == True:
        purchase['total'] = total
    print(total)
    return total
            
        
purchase = {
    'id': 99,
    'books': [{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'price': 19.99
    }, {
        'title': 'Ulysses',
        'author': 'James Joyce',
        'price': 23.99
    }, {
        'title': 'The Odyssey',
        'author': 'Homer',
        'price': 7.99
    }],
    'total': 0
    }
    
calculate_purchase_price(purchase, set_to_dict=False)
    
    
