from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.views import APIView

from catalog.application.search_product import SearchProductDto, SearchProductUseCase
from catalog.infrastructure.product_repository_django import ProductRepositoryDjango
from shared.infrastructure import JSONEncoder


class SearchProductView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        dto = SearchProductDto(name='Zink')
        use_case = SearchProductUseCase(repository=ProductRepositoryDjango())
        response = use_case(dto=dto)

        return JsonResponse(data=response.dict(), encoder=JSONEncoder)
