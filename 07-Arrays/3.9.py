arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]
arr3 = [3,2,1]
arr4 = [3,2]


def compare(array1, array2):
    if len(array1) != len(array2):
        return 'arrays are not the same'

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return 'arrays are not the same'
    return 'arrays are the same'

print(compare(arr1,arr2))
print(compare(arr3,arr4))
