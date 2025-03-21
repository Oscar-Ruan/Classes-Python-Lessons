#notes

class Merchant:
    def __init__(self, name, products): #defines the look of the Merchant
        self.name= name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Rachel = Merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = Merchant("Kammy", ["Penguins", "Whales", "Capybaras"])
print(Rachel.sell("Human"))
print(Kammy.sell("Capybaras"))