def create_cook_book(file_name):
	cook_book = {}

	with open(file_name, 'r', encoding='utf-8') as file:
		while True:
			dish = file.readline().strip()
			if not dish:
				break

			quantity = int(file.readline().strip())
			ingredients = []

			for i in range(quantity):
				ingredient = file.readline().strip().split('|')
				ingredients.append(
					{'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
			cook_book[dish] = ingredients
			file.readline()

	return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
	shop_list = {}
	for dish in dishes:
		if dish in cook_book:
			for ingredient in cook_book[dish]:
				ingredient_name = ingredient['ingredient_name']
				ingredient['quantity'] *= person_count
				ingredient.pop('ingredient_name')
				if ingredient_name not in shop_list:
					shop_list[ingredient_name] = ingredient
				else:
					shop_list[ingredient_name]['quantity'] += ingredient['quantity']
	return shop_list
