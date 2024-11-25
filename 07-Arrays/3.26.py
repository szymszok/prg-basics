import math
import matplotlib.pyplot as plt

x = []
y = []

for i in range(0,361):
    x.append(i)

for i in x:
    y.append(math.sin(math.radians(i)))

plt.plot(x,y)
plt.grid()
plt.show()