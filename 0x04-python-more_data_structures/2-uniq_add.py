#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    numb = 0

    for n in uniqlist:
        numb += n

    return (numb)
