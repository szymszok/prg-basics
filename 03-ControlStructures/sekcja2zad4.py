# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: ')) 
operator = input('Enter operator: ')
result = 0
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print('invalid data')

print(f'Result: {result}')