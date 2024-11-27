arr = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16]
]

def find(array):
    maxx = 0
    minn = 0
    min_position = (-1, -1)
    max_position = (-1, -1)
    for i in range(len(array)):
        for j in range(len(array[i])):
            value = array[i][j]
            if value < minn:
                minn = value
                min_position = (i, j)
            if value > maxx:
                maxx = value
                max_position = (i, j)
    return (maxx, minn), (max_position, min_position)

((max_value, min_value), (max_posit, min_posit)) = find(arr)
print(f'Max value: {max_value} at position: {max_posit}')
print(f'Min value: {min_value} at position: {min_posit}')


"""
    i = 0
    j = 0
    for item in array:
        if i > maxx:
            maxx = i
        elif i < minn:
            minn = i
        for j in item:
            if j > maxx:
                maxx = j
            elif j < minn:
                minn = j
    return maxx,minn, 
    """

