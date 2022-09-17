data="A message from csev@umich.edu to about meeting"
atsig=data.find('@')
print(atsig)
space=data.find(' ',atsig)
print(space)
data=data[atsig+1 : space]
print(data)