def calculate_purchase_price(purchase, set_to_dict=False):
    purchase_total = 0
    
    for _k_, _v_ in purchase.items():
        if _k_ == 'books':
            for v in _v_:
                for p, c in v.items():
                    if p == 'price':
                        purchase_total += c
                        
    if set_to_dict == True:
        purchase.update({'total' : purchase_total})
        
    return purchase_total
    
''' DISCUSSED MORE EFFICIENT SOLUTION

def calculate_purchase_price(purchase, set_to_dict=False):

    books = purchase['books']
    total = 0

    for book in books:
        total += book.get('price')

    if set_to_dict == True:
        purchase['total'] = total

    return total
    
'''