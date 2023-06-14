"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

import src.linked_list


class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = src.linked_list.LinkedList()
        ll.insert_beginning({'id': 1})

        self.assertEqual(ll.tail.data, {'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node, None)

    def test_insert_at_end(self):
        ll = src.linked_list.LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})

        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.head.data, {'id': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)

    def test_str(self):
        ll = src.linked_list.LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})

        self.assertEqual(str(ll), "{'id': 2} -> {'id': 3} -> None")
