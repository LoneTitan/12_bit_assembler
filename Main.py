import Opcode_Table
import Symbol_Table 
import take_Input
import re

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

	return line


def passOne():
	for x in range(len(program)):
		program[x] = remove_Comments(program[x])		
		program[x] = remove_colon(program[x])
		print(program[x])

def passTwo():

	pass

def createBinary():
	pass




program = take_Input.takeInput()

passOne()
passTwo()
if(isCorrect):
	createBinary()