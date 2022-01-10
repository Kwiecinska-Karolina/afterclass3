import csv

pola=[]
wiersze=[]
    
with open('students.txt','r') as csvf:
    csvreader=csv.reader(csvf, delimiter=',')
    pola= next(csvreader)
    wiersze=[i for i in csvreader]
    st=""
    for j in wiersze:
        for x in range(1):
            if j[2]<str(30):
                st = st+(j[0]+" "+j[1]+" "+j[4] + "\n")
    print( st )     


