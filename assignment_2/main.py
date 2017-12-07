def calculate_purchase_price(purchase, set_to_dict=False):
    books = purchase['books']
    total = 0
    
    for book in books:
        total += book.get('price')
        
    if set_to_dict == True:
        purchase['total'] = total
        
    return total 
