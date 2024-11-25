import random
arr = [7,9,2,4,5,6]

def rand_elem(array):
    i = random.randint(0,5)
    return array[i]

print(rand_elem(arr))
