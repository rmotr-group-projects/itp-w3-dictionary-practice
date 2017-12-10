def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    newbook = {
        'title': title,
        'author': author,
        'price': price
    }
    purchase_dict['books'].append(newbook)
    return purchase_dict

#def add_book_to_purchase(purchase_dict, title, author, price=0.99):
#   newdict = {}
#   newdict['title'] = title
#   newdict['author'] = author
#   newdict['price'] = price
#   purchase_dict['book '].append(newdict)
#   return purchase_dict