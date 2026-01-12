import json
import re

# Open the file and load the data
with open('Tasks/data/userdata.json', 'r') as file:
    data = json.load(file)


def is_valid_email(email):
    # Basic regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def check_validity(y):
    errors =[] 
    if not isinstance(y["id"] , int ) or y["id"] <=0 :
        errortext = "id is not valid"
        errors.append(errortext)
    if not isinstance(y["name"] , str) or (y["name"]).strip()=="" :
        errortext = "name is invalid"
        errors.append(errortext)
    if not is_valid_email(y["email"]):
        errors.append("Email is not valid")
    # this is for age 
    try :
        y["age"] = int(y["age"])            
        y["isadult"] = y["age"]>=18 
    except Exception as err :
        errors.append("age is invalid")

    return errors 

valid_users =[]
invalid_users = []
for user in data : 
    temp = check_validity(user)
    if not len(temp):
        # print("This is a valid user ")
        # print(temp)
        valid_users.append(user)
    else:
        # print("This is a nooooot user ")
        # print(temp)
        invalid_users.append({"user": user , "error" : temp})

print("this is the list of valid users ---/n")

print(valid_users)

print("this is the list of invalid users")

print(invalid_users)




