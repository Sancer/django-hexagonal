
from shared.domain.criteria.filter_operator import FilterOperator


class Filter:
    def __init__(self, field: str, operator: FilterOperator, value: str):
        self.field = field
        self.operator = operator
        self.value = value

    @staticmethod
    def from_values(values: dict):
        field = values.get('field')
        operator = values.get('operator')
        value = values.get('value')

        if not field or not operator or not value:
            raise ValueError("The filter is invalid")

        return Filter(field, FilterOperator.from_value(operator), value)
