from catalog.domain import Product
from catalog.domain.product_repository import ProductRepository

from catalog.infrastructure.models import Product as ProductModel

class ProductRepositoryDjango(ProductRepository):
    def search(self) -> Product:
        products = ProductModel.objects.all()
        return [self.to_domain(product) for product in products]

    @staticmethod
    def to_domain(product: ProductModel) -> Product:
        return Product(
            name=product.name,
            description=product.description,
        )