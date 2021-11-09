# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

print(x)

""" Return the_id field"""
print(x.inserted_id)

