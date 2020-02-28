# б) Задача. Визначити загальну вартість всіх товарів, випущених в поточному році і
# вивести інформацію про ці товари. Поля структури: Найменування, Виробник, Рік
# випуску, Кількість, Ціна.
while True:
    goods = [{'name': 'telescope', 'maker': 'Sky-Watcher', 'year': 2020, 'number': 1534, 'price': 1000},
             {'name': 'smartphone', 'maker': 'Apple', 'year': 2019, 'number': 1324, 'price': 2000},
             {'name': 'car', 'maker': 'Tesla', 'year': 2018, 'number': 763, 'price': 300000},
             {'name': 'rocket', 'maker': 'SpaceX', 'year': 2020, 'number': 23, 'price': 1000000}]
    num, value, elements = 1, 0, []

    for items in range(len(goods)):
        year = goods[items].get('year')
        if year == 2020:
            value += goods[items].get('number') * goods[items].get('price')
            elements.append(items)
    else:
        print(f'Загальна вартість товарів: {value} USD\n')

    for info in elements:
        while num:
            print(f'{num}. Назва: {goods[info].get("name")}\n   Виробник: {goods[info].get("maker")}\n'
                  f'   Рік: {goods[info].get("year")}\n   Кількість: {goods[info].get("number")} шт.'
                  f'\n   Ціна: ${goods[info].get("price")}\n')
            num += 1
            break

    if not input('One more? (YES - Enter, NO - something)'):
        continue
    break
