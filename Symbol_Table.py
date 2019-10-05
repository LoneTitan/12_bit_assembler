import Symbol
Symbol_Table = {}
'''
/////////////////////////////////////////////////////////////////////////
Every fuction returns 0 on correct running else returns a negative number
/////////////////////////////////////////////////////////////////////////
'''

# Adding label to the symbol table if label is declared
def addLabelwithLocation(symbol,location):
	if symbol.name not in Symbol_Table:
		Symbol_Table[symbol.name] = [location , symbol.Type]
		return 0
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
		return 0



def getlocation(symbol):
	if symbol in Symbol_Table:
		return Symbol_Table[symbol]
		return 0
	else :
		return -2
