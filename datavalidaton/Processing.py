import json
import re

# Open the file and load the data

with open('D:/Advanced-python/Tasks/data/userdata.json', 'r') as file:
    data = json.load(file)

async def loaddata():
    return data 

# def is_valid_email(email):
#     # Basic regex for email validation
#     return re.match(r"[^@]+@[^@]+\.[^@]+", email)


# def check_validity(y):
#     errors =[] 
#     if not isinstance(y["id"] , int ) or y["id"] <=0 :
#         errortext = "id is not valid"
#         errors.append(errortext)
#     if not isinstance(y["name"] , str) or (y["name"]).strip()=="" :
#         errortext = "name is invalid"
#         errors.append(errortext)
#     if not is_valid_email(y["email"]):
#         errors.append("Email is not valid")
#     # this is for age 
#     try :
#         y["age"] = int(y["age"])            
#         y["isadult"] = y["age"]>=18 
#     except Exception as err :
#         errors.append("age is invalid")

#     return errors 


# def process_users():
#     valid_users =[]
#     invalid_users = []
#     summary = {
#         "total_users": 0,
#         "valid_users": 0,
#         "invalid_users": 0,
#         "adult_users": 0
#     }
#     for user in data : 
#         summary["total_users"]+=1
#         temp = check_validity(user)
#         if not len(temp):
#             summary["valid_users"]+=1
#             valid_users.append(user)
#             if user["age"] >= 18:
#                 summary["adult_users"]+=1 
#         else:
#             summary["invalid_users"]+=1
#             invalid_users.append({"user": user , "error" : temp})
    
#     return valid_users , invalid_users , summary 





