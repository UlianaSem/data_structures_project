"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import contextlib
import io
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

    def test_to_list(self):
        ll = src.linked_list.LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()

        self.assertEqual(str(lst[0]), "{'id': 0, 'username': 'serebro'}")
        self.assertEqual(len(lst), 4)

    def test_get_data_by_id(self):
        ll = src.linked_list.LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        self.assertEqual(ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(7), None)

        ll.insert_at_end('idusername')

        s = io.StringIO()

        with contextlib.redirect_stdout(s):
            ll.get_data_by_id(7)

        self.assertEqual(s.getvalue(), 'Данные не являются словарем или в словаре нет id.\n')
