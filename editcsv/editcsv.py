
#!/usr/bin/python3
import csv
lines = list()

with open('newList2.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if '.de' in row[0]:
                print('removed', end=',')

                lines.remove(row)

with open('newList3.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)