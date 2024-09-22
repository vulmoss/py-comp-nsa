#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/27 21:50
# @Author   : VulMoss
# @Site     : 
# @File     : guess_card.py
# @Software : PyCharm

'''
魔术师利用一副牌中的13张黑桃，预先将它们排好后叠在一起，并使牌面朝下。然后他对观众说：我不看牌，只要数数就可以猜到每张牌是什么，
我大声数数，你们听，不信你们就看。魔术师将从最上面的一张牌开始数，第一张把它翻过来正好是黑桃A，他将黑桃A放在桌子上，然后按顺序从上到下数手中
的余牌，第二次数1、2，将第一张牌放在这叠牌的下面，将第二张牌翻过来，正好是黑桃2，也将它放在桌子上，第三次数1、2、3，将前面两张依次放在这叠牌的下面，再翻第三张牌正好是黑桃3，这样依次进行，将13张牌全部翻出来，准确无误。问魔术师手中的牌原始次序是怎样安排的？
'''
def guessCard():
    a = [0] * 14 #定义一个数组 14个元素 因为是真实世界，数组的下标从1开始算起
    j = 1         #数组的下标，盒子的序号
    for i in range(1,14): #从1 开始 到13 循环 i 表示牌的序号
        n = 1             #记录当前的空盒子的序号,从1 开始
        while n <=i:
            if j > 13:
                j = 1
            if a[j]:    #当不是空盒子的时候，j到下一个盒子
                 j += 1
            else:
                if n == i: #空盒子的话，把牌放到空盒子中
                    a[j] = i  #这个牌就是数组中j索引对应的
                j += 1
                n += 1
    print(a[1:])
if __name__ == "__main__":
    guessCard()