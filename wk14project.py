
#create a variable to hold a list of aws services
aws_services = []

aws_services.append('EC2')
aws_services.append('Lambda')
aws_services.append('DynamoDB')
aws_services.append('S3')
aws_services.append('Cloud9')

#print the list and the length of the list

length = len(aws_services)
print("Here is a list of services", aws_services, "Here is the length of this list", length)

#we will now delete two services from the list
del aws_services[1]
del aws_services[2]
updated_list = list(aws_services)

print("I removed the first two services from the list", updated_list)

new_length = len(updated_list)
print("new length of updated list", updated_list)
