"""Задание 3:	Реализуйте класс Shop. Предусмотреть возможность работы с
                произвольным числом продуктов, поиска продуктов по названию,
                добавления их в магазин и удаления продуктов из него."""
class Shop:
    def __init__(self):
        self.products = []


    def add_product(self, product: dict):
        self.products.append(product)


    def delete_prod(self, product):
        self.products.remove(product)

    def show_products(self):
        print(self.products)


shop_1 = Shop()

product1 = {"Название продукта": "Молоко", "Количество продукта": 50, "Цена": 4}
product2 = {"Название продукта": "Кефир", "Количество продукта": 50, "Цена": 3}
product3 = {"Название продукта": "Хлеб", "Количество продукта": 20, "Цена": 2}

shop_1.add_product(product1)
shop_1.add_product(product2)
shop_1.add_product(product3)


shop_1.delete_prod(product1)
shop_1.delete_prod(product2)
shop_1.show_products()
