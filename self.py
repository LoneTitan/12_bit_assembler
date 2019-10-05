import Opcode_Table as op
def check_in_Table(table, key_word):
    for i in range(0, len(table)):
        if(table[i][0] == key_word):
            return True;
    return False;
def check_in_Opcode_Table(table, key_word):
    if(key_word in table):
        return True
    return False

def isNum(key_word) :
    for i in range(len(key_word)) :
        if key_word[i].isdigit() != True :
            return False
    return True

symbol_Table = []
file = open("inputfile.txt","r")
f1 = file.readlines()
memoryAllocator = len(f1) + 1
for i in range(0,len(f1)):
    #TODO : add error check for excess length
    f1[i] = f1[i][0:-1];
    a = f1[i].split(" ")
    #Check of literal colon
    if(a[0][-1] == ':'):
        #If present in symbol table
        check_if_present_in_symbol = check_in_Table(symbol_Table,a[0][:-1])
        #Redifining error in literal table
        if(check_if_present_in_symbol):
            print("Literal Already defined earlier")
            exit();
        #If opcode is there after literal
        if(check_in_Opcode_Table(op.Opcodes,a[1])):
            #Wrong length
            if(len(a) - 2 != op.Opcodes[a[1]][2]):
                print("Wrong Length")
                exit();
            #Variable defined but not used error
            if(op.Opcodes[a[1]][2] == 2):
                if(not isNum(a[2])):
                    if(symbol_Table[a[2]] == -1):
                        print("Variable not defined but used")
                        exit()
            #Special consideration for inp
            if(a[1] == 'INP'):
                try:
                    symbol_Table.append([a[1],"Int",int(input())])
                except Exception as e:
                    print("Not a numeric value")
                    exit()
        else:
            print("Wrong Op Code")
            exit();
        #Append in symbol table
        symbol_Table.append([a[0][:-1], "Lit", i])
    #Check of Opcode
    elif(check_in_Opcode_Table(op.Opcodes,a[0])):
        #Wrong number of arguments
        if(len(a) - 1 != op.Opcodes[a[0]][2]):
            print("Wrong Length")
            exit()
        #Variables defined but not used
        if(op.Opcodes[a[0]][2] == 2):
            if(not isNum(a[2])):
                if(symbol_Table[a[2]] == -1):
                    print("Variable not defined but used")
                    exit()
        #Special case for INP
        if(a[0] == 'INP'):
            try:
                symbol_Table.append([a[0],"Int",a[1]])
            except Exception as e:
                print("Not a numeric value")
                exit()

    else:
        print("Wrong Op Code")
        exit();
print(symbol_Table)
