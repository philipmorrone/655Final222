import listoflistins

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  #list of instructions

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))

y = listoflistins.lol(instructions)

print(y[0][0])


