#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        n_tuple = (len(sentence), sentence[0])
        return n_tuple
    else:
        n_tuple = (len(sentence), None)
        return n_tuple
