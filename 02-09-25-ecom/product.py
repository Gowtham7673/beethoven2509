# id, name, description, category, tags, stock, price
class Product:
    def __init__(self, id, name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.cateogry = category
        self.tags = tags
        self.stock = stock
        self.price = price

    def __str__(self):
        return f'[id = {self.id},name = {self.name},description ={self.description},category = {self.cateogry},tags = {self.tags},stock = {self.stock},price = {self.price}]'
    def __repr__(self):
        return self.__str__()
mobile_vivo = Product(1001, 'iq z9s', 'Good camera quality', 'mobile', 'elctronic device', 10, 20000)
print(mobile_vivo)