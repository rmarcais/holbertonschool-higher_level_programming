#!/usr/bin/python3
"""100-singly_linked_list.py

Write a class Node that defines a node of a singly linked list by:

- Private instance attribute: data:
-- property def data(self): to retrieve it
-- property setter def data(self, value): to set it:
. data must be an integer, otherwise raise
 a TypeError exception with the message data must be an integer

- Private instance attribute: next_node:
-- property def next_node(self): to retrieve it
-- property setter def next_node(self, value): to set it:
. next_node can be None or must be a Node, otherwise raise a
 TypeError exception with the message next_node must be a Node object

- Instantiation with data and next_node:
 def __init__(self, data, next_node=None):

And, write a class SinglyLinkedList that defines a singly linked list by:

- Private instance attribute: head (no setter or getter)

- Simple instantiation: def __init__(self):

- Should be printable:
-- print the entire list in stdout
-- one node number by line

- Public instance method: def sorted_insert(self, value):
 that inserts a new Node into the correct
 sorted position in the list (increasing order)
"""


class Node:
    """class that defines a node of a singly linked list."""

    """Initializes a node with parameters data and next_node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property method."""
        return self.__data

    @data.setter
    def data(self, value):
        """property method."""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property method."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property method."""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list."""

    """Initializes a signly linked list."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the sll."""
        newnode = Node(value)
        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            newnode.next_node = tmp.next_node
            tmp.next_node = newnode

    def __str__(self):
        """This method tells to the main program how to print the singly
        linked list."""
        LL = []
        tmp = self.__head
        while tmp is not None:
            LL.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(LL))
