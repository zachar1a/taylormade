import csv


with open('baseData.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row['Link'])
