def fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n):
        a, b = b, a + b
    return b

number = int(input('Enter number: '))
print(fibonacci(number))