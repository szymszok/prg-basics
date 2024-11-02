def neg_even(x, y):
    total_sum = 0
    for i in range(x, y):
        if i % 2 == 0 and i < 0:
            total_sum += 1
    
    return total_sum

x = int(input('Enter starting range: '))
y = int(input('Enter ending range: '))
print(neg_even(x, y))