distance = int(input('Enter distance in km: '))
travel_hours = int(input('Enter number of travel hours: '))
travel_minutes = int(input('Enter number of travel minutes: '))

avg_speed = lambda distance,hours,minutes: distance/(minutes/60 + hours)

result = avg_speed(distance,travel_hours,travel_minutes)

print(f'Average speed: {round(result,2)} km/h')