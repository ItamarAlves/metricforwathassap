#/usr/bin/python3
import csv

# diasAusente = input('Digite a quantidade de dias que queira validar a ausência \n')

group = open('grupo.txt', 'r')
lines_group = group.readlines()

with open('groups.csv', mode='w', newline='') as csv_file:
    fieldnames = ["Date", "Number"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for line in lines_group:
        date = line[3:10]
        number = line[19:36]
        if date == '03/2021':
            writer.writerow({"Date":date, "Number":number})
