#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/ring/bell.html:repeat:switch"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image

img = Image.open(get_challenge.download("http://www.pythonchallenge.com/pc/ring/bell.png", "repeat", "switch"))
r,g,b = img.split()
r.show()
g.show()
b.show()

gdata = list(g.getdata())  
paris=[(gdata[i],gdata[i+1]) for i in range(0,len(gdata),2)] # 根據"my paris" 將像素兩兩分為一組
# 可以看出基本上每個paris內兩像素之差都為42
print(paris[:10])

diffs=[abs(i[0]-i[1]) for i in paris] # 計算兩兩像素之差的絕對值
print(diffs[:10])
    
s = ''

for i in diffs:  
    if i != -42 and i != 42:  
        s += chr(abs(i))  
print(s)

# 難道是發音像 who done it 誰做了這些
print('Guido Van Rossum'.split()[0])