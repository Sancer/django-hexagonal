from dataclasses import dataclass

from shared.domain.value_objects import String


@dataclass
class SearchProductDto:
    filters: dict = None
    order_by: str = 'name'
    order_type: str = 'asc'
    offset: int = 0
    limit: int  = 25

