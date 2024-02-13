

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
            self.owner = input_owner
            self.make = input_make
            self.model = input_model
            self.color = input_color
            self.year = input_year

cars_list = []
owner_garage = Garage(cars_list)

#appends car details to list then inputs them into garage
def add_new_car():
    car_owner = input("What is your name: ")
    car_make = input("Car's make: ")
    car_model = input("Car's model: ")
    car_color = input("Car's color: ")
    car_year = input("Car's year: ")
    new_car = Car(car_color, car_make, car_model, car_year, car_owner)
    cars_list.append(new_car)
    print(f"{car_owner}'s car added to the list.")
    owner_garage = Garage(cars_list)

#show all cars in garage
def show():
    print("Cars in the garage:")
    for car in owner_garage.cars:
        print(f"{car.owner}'s {car.color} {car.make} {car.model} ({car.year})")

#actions for user
def doaction(action):
    if action == "add":
        add_new_car()
    if action == "show":
        show()
    if action == "help":
        print("'add': add cars")
        print("'show': show cars")
        print("'quit': exit program")

car_owner = ''
#input for user
while car_owner != 'quit':
    action = input("What would you like to do ('help' for assistance): ")
    doaction(action)
