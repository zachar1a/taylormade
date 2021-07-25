import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import os, pathlib, csv



class shoeFile:
    def __init__(self, sn):
        self.shoeName = sn
        self.shoeDF = pd.read_csv('../Historical Data/'+self.shoeName)
        self.salesInPastMonth = 0

        ''' strip $ from Price and cast value from string to int '''
        self.shoeDF['Price'] = self.shoeDF['Price'].apply(lambda x: x.replace('$','') if '$' in list(x) else x)
        self.shoeDF['Price'] = self.shoeDF['Price'].apply(pd.to_numeric)

        ''' strip $ from MSRP and cast value from string to int '''
        self.shoeDF['MSRP']  = self.shoeDF['MSRP'].apply(lambda x: x.replace('$','') if '$' in list(x) else x)
        self.shoeDF['MSRP']  = self.shoeDF['MSRP'].apply(pd.to_numeric)

        ''' MSRP is added to each row so the mean is the MSRP '''
        self.MSRP = self.shoeDF['MSRP'].mean()

        self.uniqueDays = self.shoeDF['Date'].unique()[:31]
        for ud in self.uniqueDays:
            self.salesInPastMonth += len(self.shoeDF[self.shoeDF['Date'] == ud])
        self.pastMonthDF = self.shoeDF[:self.salesInPastMonth]
    def writeToFile(self, fileName, data):
        ''' write to specified file '''

        with open (fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()

    def openFileOrCreateFileAnalysis(self, data):
        ''' opens or creates Analysis.csv '''

        os.chdir(pathlib.Path(__file__).parent.absolute())
        if 'Analysis.csv' in os.listdir():
            self.writeToFile('Analysis.csv', data)
        else:
            with open('Analysis.csv', 'a', newline='') as file:
                csv.writer(file).writerow(['Shoe Name','Unique Days','Sales Per Day', 'Sales in past month',
                                           'Total Sales', 'MSRP', 'Mean', 'Total Mean', 'Median',
                                           'Total Median', 'Ratio Buy to Sale', 'Ratio Sale to Buy'])#, 'Sizes'])
                file.close()
                self.writeToFile('Analysis.csv', data)

# All of the brands are held inside of the Historical Data dir
# this iterates through all the brands and finds the historical data
# from the shoes in each brand dir and runs it through the
# analysis
for d in os.listdir('../Historical Data/'):
    if d == '.DS_Store':
        continue
    os.chdir('../Historical Data/')
    for f in os.listdir():
        x = shoeFile(f)

        data = (str(f.split('.')[0]), (len(x.uniqueDays)),(x.salesInPastMonth/len(x.uniqueDays)), x.salesInPastMonth,
         len(x.shoeDF),x.MSRP, x.pastMonthDF['Price'].mean(), x.shoeDF['Price'].mean(),
         x.pastMonthDF['Price'].median(),x.shoeDF['Price'].median(),
         x.MSRP / x.pastMonthDF['Price'].mean(),
         x.pastMonthDF['Price'].mean() / x.MSRP)
        # ,x.pastMonthDF.groupby('Size').count()['Date']))
        '''
        print('Shoe Name: ' + str(f.split('.')[0]))
        print('Unique days: ' + str(len(x.uniqueDays)))
        print('Sales in past month: ' + str(x.salesInPastMonth))
        print('Total Sales: ' + str(len(x.shoeDF)))
        print('MSRP: ' + str(x.MSRP))
        print('Mean: ' + str(x.pastMonthDF['Price'].mean()))
        print('Total Mean: ' + str(x.shoeDF['Price'].mean()))
        print('Median: ' + str(x.pastMonthDF['Price'].median()))
        print('Total Median: ' + str(x.shoeDF['Price'].median()))
        print('Ratio Buy to Sale: ' + str(x.MSRP / x.pastMonthDF['Price'].mean()))
        print('Ratio Sale to Buy: ' + str(x.pastMonthDF['Price'].mean() / x.MSRP))
        print(x.pastMonthDF.groupby('Size').count()['Date'])
        '''
        x.openFileOrCreateFileAnalysis(data)
