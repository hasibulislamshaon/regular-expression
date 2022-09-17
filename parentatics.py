import re
g="From: hasibul35-506@diu.edu.bd google"
finda=re.findall('^From: (\S+@\S+)',g)
print(finda)