import re
lines=open('naruto.txt')
for word in lines:
    word=word.rstrip()
    if re.search('A: ', word):
     print(word)
