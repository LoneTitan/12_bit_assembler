import Opcode_Table
import Symbol_Table 
import take_Input
import re
import errorlist

FILE_NAME="inputfile.txt"
program = []     # assembly code from the file
bin_program = [] # Converted Binary Program
MAX_LOCATION_COUNTER_VALUE = 255 # ONLY USING DIRECT ADDRESSING  if lc greater than 255 fatal error
location_counter = 0  #always set location counter to zero after the pass
isCorrect = True  #If code is not correct do not generate binary
errors = [] # Stores error coming in these two passes

def remove_Comments(line):
	flag = False
	z = -1
	for z in range(len(line)):
		if("//" in line[z]):
			flag = True
			break
	if(flag):
		index = line[z].find("//")
		if(index == 0):
			line = line[:z]
		else:
			line =  line[:z+1]
			line[z] = line[z][:index]
	return line
	
def remove_colon(line):
	flag = False
	z = -1
	for z in range(len(line)):
		if(":" in line[z]):
			flag = True
			break
	if(flag):
		index = line[z].find(":")
			
		line = line[:z]+[line[z][:index]]+[line[z][index+1:]]+line[z+1:]
	while('' in line):
		line.remove('')

	return line,flag


def passOne():
	global location_counter
	global isCorrect

	for x in range(len(program)):
		error = 0
		program[x] = remove_Comments(program[x])		
		program[x],label_present = remove_colon(program[x])
		
		if(location_counter>255):
			error = -8
			isCorrect = False

		if(error<0):
			errorlist.storeError(error,"CRITICAL",-1)
			break

		if(label_present):
			error = Symbol_Table.addLabelwithLocation(program[x][0],location_counter)
		

		if(error<0):
			errorlist.storeError(error,program[x][0],location_counter)
			isCorrect = False

		if(label_present):
			program[x].pop(0)
		
		

		if(len(program[x])>2):
			isCorrect = False
		
		opcode = program[x][0]

		Opcode_info,error = Opcode_Table.CheckOpcode(opcode)
	
		if(error<0):
			isCorrect = False
			errorlist.storeError(error,program[x][0],location_counter)
			location_counter += 1
			continue

		opcode , MRI , operands , definative , accept_variable = Opcode_info

		if(MRI == 0):
			
			if(opcode == "1100" and location_counter!=len(program)-1):
				error = -13


			elif(len(program[x][1:])!=0):
		
				error = -9
			

		
			if(error<0):

				isCorrect = False
				errorlist.storeError(error,program[x][0],location_counter)
				location_counter += 1
				continue 

		else:

			if (len(program[x][1:])!=operands):

				if(len(program[x][1:])>operands):

					error = -10
					err_str= ""
					for i in program[x][1:]:
						err_str+=i
						err_str+=" "

					errorlist.storeError(error,err_str,location_counter)

				if(len(program[x][1:])<operands):
				
					error = -11
					errorlist.storeError(error,program[x][0],location_counter)

				if(error<0):
					isCorrect = False
					location_counter += 1
					continue

			else:
				if(not accept_variable):
					
					error = Symbol_Table.addLabel(program[x][1])
				
				else:
					if(definative):
						
						error = Symbol_Table.addVariable(program[x][1])
					
					else:
						
						if(Symbol_Table.isSymbolPresent(program[x][1],"Variable")):
					
							error = Symbol_Table.addVariable(program[x][1])
					
						else:
							error = -12

				if(error<0):
					isCorrect = False
					errorlist.storeError(error,program[x][1],location_counter)
					location_counter += 1
					continue

		location_counter += 1

	if("STP" not in program[-1]):
		error = -14
		error.storeError(error,"STP",location_counter)

	error = 0
	for i in Symbol_Table.Symbol_Table:
		
		if(Symbol_Table.Symbol_Table[i][1] == "Variable"):
			Symbol_Table.Symbol_Table[i][0] = location_counter
			location_counter += 1
		
		if(Symbol_Table.Symbol_Table[i][1] == "Label"):
			if(Symbol_Table.Symbol_Table[i][0] == -1):
				error = -15


		if(location_counter>255):
			error = -8

		if(error<0):
			isCorrect = False
			errorlist.storeError(error,"CRITICAL",-1)
			if(error == -8):
				break

		





def passTwo():
	global location_counter
	global program
	global bin_program
	global isCorrect
	for i in program:
		error = 0
		instruction = ""
		Opcode_info,error = Opcode_Table.CheckOpcode(i[0])
		opcode , MRI , operands , definative , accept_variable = Opcode_info
		if(MRI == 0):
			instruction = opcode +"00000000"
		else:
			symbol_address = Symbol_Table.getlocation(i[1])
			if(symbol_address == -1):
				error = -15
				errorlist.storeError(error,i[1],location_counter)
				isCorrect = False
			else:
				symbol_address = bin(symbol_address)[2:]
				symbol_address = "0"*(len(symbol_address))+symbol_address
				instruction = opcode + symbol_address
		bin_program.append(instruction)
		location_counter += 1
		

def createOutputFile():
	global FILE_NAME
	try:
		f = open(FILE_NAME+"_Output.txt", 'r+')
		f.truncate(0)
	except Exception:
		f = open(FILE_NAME+"_Output.txt",'w')
		f.close()
def createBinary():
	global bin_program
	global FILE_NAME
	f = open(FILE_NAME+"_Output.txt",'w')
	for i in bin_program:
		f.write(i)
		f.write("\r\n")
	f.close()



def main():
	global program
	global location_counter
	global isCorrect
	program = take_Input.takeInput("inputfile")
	errorlist.clear_error_file()
	passOne()
	location_counter = 0
	if(isCorrect):
		passTwo()
	if(isCorrect):
		createOutputFile()
		createBinary()
		print("_Output stored in inputfile_Output.txt")
		return
	print("Error stored in inputfile_error.txt")

if __name__ == "__main__":
	main()
