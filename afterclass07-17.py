file_1 = open('sample1.txt','r')
zaw=file_1.read()
file_2 = open('copy.txt','w')
for i in zaw:
    file_2.write(i)

file_1.close()
file_2.close()