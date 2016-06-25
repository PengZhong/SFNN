# -*- coding: utf-8 -*-
"""

"""
import training_test_data
import assessment
import os
# import runpy

# generate training file and test file
source_data_path = r'.\data\iris.txt'
training_file_path = r'.\data\training4.dat'
testing_file_path = r'.\data\test4.dat'
training_test_data.generate_training_testing_data(source_data_path, training_file_path, testing_file_path)
output_path = r'.\result\output4.csv'

# runpy.run_path(r'.\sfnn_without_thin.py training_file_path testing_file_path output_path')
os.system("python .\sfnn_without_thin.py %s %s %s" % (training_file_path, testing_file_path, output_path))
print "accuracy:", assessment.accuracy(output_path)
