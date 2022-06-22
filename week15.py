"""
# week 15 Project using random EC2 Name Generator
#create a unique name generator

"""
import random
import string
def string_generator(size=7, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
#Allow the user to input the name of their department that is used in the unique name
number = int(input("enter number of unique names of EC2 instances: "))
department = input("Enter one of these department: Human Resources, Accounting, FinOps: ")
for _ in department:
    if department == "Human Resources":
        print("Human Resources")
        break
    elif department == "Accounting":
        print("Accounting")
        break
    elif department == "FinOps":
        print("FinOps")
        break

#Print out unique names of instances

for _ in range(1, number +1):
    Unique_name = department
    ec2_identity = unique_name + "-" +string_generator()
    print("your EC2's unique name is:", ec2_identity)
    
    