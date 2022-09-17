import re
g="From: hasibul35-506@diu.edu.bd google"
x=re.findall('^From: (\S+@\S+)',g)
print(x)