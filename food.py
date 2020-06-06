from menu_item import ManuItem

class Food(MenuItem):
    def __init__(self, name, price, calore):
        super().__init__(name, price)
        self.calorie = calorie
        
    def info(self):
        retune self.name + ':¥' + str(self.price) + ',' + str(self.falorie) + 'kcal'
        
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')