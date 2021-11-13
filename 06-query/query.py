import pymongo

#Find document(s) with the address "Park Lane 38":


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]


myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)


for x in mydoc:
    print(x)

