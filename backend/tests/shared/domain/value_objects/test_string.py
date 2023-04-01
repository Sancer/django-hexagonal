import unittest

from shared.domain.value_objects import String


class TestString(unittest.TestCase):

    def test_ok(self):
        value = 'asd'
        obj = String(value)
        self.assertEqual(obj.value, value)

    def test_to_str(self):
        value = 'asd'
        obj = String(value)
        self.assertEqual(str(obj), value)

    def test_equal(self):
        value = 'asd'
        obj1 = String(value)
        obj2 = String(value)
        self.assertTrue(obj1 == obj2)

    def test_not_equal(self):
        obj1 = String('asd')
        obj2 = String('other')
        self.assertFalse(obj1 == obj2)

    def test_add(self):
        value1 = 'asd'
        obj1 = String(value1)
        value2 = 'qwe'
        obj2 = String(value2)
        self.assertEqual(obj1 + obj2, String(value1 + value2))
