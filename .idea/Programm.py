#Write a program to list the folders and check how many files are there
#directories kitni hain
#Andar folders kitne hain
#files kitni hain
import os

directories = input("Please provide me the list of directories with space  ")
print(directories)

for folder in directories:
    files = os.listdir()
    print(files)
    #Here the output was in list

for file in files:
    print(file)




