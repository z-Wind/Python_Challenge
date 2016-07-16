#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/hex/lake.html"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
import wave
from PIL import Image

wavs = [wave.open(get_challenge.download('http://www.pythonchallenge.com/pc/hex/lake%d.wav' % i, 'butter', 'fly')) for i in range(1, 26)]

def jig(w): 
    return Image.frombytes('RGB', (60,60), w.readframes(w.getnframes()))

jigsaw = Image.new('RGB', (300,300), 0)
for i in range(len(wavs)): 
    jigsaw.paste(jig(wavs[i]), (60 * (i % 5), 60 * (i // 5)))

jigsaw.show()