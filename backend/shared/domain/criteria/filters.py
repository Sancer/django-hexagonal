from typing import List, Dict, TypeVar

from shared.domain.criteria.filter import Filter

T = TypeVar('T', bound='Filters')


class Filters:
    filters: List[Filter]

    def __init__(self, filters: List[Filter]):
        self.filters = filters

    @staticmethod
    def from_values(filters: List[Dict[str, str]]) -> T:
        return Filters([Filter.from_values(filter) for filter in filters])

    @staticmethod
    def none() -> T:
        return Filters([])