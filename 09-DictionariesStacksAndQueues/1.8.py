price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
before_discount = 0
for item, price in price_list.items():
    print(f'{item}: {price}')
    before_discount += price
    formated_before = '{:.2f}'.format(before_discount)
print(f'Price before discount: {formated_before}')
print()
after_dicount = 0
for item, price in price_list.items():
    price = price - (price * 0.1 )
    formated_price = '{:.2f}'.format(price)
    print(f'{item}: {formated_price}')
    after_dicount += price

print()
formated_after = '{:.2f}'.format(after_dicount)
print(f'Full price after discount: {formated_after}')
