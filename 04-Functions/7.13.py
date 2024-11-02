def string(n):
    final = ''
    for i in range(1, n + 1):
        word = str(i)
        final += word
    return final


number = int(input('Enter number: '))
print(string(number))

