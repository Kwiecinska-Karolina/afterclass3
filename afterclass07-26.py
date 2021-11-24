import re
str="To be, or not to be, that is the question"
letters= re.findall("\s",str)

print(len(letters)+1)
