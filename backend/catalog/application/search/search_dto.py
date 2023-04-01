from dataclasses import dataclass

from shared.domain.value_objects import String


@dataclass
class SearchDto:
    name: String
