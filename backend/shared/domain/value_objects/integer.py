from __future__ import annotations

from dataclasses import dataclass

from .value_object import ValueObject


@dataclass(frozen=True)
class Integer(ValueObject):
    value: int

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other: Integer) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value

    def __add__(self, other: Integer) -> Integer:
        return Integer(self.value + other.value)