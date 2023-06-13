import unittest
import src.queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = src.queue.Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(len(queue.queue), 3)
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertIs(queue.tail.next_node, None)
        with self.assertRaises(AttributeError):
            queue.tail.next_node.data

    def test_str(self):
        queue = src.queue.Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')

        self.assertEqual(str(queue), "data1\ndata2")

    def test_dequeue(self):
        queue = src.queue.Queue()

        self.assertEqual(queue.dequeue(), None)

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(len(queue.queue), 1)
        self.assertEqual(queue.dequeue(), 'data3')
