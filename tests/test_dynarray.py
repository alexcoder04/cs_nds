import unittest
from cs_nds import DynArray

class TestDynArray(unittest.TestCase):
    def setUp(self):
        self.da = DynArray()
        self.da.append(1)
        self.da.append(2)
        self.da.append(3)
        self.da.append(4)

    def test_append(self):
        self.da.append(5)
        self.assertEqual(self.da.getLength(), 5)
        self.assertEqual(self.da.getItem(4), 5)

    def test_delete(self):
        self.da.delete(1)
        self.assertEqual(self.da.getLength(), 3)
        self.assertEqual(self.da.getItem(1), 3)

    def test_insertAT(self):
        self.da.insertAT(2, 5)
        self.assertEqual(self.da.getLength(), 5)
        self.assertEqual(self.da.getItem(2), 5)

    def test_getItem(self):
        self.assertEqual(self.da.getItem(2), 3)

    def test_setItem(self):
        self.da.setItem(2, 5)
        self.assertEqual(self.da.getItem(2), 5)

    def test_isEmpty(self):
        empty_da = DynArray()
        self.assertTrue(empty_da.isEmpty())
        self.assertFalse(self.da.isEmpty())

    def test_getLength(self):
        self.assertEqual(self.da.getLength(), 4)

    def test_from_list(self):
        da_from_list = DynArray.from_list([1, 2, 3, 4])
        self.assertEqual(self.da.getLength(), da_from_list.getLength())
        for i in range(self.da.getLength()):
            self.assertEqual(self.da.getItem(i), da_from_list.getItem(i))

    def test_from_elements(self):
        da_from_elements = DynArray.from_elements(1, 2, 3, 4)
        self.assertEqual(self.da.getLength(), da_from_elements.getLength())
        for i in range(self.da.getLength()):
            self.assertEqual(self.da.getItem(i), da_from_elements.getItem(i))

if __name__ == '__main__':
    unittest.main()

