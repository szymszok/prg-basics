time = int(input('Enter parking hours '))
price = 0
if time >= 1 and time <=2:
    price = time * 5
elif time >=3 and time <=6:
    price = time * 15
elif time > 6:
    price = time * 20

print(f'Your parking for {time} hours, cost {price}')