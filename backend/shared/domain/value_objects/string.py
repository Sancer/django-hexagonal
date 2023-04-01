from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class String:
    value: str

    def __str__(self) -> str:
        return f'{self.value}'

    def __add__(self, other: String) -> String:
        return String(f'{self}{other}')

    def __eq__(self, other: String) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value
