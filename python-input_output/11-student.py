#!/usr/bin/python3
"""
Student to disk and reload module
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
