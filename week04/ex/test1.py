import json
import csv


def json_to_tsv(jname, tsv):
    f = open(jname)
    data = json.load(f)
    with open(tsv, 'w') as output_file:
        dw = csv.DictWriter(output_file, sorted(data[0].keys()), delimiter='\t')
        dw.writeheader()
        dw.writerows(data)

json_to_tsv("JSON.json", "asd.tsv")