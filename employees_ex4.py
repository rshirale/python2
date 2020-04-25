import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees1.py FILE")
filename = sys.argv[1]

Ids = {'Adams Andrew':1,'Callahan Laura':2,'Edwards Nancy':3,'Johnson Steve':4,
        'King Robert':5,'Mitchell Michael':6,'Park Margaret':7,'Peacock Jane':8}

# Print employees' names
with open(filename, "r") as file:
    reader = csv.DictReader(file)

    print("ID","LastName,Firstname")

    id_num = 1
    for row in reader:
        FirstName = row["FirstName"]
        LastName = row["LastName"]
        Manager = row["Manager"]
        #print(f"{id_num}",f"{Manager}", f",{LastName}", f",{FirstName}")
        print(f"{id_num}",f"{Ids['Adams Andrew']}",f"{LastName}", f"{FirstName}")
        id_num+=1
