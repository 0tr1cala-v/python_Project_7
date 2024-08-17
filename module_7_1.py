from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_1 = file.read()
        file.close()
        return list_1

    def add(self, *products):
        for i in products:
            product_ = (str(i))
            file = open(self.__file_name, 'r')
            list_2 = file.read()
            file.close()
            if product_ in list_2:
                print(f'Продукт {product_} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{product_}')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())