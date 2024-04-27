# Write a program to list the number of files in the folder under linux
import os

directory = input("Please enter the correct directory ")
print(directory)

for folder in directory:
    try:
        files = os.listdir()
    except FileNotFoundError:
        print(files)

for file in files:
    print(file)