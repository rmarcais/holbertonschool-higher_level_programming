#!/usr/bin/python3
"""Serialization using the pickle module"""

import pickle


class CustomObject:
    """Custom class"""

    def __init__(self, name, age, is_student):
        """Initialization"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes"""

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and save it
        to the provided filename <filename>
        """

        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of the
        CustomObject from the provided filename <filename>
        """

        try:
            with open(filename, "rb") as f:
                instance = pickle.load(f)
            return instance
        except Exception:
            return None
