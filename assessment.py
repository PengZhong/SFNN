# -*- coding: utf-8 -*-
"""
author: Zhong Peng
assessment of classification result
"""
from __future__ import division
import csv


def accuracy(output_file_path):
    """read data from output csv file, the first column represent the true class
    and the second column represent the predicted class"""
    accurate_count = 0
    all_count = 0
    with open(output_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            all_count += 1
            if row[0] == row[1]:
                accurate_count += 1
    return accurate_count / all_count


if __name__ == '__main__':
    print accuracy(r'.\result\output4.csv')
