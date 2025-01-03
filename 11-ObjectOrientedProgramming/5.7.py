from staticticclass import stat


arr = [12,37,6,9]
last_num = int(input('Podaj liczbę aby dodać ją do tablicy: '))
arr.append(last_num)
stats = stat(arr)
print(stats.display())
