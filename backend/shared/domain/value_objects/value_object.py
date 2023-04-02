from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    value: any

    def dict(self):
        return self.value

    def json(self):
        return json.dumps(self.dict(), ensure_ascii=False)

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other: ValueObject) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value

    def __repr__(self)-> str:
        return self.json()
