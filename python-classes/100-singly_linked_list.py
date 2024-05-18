#!/usr/bin/python3
"""
This module defines two classes: Node and SinglyLinkedList.
The Node class creates nodes for use in a singly linked list,
where each node contains integer data and a reference to the next node.
The SinglyLinkedList class manages a singly linked list, allowing for
insertions in a sorted order and providing a method to print the list.
"""

class Node:
    """
    Defines a node for a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a Node with data and an optional next node.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data from the node.
        
        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data for the node, ensuring it is an integer.

        Args:
            value (int): The data to set in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.
        
        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node, None): The node to set as the next node.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Defines a singly linked list.
    """
    def __init__(self):
        """
        Initialize the singly linked list with no nodes.
        """
        self.__head = None

    def __str__(self):
        """
        Define the print() representation of the linked list, showing all node values.
        
        Returns:
            str: A string representation of all node values, one per line.
        """
        node = self.__head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Insert a new value into the list at the correct sorted position.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
