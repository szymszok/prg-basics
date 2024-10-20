car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed >= 40 and car_speed <= 140:
    print('Correct car speed')
else:
    print('Car speed is too low or too high')
