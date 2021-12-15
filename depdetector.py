import createTD

myTD = createTD.TD()
myTD2 = createTD.TD()


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
                        print("Dependency:", myListOfIns[x], myListOfIns[x + 1], "with register: ",
                              myListOfIns[x][haz])
                    elif arg1 in myListOfIns[x + 2]:
                        print("Dependency:", myListOfIns[x], myListOfIns[x + 2], "with register: ",
                              myListOfIns[x][haz])
                    else:
                        continue
        elif x == 2:
            if myListOfIns[x][0] != "sw":
                arg1 = myListOfIns[x][1]
                # print(arg1)
                if arg1 in myListOfIns[x + 1]:
                    haz = myListOfIns[x].index(arg1)
                    print("Dependency:", myListOfIns[x], myListOfIns[x + 1], "with register: ",
                          myListOfIns[x][haz])
            else:
                continue
        elif x == 3:
            # print("don't need to check")
            print()
        else:
            print("fallthrough")

    # print("Initial Timing Diagram:")
    # for i in myTD.initTD:
        # print(''.join(i))
    print()


def nfu(myListOfIns):
    fired = 0
    for x in range(0, 4):
        if x == 0:
            nextIns = myListOfIns[x + 1]
            nextins2 = myListOfIns[x + 2]
            arg1 = myListOfIns[x][1]
            # print("nextins0: ", nextIns[2:4])

            sw1 = 0
            sw2 = 0
            if nextIns[0] == "lw" and arg1 in nextIns[1:4]:
                sw1 = 1
            if nextins2[0] == "lw" and arg1 in nextins2[1:4]:
                sw2 = 1

            print("swi 0+1: ", sw1)
            print("swi 0+2: ", sw2)

            if arg1 in nextIns and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 2, "s")
                myTD.insert(x + 1, 3, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 3, 0, "-")
                myTD.insert(x + 3, 0, "-")
                fired = 1
            elif arg1 in nextins2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 3, "s")
                myTD.insert(x + 3, 3, "-")
                fired = 1
            print("Fired: ", fired)

        elif x == 1:
            nextIns = myListOfIns[x + 1]
            nextins2 = myListOfIns[x + 2]
            arg1 = myListOfIns[x][1]

            sw1 = 0
            sw2 = 0
            if nextIns[0] == "lw" and arg1 in nextIns[1:4]:
                sw1 = 1
            if nextins2[0] == "lw" and arg1 in nextins2[1:4]:
                sw2 = 1

            print("swi 1+1: ", sw1)
            print("swi 1+2: ", sw2)

            if arg1 in nextIns and fired < 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 3, "s")
                myTD.insert(x + 1, 4, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")

            elif arg1 in nextins2 and fired < 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 4, "s")

            elif arg1 in nextIns and fired == 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 5, "s")
                myTD.insert(x + 1, 6, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")

            elif arg1 in nextins2 and fired == 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 5, "s")

            fired = 2
            print("Fired: ", fired)

        elif x == 2:
            nextIns = myListOfIns[x + 1]
            arg1 = myListOfIns[x][1]
            floc = myTD.ins4.index("F")
            # print("floc: ",floc)

            sw1 = 0
            if nextIns[0] == "lw" and arg1 in nextIns[1:4]:
                sw1 = 1

            print("swi 2+1: ", sw1)

            if arg1 in nextIns and fired <2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, floc+1, "s")
                myTD.insert(x + 1, floc+2, "s")

                # myTD.insert(x + 1, 4, "s")
                # myTD.insert(x + 1, 5, "s")
            elif arg1 in nextIns and fired == 2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, floc + 1, "s")
                myTD.insert(x + 1, floc + 2, "s")

                # myTD.insert(x + 1, 8, "s")
                # myTD.insert(x + 1, 9, "s")

    print("No Forwarding Unit:")
    for i in myTD.initTD:
        print(''.join(i))
    print()

def wfu(myListOfIns):
    for x in range(0,4):
        if x == 0:
            if myListOfIns[x][0]=="lw":
                nextins = myListOfIns[x+1]
                arg1 = myListOfIns[x][1]
                if arg1 in nextins:
                    myTD2.insert(x+1, 3, "s")
                    myTD2.insert(x+2, 3, "s")
                    myTD2.insert(x+3, 0, "-")
                fired = 1

        elif x == 1:
            if myListOfIns[x][0]=="lw":
                nextins = myListOfIns[x+1]
                arg1 = myListOfIns[x][1]
                if arg1 in nextins:
                    dloc = myTD2.ins3.index("D")
                    floc = myTD2.ins4.index("F")
                    myTD2.insert(x+1, dloc+1,"s")
                    myTD2.insert(x+2, floc+1,"s")



        elif x == 2:
            if myListOfIns[x][0]=="lw":
                nextins = myListOfIns[x+1]
                arg1 = myListOfIns[x][1]
                if arg1 in nextins:
                    dloc = myTD2.ins3.index("D")
                    floc = myTD2.ins4.index("F")
                    myTD2.insert(x+1, dloc+2,"s")

    print("With Forwarding Unit:")
    for i in myTD2.initTD:
        print(''.join(i))
    print()