import random

for i in range(1,8):
    for j in range(1,7):
        j = random.randint(1,49)
        print(j, end=' ')
    i = random.randint(1,49)
    print(i)