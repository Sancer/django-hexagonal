from django.test import TestCase
from django.urls import reverse

from catalog.infrastructure.models import Product as ProductModel


class IntegrationSearchProductView(TestCase):
    url = '/catalog/product/'

    def setUp(self) -> None:
        self.product = ProductModel(name='Zink')
        self.product.save()

    def tearDown(self) -> None:
        self.product.delete()

    def test_url_contract(self):
        self.assertEqual(self.url, reverse("catalog:search"))

    def test_ok(self):
        response = self.client.get('/catalog/product/')
        data = response.json()

        self.assertEqual(data["count"], 1)
        self.assertEqual(len(data["results"]), 1)
        self.assertIn('id', data['results'][0])
        self.assertIsInstance(data['results'][0]['id'], str)
        self.assertIn('name', data['results'][0])
        self.assertIsInstance(data['results'][0]['name'], str)
        self.assertIn('description', data['results'][0])
        self.assertIsInstance(data['results'][0]['description'], str)

