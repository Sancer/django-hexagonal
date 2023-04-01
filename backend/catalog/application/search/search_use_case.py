from shared.domain.responses import PaginatedResponse
from .search_dto import SearchDto


class SearchUseCase:

    def __call__(self, dto: SearchDto) -> PaginatedResponse[int]:
        return PaginatedResponse(count=1, results=[1])