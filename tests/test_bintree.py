import unittest

from cs_nds import BinTree

class TestBinTree(unittest.TestCase):

    def test_init(self):
        tree = BinTree()
        self.assertIsNone(tree._BinTree__value)
        self.assertIsNone(tree._BinTree__left)
        self.assertIsNone(tree._BinTree__right)

    def test_hasItem(self):
        tree = BinTree(5)
        self.assertTrue(tree.hasItem())
        tree.deleteItem()
        self.assertFalse(tree.hasItem())

    def test_getItem(self):
        tree = BinTree(3)
        self.assertEqual(tree.getItem(), 3)
        tree = BinTree()
        self.assertIsNone(tree.getItem())

    def test_setItem(self):
        tree = BinTree()
        tree.setItem(10)
        self.assertEqual(tree._BinTree__value, 10)

    def test_isLeaf(self):
        tree = BinTree(5)
        self.assertTrue(tree.isLeaf())
        tree.setLeft(BinTree())
        self.assertFalse(tree.isLeaf())

    def test_hasLeft(self):
        tree = BinTree(5)
        self.assertFalse(tree.hasLeft())
        tree.setLeft(BinTree())
        self.assertTrue(tree.hasLeft())

    def test_getLeft(self):
        tree = BinTree(5)
        left = BinTree(4)
        tree.setLeft(left)
        self.assertEqual(tree.getLeft(), left)

    def test_setLeft(self):
        tree = BinTree(5)
        left = BinTree(4)
        tree.setLeft(left)
        self.assertEqual(tree._BinTree__left, left)

    def test_deleteLeft(self):
        tree = BinTree(5)
        left = BinTree(4)
        tree.setLeft(left)
        tree.deleteLeft()
        self.assertIsNone(tree._BinTree__left)

    def test_hasRight(self):
        tree = BinTree(5)
        self.assertFalse(tree.hasRight())
        tree.setRight(BinTree())
        self.assertTrue(tree.hasRight())

    def test_getRight(self):
        tree = BinTree(5)
        right = BinTree(6)
        tree.setRight(right)
        self.assertEqual(tree.getRight(), right)

    def test_setRight(self):
        tree = BinTree(5)
        right = BinTree(6)
        tree.setRight(right)
        self.assertEqual(tree._BinTree__right, right)

    def test_deleteRight(self):
        tree = BinTree(5)
        right = BinTree(6)
        tree.setRight(right)
        tree.deleteRight()
        self.assertIsNone(tree._BinTree__right)

if __name__ == '__main__':
    unittest.main()

