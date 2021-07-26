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
                                           'Total Median', 'Ratio Buy to Sale', 'Ratio Sale to Buy'
                                           ,'s4','s4_5','s5','s5_5','s6','s6_5','s7','s7_5','s8','s8_5'
                                           ,'s9','s9_5','s10','s10_5','s11','s11_5','s12','s12_5','s13','s13_5'
                                           ,'s14','s14_5','s15','s15_5','s16','s16_5','s17','s17_5','s18','s18_5'
                                           ])
                file.close()
                self.writeToFile('Analysis.csv', data)

# iterates through shoe files in Historical Data

if os.listdir('../Historical Data/'):
    os.chdir('../Historical Data/')
    for f in os.listdir():
        x = shoeFile(f)

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
        '''
        #print(x.pastMonthDF.groupby('Size').count()['Date'])
        dft = x.pastMonthDF.groupby('Size').count()
        #print(len(dft.T.columns))
        s4   = 0
        s4_5 = 0
        s5   = 0
        s5_5 = 0
        s6   = 0
        s6_5 = 0
        s7   = 0
        s7_5 = 0
        s8   = 0
        s8_5 = 0
        s9   = 0
        s9_5 = 0
        s10  = 0
        s10_5= 0
        s11  = 0
        s11_5= 0
        s12  = 0
        s12_5= 0
        s13  = 0
        s13_5= 0
        s14  = 0
        s14_5= 0
        s15  = 0
        s15_5= 0
        s16  = 0
        s16_5= 0
        s17  = 0
        s17_5= 0
        s18  = 0
        s18_5= 0

        for s in dft.T.columns:
            print(s)
            if s == 4.0:
                s4 = dft.T.at['Time', s]
            elif s == 4.5:
                s4_5 = dft.T.at['Time', s]
            elif s == 5.0:
                s5 = dft.T.at['Time', s]
            elif s == 5.5:
                s5_5 = dft.T.at['Time', s]
            elif s == 6:
                s6 = dft.T.at['Time', s]
            elif s == 6.5:
                s6_5 = dft.T.at['Time', s]
            elif s == 7.0:
                s7 = dft.T.at['Time', s]
            elif s == 7.5:
                s7_5 = dft.T.at['Time', s]
            elif s == 8.0:
                s8 = dft.T.at['Time', s]
            elif s == 8.5:
                s8_5 = dft.T.at['Time', s]
            elif s == 9.0:
                s9 = dft.T.at['Time', s]
            elif s == 9.5:
                s9_5 = dft.T.at['Time', s]
            elif s == 10.0:
                s10 = dft.T.at['Time', s]
            elif s == 10.5:
                s10_5 = dft.T.at['Time', s]
            elif s == 11.0:
                s11 = dft.T.at['Time', s]
            elif s == 11.5:
                s11_5 = dft.T.at['Time', s]
            elif s == 12.0:
                s12 = dft.T.at['Time', s]
            elif s == 12.5:
                s12_5 = dft.T.at['Time', s]
            elif s == 13.0:
                s13 = dft.T.at['Time', s]
            elif s == 13.5:
                s13_5 = dft.T.at['Time', s]
            elif s == 14.0:
                s14 = dft.T.at['Time', s]
            elif s == 14.5:
                s14_5 = dft.T.at['Time', s]
            elif s == 15.0:
                s15 = dft.T.at['Time', s]
            elif s == 15.5:
                s15_5 = dft.T.at['Time', s]
            elif s == 16.0:
                s16 = dft.T.at['Time', s]
            elif s == 16.5:
                s16_5 = dft.T.at['Time', s]
            elif s == 17.0:
                s17 = dft.T.at['Time', s]
            elif s == 18.0:
                s18 = dft.T.at['Time', s]
            elif s == 18.5:
                s18_5 = dft.T.at['Time', s]

        sizes = '''
                {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}
                ,{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29}
                '''.format(s4
                   ,s4_5
                   ,s5
                   ,s5_5
                   ,s6
                   ,s6_5
                   ,s7
                   ,s7_5
                   ,s8
                   ,s8_5
                   ,s9
                   ,s9_5
                   ,s10
                   ,s10_5
                   ,s11
                   ,s11_5
                   ,s12
                   ,s12_5
                   ,s13
                   ,s13_5
                   ,s14
                   ,s14_5
                   ,s15
                   ,s15_5
                   ,s16
                   ,s16_5
                   ,s17
                   ,s17_5
                   ,s18
                   ,s18_5)

        print(sizes)

        data = (str(f.split('.')[0]), (len(x.uniqueDays)),(x.salesInPastMonth/len(x.uniqueDays)), x.salesInPastMonth,
         len(x.shoeDF),x.MSRP, x.pastMonthDF['Price'].mean(), x.shoeDF['Price'].mean(),
         x.pastMonthDF['Price'].median(),x.shoeDF['Price'].median(),
         x.MSRP / x.pastMonthDF['Price'].mean(),
         x.pastMonthDF['Price'].mean() / x.MSRP
         ,s4,s4_5,s5,s5_5,s6,s6_5,s7,s7_5,s8,s8_5
         ,s9,s9_5,s10,s10_5,s11,s11_5,s12,s12_5,s13,s13_5
         ,s14,s14_5,s15,s15_5,s16,s16_5,s17,s17_5,s18,s18_5)

        x.openFileOrCreateFileAnalysis(data)
