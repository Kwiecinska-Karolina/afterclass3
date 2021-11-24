file_1=open('MeatAndFish.txt','r')
f_1= file_1.readlines()
file_2=open('GrainsAndBread.txt','r')
f_2= file_2.readlines()
file = open('shoppinglist.txt','a')

for i in f_1:
    file.write(i)
for i in f_2:
    file.write(i)

file_1.close()
file_2.close()
file.close()