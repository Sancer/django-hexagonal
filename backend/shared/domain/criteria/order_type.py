from shared.domain.value_objects import EnumValueObject
from enum import Enum


class OrderTypes(Enum):
    ASC = 'asc'
    DESC = 'desc'
    NONE = 'none'


class OrderType(EnumValueObject):

    def __init__(self, value: OrderTypes):
        super().__init__(value, list(OrderTypes))

    def is_none(self) -> bool:
        return self.value == OrderTypes.NONE

    def is_asc(self) -> bool:
        return self.value == OrderTypes.ASC
    
