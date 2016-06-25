# -*- coding: utf-8 -*-
"""

"""
import training_test_data
import assessment
import os
# import runpy

# generate training file and test file
source_data_path = r'.\data\wine.txt'
training_file_path = r'.\data\wine_train1.dat'
testing_file_path = r'.\data\wine_test1.dat'
training_test_data.generate_training_testing_data(source_data_path, training_file_path, testing_file_path)
output_path = r'.\result\wine_output1.csv'

# runpy.run_path(r'.\sfnn_without_thin.py training_file_path testing_file_path output_path')
os.system("python .\sfnn_without_thin.py %s %s %s" % (training_file_path, testing_file_path, output_path))
print "accuracy:", assessment.accuracy(output_path)
