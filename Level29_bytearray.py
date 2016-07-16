#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/ring/guido.html:repeat:switch"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
import bz2  

data = get_challenge.download("http://www.pythonchallenge.com/pc/ring/guido.html", "repeat", "switch")
s = [len(sp) for sp in data.getvalue().split(b"\n")[12::]]  
text = bytearray(s)
print(text)
print(bz2.decompress(text).decode())