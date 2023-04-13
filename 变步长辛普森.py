# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:20:47 2023

@author: 86319
"""

import math
import numpy as np
import matplotlib.pyplot as plt
#待求解数值积分sqrt(x) * log(x)
def f1(x):
    if (float(np.fabs(x))<1e-15) :
        return 0
    y=np.sqrt(x) * np.log(x)
    return y
#待求解数值积分sin(x)/x
def f2(x):
    if (float(np.fabs(x)) < 1e-15):
        return 1
    y=np.sin(x)/x
    return y
#梯形公式 f为待求解积分 a为积分下限 b为积分上限
def TX(f,a,b):
    TX = 0.5 * (b - a) * (f(a) + f(b))
    print("梯形公式计算结果为：TX = ", TX)
#辛普森公式 f为待求解积分 a为积分下限 b为积分上限
def XPS(f,a,b):
    XPS = (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6.0
    print("辛普森公式计算结果为：XPS = ", XPS)
#复化梯形公式 f为待求解积分 a为积分下限 b为积分上限 n为区间等分数
def FHTx(f,a,b,n):
    ti=0.0
    h=(b-a)/n
    ti=f(a)+f(b)
    for k in range(1,int(n)):
        xk=a+k*h
        ti = ti + 2 * f(xk)
    FHTx = ti*h/2
    print("复化梯形公式计算结果为：FHTx = ", FHTx)
#复化辛普森公式 f为待求解积分 a为积分下限 b为积分上限 n为区间等分数
def FHXPs(f,a,b,n):
    si=0.0
    h = (b - a) / (2 * n)
    si=f(a)+f(b)
    for k in range(1,int(n)):
        xk = a + k * 2 * h
        si = si + 2 * f(xk)
    for k in range(int(n)):
        xk = a + (k * 2 + 1) * h
        si = si + 4 * f(xk)
    FHXPs = si*h/3
    print("复化辛普森公式计算结果为：FHXPs = ", FHXPs)

def main():
    a = input("a = ")  # 积分下限
    b = input("b = ")  # 积分上限
    a = float(a)  # 强制转换为float类型
    b = float(b)
    n = input("n = ") #将区间分成为n等份
    n = float(n)
    #TX(f2,a,b) #调用梯形公式求解
    #XPS(f2,a,b) #调用辛普森公式求解
    #FHTx(f2,a,b,n) #调用复化梯形公式求解
    FHXPs(f2,a,b,n) #调用复化辛普森公式求解


if __name__ == '__main__':
    main()
