import os, csv, pathlib


def loadData():
    with open('Scrappers/Brand Data/Hibbett/baseData.csv') as reader:

        data = []
        for row in csv.DictReader(reader):
            data.append(row['Shoe'])

    return data

# basic write to file function
def writeData(fileName, data):
    '''
    The purpose of this test is to see
    if an if statement is working or not
    '''
    data_= loadData()

    print(data[0])
    if data[0] in data_:
        return
    else:
        with open(fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()

def findUnique():
    data = loadData()
    print(list(data))

findUnique()
