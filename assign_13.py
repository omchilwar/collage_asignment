import csv
import json

with open('assignment_12&13/j.json','r') as jf:
    data=json.load(jf)

with open('filecopy.csv','w') as csvf:
    fieldname=data[0].keys()
    writer = csv.DictWriter(csvf,fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(data)

    print('json data converted to csv successfullly')
