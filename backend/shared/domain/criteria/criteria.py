from typing import Optional
from backend.shared.domain.criteria.filters import Filters
from backend.shared.domain.criteria.order import Order

class Criteria:
    def __init__(self, filters: Filters, order=Order, offset: Optional[int] = None, limit: Optional[int] = None):
        self.filters = filters
        self.order = order
        self.offset = offset
        self.limit = limit

    def has_filters(self) -> bool:
        return not self.filters.is_empty()
    
