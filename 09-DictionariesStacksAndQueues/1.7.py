store = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
counter = 0
for object, quantity in store.items():
    counter += quantity
    print(f'{object}: {quantity}')
    
print()
print(f'Total number of products: {counter}')