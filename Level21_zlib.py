# package.pack from Level 20
__author__ = 'Administrator'

import zlib
import bz2

def decompress(data,logo):
    if data[:2] == b'x\x9c':
        logo.append(' ')
        return zlib.decompress(data)
    elif data[:2] == b'BZ':
        logo.append('b')
        return bz2.decompress(data)
    elif data[len(data)-2:] == b'\x9cx':
        logo.append('\n')
        return zlib.decompress(data[::-1])
    elif data[len(data)-2:] == b'ZB':
        logo.append('B')
        return bz2.decompress(data[::-1])
    else:
        print(data[::-1])

pack = open('./Level 21/package.pack','rb').read()
logo = [];

while True:
    try:
        pack = decompress(pack,logo)
    except:
        break

print(''.join(logo))