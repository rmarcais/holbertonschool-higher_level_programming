#!/usr/bin/python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass of Animal"""

    def sound(self):
        return "Meow"
