import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
m=0
for i in temperatures:
    m = m + int(i)
print(m)