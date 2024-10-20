amount = int(input('Enter the amount in PLN: '))
coin_1 = 0
coin_2 = 0
coin_5 = 0


coin_5 = amount // 5 
amount %= 5
coin_2 = amount // 2
amount %= 2
coin_1 = amount


print(f'The amount of PLN {amount} in coins: ')
print(f'5 PLN coins: {coin_5}')
print(f'2 PLN coins: {coin_2}')
print(f'1 PLN coins: {coin_1}')