# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0

# Calculate the sum of even numbers
while :
    if N % 2 == 0:
        sum_even += N

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")