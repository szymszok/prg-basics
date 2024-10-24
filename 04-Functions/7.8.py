def f(amount_to_pay):
    coin_1 = 0
    coin_2 = 0
    coin_5 = 0
    coin_5 = amount_to_pay // 5
        
    coin_2 = (amount_to_pay - coin_5 * 5) // 2
    coin_1 = amount_to_pay - (coin_5 * 5) - (coin_2 * 2)

    return coin_1 + coin_2 + coin_5

number = int(input('Enter number: '))
print(f(number))