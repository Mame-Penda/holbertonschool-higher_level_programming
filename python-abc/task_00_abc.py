#!/usr/bin/pyton3
from abc import ABC, abstractmethod


class Animal (ABC):
    @abstractmethod
    def sound(self):
        """define how an animal sound."""
        pass


class Dog(Animal):
    """Dog class."""
    def sound(self):
        """Sound method """
        return "Bark"


class Cat(Animal):
    """Cat class """
    def sound(self):
        """sound method """
        return "Meow"
