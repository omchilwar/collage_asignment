import csv
file = "assignment_12&13/file.csv"
with open(file,'r') as f:
    reader=csv.reader(f)
    row_count=0
    for r in reader:
        row_count+=1
    print("total rows",row_count)    