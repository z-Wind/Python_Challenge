#http://www.pythonchallenge.com/pc/def/map.html
__author__ = 'z-Wind'

import string

def trans(text):
    frm = bytearray(string.ascii_lowercase,"UTF-8")
    to = bytearray(string.ascii_lowercase[2:]+string.ascii_lowercase[:2],"UTF-8")

    table = bytes.maketrans(frm,to)

    return text.translate(table)

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
... amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
... ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
... lmu ynnjw ml rfc spj."""

print(trans(text))