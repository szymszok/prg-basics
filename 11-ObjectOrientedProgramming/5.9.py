from employeclass import C


name = input('Podaj imie: ')
surname = input('Podaj naziwsko: ')
age = int(input('Podaj wiek: '))
seniority = int(input('Podaj ilosc przepracowanych lat: '))
employ = C(name,surname,age,seniority)

print(employ.display())