#Split by midwest, west, south and north-east

#US centrous bureau Google

import csv
import numpy as np 
import pandas as pd 
count = 0

list1 = ['WA', 'MT', 'ID', 'WY', 'OR', 'CA', 'NV', 'VT', 'CO', 'AZ', 'NM']
list2 = ['ND', 'SD', 'NE', 'KS', 'MO', 'IA', 'MN', 'WI', 'IL', 'IN', 'MI', 'OH']
list3 = ['TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'GA', 'FL', 'SC', 'NC', 'VA', 'WV', 'DC', 'MD', 'DE']
list4 = ['PA', 'NY', 'NJ', 'CT', 'RI', 'MA', 'VT', 'NH', 'ME']

west = set()
midWest = set()
south = set()
northEast = set()

for _ in list1:
    west.add(_)
for _ in list2:
    midWest.add(_)
for _ in list3:
    south.add(_)
for _ in list4:
    northEast.add(_)
myDict = {}

with open('datafest2018-Updated-April12.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if ( line[14] != 'estimatedSalary'):
            count = count + 1
            if ( line[3] == 'US' ):
                if (line[4] not in myDict):
                    myDict[line[4]] = 1
                else:
                    myDict[line[4]] = myDict[line[4]] + 1
        if ( count > 14586000 ):
            break
    print(myDict)

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

total_civilian_workplace = 157833000
#Also found this value to be 20 million?
numberofunemployed = 15330800

west_unemployment = [5.2, 4.6, 5.2, 5.1, 4.8, 3.7, 4.0, 4.8, 3.0, 6.6,  3.1, ]
midwest_unemployment = [3.0, 2.8, 3.4, 4.2, 4.4, 3.6, 3.9, 4.0, 5.7,4.0, 5.0, 4.9]
south_unemployment = [5.0, 4.6, 6.1, 3.9, 5.6, 6.2, 4.9, 4.8, 5.4, 4.9, 4.3, 5.1, 4.1, 5.9, 5.8, 4.1, 4.3]
northeast_unemployment = [5.6, 4.9, 4.7, 4.4, 5.0, 2.8, 3.1, 2.6, 3.8]

west_unemployment_value = sum(west_unemployment)
midwest_unemployment_value = sum(midwest_unemployment)
south_unemployment_value = sum(south_unemployment)
northeast_unemployment_value = sum(northeast_unemployment)

#Finding ratios of

unemployment_West = numberofunemployed * west_unemployment_value/220.4
unemployment_MidWest = numberofunemployed * midwest_unemployment_value/220.4
unemployment_South = numberofunemployed * south_unemployment_value/220.4
unemployment_NorthEast = numberofunemployed * northeast_unemployment_value/220.4

for i in west:
    sum1 = sum1 + myDict[i]
for i in midWest:
    sum2 = sum2 + myDict[i]
for i in south:
    sum3 = sum3 + myDict[i]
for i in northEast:
    sum4 = sum4 + myDict[i]

print("The number of jobs in west are :", sum1)
print("The number of jobs in midWest are :", sum2)
print("The number of jobs in south are :", sum3)
print("The number of jobs in northEast are :", sum4)

print("west_unemployment_value : ", west_unemployment_value)
print("midwest_unemployment_value : ", midwest_unemployment_value)
print("south_unemployment_value : ", south_unemployment_value)
print("northeast_unemployment_value : ", northeast_unemployment_value)
#FIND OUT NUMBER OF JOBS PER REGION

#Northeast	56209510	44395787	79.0
#Midwest	67941429	52365145	77.1
#South	    122319574	93940139	76.8
#West	    76657000	58784157	76.7


workForce_West = 3484905
workForce_MidWest = 3401434
workForce_South = 5912514
workForce_NorthEast = 2566727

jobsPerPersonWest = sum1/workForce_West
jobsPerPersonMidWest = sum2/workForce_MidWest
jobsPerPersonSouth = sum3/workForce_South
jobsPerPersonNorthEast = sum4/workForce_NorthEast

print(jobsPerPersonWest)
print(jobsPerPersonMidWest)
print(jobsPerPersonSouth)
print(jobsPerPersonNorthEast)

print(unemployment_West)
print(unemployment_MidWest)
print(unemployment_South)
print(unemployment_NorthEast)