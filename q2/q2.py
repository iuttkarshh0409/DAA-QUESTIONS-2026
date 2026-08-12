import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        contents = file.read()

    print(contents.upper())

else:
    print("File not found.")