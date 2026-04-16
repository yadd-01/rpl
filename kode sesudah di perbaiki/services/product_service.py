from models.inventory import Inventory
from models.product import Product

class ProductService:
    def __init__(self):
        self.inventory = Inventory()

    def create_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.inventory.add_product(product)

    def list_products(self):
        return self.inventory.get_all_products()

    def search_product(self, name):
        return self.inventory.find_product(name)

    def update_product(self, name, price, stock):
        product = self.inventory.find_product(name)
        if product:
            product.update(price, stock)
            return True
        return False

    def delete_product(self, name):
        return self.inventory.delete_product(name)