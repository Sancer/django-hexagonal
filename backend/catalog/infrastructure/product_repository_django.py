from catalog.domain import Product, ProductDescription, ProductName, ProductId, ProductRepository
from catalog.infrastructure.models import Product as ProductModel


class ProductRepositoryDjango(ProductRepository):
    def search(self) -> Product:
        products = ProductModel.objects.all()
        return [self.to_domain(product) for product in products]

    @staticmethod
    def to_domain(product: ProductModel) -> Product:
        return Product(
            id=ProductId(str(product.id)),
            name=ProductName(product.name),
            description=ProductDescription(product.description),
        )
