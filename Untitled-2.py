import csv
import json

with open ("D:\\PYTON PROGRAMMING\\Untitled-2.csv","r") as f:
    csv_reader = csv.reader(f)
    content = list(csv_reader)
    header = content[0]
    rows = content[1:]
    for row in rows:
        Total = (sum(map(int,row[-3:])))
        average = Total / len(row[-3:])
        #print(average)
        
        

with open ("D:\\PYTON PROGRAMMING\\Untitled-2.json","r") as f:
    data = json.load(f)

student = data["students"]
for val in student:
    name = val["name"]
    age = val["age"]
    city = val["city"]
    for row in rows:
        Total = (sum(map(int,row[-3:])))
        average = Total / len(row[-3:])
    print(f"Name: {name} \n Age: {age} \n City: {city} \n Total Marks: {Total} \n Average Marks: {average}")
    