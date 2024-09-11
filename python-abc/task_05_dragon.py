#!/usr/bin/python3
"""The Mystical Dragon"""


class SwimMixin():
    """First Mixin class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """Second Mixin class"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Inherits from both SwimMixin and FlyMixin"""

    def roar(self):
        print("The dragon roars!")
