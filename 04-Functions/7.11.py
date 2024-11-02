def check(n1, n2, n3):
    if n1 > 0 and n2 > 0 and n3 > 0:
        is_true = False
    else:
        is_true = True
    return is_true
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
print(check(num1, num2, num3))
