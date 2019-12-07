from pymongo import MongoClient


# print('Connecting to database')
cluster = MongoClient("mongodb+srv://TalJG:SteveNash13@cluster0-zmj3y.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["NBA_games_results"]
collection = db["games_sessions"]

documents = db.collection.find({})
print(documents)
for game in documents:
    print(game)

print("done")
