###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('Podaj wartosć a: ')
b = input('Podaj wartosć b: ')
c = input('Podaj wartosć c: ')
volume = int(a) * int(b) * int(c)
surface_area = 2 * (int(a) * int(c)) + 2 * (int(b) * int(c)) + 2 * (int(a) * int(b))


print(volume)
print(surface_area)
