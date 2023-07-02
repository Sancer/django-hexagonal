from abc import ABC, abstractmethod
from typing import TypeVar

from .product import Product
from shared.domain.criteria import Criteria


T = TypeVar("T")


class ProductRepository(ABC):

    @abstractmethod
    def search(self, criteria: Criteria) -> list[Product]:
        raise NotImplementedError
