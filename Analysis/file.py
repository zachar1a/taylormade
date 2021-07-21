import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts

class shoeFile:
    def __init__(self, sn):
        self.shoeName = sn
        self.shoeDF = pd.read_csv('../Historical Data/'+self.shoeName+'.csv')
        self.salesInPastMonth = 0

        self.shoeDF['Price'] = self.shoeDF['Price'].apply(lambda x: x.replace('$','') if '$' in list(x) else x)
        self.shoeDF['Price'] = self.shoeDF['Price'].apply(pd.to_numeric)

        uniqueDays = self.shoeDF['Date'].unique()[:31]
        for ud in uniqueDays:
            self.salesInPastMonth += len(self.shoeDF[self.shoeDF['Date'] == ud])
        self.pastMonthDF = self.shoeDF[:self.salesInPastMonth]

x = shoeFile('Jordan 1 Centre Court White University Red')
print(x.shoeDF['Price'].mean())

month = [x.split(' ')[1] for x in x.shoeDF['Date']]
day = [str(x.split(' ')[2]) for x in x.shoeDF['Date']]
year = [x.split(' ')[3] for x in x.shoeDF['Date']]

for idx, m in enumerate(month):
    if m == 'January':
        month[idx] = str(1)
    elif m == 'February':
        month[idx] = str(2)
    elif m == 'March':
        month[idx] = str(3)
    elif m == 'April':
        month[idx] = str(4)
    elif m == 'May':
        month[idx] = str(5)
    elif m == 'June':
        month[idx] = str(6)
    elif m == 'July':
        month[idx] = str(7)
    elif m == 'August':
        month[idx] = str(8)
    elif m == 'September':
        month[idx] = str(9)
    elif m == 'October':
        month[idx] = str(10)
    elif m == 'November':
        month[idx] = str(11)
    elif m == 'December':
        month[idx] = str(12)

numDate = []
for idx,d in enumerate(x.shoeDF['Date']):
    numDate.append(day[idx].strip(',') + month[idx] + year[idx])


print(len(x.pastMonthDF))
