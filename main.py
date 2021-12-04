import listoflistins
import eval

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  # list of instructions

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))
    print(instructions[i])

# Tokenized Instructions
listOfIns = listoflistins.lol(instructions)

for i in listOfIns:
    print(i)

for x in range(0, 4):
    if x < 2:
        next2 = listOfIns[x+1]+listOfIns[x+2]
        # print(listOfIns[x][0])
        # print("next 2:", next2)
        if listOfIns[x][0] != "sw":
            arg1 = listOfIns[x][1]
            # print(arg1)
            if arg1 in next2:
                haz = listOfIns[x].index(arg1)
                if arg1 in listOfIns[x+1] and arg1 in listOfIns[x+2]:
                    print("Data Dependency:", listOfIns[x], listOfIns[x+1], "with register: ", listOfIns[x][haz])
                    print("Data Dependency:", listOfIns[x], listOfIns[x+2], "with register: ", listOfIns[x][haz])
                elif arg1 in listOfIns[x+1]:
                    print("Data Dependency:", listOfIns[x], listOfIns[x + 1], "with register: ", listOfIns[x][haz])
                elif arg1 in listOfIns[x+2]:
                    print("Data Dependency:", listOfIns[x], listOfIns[x + 2], "with register: ", listOfIns[x][haz])
                else:
                    continue
    elif x == 2:
        if listOfIns[x][0] != "sw":
            arg1 = listOfIns[x][1]
            # print(arg1)
            if arg1 in listOfIns[x+1]:
                haz = listOfIns[x].index(arg1)
                print("Data Dependency:", listOfIns[x], listOfIns[x + 1], "with register: ", listOfIns[x][haz])
        else:
            continue
    elif x==3 :
        # print("don't need to check")
        print()
    else:
        print("fallthrough")