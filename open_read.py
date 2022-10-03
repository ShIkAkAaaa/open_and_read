# первая задача
from pprint import pprint

cook_book = {}

with open('dz.txt', encoding='utf-8') as file:
    for string in file:
        name = string.strip()
        quantity = int(file.readline().strip())
        food = []
        for ingredients in range(quantity):
            ingr_dict = {}
            ingr = file.readline().split('|')
            ingr_dict['ingredient_name'] = ingr[0].strip()
            ingr_dict['quantity'] = ingr[1].strip()
            ingr_dict['measure'] = ingr[2].strip()
            food.append(ingr_dict)
        file.readline()
        cook_book[name] = food
pprint(cook_book)

# вторая задача
def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in cooking_list:
                    value = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                    cooking_list[ingr['ingredient_name']] = value
                else:
                        cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return cooking_list
# проверка
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))