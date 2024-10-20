time_24 = input('Enter time (24-hour format): ')
time_12 = int(time_24[:2]) - 12

print(f'Time in 12-hour format: {time_12}:{time_24[-2:]}pm')