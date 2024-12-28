def f(arr):
    """Returns the number in the array that is different from the others."""
    # Use a dictionary to count occurrences of each number
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Find the number that occurs only once
    for num, cnt in count.items():
        if cnt == 1:
            return num

print(f([7,7,7,7,5,7,7,7]))