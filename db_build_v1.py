from pymongo import MongoClient
from datetime import datetime
import json
import requests




client = MongoClient("mongodb://localhost:27017")
db = client.primer
'''
db.drummers.drop()

db.drummers.insert_one(
    {
        "name": "chetcarello",
        "bio": "Hot new dude on scene!"
    }
)

db.drummers.update_one(
    { "name": "chetcarello" },
    {
        "$set": {
            "bio": "Check out this dude!"
        }
    }
)

db.drummers.update_one(
    { "name": "stevegadd" },
    {
        "$set": {
            "bio": "Stephen Kendall (Steve) Gadd, born April 9, 1945, is an American musician.\n\n" +
                   "Gadd is one of the most well-known and highly regarded session and studio drummers\n" +
                   "in the industry, recognized by his induction into the Modern Drummer Hall of Fame in 1984.\n" +
                    "Know for his impeccable ability to lay a groove in the pocket."
        }
    }
)

db.drummers.insert_many(
    [
        {"name": "Steve Gadd"},
        {"name": "Buddy Rich"},
        {"name": "Chet Carello"},
        {"name": "Neil Peart"},
        {"name": "Vinnie Colaiuta"},
        {"name": "Carter Beauford"}
    ]
)

db.drummers.insert_one(
    {
        "list": "drummer_list",
        "names": "Steve Gadd, Buddy Rich, Chet Carello, Neil Peart, Vinnie Colaiuta, Carter Beauford"
    }
)

'''
db.drummers.insert_one(
    {
        "list": "drummer_list",
        "names": ("Steve Gadd", "Buddy Rich", "Chet Carello", "Neil Peart", "Vinnie Colaiuta",  "Carter Beauford")
    }
)



cur = db.drummers.find()
options = list()
for doc in cur:
    if doc['list'] == "drummer_list":

        for index, item in enumerate(doc['names']):
            options.append(item)

            #options.append(doc['names'])

'''
#print q_list
#for q in q_list:
#    print q

cur = db.drummers.find()
for doc in cur:
    if doc['list'] == "drummer_list":
        resp =  doc['names']
        print type(resp)
        page = json.dumps(resp)
        print type(page)
        print page
        page = json.loads(page)
        print type(page)
        print page

'''