myList = [1,'a','b',0,15]
def filter_list(l):
  filteredList = []
  for i in range(0,len(l)):
      if type(l[i]) == int:
          filteredList.append(l[i])
      else:
          pass
  return filteredList

print(filter_list(myList))

#print(type(myList[4])==int)