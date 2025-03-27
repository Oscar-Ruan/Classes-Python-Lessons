#notes

""" class Merchant:
    def __init__(self, name, products): #defines the look of the Merchant
        self.name= name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Rachel = Merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = Merchant("Kammy", ["Penguins", "Whales", "Capybaras"])
print(Rachel.sell("Human"))
print(Kammy.sell("Capybaras")) """


import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}

#the code above created defines the class, creating how the class is structured and how it is modeled/blueprinted

my_car = Car("Toyota", "Camry", 2023, "camry_image.jpg")
print(my_car.display_info())

new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

cars_data.append(new_car.to_dict())

with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)

