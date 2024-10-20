number = input('Enter EAN-13 article number: ')
number_is = ''
if len(number) == 13:
    print('Article number is correct')
    number_is = True
else:
    print('Article number is incorrect')
    number_is = False

if number_is == True and number[:3] == '590':
    print('Article manufactured in Poland ')
