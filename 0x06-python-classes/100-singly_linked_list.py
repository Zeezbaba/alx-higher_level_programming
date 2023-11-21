#!/usr/bin/python3
"""module for a Node"""


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):
        """initializing the node with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data property"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data property"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node property
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value of next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initializing the singly linked list"""

        self.head = None

    def __str__(self):
        """create printable list"""

        printsll = ""
        current_location = self.head
        while current_location:
            printsll += str(current_location.data) + "\n"
            current_location = current_location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted value
        Args:
            value: what the value will be on the node
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current_location = self.head
        while current_location.next_node and current_location.next_node.data < value:
            current_location = current_location.next_node
        if current_location.next_node:
            new_node.next_node = current_location.next_node
        current_location.next_node = new_node
