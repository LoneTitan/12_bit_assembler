import Opcode_Table
import Symbol_Table 
import take_Input
import re
import errorlist

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
	for x in range(len(program)):
		error = 0
		program[x] = remove_Comments(program[x])		
		program[x],label_present = remove_colon(program[x])
		print(label_present)
		if(label_present):
			error = Symbol_Table.addLabelwithLocation(program[x][0],location_counter)

		if(error<0):
			errorlist.storeError(error,program[x][0],location_counter)
			isCorrect = False
		print(Symbol_Table.Symbol_Table)
		location_counter += 1




def passTwo():

	pass

def createBinary():
	pass




program = take_Input.takeInput("inputfile.txt")

passOne()
passTwo()
if(isCorrect):
	createBinary()