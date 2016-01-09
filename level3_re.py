#http://www.pythonchallenge.com/pc/def/equality.html
__author__ = 'z-Wind'

import re

s = ''.join([line.rstrip() for line in open('level3_re.txt')])

result = re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',s)

print(''.join(result))
