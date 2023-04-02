from dataclasses import dataclass

from shared.domain.responses import PaginatedResponse
from .search_product_dto import SearchProductDto
from catalog.domain import Product, ProductRepository


@dataclass
class SearchProductUseCase:
    repository: ProductRepository

    def __call__(self, dto: SearchProductDto) -> PaginatedResponse[Product]:
        products = self.repository.search()
        return PaginatedResponse(count=1, results=products)
