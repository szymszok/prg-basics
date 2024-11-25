arr1 = [7,5,4,2]
arr2 = [7,9,2,4,5,6]

def f(array1,array2):
    set1 = set(array1)
    set2 = set(array2)

    return set1.issubset(set2)
        
print(f(arr1,arr2))
