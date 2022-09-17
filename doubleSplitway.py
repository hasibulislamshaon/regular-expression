data="A message from csev@umich.edu to about meeting"
words=data.split()
email=words[3]
pieces=email.split('@')
print(pieces[1])