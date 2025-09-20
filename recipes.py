from pprint import pprint

FILE = 'recipes.txt'


def make_dict(file):
    txt = open(file, 'r')
    resipes = (x.split('\n') for x in txt.read().split('\n\n'))
    cook_book = {x[0]: [dict(zip(('ingredient_name', 'quantity', 'measure'),
                 x[i].split(' | '))) for i in range(2, 2 + int(x[1]))] for x in resipes}
    return (cook_book)


print(make_dict(FILE))


def get_shop_list_by_dishes(dishes_list, person_count):

    shop_list = {}

    cook_book = make_dict(FILE)

    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient]['quantity'] += int(
                        ingredient['quantity']) * 3
                else:
                    name = ingredient['ingredient_name']
                    shop_list[name] = {'measure': ingredient['measure'],
                                       'quantity': ingredient['quantity']}

    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
