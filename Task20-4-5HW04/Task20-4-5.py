import json
from datetime import datetime
with open("Task20-4-5HW04/orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
max_price = 0
max_order = ''
max_quantity = 0
orders_by_day = {} #выделяем отдельный словарь под определение даты
max_orders_per_day = 0  #для выяснения максимального ко-ва заказов
day_with_max_orders = '' #выделяем отдельную переменную для фиксации даты
order_to_user = {} #выделяем отдельный словарь под пользователя
max_order_user = '' #выделяем отдельную переменную для пользователя
max_order_per_user = 0 #переменная для сравнения кол-во заказов пользователями
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    #получаем кол-во товаров в заказе
    quantity = orders_data['quantity']
    #преобразуем и получаем дату
    date = orders_data['date']
    date_obj = datetime.strptime(date, "%Y-%d-%m")
    date = date_obj.strftime("%d-%m-%Y")
    #получаем пользователя
    user = orders_data['user_id']
    #получаем цену
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
    # если кол-во товаров больше максимального - запоминаем номер заказа и кол-во товаров
    if quantity > max_quantity:
        max_quantity_order = order_num
        max_quantity = quantity
    if date in orders_by_day:
        orders_by_day[date] += 1
    else:
        orders_by_day[date] = 1
    if user in order_to_user:
        order_to_user[user]+= 1
    else:
        order_to_user[user] = 1
#запускаем цикл для словаря orders_by_day 
for date, count  in orders_by_day.items():
    if count  > max_orders_per_day:
        max_orders_per_day = count 
        day_with_max_orders = date
#запускаем цикл для словаря оrder_to_user
for user, count in order_to_user.items():
    if count  > max_order_per_user:
            max_order_per_user = count 
            max_order_user = user
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
print(f'Номер заказа с самым большим количеством товаров: {max_quantity_order}, количество товаров: {max_quantity}')
print(f'{day_with_max_orders} было сделано наибольшее количество заказов: {max_orders_per_day}')
print(f'Пользователь {max_order_user} сделал наибольшее количество заказов в июле: {max_order_per_user}')
#переиспользуем переменные и словарь
order_to_user = {}
max_order_user = '' 
max_order_per_user = 0  
total_price_july = 0 
july_order_count = 0
total_quantity_july = 0
for order_num, orders_data in orders.items():
    date = orders_data['date']
    date_obj = datetime.strptime(date, "%Y-%d-%m")
    date = date_obj.strftime("%d-%m-%Y")
    if date.endswith('07-2023'):
        user = orders_data['user_id']
        price = orders_data['price']
        total_price_july += price
        july_order_count += 1
        total_quantity_july += quantity
        if user in order_to_user:
            order_to_user[user] += price
        else:
            order_to_user[user] = price
for user, total_price in order_to_user.items():
    if total_price > max_order_per_user:
        max_order_per_user = total_price
        max_order_user = user
print(f'Пользователь {max_order_user} потратил наибольшую сумму за июль: {max_order_per_user}')
#выводим среднюю сумму заказа за июль + добавляем штрих, если по какой-то причине данных нет
if july_order_count > 0:
    average_order_price = total_price_july / july_order_count
    print(f'Средняя стоимость заказа в июле: {average_order_price}')
else:
    print('Заказы за июль не найдены.')
#выводим среднюю стоимость товара за июль + добавляем штрих, если по какой-то причине данных нет
if total_quantity_july > 0:
    avg_price_per_item = total_price_july / total_quantity_july
    print(f'Средняя стоимость одного товара в июле: {avg_price_per_item}')
else:
    print('Нет данных о количестве товаров за июль.')