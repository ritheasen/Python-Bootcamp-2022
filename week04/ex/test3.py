import json
import csv

jf = open("JSON.json","r")
j = json.loads(jf)

with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(j[0].keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(j)