import symbol
symbols = []
def takeInput():
    file = open("inputfile.txt","r")
    f1 = file.readlines()
    print(len(f1))
    for i in range(0,len(f1)):
        #add error check for excess length
        a = f1[i].split(" ")
        print(a[0])
        symbols.append(a[0])
        if(a[0])
takeInput()
print(symbols)
