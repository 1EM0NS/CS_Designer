# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
#__author__: Ed Frey
#date:  2018/8/8
from PIL import Image

def trans_PNG(initial_pic, new_pic):
    '''
    to get a transparent picture
    :param initial_pic: initial picture's path
    :param new_pic: the transparent picture's path
    :return:
    '''
    img = Image.open(initial_pic)
        #将图片转换为四通道，而第四个通道是我们要修改的透明度，
        #值可以设置成0-255之间的值，透明度会不太一样，看脑洞有多大咯。
    img = img.convert("RGBA")
    x, y = img.size
    for i in range(x):
        for j in range(y):
            #取四个通道的值，然后用切片取前三个不变，最后一个改为240
            color = img.getpixel((i, j))
            color = color[:-1] + (240,)
            img.putpixel((i, j), color)

    #将白色及近似白色的地方改成半透明
    datas = img.getdata()
    new_data = list()
    for item in datas:
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            new_data.append((255, 255, 255, 210))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(new_pic, "PNG")

if __name__ == '__main__':

    trans_PNG("C:/Users/User/Desktop/计算机软件综合实验/计算机软件综合实验/navigation/resource/bg.png", "C:/Users/User/Desktop/计算机软件综合实验/计算机软件综合实验/navigation/resource/test02.png")