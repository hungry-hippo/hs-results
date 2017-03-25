import csv, os, sys

os.rename('WBRoll.txt','WBRoll_prev.txt')

with open('WBResult.csv','rb') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        if row['No.']=='2500':
            with open("WBRoll.txt",'a') as f:
                f.write(str(row['ROLL'])+'\n')
            print row['ROLL']
    
