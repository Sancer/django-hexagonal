import json
from dataclasses import dataclass

from shared.domain.value_objects import Uuid, String


class ProductId(Uuid):
    pass


class ProductName(String):
    pass


class ProductDescription(String):
    pass


@dataclass
class Product:
    id: ProductId
    name: ProductName
    description: ProductDescription

    def dict(self):
        return self.__dict__

    def json(self):
        return json.dumps(self.dict(), ensure_ascii=False)

    def __repr__(self):
        return self.json()
