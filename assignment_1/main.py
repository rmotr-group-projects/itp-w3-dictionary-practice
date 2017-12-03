def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    listofbooks = purchase_dict['books']
    newbook = {}
    newbook['title'] = title
    newbook['author'] = author
    newbook['price'] = price
    listofbooks.append(newbook)
    purchase_dict['books'] = listofbooks
    return purchase_dict

