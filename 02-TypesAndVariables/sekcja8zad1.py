# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# display results

radius = int(input('Enter radius: '))
pi = float(3.14)
area = pi * radius ** 2
circumference = (2 * pi) * radius

print(f'Area: {area}, Circumference: {circumference}')