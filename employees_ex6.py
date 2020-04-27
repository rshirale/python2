#!/usr/bin/env python3

import numpy as np
import pandas as pd
import csv
import sys

# Check for filename
if len(sys.argv) != 2:
    sys.exit("Usage: python3 employees6.py FILE")

# Import employees
df = pd.read_csv(sys.argv[1])

id_num = 1
for row in df:
   FirstName = row["FirstName"]
   LastName = row["LastName"]
   Manager = row["Manager"]
   #print(f"{Manager}")
   #if Manager == Ids.items:
   print(f"{id_num}",f"{Manager}", f",{LastName}", f",{FirstName}")
   #print(f"{id_num}",f"{Ids:[]}",f"{LastName}", f"{FirstName}")
   id_num+=1
