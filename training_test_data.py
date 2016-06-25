# -*- coding: utf-8 -*-
"""
根据原始数据集生成测试集和训练集
根据数据条目总数按照80%, 20%的比例划分训练集和测试集
训练集和测试集中每个类别的数量与该类占数据总数的百分比相同
"""
import random
import os
from collections import OrderedDict


def generate_training_testing_data(source_file_path, training_file_path, testing_file_path):
    """generate training data file and testing data file from source data, 80% and 20%
    of source data respectively"""
    # save all data in list
    all_line = list()
    all_str_line = list()
    class_list = list()
    f = open(source_file_path, "rb")
    for line in f:
        all_str_line.append(line)
        line = line.strip().split(',')
        all_line.append(line)
        class_list.append(line[-1])
    f.close()

    # generate training and testing list of index
    all_line_num = len(all_line)
    training_num = int(round(all_line_num * 0.8))
    testing_num = all_line_num - training_num

    training_index = list()
    class_count = len(set(class_list))
    class_index = 0
    for i in range(0, class_count):
        class_num = class_list.count(class_list[class_index])
        training_index.extend(random.sample(range(class_index, class_index + class_num), class_num * training_num / all_line_num))
        class_index = class_index + class_num

    training_index.sort()
    testing_index = list(set(range(0, all_line_num)) - set(training_index))
    testing_index.sort()

    print training_index
    print testing_index

    # save training data into file
    f = open(training_file_path, "wb")
    for index in training_index:
        f.write(all_str_line[index])
    f.close()

    # save testing data into file
    f = open(testing_file_path, "wb")
    for index in testing_index:
        f.write(all_str_line[index])
    f.close()


if __name__ == '__main__':
    generate_training_testing_data("iris.txt", "1.dat", "2.dat")
