import listoflistins
import depdetector

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  # list of instructions


for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))
    #print(instructions[i])

# Tokenized Instructions
ListOfIns = listoflistins.lol(instructions)
print()
for i in ListOfIns:
    print(i)

print()

depdetector.detector(ListOfIns)
depdetector.nfu(ListOfIns)
