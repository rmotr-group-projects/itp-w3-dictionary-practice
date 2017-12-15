def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    book = {}
    book['title'] = title
    book['author'] = author
    book['price'] = price
    
    purchase_dict['books'].append(book)
    

'''
add_book_to_purchase(
        purchase_dict,
        title='The Odyssey',
        author='Homer',
        price=7.99)
'''
