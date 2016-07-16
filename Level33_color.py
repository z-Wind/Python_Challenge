#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/rock/beer.html:kohsamui:thailand"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image
import math
import os

if not os.path.exists('.\Level33'):
    os.mkdir('.\Level33')

data = get_challenge.download("http://www.pythonchallenge.com/pc/rock/beer2.png", "kohsamui", "thailand")
im = Image.open(data)

f = im.getdata()
color = im.getcolors()
print(color)

# remove maximum and output to image
for i in range(len(color)-1, -1, -2):
    s = []
    t = []
    for j in f:
        if j != color[i][1] and j != color[i-1][1]:
            s.append(j)
            t.append(0)
        else:
            if j == color[i][1]:
                t.append(1)
            else:
                t.append(0)
    f = s
    n = int(math.sqrt(len(t)))
    new = Image.new('1', (n, n))
    new.putdata(t)
    new.save('.\level33\%d.png' % ((len(color)-i+1)/2))
