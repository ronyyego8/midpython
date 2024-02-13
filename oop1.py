class Fruits:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):

        print(f"My favorite fruit is {self.name} and the color is " f"{self.color}")


myobj = Fruits("Banana", "yellow")
myobj.display()
