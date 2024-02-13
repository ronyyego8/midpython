class Gari:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_gari(self):
        return f"{self.make} {self.model} {self.year}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on the odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Gari("Ford", "Ranger", 2023)
print(my_car.describe_gari())
print(my_car.read_odometer())
my_car.update_odometer(100)
print(my_car.read_odometer())
my_car.increment_odometer(50)
print(my_car.read_odometer())
