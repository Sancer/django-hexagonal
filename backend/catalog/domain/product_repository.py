from abc import ABC, abstractmethod
from typing import TypeVar

from .product import Product

T = TypeVar("T")


class ProductRepository(ABC):

    @abstractmethod
    def search(self) -> list[Product]:
        raise NotImplementedError
