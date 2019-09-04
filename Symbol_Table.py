Symbol_Table = {}

# Adding new symbols to the table with thier locations
def addtoTable(symbol):
	if(symbol.Type.equals("Variable")):
		



def getlocation(symbol):
	if symbol in Symbol_Table:
		return Symbol_Table[symbol]
	else :
		return -2
