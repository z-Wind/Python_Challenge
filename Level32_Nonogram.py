#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/rock/arecibo.html:kohsamui:thailand"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image
import copy
import time


def getdata(url):
    f = get_challenge.download(url, "kohsamui", "thailand")
    flag = -1
    size = []
    hor = []
    ver = []
    temp = [size, hor, ver]
    for i in f.getvalue().decode().split('\n'):
        if i == '':
            pass
        elif i[0] == '#':
            flag += 1
        else:
            temp[flag].append(list(map(int, i.split())))

    return (size[0][0], size[0][1], hor, ver)


def genv(v, l, marks):
    '''遞歸方式獲取可能的排列
    v=描述串(列表) l=行/列長度 marks=(填滿,留空)
    '''
    r = []
    if v:
        for i in range(l-(len(v)-1)-sum(v)+1):  # 長度-中間留空-總填滿 = 可移動空間
            ri = marks[1]*i + marks[0]*v[0]  #開頭
            if len(v) == 1:
                r += [ri + marks[1]*(l-len(ri))]  # 剩下留空
            else:
                rr = genv(v[1:], l-len(ri)-1, marks)  # 長度少 1 因需留空
                r += [ri + marks[1] + vv for vv in rr]
        return r
    else:
        return [marks[1]*l]


# 必定的值
def confirmedSingle(origin, idx, l):
    '''檢查 l 中所有 item 的第 idx 項是否一致，不一致則返回原值，否則返回這項的值'''
    for item in l:
        if item[idx] != l[0][idx]:
            return origin
    return l[0][idx]


# 填滿確定值
def confirmed(table, hl, vl):
    '''table 填入所有確定的值'''

    for j, l in enumerate(hl):
        for i in range(len(l[0])):
            table[j][i] = confirmedSingle(table[j][i], i, l)

    for i, l in enumerate(vl):
        for j in range(len(l[0])):
            table[j][i] = confirmedSingle(table[j][i], j, l)

    return table


# 檢查是否符合
def checkMatch(tl, l):
    for i in range(len(tl)):
        if tl[i] != "?" and tl[i] != l[i]:
            return False
    return True


# 去掉不符合的組合
def removeMismatch(table, hls, vls):
    thl = []
    tvl = []
    for j, hl in enumerate(hls):
        t = []
        for rl in hl:
            if checkMatch(table[j], rl):
                t.append(rl)
        if t:
            thl.append(t)

    for i, vl in enumerate(vls):
        t = []
        for cl in vl:
            if checkMatch([l[i] for l in table], cl):
                t.append(cl)
        if t:
            tvl.append(t)

    return (thl, tvl)


# 檢查所有組合的可能性
def combineAll(tables, hl, vl, size, checktable=[], xy=(0, 0), getOne=False):
    # print(xy)
    if hl:  # 利用 hl 組合可能的 table
        # 利用 hl 檢查可能的 vl
        for l in hl[0]:
            tvl = []
            for i, vs in enumerate(vl):
                t = []
                for col in vs:
                    if col[xy[1]] == l[i]:
                        t.append(col)
                if not t:
                    tvl = []
                    break
                tvl.append(t)
            if not tvl:
                continue

            checktable.append(l)

            print('\n', xy)
            print('\n'.join(checktable))
            ans = combineAll(tables, hl[1:], tvl, size, checktable, xy=(xy[0], xy[1]+1), getOne=getOne)
            if ans:
                tables.append(copy.deepcopy(ans))
            if tables and getOne:
                return None
            # 回覆原本的狀態
            checktable.pop()

        return None

    else:  # if len(vl) == size[1]:
        return checktable


def measureTime(func):
    def with_measureTime(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start)
        print("get elapsed:", elapsed)
        input("pause...")
        return result
    return with_measureTime


@measureTime
def solved(width, height, hnum, vnum):
    # print(width, height, hnum, vnum)
    table = [["?" for _ in range(width)] for _ in range(height)]

    Hlist = [genv(a, width, ('1', '0')) for a in hnum]
    Vlist = [genv(a, height, ('1', '0')) for a in vnum]
    # print('all possible row/col generated.')
    # 此部分還可改進速度，將 confirmed & removeMismatch 合併寫，如 solvedFast
    # 但考慮可讀性就不修了
    while True:
        sumH = sum([len(x) for x in Hlist])
        sumV = sum([len(x) for x in Vlist])

        table = confirmed(table, Hlist, Vlist)
        Hlist, Vlist = removeMismatch(table, Hlist, Vlist)

        print('H after: ',)
        print(','.join([str(len(x)) for x in Hlist]))
        print('V after: ',)
        print(','.join([str(len(x)) for x in Vlist]))
        sumHt = sum([len(x) for x in Hlist])
        sumVt = sum([len(x) for x in Vlist])

        if sumH == sumHt and sumV == sumVt:
            break

    # print('removeMismatch')
    tables = []
    combineAll(tables, Hlist, Vlist, (width, height), getOne=True)

    # print(tables)
    if tables:
        print("\nfinish")
        for t in tables:
            print('\n'.join(t))
    else:
        print("no solution")

    imgs = []
    for t in tables:
        img = Image.new('L', (width, height))
        img.putdata([(x == '0') and 255 or 0 for l in t for x in l])
        imgs.append(img.resize((width*10, height*10)))

    return imgs


@measureTime
def solvedFast(width, height, hnum, vnum):
    # print(width, height, hnum, vnum)
    table = [["?" for _ in range(width)] for _ in range(height)]

    Hlist = [genv(a, width, ('1', '0')) for a in hnum]
    Vlist = [genv(a, height, ('1', '0')) for a in vnum]

    totalnumber = width*height
    resovlednumber = 0
    itercnt = 1
    resovled = table
    while resovlednumber < totalnumber:
        print('nitercnt=%d' % (itercnt))
        for i, rows in enumerate(Hlist):
            for j in range(width):
                if resovled[i][j] == '?':
                    t = confirmedSingle(None, j, rows)
                    if t:
                        resovled[i][j] = t
                        Vlist[j] = [item for item in Vlist[j] if item[i] == t]  # 馬上用確定的點來減少Vlist對應列的可能數量
                        resovlednumber += 1
        for i, cols in enumerate(Vlist):
            for j in range(height):
                if resovled[j][i] == '?':
                    t = confirmedSingle(None, j, cols)
                    if t:
                        resovled[j][i] = t
                        Hlist[j] = [item for item in Hlist[j] if item[i] == t]  # 馬上用確定的點來減少Hlist對應行的可能數量
                        resovlednumber += 1

        print('H after: ',)
        print(','.join([str(len(x)) for x in Hlist]))
        print('V after: ',)
        print(','.join([str(len(x)) for x in Vlist]))
        itercnt += 1

    # print(tables)
    print("\nfinish")
    print('\n'.join([''.join(l) for l in resovled]))

    img = Image.new('L', (width, height))
    img.putdata([(x == '0') and 255 or 0 for l in resovled for x in l])
    return img.resize((width*10, height*10))


# width, height, hnum, vnum = getdata("http://www.pythonchallenge.com/pc/rock/warmup.txt")
# result = solved(width, height, hnum, vnum)
width, height, hnum, vnum = getdata("http://www.pythonchallenge.com/pc/rock/up.txt")
result = solvedFast(width, height, hnum, vnum)
result = solved(width, height, hnum, vnum)[0]

# google Free" as in "Free speech", not as in "free 可得 beer
