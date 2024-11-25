arr = [7,9,2,4,5,6]

def f(array):
    even = []
    odd = []
    for i in array:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even + odd

print(f(arr))