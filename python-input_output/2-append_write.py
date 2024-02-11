#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append the given text to the specified file and return the number of characters added."""
    with open(filename, 'a') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
