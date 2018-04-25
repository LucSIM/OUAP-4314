import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

#CSV to JSON Conversion
csvfile = open('ks-projects-201801-sample.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.october_mug_talk
db.segment.drop()
header= ["ID", "name","category","main_category","currency","deadline","goal","launched","pledged","state","backers","country","usd pledged","usd_pledged_real"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)

db.collection_names()
collec=db.segment
sorted = collec.find().sort("pledged",-1).limit(5)
for x in sorted:
    print(x)
    
success = collec.find({"state":"successful"})
i=0
for x in success:
    i+=1
print("Number of success: "+str(i))

cats=collec.aggregate([{"$group" : {"_id" : "$category", "count" : {"$sum" : 1}}}])
for x in cats:
    print(x)
    
fr = collec.find({"country":"FR"})
i=0
for x in fr:
    i+=1
print("Number of french  projetcs that started before 2016: "+str(i))