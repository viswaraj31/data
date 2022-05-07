from email import header
import pandas as pd
import csv

df = pd.read_csv("dwarf.csv")

df = df.dropna()

df["Mass"] = df["Mass"].astype("float")

df["Mass"] = df["Mass"] * 0.000954588
df["Radius"] = df["Radius"] * 0.102763

df.drop(['Unnamed: 0'],axis = 1,inplace = True)
df.reset_index(drop = True,inplace=True)

df.to_csv("sorted.csv")

dwarf_data = []
dwarf_head = []
star_data = []
star_head = []

data =[]
data2 =[]

with open("STAR.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        data.append(i)

star_head = data[0]
star_data = data[1:]
    
with open("sorted.csv") as f:
    reader = csv.reader(f)
    for i in reader :
        data2.append(i)

dwarf_head = data[0]
dwarf_data = data[1:]

headers = star_head + dwarf_head
star = []

for i in star_data :
    star.append(i)

for i in dwarf_data :
    star.append(i)

with open ("final.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(star)
