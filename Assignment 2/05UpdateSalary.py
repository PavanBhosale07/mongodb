from pymongo import MongoClient

id=int(input('Enter employee ID to modify : '))
qr={}
qr["_id"]=id

print(qr)

sala=int(input('Enter new salary : '))
ch={}
ch["salary"]=sala

print(ch)

upd={"$set":ch}

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

coll.update_one(qr,upd)
print('document updated...')

for doc in coll.find(qr):
    print(doc)

