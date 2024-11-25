arr = [7,9,2,4,5,6]

def f(arr,number):
    arr1 = []
    for i in arr:
        if int(i) > number:
            arr1.append(i)
    
    return arr1

num = int(input('Podaj liczbę: '))

print(f(arr,num))