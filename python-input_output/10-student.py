#!/usr/bin/python3
"""
mod 10
"""

class Student:
    """
    Represents a student with first name, last name, and age attributes,
    capable of serializing its data to a dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is provided and it's a list of strings, only attributes
        listed in attrs are included in the dictionary.

        Args:
            attrs (list, optional): Attributes to include in the dictionary.

        Returns:
            dict: A dictionary containing key/value pairs of attributes.
            Only includes specified attributes if attrs is provided,
            otherwise includes all attributes.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr) 
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
