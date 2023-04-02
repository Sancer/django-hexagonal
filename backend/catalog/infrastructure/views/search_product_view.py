from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.views import APIView

from catalog.application.search import SearchDto, SearchUseCase
from catalog.infrastructure import ProductRepositoryDjango
from shared.infrastructure import JSONEncoder


class SearchProductView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        dto = SearchDto(name='Zink')
        use_case = SearchUseCase(repository=ProductRepositoryDjango())
        response = use_case(dto=dto)

        return JsonResponse(data=response.dict(), encoder=JSONEncoder)
