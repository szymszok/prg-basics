cena = float(input('Podaj cenę: '))
rabat = float(input('Podaj rabat w %: '))
po_rabat =  (cena / 100) * rabat
cena_po = cena - float(po_rabat)
ulga = cena - float(cena_po)

print(cena)
print(rabat)
print('Cena po rabacie: '"{:.2f}".format(cena_po))
print('Ulga: '"{:.2f}" .format(ulga))