import csv
print("######################")
with open('innovator.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
print("\n\n\n")        
with open('innovator.csv', 'r') as file:
    reader = csv.reader(file,delimiter="\t")
    for row in reader:
        print(row)