from vehicle import my_vehicle

class Car(my_vehicle):
    def __init__(self, model, year, color):
        super().__init__(model)
        self.year = year
        self.color = color
    def information(self):
        super().Information()
        print('Year is: ',self.year)
        print('Color is: ',self.color)


car = Car('BMV', 2005, 'black')
car.information()
