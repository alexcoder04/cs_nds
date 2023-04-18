import unittest
from cs_nds import Stack

class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.top(), 3)

    def test_pop(self):
        s = Stack.from_list([1, 2, 3])
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_top(self):
        s = Stack.from_string("hello")
        self.assertEqual(s.top(), "o")

    def test_isEmpty(self):
        s1 = Stack()
        s2 = Stack.from_list([1, 2, 3])
        self.assertTrue(s1.isEmpty())
        self.assertFalse(s2.isEmpty())

    def test_from_string(self):
        s = Stack.from_string("world")
        self.assertEqual(s.pop(), "d")
        self.assertEqual(s.pop(), "l")
        self.assertEqual(s.pop(), "r")
        self.assertEqual(s.pop(), "o")
        self.assertEqual(s.pop(), "w")

    def test_from_list(self):
        s = Stack.from_list([1, 2, 3])
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_from_elements(self):
        s = Stack.from_elements(4, 5, 6)
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.pop(), 4)


if __name__ == '__main__':
    unittest.main()

