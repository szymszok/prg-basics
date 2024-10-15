age = int(input('Enter your age '))
group = ''
if age < 13:
    group = 'Child'
elif age in range(13,20):
    group = 'Teen'
elif age in range(20,65):
    group = 'Adult'
elif age >= 65:
    group = 'Senior'

print(f'Your group is {group}')