def takeInput(filename):
	line = []
	file = open(filename+".txt","r")
	f1 = file.readlines()
	for i in range(0,len(f1)):
        #add error check for excess length
		f1[i] = f1[i][0:-1]
		a = f1[i].split(" ")
		line.append(a)
	file.close()
	return line