import instok

file1 = open("inputProg.txt", "r")
inputProg = file1.readlines()
instructions = []

for i in range(len(inputProg)):
    instructions.append(inputProg[i].strip('\n'))

one = instok.tokenized_ins(instructions[0])

print()
print()
#toast

