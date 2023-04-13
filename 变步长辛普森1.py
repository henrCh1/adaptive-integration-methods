# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:51:17 2023

@author: 86319
"""

import numpy as np
import math

# 定义一个函数，用于求给定函数在指定区间内各点的值的总和
def summation(f, range):
   r = 0
   for i in range:
      r += f(i)
   return r

# 定义辛普森积分函数，f为函数，h为区间宽度，2n为区间个数，min为积分下限，max为积分上限
def simpson(f, h, min, max):
   # 计算n值
   n = math.floor((max - min) / (h * 2))
   print('N', 2*n)
   print('h', h)
    
   # 定义 lambda 函数 g(i)，用于计算每个区间边界的函数值
   g = lambda i: f(min + i * h)

   # 计算 a、b、c、d 值
   a = g(0)
   b = summation(lambda i: g(2 * i - 1), range(1, n+1))
   c = summation(lambda i: g(2 * i), range(1, n))
   d = g(2 * n)

   # 返回辛普森积分结果
   return (h / 3) * (a + (4 * b) + (2 * c) + d)

def adaptive_integration(f, min, max, eps):
    # 初始化上一次计算的积分值
    I_old = 0
    # 初始化区间数量
    h = 0.1
        # 利用 Simpson 公式计算初始积分值
    I_new = simpson(f, h, min, max)
    # 当前积分值与上一次计算的积分值相差较大时，继续进行迭代
    while np.abs(I_new - I_old) > eps:
        # 更新上一次计算的积分值
        I_old = I_new
        # 将区间数量加倍
        h /= 2
    # 利用梯形公式计算当前积分值
        I_new = simpson(f, h, min, max)
        error = np.abs(I_new - I_old)
    # 输出积分值和误差值
    return I_new,error

# 定义函数 f(r)
f = lambda x: (math.sqrt(400*((math.sin(x))**2)+100*((math.cos(x))**2)))

result,error = adaptive_integration(f, 0, 2*math.pi , 1e-8)
# 输出积分值
print('积分结果为：',result)
print('误差值为：',error)
