# Write a program to pull the requests from the api and get me the names of the

import requests

response = requests.get(" https://api.github.com/repos/kubernetes/kubernetes/pulls")
dataset = response.json()
print(dataset)

for i in range(len(dataset)):
    print("the value of user:", dataset[i]["user"]["login"])