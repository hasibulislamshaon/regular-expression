import re
lines=open('naruto.txt')
for words in lines:
    words=words.rstrip()
    if re.search('A: ', words):
     print(words)
