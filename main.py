# -*- coding: utf-8 -*-
"""

"""
import training_test_data
import os
# import runpy

# generate training file and test file
source_data_path = r'.\data\iris.txt'
training_file_path = r'.\data\training3.dat'
testing_file_path = r'.\data\test3.dat'
training_test_data.generate_training_testing_data(source_data_path, training_file_path, testing_file_path)
output_path = r'.\result\output3.csv'

# runpy.run_path(r'.\sfnn_without_thin.py training_file_path testing_file_path output_path')
os.system("python .\sfnn_without_thin.py %s %s %s" % (training_file_path, testing_file_path, output_path))
