def f(product_code):
    summ = 0
    for char in product_code[:-1]:
        summ += int(char)
        
        if summ % 7 == int(char[-1]):
            return True
        else:
            return False

print(f("1082"))
print(f("2035"))
print(f("7071"))
