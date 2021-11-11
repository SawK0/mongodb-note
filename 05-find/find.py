# To select data from a collection in MongoDB, we can use the find_one() method.
# find_one() return the first occurrence in the selection

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)
