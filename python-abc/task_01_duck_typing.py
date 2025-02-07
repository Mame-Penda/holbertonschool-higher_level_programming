#!/usr/bin/python3
"""Interfaces, and Duck Typing"""
from abc import ABC, abstractmethod
import math


class shape (ABC):
     @abstractmethod
     def area(self):
      """Area method."""
pass

class perimeter (ABC):
    @abstractmethod
    def perimeter(self):
     """Perimeter method."""
pass

class Circle(shape):
   """Circle class."""
   def __init__(self, radius):
    """the constructor shape."""
    self.radius = radius
   def area(self):
    """Calcul and return area circle."""
    return math.pi * self.radius ** 2

   def perimeter(self):
    """Calcul and return perimeter circle."""
    return 2 * math.pi * self.radius


class Rectangle(shape):
  """Class of rectangle."""
  def __init__(self, width, height):
    """initialize Rectangle."""
    self.width = width
    self.height = height

  def area(self):
   """Calcule and return area of the Rectangle."""
   return self.width * self.height

  def perimeter(self):
   """Calcul and return perimeter of the rectangle."""
   return 2 * (self.width + self.height)

  def shape(shape):
   """Print area and perimeter."""
   print(f"Area: {shape.area()}")
   print(f"Perimeter: {shape.perimeter()}")
