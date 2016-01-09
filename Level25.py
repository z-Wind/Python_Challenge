#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/hex/lake.html"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
import wave

wavs = [wave.open(get_challenge.download('butter', 'fly', 'http://www.pythonchallenge.com/pc/hex/lake%d.wav' % i)) for i in range(1, 26)]
