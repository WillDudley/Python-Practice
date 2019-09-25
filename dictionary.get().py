def mytest(x):
	return 	x[1] if len(x)==2 else x[3] if len(x)==4 else 'None'

print(mytest(['a','b', 'c', 'd']))