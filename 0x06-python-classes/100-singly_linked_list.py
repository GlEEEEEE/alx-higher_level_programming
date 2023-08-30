#!/usr/bin/python3
"""
This module contains the Node and SinglyLinkedList classes
"""


class Node:
    """
    A class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a Node instance with data and optional next_node
        Args:
            data (int): The data value of the node
            next_node (Node, optional): The next node in the linked list (default is None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data value of the node
        Returns:
            int: The data value of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node
        Args:
            value (int): The data value to be set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list
        Returns:
            Node: The next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list
        Args:
            value (Node): The next node to be set
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list
    """
    def __init__(self):
        """
        Initialize an empty singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order)
        Args:
            value (int): The value of the new Node to be inserted
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Convert the linked list to a string representation
        Returns:
            str: The string representation of the linked list
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.sorted_insert(5)
    linked_list.sorted_insert(3)
    linked_list.sorted_insert(8)
    linked_list.sorted_insert(1)
    linked_list.sorted_insert(10)
    print(linked_list)
