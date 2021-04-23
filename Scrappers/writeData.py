import os, csv

class writeData:
    def __init__(self):
        print('initing')


    def writeToFile(self, fileName, data):
        with open (fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()
  
    def openFileOrCreateFile(self, fileName, data):
        pathToHistoricalData = '../Historical Data/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            print("here")
            self.writeToFile(fileName, data)
        else:
            os.chdir(pathToHistoricalData)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Date', 'Size', 'Price'])
                file.close()
            self.writeToFile(fileName, data)

    def returnDateAndTimeArray(fileName):
        timeArray = []
        with open(fileName, 'r') as file:
            for row in file:
                print(row['Time'])
                timeArray.append((row['Date'],row['Time']))
        return timeArray
            


