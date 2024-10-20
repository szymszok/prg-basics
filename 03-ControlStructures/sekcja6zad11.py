price = 200
new_price = 140
percent = price / 100
discount = (price - new_price) / percent
print(f'Previous product price {price}')
print(f'Current product price {new_price}')
if discount > 10:
    print('Buy the product!!')
    print(f'Product price reduces by {discount}%')
else:
    print('There is no good recommendation ')

