from catalog.domain import ProductRepository, Product


class ProductRepositoryMemory(ProductRepository):
    def search(self) -> list[Product]:
        return [
            Product(name='test_name', description='test_description'),
        ]