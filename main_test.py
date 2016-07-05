# -*- coding: utf-8 -*-
"""

"""
import training_test_data
import assessment
import os
# import runpy


def run():
    # generate training file and test file
    s = 'iris'
    source_data_path = r'.\data\%s.txt' % s
    training_file_path = r'.\data\%s_train1.dat' % s
    testing_file_path = r'.\data\%s_test1.dat' % s
    training_test_data.generate_training_testing_data(source_data_path, training_file_path, testing_file_path)
    output_path = r'.\result\wine_output1.csv'

    os.system("python .\sfnn_test.py %s %s %s" % (training_file_path, testing_file_path, output_path))
    accuracy = assessment.accuracy(output_path)
    return accuracy

accuracy_li = list()
for i in range(0, 10):
    accur = run()
    print accur
    accuracy_li.append(accur)

print sum(accuracy_li) / 10
