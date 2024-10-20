science = input('Are you interested in computer science? (y/n): ')
computer = input('Are you interested in computer games? (y/n): ')
instagram = input('Do you have ? (y/n): ')

if science == 'y':
    is_science = 'Yes'
else:
    is_science = 'No'
if computer == 'y':
    is_computer = 'Yes'
else:
    is_computer = 'No'
if instagram == 'y':
    is_instagram = 'Yes'
else:
    is_instagram = 'No'

print(f'Interested in computer science: {is_science}')
print(f'Playing computer games: {is_computer}')
print(f'Has an Instagram account: {is_instagram}')