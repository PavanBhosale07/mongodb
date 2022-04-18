from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

code=int(input('Enter worker ID : '))
qr={}
qr["_id"]=code

for doc in coll.find(qr):
    print(doc)
