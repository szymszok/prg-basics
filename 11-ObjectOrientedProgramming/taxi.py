class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        
    
    def print_receipt(self):
        return (f'Distance: {self.distance}, Rate: {self.rate_per_km}, Fare: {self.fare}')


def main():
    # your program
    ride1 = TaxiRide(3)
    ride2 = TaxiRide(3)

    ride1.calculate_fare(20)
    ride2.calculate_fare(10)
    

    print(ride1.print_receipt())
    print(ride2.print_receipt())

    

if __name__ == "__main__":
    main()
