# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    result = 0
    for row in seats:
        for item in row:
            result += 1
    return result

def seats_available(seats):
    result = 0
    for row in seats:
        for item in row:
            if item == 'A':
                result += 1
    return result

def seats_booked(seats):
    result = 0
    for row in seats:
        for item in row:
            if item == 'B':
                result += 1
    return result

def seat_status(seats, row, place):
    if seats[row][place] == 'A':
        return 'Notbooked'
    else:
        return 'Booked'
        
    

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:',  seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 0, 0))
print('Seat in row 5, place 5:',  seat_status(cinema_seats, 4, 4))
print('Seat in row 3, place 5:',  seat_status(cinema_seats, 2, 4))