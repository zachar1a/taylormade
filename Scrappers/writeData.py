import os, csv, pathlib

class writeData:
    '''
    This class is used to create files
    for historical data
    '''

    def __init__(self):
        print('initing')

    def writeToFile(self, fileName, data):
        ''' write to specified file '''
        with open (fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()

    def openFileOrCreateFileAnalysis(self, data):
        os.chdir(pathlib.Path(__file__).parent.absolute())
        if 'Analysis.csv' in os.listdir():
            self.writeToFile('Analysis.csv', data)
        else:
            with open('Analysis.csv', 'a', newline='') as file:
                csv.writer(file).writerow(['Shoe Name','Unique Days', 'Sales in past month',
                                           'Total Sales', 'MSRP', 'Mean', 'Total Mean', 'Median',
                                           'Total Median', 'Ratio Buy to Sale', 'Ratio Sale to Buy', 'Sizes'])
                file.close()
            self.writeToFile('Analysis.csv', data)

    def openFileOrCreateFile(self, fileName, data):
        ''' if file !Exist then create file '''
        os.chdir(pathlib.Path(__file__).parent.absolute())
        pathToHistoricalData = '../Historical Data/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            self.writeToFile(fileName, data)
        else:
            os.chdir(pathToHistoricalData)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Date', 'Time', 'Size', 'Price', 'MSRP'])
                file.close()
            self.writeToFile(fileName, data)

    def openFileOrCreateFileNike(self, fileName, data):
        ''' Creates an expandedData file for Nike '''
        os.chdir(pathlib.Path(__file__).parent.absolute())
        pathToNike = '../Shoe Brands/Nike/'
        if fileName in os.listdir(pathToHistoricalData):
            os.chdir(pathToHistoricalData)
            self.writeToFile(fileName, data)
        else:
            os.chdir(pathToHistoricalData)
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Date', 'Time', 'Size', 'Price', 'MSRP'])
                file.close()
            self.writeToFile(fileName, data)

    def openFileOrCreateFileHibbett(self, fileName, data):
        ''' creates a baseData file for Hibbett '''
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
                csv.writer(file).writerow(['Shoe', 'Link', 'MSRP'])
                file.close()
            self.writeToFile(fileName, data)
            os.chdir('../../')


