import math
height = input('Podaj wysokość horyzontu w metrach: ')
pierwiastek = math.sqrt(int(height))
distance = 3.57 * pierwiastek
print('Wysokość horyzontu: ', distance)
