import unittest
from cs_nds import Queue

class TestQueue(unittest.TestCase):
    def test_isEmpty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        q.enqueue(1)
        self.assertFalse(q.isEmpty())

    def test_head(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.head()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.head(), 1)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.isEmpty())

    def test_dequeue(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertTrue(q.isEmpty())

if __name__ == '__main__':
    unittest.main()

