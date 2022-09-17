import re
x=input("Enter the line from here: ")
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[aeiou]+',x)
print(y)