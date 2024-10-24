def f(binary_number):
    for char in binary_number:
        if char == '1' or char == '0':
            is_true = True
        else:
            is_true = False
            break

    return is_true


number = input('Enter numbers to check: ')
print(f(number))