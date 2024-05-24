#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Method that should do nothing on its own."""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())
