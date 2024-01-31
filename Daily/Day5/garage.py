

#garage class that stores several cars
class Garage():
    def __init__(self, cars=[]):
        self.cars = cars
    def add_car(self, car_to_add):
        self.cars.append(car_to_add)


#car class
#cars should keep track of color, make, model, year, owner
class Car():
        def __init__(self, input_color, input_make, input_model, input_year, input_owner):
            self.color = input_color
            self.make = input_make
            self.model = input_model
            self.year = input_year
            self.owner = input_owner

#person class
#name, DL#

claire = Car("silver", "subaru", "forrester", 2010, None)
corys_garage = Garage()

print(corys_garage.cars)

corys_garage.add_car(claire)

print(corys_garage.cars)[0]
