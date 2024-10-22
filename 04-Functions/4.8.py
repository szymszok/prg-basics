
def time_string(hours, minutes, time_format):
    if time_format == '12' and hours > 12:
        full_time = f'{hours - 12}:{minutes}pm'
    elif time_format == '12' and hours < 12:
        full_time = f'{hours}:{minutes}am'
    else:
        full_time = hour + ':' + minutes
        



    return full_time

min = int(input('Enter minutes: '))
hour = int(input('Enter hours: '))
format = input('Enter time format(12 or 24): ')

print(f'Your time is: {time_string(hour, min, format)}')