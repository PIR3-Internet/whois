#!/usr/bin/python3
import whois
import csv

T = open("list2m2020.csv","r")
myReader = csv.reader(T)

for row in myReader:
    if row:
        
        print(row[0],end=';')
        domain=whois.query(row[0])
        print(domain.registrar)
    
        

