import os, csv, pathlib

class writeData:
    '''
    This class is used to create files
    for historical data
    '''

    def __init__(self):
        print('initing')


    def writeToFile(self, fileName, data):
        with open (fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()
  
    def openFileOrCreateFile(self, fileName, data):
        os.chdir(pathlib.Path(__file__).parent.absolute())
        pathToHistoricalData = '../Historical Data/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            self.writeToFile(fileName, data)
        else:
            os.chdir(pathToHistoricalData)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Date', 'Time', 'Size', 'Price'])
                file.close()
            self.writeToFile(fileName, data)

    def openFileOrCreateFileNike(self, fileName, data):
        os.chdir(pathlib.Path(__file__).parent.absolute())
        pathToNike = '../Shoe Brands/Nike/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            self.writeToFile(fileName, data)
        else:
            os.chdir(pathToHistoricalData)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Date', 'Time', 'Size', 'Price'])
                file.close()
            self.writeToFile(fileName, data)

    def openFileOrCreateFileHibbett(self, fileName, data): 
        os.chdir(pathlib.Path(__file__).parent.absolute())
        print(os.getcwd())
        pathToHibbett = 'Brand Data/Hibbett/'
        if fileName in os.listdir(pathToHibbett):
            os.chdir(pathToHibbett)
            self.writeToFile(fileName, data)
            os.chdir('../../')
        else:
            os.chdir(pathToHibbett)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Shoe', 'Link'])
                file.close()
            self.writeToFile(fileName, data)
            os.chdir('../../')


'''
    def returnDateAndTimeArray(self, fileName):
        timeArray = []
        pathToHistoricalData = '../Historical Data/'
        resetPath = '../Scrappers/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            with open(fileName, 'r') as file:
                file = csv.DictReader(file)
                for row in file:
                    print(row['Time'])
                    timeArray.append((row['Date'],row['Time']))
            os.chdir(resetPath)
            return timeArray
        else:
            os.chdir(resetPath)
            return None
'''
