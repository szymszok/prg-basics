speed = int(input('Podaj prędkość(m/s): '))

ms_to_kmh = lambda x: x * 3.6

result = ms_to_kmh(speed)

print(f'Speed is: {result} km/h')