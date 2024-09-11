#!/usr/bin/python3
"""CountedIterator - Keeping Track of Iteration"""

from abc import ABC, abstractmethod


class CountedIterator():
    """
    Class that extends the built-in iterator
    obtained from the iter function
    """

    def __init__(self, iter_obj):
        """Initialization"""
        self.iterator = iter(iter_obj)
        self.counter = 0

    def get_count(self):
        """Returns the current value of the counter"""
        return self.counter

    def __next__(self):
        """Returns the next item of the original iterator"""
        self.counter += 1
        return next(self.iterator)
