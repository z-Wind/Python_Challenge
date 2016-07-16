#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/hex/speedboat.html"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image
import bz2,keyword  

data = get_challenge.download('http://www.pythonchallenge.com/pc/hex/zigzag.gif', 'butter', 'fly')
f = Image.open(data)
fd = f.tobytes()
fp = f.palette.getdata()[1][::3]

table = bytes.maketrans(bytearray([i for i in range(256)]), fp)
ftran = fd.translate(table)

print("fd[1:10]:", fd[1:10])
print("ftran[:10]:", ftran[:10])

diff = [bytes(0),bytes(0)]
img = Image.new('1',f.size,0)  
for i in range(1,len(fd)):     
    if fd[i]!=ftran[i-1]:  
        diff[0] += bytes([fd[i]])
        diff[1] += bytes([ftran[i-1]])
        img.putpixel(((i-1)%f.size[0],(i-1)//f.size[0]),1) 
 
img.show()
text = bz2.decompress(diff[0])
print(text[:50])

s = set()
for byteStr in text.split():  
    if not keyword.iskeyword(byteStr.decode()):  
        s.add(byteStr.decode())

print(s)        