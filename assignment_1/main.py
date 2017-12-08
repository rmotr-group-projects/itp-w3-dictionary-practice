def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    
    for k, v in purchase_dict.items():
            if k == 'books':
                return v.append({
                            'title': title,
                            'author': author,
                            'price': price
                        })
           
           
'''TEMPLATE
{
    'title': title,
    'author': author,
    'price': price
}
'''