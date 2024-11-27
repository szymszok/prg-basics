arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

def replace_arr(array):
    
    array[0], array[-1] = array[-1], array[0]

for row in arr:
    print(row)

print()   
replace_arr(arr)

for row in arr:
    print(row)