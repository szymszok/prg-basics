arr = [4,36,12,28,9,44,5]

def bubblesort(array):
    return sorted(array)

print(bubblesort(arr))


#ZROBIONE SORTOWANIEM BABELKOWYM

def bubblesort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Test arrays
arrays_to_sort = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [3, 0, 2, 5, -1, 4, 1]
]

# Sort and print the results
for array in arrays_to_sort:
    sorted_array = bubblesort(array)
    print(f"Original array: {array}")
    print(f"Sorted array: {sorted_array}\n")