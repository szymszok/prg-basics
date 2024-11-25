arr = [15, 8, 31, 47, 2, 19]

result = 0
summ = 0
i = 0
for num in arr:
    summ += num
    result = summ / len(arr)


print(result)