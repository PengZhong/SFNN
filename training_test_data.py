# -*- coding: utf-8 -*-
"""
根据原始数据集生成测试集和训练集
"""
import random
import os


def generate_training_testing_data(source_file_path, training_file_path, testing_file_path):
    """generate training data file and testing data file from source data, 80% and 20%
    of source data respectively"""
    # save all data in list
    all_line = list()
    f = open(source_file_path, "rb")
    for line in f:
        all_line.append(line)
    f.close()

    # generate training and testing list of index
    all_line_num = len(all_line)
    training_num = int(round(all_line_num * 0.8))
    testing_num = all_line_num - training_num
    training_index = random.sample(range(0, all_line_num), training_num)
    training_index.sort()
    testing_index = list(set(range(0, all_line_num)) - set(training_index))
    testing_index.sort()

    # save training data into file
    f = open(training_file_path, "wb")
    for index in training_index:
        f.write(all_line[index])
    f.close()

    # save testing data into file
    f = open(testing_file_path, "wb")
    for index in testing_index:
        f.write(all_line[index])
    f.close()


if __name__ == '__main__':
    generate_training_testing_data("iris.txt", "1.dat", "2.dat")
