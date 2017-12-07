def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    new_purchase = {
        'title' : title,
        'author' : author,
        'price' : price
        }
    
    purchase_dict['books'].append(new_purchase)
            
    return purchase_dict
