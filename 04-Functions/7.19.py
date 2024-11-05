def summary(number):
    full_sum = 0
    digit = 0
    for char in number:
      if number.count(char)  > 1:
        full_sum += int(number)

    return full_sum
        


print(summary('230335'))#nie dziala 