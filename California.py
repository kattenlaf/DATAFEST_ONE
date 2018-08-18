import csv

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

dictionaryOfCities = {}
numofCalClicks = 0
totalCalClicks = 0
clicksminusLocal = 0
with open('datafest2018-Updated-April12.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if ( line[14] != 'estimatedSalary'):
            count = count + 1
            if ( line[4] == 'CA'):
                totalCalClicks = totalCalClicks + int(line[21])
                clicksminusLocal = clicksminusLocal + (int(line[21]) - int(line[22]))
                if (line[5] not in dictionaryOfCities):
                    dictionaryOfCities[line[5]] = 1
                else:
                    dictionaryOfCities[line[5]] = dictionaryOfCities[line[5]] + 1
        if ( count > 14856000 ):
            break

myclicks = 0
for key in dictionaryOfCities:
    myclicks = myclicks + dictionaryOfCities[key]

#TOTAL NUMBER OF CLICKS = 327376633
print(totalCalClicks)
print(clicksminusLocal)
print(myclicks)
clicksOutSideCalifornia = totalCalClicks - clicksminusLocal - myclicks
print(clicksOutSideCalifornia)
print(dictionaryOfCities)