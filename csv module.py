import csv

with open ("D:\PYTON PROGRAMMING\marks.csv", "r") as f:
    reader = csv.reader(f)
    content = list(reader)
    
    header = content[0]
    rows = content[1:]
    
    for row in rows:
        name = row[0]
        marks = list(map(int,row[1:]))
        total_mark = sum(marks)
        average_mark = total_mark / len(marks)
        if average_mark >= 80:
            print(f"{name}: Total = {total_mark}, Average = {average_mark:.2f} ->  passed with distinction")
        elif average_mark >= 50:
            print(f"{name}: Total = {total_mark}, Average = {average_mark:.2f} ->  passed")
        else :
            print(f"{name}: Total = {total_mark}, Average = {average_mark:.2f} ->  failed") 


