import json
import csv

def tsv_to_json(tsvfile,jsonfile):

    data = {}

    tsvfile = open(tsvfile)
    tsvReader = csv.DictReader(tsvfile, delimiter="\t")
    for row in tsvReader:
        first = row['content']
        data[first] = row
            
    #print(d)
    jsonfile = open("JSONtest.json", 'w') 
    jsonfile.write(json.dumps(data, indent=3))
    
tsv_to_json("JSON.tsv","JSONtest23.json")