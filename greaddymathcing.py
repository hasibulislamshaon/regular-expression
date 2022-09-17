import re
x='From: using the: Charecter'
y=re.findall('^F.+:',x)#greedy match
print(f"Greedy: {y}")
y=re.findall('^F.+?:',x)#not greedy match
print(f"Not greedy: {y}")