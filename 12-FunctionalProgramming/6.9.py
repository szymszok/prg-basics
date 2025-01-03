temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive = list(filter(lambda town: temperatures[town] > 0, temperatures))
for i in positive:
    print(i, end=' ')
