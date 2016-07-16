# http://www.pythonchallenge.com/pc/hex/bonus.html
__author__ = 'chihchieh.sun'

import string

def trans(text, shif_num):
    frm = bytearray(string.ascii_lowercase,"UTF-8")
    to = bytearray(string.ascii_lowercase[shif_num:]+string.ascii_lowercase[:shif_num],"UTF-8")

    table = bytes.maketrans(frm,to)

    return text.translate(table)

org_str = "va gur snpr bs jung"

print(trans(org_str, 13))

import this

