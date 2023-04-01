import unittest
from uuid import uuid4

from shared.domain.value_objects import Uuid


class TestUuid(unittest.TestCase):

    def test_ok(self):
        value = str(uuid4())
        obj = Uuid(value)
        self.assertEqual(obj.value, value)

    def test_to_str(self):
        value = str(uuid4())
        obj = Uuid(value)
        self.assertEqual(str(obj), value)

    def test_equal(self):
        value = str(uuid4())
        obj1 = Uuid(value)
        obj2 = Uuid(value)
        self.assertTrue(obj1 == obj2)

    def test_not_equal(self):
        obj1 = Uuid(str(uuid4()))
        obj2 = Uuid(str(uuid4()))
        self.assertFalse(obj1 == obj2)
