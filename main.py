import listoflistins
import eval

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []  #list of instructions

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))

myLists = listoflistins.lol(instructions)

eval.evaluator(myLists)


