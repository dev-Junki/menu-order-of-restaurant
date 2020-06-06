from food import Food
from drink import Drink


food1 = Food('サンドイッチ',500,330)
food2 = Food('チョコケーキ',400,450)
food3 = Food('シュークリーム',200,180)

foods = [food1, food2, food3]


drink1 = Drink('コーヒー',300,180)
drink2 = Drink('オレンジジュース',200,350)
drink3 = Drink('エスプレッソ',300,30)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
   print(str(index) + '.' + food.info())
   index += 1
   
   
print('飲み物メニュー')
index = 0
for drink in drinks:
   print(str(index) + '.' + fdrink.info())
   index += 1

print('--------------------')

food_order = 0

#注文する食べ物メニューを変数selected_foodに代入してください。
selected_food = foods[food_order]

drink_order = 0

#注文する飲み物メニューを変数selected_drinkに代入してください。
selected_drink = drinks[drink_order]

#「○○と□□を注文します」となるように出力してください。
print(selected_food.name + 'と' + selected_drink.name + 'を注文します')

count = 3

#「○○セット購入します」となるように出力してください。
print(str(count) + 'セット購入します')

# selected_foodとselected_drinkのそれぞれに対して、get_toral_priceメソッドを呼び出してください。
print('合計は' +str(result) + '円です')




