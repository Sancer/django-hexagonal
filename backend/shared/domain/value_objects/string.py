from __future__ import annotations

from dataclasses import dataclass

from .value_object import ValueObject


@dataclass(frozen=True)
class String(ValueObject):
    value: str

    def __add__(self, other: String) -> String:
        return String(f'{self}{other}')

    def __eq__(self, other: String) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value
