# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:54:21 2023

@author: 86319
"""

# 导入 math 模块
import math
import numpy as np

# 定义梯形法函数，
def trapezoid(f, n, min, max):
    h = (max - min) / n
    S = 0
    for i in range(1, n):
        S += f(min + i * h) * h
        S1 = S + 0.5 * h * (f(min) + f(max))
    return S1

# 定义一个函数，用于求给定函数在指定区间内各点的值的总和
def summation(f, n, min, max):
   h = (max - min) / n
   r = 0
   for i in range(0, n):
      r += f(min + (i + 1/2) * h)
   return r

def adaptive_integration(f, min, max, eps):
    # 初始化上一次计算的积分值
    I_old = 0
    # 初始化区间数量
    n = 2

        # 利用 Simpson 公式计算初始积分值
    I_new = trapezoid(f, n, min, max)
    # 当前积分值与上一次计算的积分值相差较大时，继续进行迭代
    while np.abs(I_new - I_old) > eps:
        # 更新上一次计算的积分值
        I_old = I_new
        # 将区间数量加倍
        n *= 2
    # 利用梯形公式计算当前积分值
        h = (max - min) / n
        I_new = (1/2) * I_old + (h/2) * summation(f, n, min, max)
        error = np.abs(I_new - I_old)
        print(n)
    # 输出积分值和误差值
    return I_new,error


# 定义函数 f(r)
f = lambda r: (4 * math.pi * 10 ** (-7) * 600 * r ** 3) / (2 * (r ** 2 + 1) ** (3 / 2))

result, error = adaptive_integration(f, 0, 1, 1e-10)
# 输出积分值
print('积分结果为：',result)
print('误差值为：',error)
