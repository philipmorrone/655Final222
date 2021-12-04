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

for i in ListOfIns:
    print(i)

depdetector.detector(ListOfIns)

ins1 = ["F", "D", "X", "M", "W"]
ins2 = ["-", "F", "D", "X", "M", "W"]
ins3 = ["-", "-", "F", "D", "X", "M", "W"]
ins4 = ["-", "-", "-", "F", "D", "X", "M", "W"]

#ins2.insert(2,"s")
#ins3.insert(2,"-")
#ins4.insert(3,"-")

print("", ins1, "\n", ins2, "\n", ins3, "\n", ins4)