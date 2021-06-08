
#!/usr/bin/python3
import csv
lines = list()

with open('list1m2020.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if '.sc' in row[0]:
                print('removed', end=',')
                lines.remove(row)

            if '.br' in row[0]:
                print('removed', end=',')
                lines.remove(row)

            if '.ao' in row[0]:
                print('removed', end=',')
                lines.remove(row)

            if '.gt' in row[0]:
                print('removed', end=',')
                lines.remove(row)
                
            if '.google' in row[0]:
                print('removed', end=',')
                lines.remove(row)

            if '.lk' in row[0]:
                print('removed', end=',')
                lines.remove(row)

            if '.ec' in row[0]:
                print('removed', end=',')
                lines.remove(row)
            
            if '.sk' in row[0]:
                print('removed', end=',')
                lines.remove(row)
            
with open('newList1.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)