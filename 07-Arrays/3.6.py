arr = [15, 8, 31, 47, 2, 19]

summ = 0
count = 0

i = 0
while i < len(arr):
    summ += arr[i]
    count += 1
    i += 1

print(summ / count)