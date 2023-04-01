import unittest

from shared.domain.value_objects import Integer


class TestInteger(unittest.TestCase):

    def test_ok(self):
        value = 123
        obj = Integer(value)
        self.assertEqual(obj.value, value)

    def test_to_str(self):
        value = 123
        obj = Integer(value)
        self.assertEqual(str(obj), str(value))

    def test_equal(self):
        value = 123
        obj1 = Integer(value)
        obj2 = Integer(value)
        self.assertTrue(obj1 == obj2)

    def test_not_equal(self):
        obj1 = Integer(123)
        obj2 = Integer(456)
        self.assertFalse(obj1 == obj2)

    def test_add(self):
        value1 = 123
        obj1 = Integer(value1)
        value2 = 456
        obj2 = Integer(value2)
        self.assertEqual(obj1 + obj2, Integer(value1 + value2))
