from typing import Optional, Type, TypeVar

from shared.domain.criteria.order_by import OrderBy
from shared.domain.criteria.order_type import OrderType, OrderTypes


class Order:
    def __init__(self, order_by: OrderBy, order_type: OrderType):
        self.order_by = order_by
        self.order_type = order_type

    @classmethod
    def from_values(cls, order_by: Optional[str] = None, order_type: Optional[str] = None) -> Order:
        if not order_by:
            return cls.none()
        return cls(OrderBy(order_by), OrderType.from_value(order_type or OrderTypes.ASC.value))

    @classmethod
    def none(cls) -> Order:
        return cls(OrderBy(''), OrderType(OrderTypes.NONE))

    @classmethod
    def desc(cls, order_by: str) -> Order:
        return cls(OrderBy(order_by), OrderType(OrderTypes.DESC))

    @classmethod
    def asc(cls, order_by: str) -> Order:
        return cls(OrderBy(order_by), OrderType(OrderTypes.ASC))

    def has_order(self) -> bool:
        return not self.order_type.is_none()
