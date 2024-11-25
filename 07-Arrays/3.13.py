arr = [15,38,7,23,14]


def occurs(number, array):
    result = False
    for num in array:
        if number == num:
            result = True
            break
        else:
            result = False
    
    return result

    

num = int(input('Podaj numer: '))
print(occurs(num,arr))
