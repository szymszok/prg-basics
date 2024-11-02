def summary(number):
    full_sum = 0
    digit = 0
    for char in number:
        char = int(digit)
        if digit == digit:
            full_sum += digit
    return full_sum

number = input('Enter numbers: ')
print(summary(number))