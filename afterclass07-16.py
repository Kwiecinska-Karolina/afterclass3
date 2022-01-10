file=open("1.txt","r")
line=""
a = 5

for i in range(20):
    x=input("Press Enter to continue")
    for i in range(a):
        line=file.readline()
        print(line)
file.close()
