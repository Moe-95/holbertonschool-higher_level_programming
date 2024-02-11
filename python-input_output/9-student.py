#!/usr/bin/python3

class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return self.__dict__

if __name__ == "__main__":
    student = Student("John", "Doe", 23)
    print(student.to_json())
