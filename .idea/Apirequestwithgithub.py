import requests

response = requests.get(" https://api.github.com/repos/kubernetes/kubernetes/pulls")

detaileddata = response.json()

for i in range(len(detaileddata)):
    #Here the length have been considered with the system
    print("the value of :", detaileddata[i]["user"]["login"])

