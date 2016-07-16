#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/hex/decent.html
leopold.moz@pythonchallenge.com 發一封郵件，主題內容就用sorry，然後就可以得到一份回信了：

Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import hashlib   
f = open('.\\Level 26 zip\\mybroken.zip','rb').read()  
for i in range(len(f)):  
    for j in range(256):  
        repaired = f[:i]+bytes([j])+f[i+1:]  
        if hashlib.md5(repaired).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':  
            open('.\\Level 26 zip\\unbroken.zip','wb').write(repaired)  
            print(i, j)
            raise StopIteration