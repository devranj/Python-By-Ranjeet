# Write a program to list the folders and after listing the folders get inside in and check for files
import os


def main():
    directory = input("Enter the dir name with the space - ").split()
    print(directory)

    for folder in directory:
        try:
            fol = os.listdir()
        except FileNotFoundError:
         print("the values are in folder:", fol)


    for files in fol:
        if files == "":
            print(files)
    else:
        print("Files are not coreect in order")

main()
