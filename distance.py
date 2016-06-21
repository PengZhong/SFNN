# -*- coding: utf-8 -*-
"""
曼哈顿距离以及欧氏距离实现
manhattan_distance and euclidean_distance
输入为两个列表，要求列表长度相同
"""
import math

def manhattan_distance(li1, li2):
    """calculate manhattan distance between two vector"""
    if (len(li1) != len(li2)):
        print "the length of two args is not equal, return -1"
        return -1
    else:
        t = zip(li1, li2)
        distance_li = [abs(float(elem[0]) - float(elem[1])) for elem in t]
        return sum(distance_li)


def euclidean_distance(li1, li2):
    "calculate euclidean distance between two vector"
    if (len(li1) != len(li2)):
        print "the length of two args is not equal, return -1"
        return -1
    else:
        t = zip(li1, li2)
        distance_li = [abs(float(elem[0]) - float(elem[1])) for elem in t]
        distance = math.sqrt(sum(map(lambda x: x * x, distance_li)))
        return distance


if __name__ == '__main__':
    li1 = [3.5, 2, 5, 1.5, 2]
    li2 = [2, 3.5, 2, 3.5, 3]
    print euclidean_distance(li1, li2)
