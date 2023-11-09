from vehicle import my_vehicle as Vehicle

class Car(Vehicle):
    def __init__(self, model, year, color):
        super().__init__(model)
        self.year = year
        self.color = color
    def information(self):
        super().Information()
        print('Year is: ',self.year)
        print('Color is: ',self.color)
        
class Plane(Vehicle):
    def __init__(self, model, color):
        super().__init__( model)

class Boat(Vehicle):
    def __init__(self, model, year):
        super().__init__( model)

class RaceCar(Car):
    def __init__(self, color, model, year):
        super().__init__(color, model, year)

car = Car('BMV', 2005, 'black')
car.information()
