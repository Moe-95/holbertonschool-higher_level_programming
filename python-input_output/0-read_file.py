#!/usr/bin/python3

def read_file(filename=""):
    """Read and print the contents of a text file."""
    with open(filename, 'r') as file:
        print(file.read())


if __name__ == "__main__":
    read_file("my_file_0.txt")
