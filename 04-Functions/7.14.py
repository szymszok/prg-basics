def arithmetic(number1, number2, operator):
    if operator == '+':
        final = number1 + number2
    elif operator == '-':
        final = number1 - number2
    elif operator == '%':
        final = number1 % number2
    elif operator == '*':
        final = number1 * number2
    elif operator == '**':
        final = number1 ** number2
    else:
        final = 'Wrong data'
    return final

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 1: '))
oper = input('Enter operator:  ')
print(arithmetic(num1, num2, oper))