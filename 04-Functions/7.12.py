def asterisk(n):
    ast = '*'
    slash = '/'
    for i in range(n - 1):
        print(f'{ast}{slash}', end='')
    print(ast) 
    return 

number = int(input('Enter number: '))
asterisk(number)