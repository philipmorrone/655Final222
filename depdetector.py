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
    gg = 0
    hh = 0

    for x in range(0, 4):
        if x == 0:
            nextIns = myListOfIns[x + 1]
            nextins2 = myListOfIns[x + 2]
            arg1 = myListOfIns[x][1]
            # print("nextins0: ", nextIns[2:4])

            sw1 = 0
            sw2 = 0
            if nextIns[0] == "sw" and arg1 in nextIns[1:4]:
                sw1 = 1
            if nextins2[0] == "sw" and arg1 in nextins2[1:4]:
                sw2 = 1

            # print("swi 0+1: ", sw1)
            # print("swi 0+2: ", sw2)

            if (arg1 in nextIns[2:4] or sw1 == 1) and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 2, "s")
                myTD.insert(x + 1, 3, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 3, 0, "-")
                myTD.insert(x + 3, 0, "-")
                fired = 1
                gg = 1
                print("case1\n")
            elif (arg1 in nextins2[2:4] or sw2 == 1) and (arg1 not in nextIns) and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 3, "s")
                myTD.insert(x + 3, 3, "-")
                fired = 1
                print("case2\n")
            # print("Fired: ", fired)

        elif x == 1:
            nextIns = myListOfIns[x + 1]
            nextins2 = myListOfIns[x + 2]
            arg1 = myListOfIns[x][1]

            sw1 = 0
            sw2 = 0
            if nextIns[0] == "sw" and arg1 in nextIns[1:4]:
                sw1 = 1
            if nextins2[0] == "sw" and arg1 in nextins2[1:4]:
                sw2 = 1

            # print("swi 1+1: ", sw1)
            # print("swi 1+2: ", sw2)

            if (arg1 in nextIns[2:4] or sw1 == 1) and fired < 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 3, "s")
                myTD.insert(x + 1, 4, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")
                print("case3\n")

            elif (arg1 in nextins2[2:4] or sw2 == 1) and fired < 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 4, "s")
                print("case4\n")

            elif (arg1 in nextIns[2:4] or sw1 == 1) and fired == 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, 5, "s")
                myTD.insert(x + 1, 6, "s")
                myTD.insert(x + 2, 0, "-")
                myTD.insert(x + 2, 0, "-")
                print("case5\n")

            elif (arg1 in nextins2[2:4] or sw2 == 1) and gg == 1 and fired == 1 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 2, 6, "s")
                hh = 1
                print("case6\n")
            fired = 2
            # print("Fired: ", fired)

        elif x == 2:
            nextIns = myListOfIns[x + 1]
            arg1 = myListOfIns[x][1]
            floc = myTD.ins4.index("F")
            # print("floc: ",floc)

            #print("hh = ",hh)
            #print("fired = ",fired)
            #print("arg1 = ",arg1)
            #print("nextIns14: ",nextIns[1:4])

            sw1 = 0
            if nextIns[0] == "sw" and arg1 in nextIns[1:4]:
                sw1 = 1

            #print("sw: ", sw1)

            if (arg1 in nextIns[2:4] or sw1 == 1) and fired <2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, floc+1, "s")
                myTD.insert(x + 1, floc+2, "s")
                print("case7\n")

                # myTD.insert(x + 1, 4, "s")
                # myTD.insert(x + 1, 5, "s")

            elif (arg1 in nextIns[2:4] or sw1 == 1) and hh == 1 and fired == 2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, floc + 1, "s")
                print("case99\n")

            elif (arg1 in nextIns[2:4] or sw1 == 1) and fired == 2 and myListOfIns[x][0] != "sw":
                myTD.insert(x + 1, floc + 1, "s")
                myTD.insert(x + 1, floc + 2, "s")
                print("case8\n")

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

                sw1 = 0
                if nextins[0] == "sw" and arg1 in nextins[1:4]:
                    sw1 = 1

                if (arg1 in nextins[2:4] or sw1 == 1):
                    myTD2.insert(x+1, 3, "s")
                    myTD2.insert(x+2, 3, "s")
                    myTD2.insert(x+3, 0, "-")
                fired = 1

        elif x == 1:
            if myListOfIns[x][0]=="lw":
                nextins = myListOfIns[x+1]
                arg1 = myListOfIns[x][1]

                sw1 = 0
                if nextins[0] == "sw" and arg1 in nextins[1:4]:
                    sw1 = 1

                if (arg1 in nextins[2:4] or sw1 == 1):
                    dloc = myTD2.ins3.index("D")
                    floc = myTD2.ins4.index("F")
                    myTD2.insert(x+1, dloc+1,"s")
                    myTD2.insert(x+2, floc+1,"s")



        elif x == 2:
            if myListOfIns[x][0]=="lw":
                nextins = myListOfIns[x+1]
                arg1 = myListOfIns[x][1]

                sw1 = 0
                if nextins[0] == "sw" and arg1 in nextins[1:4]:
                    sw1 = 1

                if (arg1 in nextins[2:4] or sw1 ==1):
                    dloc = myTD2.ins3.index("D")
                    floc = myTD2.ins4.index("F")
                    myTD2.insert(x+1, dloc+2,"s")

    print("With Forwarding Unit:")
    for i in myTD2.initTD:
        print(''.join(i))
    print()