import Symbol
import Opcode_Table
Symbol_Table = {}
'''
/////////////////////////////////////////////////////////////////////////
Every fuction returns 0 on correct running else returns a negative number
/////////////////////////////////////////////////////////////////////////
'''

# Adding label to the symbol table if label is declared
def addLabelwithLocation(Label,location):
	
	if(str(-1) != str(Opcode_Table.CheckOpcode(Label)[1])):
		return -6

	symbol = Symbol.Symbol(Label,"Label")

	if symbol.name not in Symbol_Table:
		
		Symbol_Table[symbol.name] = [location , symbol.Type]
		return 0

	else:

		Type = Symbol_Table[symbol.name][1]

		if(Type == ("Variable")):
			return -3

		if(Type == ("Label")):
			
			address = Symbol_Table[symbol.name][0]
			
			if(address == -1):
			
				Symbol_Table[symbol.name][0] = location
				return 0
			
			return -4

def addLabel(Label):

	if(str(-1) != str(Opcode_Table.CheckOpcode(Label)[1])):
		return -6

	symbol = Symbol.Symbol(Label,"Label")

	if symbol.name not in Symbol_Table:
		
		Symbol_Table[symbol.name] = [-1 , symbol.Type]
		return 0

	else:

		Type = Symbol_Table[symbol.name][1]

		if(Type == ("Variable")):
			return -3

		return 0

def addVariable(Variable):
	if(str(-1) != str(Opcode_Table.CheckOpcode(Variable)[1])):
		return -7

	symbol =  Symbol.Symbol(Variable,"Variable")
	if symbol.name in Symbol_Table:
		if(symbol.Type == ("Label")):
			return -5
	else:
		Symbol_Table[symbol.name]=[-1,"Variable"]
	return 0


def isSymbolPresent(symbol,Type):
	if(symbol in Symbol_Table):
		if(Symbol_Table[symbol][1] == Type):
			return True
	return False

def getlocation(symbol):
	if symbol in Symbol_Table:
		return Symbol_Table[symbol][0]
