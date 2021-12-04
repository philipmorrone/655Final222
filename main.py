import listoflistins
import eval

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  #list of instructions

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))
    print(instructions[i])

myLists = listoflistins.lol(instructions)

for i in myLists:
    print(i)


eval.evaluator(myLists)

print()

