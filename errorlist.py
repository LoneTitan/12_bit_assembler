import take_Input
errorCodes = []
errorCodes = take_Input.takeInput("errorCodes.txt")
def storeError(errorcode,problem,line_number,file_name="error.txt"):
	temp = []
	error = ""
	for i in errorCodes:
		if(str(errorcode) == i[0]):
			temp = i
			break
	error += problem+ " "
	for i in temp[1:]:
		error += i
		error += " "
	error += "Error at line number:"+str(line_number)
	print(error)
	file = open(file_name,"a+")
	file.write(error+"\r\n")
	file.close()

