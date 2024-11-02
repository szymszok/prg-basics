def door(detector):
    is_in = 0
    max_in = 0
    for char in detector:
        if char == '+':
            is_in +=1
        elif char == '-':
            is_in -= 1
        if is_in > max_in:
            max_in = is_in
    if max_in >= 3:
        true_false = True
    else:
        true_false = False
    return true_false

detection = input('Enter detectors parameters: ')
print(door(detection))