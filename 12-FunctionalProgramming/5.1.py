from functools import reduce

numbers = [1, 2, 3, 4, 5]

add = lambda x,y : x + y
# Using reduce to sum the numbers
result = reduce(add, numbers)
print(result)  # Output: 15