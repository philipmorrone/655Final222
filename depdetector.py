import createTD

myTD = createTD.TD()

def detector(myListOfIns):
    print("Hazards:")
    for x in range(0, 4):
        if x < 2:
            next2 = myListOfIns[x + 1] + myListOfIns[x + 2]
            # print(listOfIns[x][0])
            # print("next 2:", next2)
            if myListOfIns[x][0] != "sw":
                arg1 = myListOfIns[x][1]
                # print(arg1)
                if arg1 in next2:
                    haz = myListOfIns[x].index(arg1)
                    if arg1 in myListOfIns[x + 1]:
                        print("Data Dependency:", myListOfIns[x], myListOfIns[x + 1], "with register: ",
                              myListOfIns[x][haz])
                    elif arg1 in myListOfIns[x + 2]:
                        print("Data Dependency:", myListOfIns[x], myListOfIns[x + 2], "with register: ",
                              myListOfIns[x][haz])
                    else:
                        continue
        elif x == 2:
            if myListOfIns[x][0] != "sw":
                arg1 = myListOfIns[x][1]
                # print(arg1)
                if arg1 in myListOfIns[x + 1]:
                    haz = myListOfIns[x].index(arg1)
                    print("Data Dependency:", myListOfIns[x], myListOfIns[x + 1], "with register: ",
                          myListOfIns[x][haz])
            else:
                continue
        elif x == 3:
            # print("don't need to check")
            print()
        else:
            print("fallthrough")

    print("Initial Timing Diagram:")
    for i in myTD.initTD:
        print(''.join(i))
    print()

def nfu(myListOfIns):
    for x in range(0, 4):
        if x == 0:
            nextIns = myListOfIns[x+1]
            nextins2 = myListOfIns[x+2]
            arg1 = myListOfIns[x][1]
            if arg1 in nextIns:
                myTD.insert(x + 1, 2, "s")
                myTD.insert(x + 1, 3, "s")
                myTD.insert(x + 2, 2, "-")
                myTD.insert(x + 2, 3, "-")
                myTD.insert(x + 3, 2, "-")
                myTD.insert(x + 3, 3, "-")
            elif arg1 in nextins2:
                myTD.insert(x + 2, 3, "s")
                myTD.insert(x + 2, 4, "s")
                myTD.insert(x + 3, 3, "-")
                myTD.insert(x + 3, 4, "-")



    print("No Forwarding Unit:")
    for i in myTD.initTD:
        print(''.join(i))

