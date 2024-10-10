import random
roll = random.randint(1,6)
is_roll = roll == 1 or roll == 6
print(roll)
print(f'Special number (1 or 6) {is_roll}')