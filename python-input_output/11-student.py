#!/usr/bin/python3
"""
mod 11
"""

class Student:
    """
    Represents a student with capabilities to serialize and deserialize
    instance attributes.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with provided attributes.

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
        Retrieves a dictionary representation of a Student instance. If attrs
        is provided and is a list of strings, only the specified attributes
        are included in the dictionary.

        Args:
            attrs (list): Optional list specifying which attributes to include
            in the resulting dictionary.

        Returns:
            dict: A dictionary representation of the instance's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) 
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs 
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from
        a provided dictionary.

        Args:
            json (dict): A dictionary with keys as the names of the public
            attributes of the instance and values as the new values for 
            these attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
