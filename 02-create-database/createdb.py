import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

""" ----- Create a Database ------
Note! the new database isn't created until you do your first insert
"""

mydb = myclient["mydatabase"]  # you can also use dot notation client.mydatabase

mydb.mycoll.insert_one({"test": 'test'})


""" Check the database """
print(myclient.list_database_names())
