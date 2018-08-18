import csv

count = 0
jobs = {}
mydictionary = { 'Paid' : 0, 'Unknown estimation' : 0}
paidClicks = 0
unpaidClicks = 0
word = 'intern'
word2 = 'Intern'
with open('datafest2018-Updated-April12.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if ( line[0] != 'date'):
            if ( word in line[9] or word2 in line[9] ):
                if(int(line[14]) == 0):
                    mydictionary['Unknown estimation'] = mydictionary['Unknown estimation'] + 1
                    unpaidClicks = unpaidClicks + int(line[21])
                else:
                    mydictionary['Paid'] = mydictionary['Paid'] + 1
                    paidClicks = paidClicks + int(line[21])
                if ( line[10] not in jobs ):
                    jobs[line[10]] = 1
                else:
                    jobs[line[10]] = jobs[line[10]] + 1
        count = count + 1

        if (count > 14586000):
            break

print(mydictionary)
print("Paid and unknown are : ",paidClicks,unpaidClicks)
print(jobs)