import createTD

myTD = createTD.TD()

def detector(myListOfIns):
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
                        myTD.insert(x+1, 2, "s")
                        myTD.insert(x+1, 3, "s")
                        #myTD.insert(x+2, 2, "-")
                        #myTD.insert(x+2, 3, "-")
                    elif arg1 in myListOfIns[x + 2]:
                        print("Data Dependency:", myListOfIns[x], myListOfIns[x + 2], "with register: ",
                              myListOfIns[x][haz])
                        myTD.insert(x + 1, 2, "s")
                        myTD.insert(x + 1, 3, "s")
                        # myTD.insert(x+2, 2, "-")
                        # myTD.insert(x+2, 3, "-")
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
                    myTD.insert(x + 1, 2, "s")
                    myTD.insert(x + 1, 3, "s")
                    # myTD.insert(x+2, 2, "-")
                    # myTD.insert(x+2, 3, "-")
            else:
                continue
        elif x == 3:
            # print("don't need to check")
            print()
        else:
            print("fallthrough")

    print("Initial Timing Diagram:\n")
    for i in myTD.initTD:
        print(i)



