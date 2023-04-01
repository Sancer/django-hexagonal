import unittest

from catalog.application.search import SearchDto, SearchUseCase


class TestSearchUseCase(unittest.TestCase):

    def test_ok(self):
        dto = SearchDto(name='uriel')
        use_case = SearchUseCase()
        response = use_case(dto=dto)
        self.assertEqual(response.count, 1)
