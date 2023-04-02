from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

from .value_object import ValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True)
class Uuid(ValueObject):
    value: str

    def __post_init__(self) -> None:
        self.ensure_is_valid_uuid(self.value)

    def ensure_is_valid_uuid(self, value) -> None:
        try:
            UUID(value, version=4)
        except (ValueError, AttributeError):
            raise InvalidArgumentError()

    @classmethod
    def create(cls) -> Uuid:
        return Uuid(str(uuid4()))
