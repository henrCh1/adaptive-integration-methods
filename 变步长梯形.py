# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:30:44 2023

@author: 86319
"""
import numpy as np

def trapezoid(f, n, min, max):
    h = (max - min) / n
    print('N', n)
    print('h', h)
    S = 0
    for i in range(1, n):
        S += f(min + i * h) * h
    return S + 0.5 * h * (f(min) + f(max))

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
        I_new = trapezoid(f, n, min, max)
        error = np.abs(I_new - I_old)
    # 输出积分值和误差值
    return I_new,error

# 定义函数 f(r)
f = lambda r: (4 * np.pi * 10 ** (-7) * 600 * r ** 3) / (2 * (r ** 2 + 1) ** (3 / 2))

# 调用 trapezoid() 函数，计算 f(r)在 [0, 1] 区间内的积分值
result, error = adaptive_integration(f, 0, 1, 1e-17)
# 输出积分值
print('积分结果为：',result)
print('误差值为：',error)
