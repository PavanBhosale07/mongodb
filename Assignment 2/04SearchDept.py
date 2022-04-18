from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

dp=input('Enter department : ')
qr={}
qr["dept"]=dp
print(qr)

for doc in coll.find(qr):
    print(doc)