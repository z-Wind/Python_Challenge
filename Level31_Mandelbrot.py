#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://www.pythonchallenge.com/pc/ring/grandpa.html:repeat:switch"""
'''一開始的網頁源碼說和Python沒有關係，點擊圖片卻需要驗證口令，口令是島嶼：國家，
那麼用Google圖片搜索搜索一下這幅圖，發現是泰國的一個祖父祖母石，
在Koh Samui, Thailand所以口令就是：kohsamui：thailand'''

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import get_challenge
from PIL import Image

def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027,max=128, size=(640, 480)):
    xstep = width / size[0]
    ystep = height / size[1]
    for y in range(size[1] - 1, -1, -1):
        for x in range(size[0]):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0+0j
            for i in range(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            yield i
            
data = get_challenge.download("http://www.pythonchallenge.com/pc/rock/mandelbrot.gif", "kohsamui", "thailand")
ufos = Image.open(data)

mandel = ufos.copy() # 直接使用原圖的類型、大小和調色板
mandel.putdata(list(mandelbrot()))
mandel.show() # 自己畫出的圖像看上去和給出的圖一樣
# 通過比較像素確定自己畫的圖和給出的圖的差異
differences = [(a - b) for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]
length = len(differences)
print(length)  # 輸出 1679，說明實際上有1679處不同
print(set(differences)) # 輸出set([-16, 16])，說明實際上所有差異都是16或者-16
factors = [x for x in range(2, length) if length % x == 0]
print(factors)
# 輸出 [23, 73] ，說明可以解析為23×73的圖像
# 構造 23×73的圖像，放大10倍後顯示
plot=Image.new('L',(23,73))
plot.putdata([(i < 16) and 255 or 0 for i in differences]) # 是-16則設為255，否則設為0
plot.resize((230, 730)).show() # 顯示一幅奇怪的圖像
# 利用 google 以圖找圖，得知名為『阿雷西博信息』(Arecibo message)