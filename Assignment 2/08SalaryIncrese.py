from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

sal=int(input('Enter salary : '))
qr={}
qr["salary"]=sal
print(qr)

gt={"$gt":qr}

for doc in coll.find(qr,gt):
    print(doc)

