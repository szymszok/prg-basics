###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Szymon' 
surname = 'Marszałek' 
characters_in_name = len(name)
ilosc_nazwisko = len(surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {ilosc_nazwisko} characters')
print(f'Your full name has {characters_in_name + ilosc_nazwisko} characters') 