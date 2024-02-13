class Cars:

    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def show(self):

        print(
            f"My dream car is {self.make} and model is a"
            f" {self.model} of color {self.color} manufactured in {self.year}"
        )


myobj = Cars("Nissan", "GT-R", "red", "2020")
myobj.show()
