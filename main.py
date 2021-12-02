import availreq

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  #list of instructions

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))

y = availreq.showavareq(instructions)

print(y[0][0])


