class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(self.distance)
        print(self.fare)
        print(self.rate_per_km)
    def __str__(self):
        return f"{self.distance} {self.fare} {self.rate_per_km}"
taxi1 = TaxiRide(10)
taxi2 = TaxiRide(30)
def main():
 print(f'{taxi1.print_receipt}')
 print(f'{taxi2.print_receipt}')   
if __name__ == "__main__":
    main()
