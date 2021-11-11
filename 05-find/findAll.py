# The find() method returns all occurrences in the selection.
# No parameters in the find() method gives you the same result as SELECT * in MySQL.


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)
