amount = int(input('Enter number of products porchased: '))
price = 50
discount = ''
count = 0
if amount > 2:
    discount = True
else:
    discount = False

if discount == True:
    count = (price / 100) * 75 * amount
else:
    count = amount * price


print(f'Number of products purchased: {amount}')
print(f'Product price: {price}')
print(f'Amount to pay: {count}')