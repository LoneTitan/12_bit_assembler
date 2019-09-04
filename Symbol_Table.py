Symbol_Table = {}

def addtoTable(symbol,location):
	if symbol not in Symbol_Table:
		Symbol_Table[symbol] = (location)


def getlocation(symbol):
	if symbol in Symbol_Table:
		return Symbol_Table[symbol]
	else :
		return -2
		