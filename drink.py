from menu_item import ManuItem

class Drink(MenuItem):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount
        
    def info(self):
        retune self.name + ':¥' + str(self.price) + ',' + str(self.amount) + 'ml'
