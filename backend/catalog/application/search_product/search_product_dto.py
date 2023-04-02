from dataclasses import dataclass

from shared.domain.value_objects import String


@dataclass
class SearchProductDto:
    name: str
