#http://www.pythonchallenge.com/pc/def/ocr.html
__author__ = 'chihchieh.sun'

s = ''.join([line.rstrip() for line in open('level2_ocr.txt')])

OCCURRENCES = {}

for c in s:
    OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1

avgOC = len(s) // len(OCCURRENCES)

print(''.join([c for c in s if OCCURRENCES[c] < avgOC]))