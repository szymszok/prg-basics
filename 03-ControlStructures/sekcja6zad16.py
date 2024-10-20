# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
spin_time = 0
rinse_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if program == 'j':
    washing_product = 'jacket'
    time = 40
elif program == 'u':
    washing_product = 'underwear'
    time = 70
elif program == 's':
    washing_product = 'shoes'
    time = 20
else:
    print('Wrong program')

if extra_rinse == 'y':
    rinse = True
    rinse_time = 15
else:
    rinse = False
if extra_spin == 'y':
    spin = True
    spin_time = 9
else:
    spin = False

total_washing_time = time + spin_time + rinse_time

print(f'Washing product: {washing_product}')
print(f'Rinse: {rinse}')
print(f'Extra spin: {spin}')
print(f'Total washing time: {total_washing_time}')