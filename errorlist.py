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

def clear_error_file(file_name="error.txt"):
	try:
		f = open(file_name, 'r+')
		f.truncate(0)
	except Exception:
		f = open(file_name,'w+')
		f.close()
