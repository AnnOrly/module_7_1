from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    _file_name = 'product.txt'

    def get_products(self):
        file = open(self._file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products): 
        for product in products:
            if product.name not in self.get_products():
                file = open(self._file_name, 'a')
                file.write((product.__str__()+'\n'))
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Rice', 2.0, 'Groceries')
p3 = Product('Apple', 3.3, 'Fruits')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())