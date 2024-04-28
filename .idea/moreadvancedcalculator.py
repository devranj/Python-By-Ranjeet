#Write a calculator programm using the function as well with the dont accept the hard code values
# For api key always use env var
import os
import sys

def add(num1,num2):
    sum = num1 + num2
    return add

def sub(num1,num2):
    subtract = num1 - num2
    return sub

def mul(num1,num2):
    multipication = num1*num2
    return mul
def div(num1,num2):
    divison = num1/num2
    return div

#From here lets allocate the value into the nums

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "add":
    addoutput = add(num1,num2)
    print("the value of addition output:", addoutput)


elif operator == "mul":
    muloutput = mul(num1,num2)
    print("the value of multipication output:", muloutput)

elif operator == "div":
    divoutput = div(num1,num2)
    print("the value of division output:", divoutput)

elif operator == "sub":
    suboutput = sub(num1,num2)
    print("the value of subtraction output is:", suboutput)

else:
    print("The value not exist")


