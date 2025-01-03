import statistics
class stat:
    def __init__(self,numbers):
        self.numbers = numbers

    def display_num(self):
        return ', '.join(map(str, self.numbers))  #<------ ważne do wypisywania wszystkiego z przecinkiem po kolei
    
    def maxx(self):
        return max(self.numbers)
    
    def minn(self):
        return min(self.numbers)

    def mean(self):
        return statistics.mean(self.numbers)
    
    def median(self):
        return statistics.median(self.numbers)

    def display(self):
        print(self.display_num())
        print(self.maxx())
        print(self.minn())
        print(self.mean())
        print(self.median())

        
