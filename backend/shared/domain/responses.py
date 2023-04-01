from dataclasses import dataclass
from typing import TypeVar, Generic

from shared.domain.value_objects import Integer

T = TypeVar("T")


@dataclass
class PaginatedResponse(Generic[T]):
    count: Integer
    results: list[T]
