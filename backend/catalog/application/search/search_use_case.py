from dataclasses import dataclass

from shared.domain.responses import PaginatedResponse
from .search_dto import SearchDto
from catalog.domain import Product, ProductRepository


@dataclass
class SearchUseCase:
    repository: ProductRepository

    def __call__(self, dto: SearchDto) -> PaginatedResponse[Product]:
        products = self.repository.search()
        return PaginatedResponse(count=1, results=products)