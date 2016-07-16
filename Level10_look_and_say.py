#http://www.pythonchallenge.com/pcc/return/bull.html => huge, file
__author__ = 'chihchieh.sun'

import itertools
import re

def look_and_say(index):
    ans = '1'
    for i in range(index):
        s = ''
        for key,group in itertools.groupby(ans):
            s += str.format('%d%s' %(len(list(group)),key))
        ans = s

    return ans

def look_and_say_re(index):
    ans = '1'
    for i in range(index):
        s = "".join([str(len(m.group(0))) + m.group(1) for m in re.finditer(r"(\d)\1*", ans)])
        ans = s

    return ans



print(len(look_and_say(30)))
print(len(look_and_say_re(30)))