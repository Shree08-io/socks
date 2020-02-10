'''Finding each shelf in cupboard has different colors of socks pairs
       BY:Shreyansh Chougule


'''
shelf=[]
while True:
	line=input("Enter Socks Pair: ")
	if line:
		sep_shelf=[]
		for i in line:
			sep_shelf.append(i)
		shelf.append(sep_shelf)
	else:
		break

for line in shelf:
	res={}
	for key in line:
		res[key] = res.get(key, 0) + 1

	check=0
	count=len(res)
	for key in res.keys():
		if(res[key]%2==0):
			check+=1
	if(check==count):
		print('Yes!!!!!')
	else:
		print('No!!!!!!')
