#Sarar Aseer & Jared Asche
#SoftDev pd06
#K07 --g
#2019-02-06
import pymongo
import json
#setup
SERVER_ADDR = "142.93.202.60"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db['primer-dataset']
with open('Hello2.json') as f:
    file_data = json.load(f)
collection.insert(file_data)
connection.close()

