
import json
import csv


jsonFile = open("JSON.json","r")
jsonData = json.loads(jsonFile)
jsonFile.close()

data = json.loads(jsonData)

tsvFile = open("TSV.tsv","w")
tsvWriter = csv.writer(tsvFile, delimiter = "\t")

tsvWriter.writerow(data[0].keys())

# for row in data:
#     tsvWriter.writerow(row.values())

dw = csv.DictWriter(tsvFile, sorted(j[0].keys()), delimiter='\t')
dw.writeheader()
dw.writerows()

tsvFile.close()

# dw = csv.DictWriter(t, sorted(j[0].keys()), delimiter='\t')
# dw.writeheader()
# dw.writerows(j)


