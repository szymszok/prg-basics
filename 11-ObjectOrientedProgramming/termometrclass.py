import random
class thermometr:
    def __init__(self):
        self.temp = None
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def work(self):
        print('Measurizg body temperature. Please wait.')
        self.temp = round(random.uniform(34.0,42.0), 1)
        if self.temp >= 37:
            print(f'Temperature: {self.temp} (fever)')
        elif self.temp >= 41:
            print(f'Temperature: {self.temp} (CRITICAL TEMPERATURE!!!)')
        else:
            print(f'Temperature: {self.temp}')