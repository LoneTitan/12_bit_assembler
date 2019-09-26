Symbol_Table = {}

# Adding label to the symbol table if label is declared
def addLabelwithLocation(symbol,location):
	if symbol.name not in Symbol_Table:
		Symbol_Table[symbol.name] = [location , symbol.Type]
	else:
		Type = Symbol_Table[symbol.name][1]

		if(Type.equals("Variable")):
			return -3

		if(Type.equals("Label")):
			address = Symbol_Table[symbol.name][0]
			if(address == -1):
				Symbol_Table[symbol.name][0] = location
				return 0
			return -4

def addVariable(symbol):
	if symbol.name in Symbol_Table:
		if(symbol.type.equals(Symbol_Table[symbol.name][1])):
			return -5
	else:
		Symbol_Table[symbol.name] = [-1,symbol.Type]
		



def getlocation(symbol):
	if symbol in Symbol_Table:
		return Symbol_Table[symbol]
	else :
		return -2
