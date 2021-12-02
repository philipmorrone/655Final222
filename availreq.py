import instok

toked_ins = []

def showavareq(ins_lis):
    for i in ins_lis:
        toked_ins.append(instok.tokenized_ins(i))

    return toked_ins