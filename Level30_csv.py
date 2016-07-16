#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/ring/yankeedoodle.html:repeat:switch"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image

csv = get_challenge.download("http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv", "repeat", "switch")
    
color = []
for line in csv.getvalue().split(b"\n"):
    for data in line.split(b","):
        d = data.decode().strip()
        if d:
            color.append(d)

length = len(color)
print(length)
# 7367

factors = [x for x in range(2, length) if length % x == 0]
print(factors)
# [53, 139] 

img = Image.new('F',(53,139)) 
img.putdata(list(map(float,color)), 256)

img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.ROTATE_90)
img.show()

d1 = color[0::3]
d2 = color[1::3]
d3 = color[2::3]

res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(d1, d2, d3)])

print(res.decode())