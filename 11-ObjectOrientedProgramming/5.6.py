from bankclass import bank

konto = bank(input('Podaj numer konta aby stworzyć: '))
while True:
    number = int(input('1- sprawdz balans, 2- dodaj środki, 3 odejmij środki: '))

    if number == 1:
        konto.display()

    elif number == 2:
        add_money = float(input('Podaj ilośc środków do wpłacenia: '))
        konto.deposit(add_money)
    elif number == 3:
        take_money = float(input('Podaj ilosc srodkow do wypłaty'))
        konto.withdraw(take_money)
  
  