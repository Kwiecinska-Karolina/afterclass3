import re
file = open('grades.txt','r')
f = file.read()
grades=re.findall('\d\.\d',f)
sum=0
mean=0
for i in grades:
    sum = sum + float(i)
mean=sum/len(grades)

file.close()
print(mean)