import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.interpolate import *


countList = []
salaryList = []
descriptionLength = []
clicksCount = []
count = 0

with open('datafest2018-Updated-April12.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if ( line[11] != 'descriptionCharacterLength'):
            #salaryList.append(int(line[14]))
            count = count + 1
            if (int(line[12]) > 70 and int(line[20]) != 0):
                descriptionLength.append(int(line[12]))
                salaryList.append(int(line[14]))
                clicksCount.append(int(line[21])/int(line[20]))
        if ( count > 1000000 ):
            break
    print(countList)
plt.scatter(descriptionLength, clicksCount, label='Test', color='k', s=1)
#p1 = np.polyfit(salaryList, clicksCount, 1)
#print(p1)

#plt.plot(salaryList, clicksCount, 'o')
#plt.plot(descriptionLength, np.polyval(p1, descriptionLength), 'r-')
plt.xlabel('Description Length')
plt.ylabel('Click Rate') #Clicks divided by job age
plt.show()
