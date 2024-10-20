decimal = int(input('Enter decimal number: '))
remainder = 0

while decimal > 0: 
    remainder = decimal % 2
    
    decimal = decimal // 2


print(f'{decimal}(10) = {remainder}(2)')
