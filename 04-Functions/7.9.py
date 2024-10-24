def even_odd(number, even):
    total_sum = 0
    for char in number:
        digit = int(char)
        if digit % 2 == 0 and even == 'True':
            total_sum += digit
        elif digit % 2 != 0 and even == 'False':
            total_sum += digit
     
    return total_sum


number = input('Type number: ')
even = input('"True" if you want even number, otherwise "False" ')

print(even_odd(number, even))
