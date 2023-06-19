class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)

        if self.head is None:
            node.next_node = None
            self.tail = node
        else:
            node.next_node = self.head

        self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)

        if self.tail is None:
            self.head = node
        else:
            self.tail.next_node = node

        self.tail = node
        node.next_node = None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        data_list = []

        node = self.head

        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list

    def get_data_by_id(self):
        """Возвращает первый найденный в LinkedList словарь с ключом 'id', значение которого равно переданному в метод
        значению"""
        pass
