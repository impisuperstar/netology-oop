from pprint import pprint

FILE = 'recipes.txt'


def make_dict(file):
    txt = open(file, 'r')
    resipes = (x.split('\n') for x in txt.read().split('\n\n'))
    cook_book = {'cook_book': {x[0]: [dict(zip(('ingredient_name', 'quantity', 'measure'),
                 x[i].split(' | '))) for i in range(2, 2 + int(x[1]))] for x in resipes}}
    return (cook_book)


print(make_dict(FILE))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {x['ingredient_name']: {'measure': x['measure'], 'quanity': int(x['quantity']) * person_count}
                 for x in make_dict(FILE).get('cook_book').get(dishes)}

    return (cook_book)


pprint(get_shop_list_by_dishes('Запеченный картофель', 3))
