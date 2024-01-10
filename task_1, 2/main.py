from pprint import pprint
from cook_book import create_cook_book
from cook_book import get_shop_list_by_dishes


def main():
	filename = 'recipes.txt'
	cook_book = create_cook_book(filename)
	dishes = ['Запеченный картофель', 'Омлет']
	person_count = 3
	shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
	pprint(cook_book)
	pprint(shop_list)


if __name__ == '__main__':
	main()
