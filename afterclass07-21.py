import random
file = open('numbers1.txt','w')
for i in range(50):
    file.write(str(random.randint(100,999))+"\n")
    
file.close()