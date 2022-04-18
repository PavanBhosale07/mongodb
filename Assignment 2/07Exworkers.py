from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

code=int(input('Enter worker ID : '))
qr={}
qr["_id"]=code
print(qr)

for doc in coll.find(qr):
    print(doc)


coll=db["exworkers"]
coll.insert_one(qr)
print('insert document in exworkers')


coll=db["workers"]
coll.delete_one(qr)
print('document deleted in from worker')