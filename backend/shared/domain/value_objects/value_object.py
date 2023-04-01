from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    value: any
    
    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other: ValueObject) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value