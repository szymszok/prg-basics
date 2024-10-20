x = int(input('Enter x: '))
y = int(input('Enter y: '))
quadrant = ''
if x > 0 and y > 0:
    quadrant = 'first quadrant'
elif x > 0 and y < 0:
    quadrant = 'second quadrant'
elif x < 0 and y < 0:
    quadrant = 'third quadrant'
elif x < 0 and y > 0:
    quadrant = 'fourth quadrant'
else:
    quadrant = 'position (0;0)'

print(f'Point P({x},{y}) is in {quadrant} of the coordinate system')