from dataclasses import dataclass
from typing import TypeVar, Generic

from shared.domain.value_objects import Integer

T = TypeVar("T")


@dataclass
class PaginatedResponse(Generic[T]):
    count: Integer
    results: list[T]

    def dict(self):
        return {
            'count': self.count,
            'results': [item.dict() for item in self.results]
        }