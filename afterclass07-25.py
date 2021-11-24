import re
str="To be, or not to be, that is the question "
liczba=re.findall("[aeiouy]",str)
x = len(liczba)
print(x)