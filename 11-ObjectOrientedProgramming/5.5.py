from termometrclass import thermometr
import random

temperatura = thermometr()

while True:
    number = int(input('Decide what to do: 0-exit, 1-measure and display, 3-turn on,4-turn off: ')) 

    if number == 0:
        print("Exiting the program.")
        break
    elif number == 1:
        temperatura.work()
    elif number == 2:
        ebook.reading()    
    elif number == 3:
        print('Turning on ...')
        temperatura.turn_on()
    elif number == 4:
        print('Turning off ...')
        temperatura.turn_off()
