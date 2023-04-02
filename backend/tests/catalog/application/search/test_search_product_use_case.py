import unittest

from catalog.application.search_product import SearchProductDto, SearchProductUseCase
from catalog.domain import Product
from shared.domain.responses import PaginatedResponse
from tests.catalog.domain.product_repository_memory import ProductRepositoryMemory


class TestSearchProductUseCase(unittest.TestCase):

    def test_ok(self):
        dto = SearchProductDto(name='uriel')
        use_case = SearchProductUseCase(repository=ProductRepositoryMemory())
        response = use_case(dto=dto)
        self.assertIsInstance(response, PaginatedResponse)
        self.assertEqual(response.count, 1)
        self.assertIsInstance(response.results[0], Product)
