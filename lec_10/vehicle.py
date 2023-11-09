class my_vehicle:
    def __init__(self, model, max_speed = 150, num_seats = 4):
        self.max_speed = max_speed
        self.num_seats = num_seats
        self.model = model
    def Information(self):
        print('Information about the car')
        print('Model is: ',self.model)
        print('Max_speed is: ',self.max_speed)
        print('Number_of_seats: ',self.num_seats)