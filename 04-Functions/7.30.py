def sum_natural(n):
    if n > 0:
        return n + sum_natural(n - 1)
    else:
        return 0



print(sum_natural(10))