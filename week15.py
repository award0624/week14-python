"""
# week 15 Project using random EC2 Name Generator
#create a unique name generator

"""
import random

# Allow the user to input the name of their department that is used in the unique name

number = int(input("enter number of unique names of EC2 instances: "))
department = input("Enter one of these department: Human Resources, Accounting, FinOps: ")

# Print out unique names of instances

ec2_identity = f"{department}-{''.join([chr(random.randint(97,123)) for i in range(7)])}"
print("your EC2's unique name is:", ec2_identity)
