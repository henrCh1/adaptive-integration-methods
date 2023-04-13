# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:44:34 2023

@author: 86319
"""

import numpy as np

def trapezoidal_rule(f, a, b, n):
    # 计算步长
    h = (b-a)/n
    # 等距离散化区间
    print('N', n)
    print('h', h)
    x = np.linspace(a, b, n+1)
    # 计算函数值
    y = f(x)
    # 利用梯形公式计算积分
    integral = (h/2)*(y[0] + 2*np.sum(y[1:n]) + y[n])
    return integral

def simpsons_rule(f, a, b, n):
    # 计算步长
    h = (b-a)/n
    # 等距离散化区间
    x = np.linspace(a, b, n+1)
    # 计算函数值
    y = f(x)
    # 利用 Simpson 公式计算积分
    integral = h/3 * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[n])
    return integral

def adaptive_integration(f, a, b, eps, method='simpson'):
    # 初始化上一次计算的积分值
    I_old = 0
    # 初始化区间数量
    n = 2
    if method == 'simpson':
        # 利用 Simpson 公式计算初始积分值
        I_new = simpsons_rule(f, a, b, n)
    elif method == 'trapezoidal':
        # 利用梯形公式计算初始积分值
        I_new = trapezoidal_rule(f, a, b, n)
    # 当前积分值与上一次计算的积分值相差较大时，继续进行迭代
    while np.abs((I_new - I_old)/I_new) > eps:
        # 更新上一次计算的积分值
        I_old = I_new
        # 将区间数量加倍
        n *= 2
        if method == 'simpson':
            # 利用 Simpson 公式计算当前积分值
            I_new = simpsons_rule(f, a, b, n)
        elif method == 'trapezoidal':
            # 利用梯形公式计算当前积分值
            I_new = trapezoidal_rule(f, a, b, n)
    return I_new
'''
def adaptive_integration_combined(f, a, b, eps):
    # 分别使用梯形公式和 Simpson 公式计算积分值
    I_trap = adaptive_integration(f, a, b, eps, method='trapezoidal')
    I_simp = adaptive_integration(f, a, b, eps, method='simpson')
    # 计算误差
    err_trap = np.abs((I_trap - I_simp)/I_trap)
    err_simp = np.abs((I_simp - I_trap)/I_simp)
    # 返回误差较小的计算结果
    if err_trap > err_simp:
        return I_simp, 'Simpson rule', err_simp
    else:
        return I_trap, 'Trapezoidal rule', err_trap
'''
# 例如计算函数 sin(x) 在区间 [0, pi] 上的积分
f = lambda r: (4 * np.pi * 10 ** (-7) * 600 * r ** 3) / (2 * (r ** 2 + 1) ** (3 / 2))
a = 0
b = 1
eps = 1e-10

# 调用 trapezoid() 函数，计算 f(r)在 [0, 1] 区间内的积分值
result = adaptive_integration(f, 0, 1, 1e-20)
# 输出积分值
print(result)

# 调用自适应积分函数 adaptive_integration_combined 计算定积分
I, method, error = adaptive_integration_combined(f, a, b, eps)

# 输出积分结果
print(f'The integral of {f.__name__} from {a} to {b} using {method} is {I:.6f}, with error {error:.6e}')

