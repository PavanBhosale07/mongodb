from pymongo import MongoClient

id=int(input('Enter employee ID : '))
qr={}
qr["_id"]=id

print(qr)

ct=input('Enter new city : ')
ch={}
ch["city"]=ct
print(ch)

updt={"$set":ch}

dep=input('Enter new department : ')
ab={}
ab["dept"]=dep
print(ab)

upd={"$set":ab}


client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

coll.update_one(qr,upd)
coll.update_one(qr,updt)
print('document updated...')

#for doc in coll.find(qr):
 #   print(doc)

