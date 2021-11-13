import pymongo

# To delete one document, we use the delete_one() method.

# The first parameter of the delete_one() method is a query object defining which document to delete.
''' Note: If the query finds more than one document, only the first occurrence is deleted.'''

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)


#print the customers collection after the deletion:
for x in mycol.find():
  print(x)
