
import json
import csv
import os.path

def json_to_tsv(jsonfile,tsvfile):

    if os.path.exists(jsonfile):
        f = open(jsonfile) 
        data = json.load(f)
        toTSVfile = open(tsvfile, "w")

        showTSV = csv.DictWriter(toTSVfile, sorted(data[0].keys()), delimiter='\t')
        showTSV.writeheader()
        showTSV.writerows(data)
        print("1")
    else:
        print("0")


json_to_tsv("example1.json","TSVtoJSON.tsv")