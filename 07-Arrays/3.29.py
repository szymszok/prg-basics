def create_2d_arr(x,y):
    arr1 = []
    for _ in range(x):
        row = [0] * y
        arr1.append(row)
    
    return arr1
rows = 5
column = 5

array_2d = create_2d_arr(rows, column)
for row in array_2d:
    print(row)