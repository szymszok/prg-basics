arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
i = 1
summ = 0
for row in arr:
    for item in row:
        if i == 4:
            summ += int(item)
    i += 1

print(summ)