def tokenized_ins(inputins):
    """

    :type inputins: str
    """
    tokes1 = inputins.replace("(", " ")
    tokes2 = tokes1.replace(")", "")
    tokes = tokes2.replace(" ", ",")
    inslist = tokes.split(",")
    return inslist
