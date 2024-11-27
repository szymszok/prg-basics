arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def modify_array(array):
    for i in range(1,6):
        for j in range(1,6):
            array[i - 1][j - 1] = i * j
    
    return array

array_ready = modify_array(arr)
for row in array_ready:
    print(row)
