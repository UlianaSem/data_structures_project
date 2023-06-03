import unittest
import src.stack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = src.stack.Stack()
        stack.push('test_data')

        self.assertEqual(stack.top.data, 'test_data')
        self.assertIsInstance(stack.stack, list)
        self.assertEqual(len(stack.stack), 1)

        stack.push('test_data_2')

        self.assertEqual(len(stack.stack), 2)

    def test_pop(self):
        stack = src.stack.Stack()
        stack.push('test_data')
        stack.push('test_data_2')

        self.assertEqual(stack.pop(), 'test_data_2')
        self.assertEqual(stack.top.data, 'test_data')
        self.assertEqual(len(stack.stack), 1)
