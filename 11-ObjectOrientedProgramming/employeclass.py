class C:
    def __init__(self,name,surname,age,senior):
        self.name = name
        self.surname = surname
        self.age = age
        self.senior = senior

    def display(self):
        if self.age >= 18:
            ready = f'{self.surname}{self.name[0]}{self.senior}'
            return ready.upper()
        else:
            ready = f'{self.surname}{self.name[0]}{self.senior}'
            return ready.lower()
            
    
