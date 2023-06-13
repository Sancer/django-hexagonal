from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class EnumValueObject(ABC, Generic[T]):
    def __init__(self, value: T, valid_values: list[T]):
        self.value = value
        self.valid_values = valid_values
        self.check_value_is_valid(value)

    def check_value_is_valid(self, value: T):
        if value not in self.valid_values:
            self.throw_error_for_invalid_value(value)

    @abstractmethod
    def throw_error_for_invalid_value(self, value: T):
        not_implemented_error_message = 'throw_error_for_invalid_value method not implemented'
        raise NotImplementedError(not_implemented_error_message)
