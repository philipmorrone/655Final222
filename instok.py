import re

def tokenized_ins(inputins):
    """

    :type inputins: str
    """
    tokes = inputins.replace(" ", ",")
    inslist = tokes.split(",")
    return inslist
