import re

file=open("sample2.txt","r")
f=file.read()
word=str(re.findall("\w{6,}",f))

file.close()
print(word+"\n")

