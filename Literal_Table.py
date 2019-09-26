import take_Input
literTable = []
def makeLiteralTable():
    input = take_Input.takeInput();
    for i in range(0,len(input)):
        temp = [input[i][0], input[i][1]]
        literTable.append(temp)
    print(literTable)
makeLiteralTable()
