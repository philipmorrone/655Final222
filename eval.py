def evaluator(ins):
    print(ins[1])

# add (arg 1), sub (arg 1), lw (arg1) can start a dependency;
# and add (args 2 and 3), sub (args 2 and 3), lw (arg 3), and sw (arg 1 and arg 3) can be linked to it.
# for lw and sw, I am skipping arg 2 which is a constant offset.
