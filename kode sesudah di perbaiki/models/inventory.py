from models.product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_all_products(self):
        return self.products

    def find_product(self, name: str):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def delete_product(self, name: str):
        product = self.find_product(name)
        if product:
            self.products.remove(product)
            return True
        return False