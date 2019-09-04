# OPCODE DECLRACTION
# 0 IS FOR NON MRI INSTRUCTIONS 
# 1 IS FOR MRI INSTRUCTIONS
Opcodes = {"CLA" : ("0000",0),
"LAC" : ("0001",1),
"SAC" : ("0010",1),
"ADD" : ("0011",1),
"SUB" : ("0100",1),
"BRZ" : ("0101",1),
"BRN" : ("0110",1),
"BRP" : ("0111",1),
"INP" : ("1000",1),
"DSP" : ("1001",1),
"MUL" : ("1010",1),
"DIV" : ("1011",1),
"STP" : ("1100",0)}


def CheckOpcode(opcode):
	if opcode not in Opcodes:
		return -1
	else:
		return Opcodes[opcode]