# -*- coding: utf-8 -*-
"""高斯型隶属函数的实现, 输入值分别为
x: 未知向量
gussian_center: 当前的高斯中心
sigma: 决定MF宽度
"""
from __future__ import division
import math


def gussian_function(x, gussian_center, sigma):
    feature_tuple = zip(x, gussian_center)
    fenzi = sum([(elem[0] - elem[1]) ** 2 for elem in feature_tuple])
    fenmu = 2 * sigma * sigma
    return math.e ** (-fenzi / fenmu)


if __name__ == '__main__':
    x = [6.3, 2.9, 5.6, 1.8]
    gussian_center = [6.5, 3.0, 5.8, 2.2]
    sigma = 1
    print gussian_function(x, gussian_center, sigma)