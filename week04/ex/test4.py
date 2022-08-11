import json
import csv

j = json.loads(r'''[
  {
    "x": "1",
    "y": "2",
    "z": "3"
  },
  {
    "x": "6",
    "y": "7",
    "z": "B"
  }
]''')

with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(j[0].keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(j)