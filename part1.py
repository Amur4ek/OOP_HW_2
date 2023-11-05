import pprint

cook_book = {}
with open("Text1.txt", "r", encoding="utf-8") as f:
    data = f.read()
    sp_list = data.split("\n\n")
    for i in sp_list:
        sp_dish = i.split("\n")
        for i in range(2, len(sp_dish)):
            value_out = sp_dish[i].split(" | ")
            value = {}
            value['ingredient_name'] = [value_out[0]]
            value['quantity'] = [value_out[1]]
            value['measure'] = [value_out[2]]
            if sp_dish[0] in cook_book:
                cook_book[sp_dish[0]].append(value)
            else:
                cook_book[sp_dish[0]] = [value]


pprint.pprint(cook_book)


#Second excersixe

# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#
#     for dish in dishes:
#         if dish in cook_book:
#             ingredients = cook_book[dish]
#             for ingredient in ingredients:
#                 name = ingredient["ingredient_name"][0]  # Получить первый элемент списка
#                 quantity = int(ingredient["quantity"][0]) * person_count  # Преобразовать строку в целое число
#                 measure = ingredient["measure"][0]
#                 if name in shop_list:
#                     shop_list[name]["quantity"] += quantity
#                 else:
#                     shop_list[name] = {"quantity": quantity, "measure": measure}
#
#     return shop_list
# result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 22)
# pprint.pprint(result)

