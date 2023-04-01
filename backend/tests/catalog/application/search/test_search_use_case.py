import unittest

from catalog.application.search import SearchDto, SearchUseCase
from catalog.domain import Product
from shared.domain.responses import PaginatedResponse
from tests.catalog.domain.product_repository_memory import ProductRepositoryMemory


class TestSearchUseCase(unittest.TestCase):

    def test_ok(self):
        dto = SearchDto(name='uriel')
        use_case = SearchUseCase(repository=ProductRepositoryMemory())
        response = use_case(dto=dto)
        self.assertIsInstance(response, PaginatedResponse)
        self.assertEqual(response.count, 1)
        self.assertIsInstance(response.results[0], Product)
