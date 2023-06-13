from enum import Enum

from shared.domain.value_objects.enum_value_object import EnumValueObject


class Operator(Enum):
    EQUAL = '='
    NOT_EQUAL = '<>'
    GT = '>'
    LT = '<'
    CONTAINS = 'CONTAINS',
    NOT_CONTAINS = 'NOT_CONTAINS'


class FilterOperator(EnumValueObject[Operator]):
    def __init__(self, value: Operator):
        super().__init__(value, list(Operator))

    @staticmethod
    def from_value(value: str):
        for operator_value in Operator:
            if value == operator_value.value:
                return FilterOperator(operator_value)

        raise ValueError(f"The filter operator {value} is invalid")

    def is_positive(self):
        return self.value != Operator.NOT_EQUAL.value and self.value != Operator.NOT_CONTAINS.value

    def throw_error_for_invalid_value(self, value: Operator):
        raise ValueError(f"The filter operator {value} is invalid")

    @staticmethod
    def equal():
        return FilterOperator.from_value(Operator.EQUAL.value)