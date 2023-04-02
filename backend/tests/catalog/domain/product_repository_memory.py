from catalog.domain import ProductRepository, Product, ProductName, ProductDescription
from shared.domain.value_objects import Uuid


class ProductRepositoryMemory(ProductRepository):
    def search(self) -> list[Product]:
        return [
            Product(id=Uuid.create(), name=ProductName('test_name'), description=ProductDescription('test_description')),
        ]