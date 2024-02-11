#!/usr/bin/python3

def write_file(filename="", text=""):
    """Write the given text to the specified file and return the number of characters written."""
    with open(filename, 'w') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
