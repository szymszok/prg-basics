#Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))
def triangle_area(a,b,c):
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print(f'The area of ​​a triangle with sides {a, b, c} is {triangle_area(a, b, c)}')
