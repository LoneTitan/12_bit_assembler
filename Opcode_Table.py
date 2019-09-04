# OPCODE DECLRACTION
Opcodes = 
{"CLA" : "0000",
"LAC" : "0001",
"SAC" : "0010",
"ADD" : "0011",
"SUB" : "0100",
"BRZ" : "0101",
"BRN" : "0110",
"BRP" : "0111",
"INP" : "1000",
"DSP" : "1001",
"MUL" : "1010",
"DIV" : "1011",
"STP" : "1100"}

def CheckOpcode(opcode):
	if opcode not in Opcodes:
		return -1
