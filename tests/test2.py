#!/usr/bin/python3
import whois
import csv

T = open("list1m2020.csv","r")
myReader = csv.reader(T)
i=0

for row in myReader:
    if i<10:
        
        print(row[0],end=';')
        #domain=whois.query(row[0])
        #print(domain.registrar)
        i=i+1
        

