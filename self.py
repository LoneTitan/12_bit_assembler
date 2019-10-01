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
literal_Table = []
symbol_Table = []
file = open("inputfile.txt","r")
f1 = file.readlines()
for i in range(0,len(f1)):
#TODO : add error check for excess length
    f1[i] = f1[i][0:-1];
    a = f1[i].split(" ")
    print(a)
    print(len(a))
    if(a[0][-1] == ':'):
        check_if_present_in_literal = check_in_Table(literal_Table,a[0][:-1])
        if(check_if_present_in_literal):
            print("Literal Already defined earlier")
            exit();
        if(check_in_Opcode_Table(op.Opcodes,a[1])):
            if(len(a) - 2 != op.Opcodes[a[1]][2]):
                print("Wrong Length")
                exit();
        else:
            print("Wrong Op Code")
            exit();
        literal_Table.append([a[0][:-1],i])
    elif(check_in_Opcode_Table(op.Opcodes,a[0])):
        if(len(a) - 1 != op.Opcodes[a[0]][2]):
            print("Wrong Length")
            exit();
    else:
        print("Wrong Op Code")
        exit();
