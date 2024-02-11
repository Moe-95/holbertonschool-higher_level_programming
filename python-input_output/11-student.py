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

    def reload_from_json(self, json):
        """Replace all attributes of the student instance with the given dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    student = Student("John", "Doe", 23)
    json_data = student.to_json()

    # Save to disk
    with open("student.json", "w") as file:
        file.write(str(json_data))

    # Reload from JSON
    student.reload_from_json(json_data)
    print(student.to_json())
