#There is a condition check on command line argumenerts whre you need to see if else condition
import sys
type = sys.argv[1]

if type == "t2.micro":
    print("we are good to go with the instance")

elif type == "t2microcost":
    print("we will charge you the minimum one")

elif type == "t2.large":
    print("We will create the large instance")

elif type == "t2largecost":
    print("We will charge the additional cost")

else:
    print("This is not allowed")