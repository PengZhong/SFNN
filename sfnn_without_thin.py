# -*- coding: utf-8 -*-
"""
the number of features N
the number of feature vectors Q
the dimension J of the labels
the number K of classes
all Q feature vectors
all Q labels
threee command line parameters: training_data_path, testing_data_path and output label path
"""
from __future__ import division
import distance
import gaussian
import copy
import sys

print sys.argv
if len(sys.argv) == 0:
    training_data_path = "training.txt"
    testing_data_path = "test.txt"
    output_path = "output.csv"
elif len(sys.argv) == 4:
    training_data_path = sys.argv[1]
    testing_data_path = sys.argv[2]
    output_path = sys.argv[3]
else:
    print "parameter numbers error, three parameters are required"

# 训练集处理
training_vector = list()
training_label = list()
f = open(training_data_path, "rb")
for line in f:
    data_li = line.strip().split(',')
    training_vector.append(data_li[:-1])
    training_label.append(data_li[-1])
f.close()

length = len(training_vector)
distance_sum = 0
distance_count = 0
for i in range(0, length - 1):
    for j in range(i + 1, length):
        distance_i_j = distance.manhattan_distance(training_vector[i], training_vector[j])
        # distance_i_j = distance.euclidean_distance(training_vector[i], training_vector[j])
        distance_sum += distance_i_j
        distance_count += 1
avg_distance = distance_sum / distance_count
print "distance_sum:", distance_sum
print "avg_distance:", avg_distance
print "distance_count:", distance_count

sigma = avg_distance / 2
G = length
print "sigma:", sigma
print "G:", G

"""
step 2:
"""
gussian_centers = copy.copy(training_vector)
# delete_index = set()
# for i in range(0, length - 1):
#     for j in range(i + 1, length):
#         # print i, j
#         vector_distance = distance.euclidean_distance(training_vector[i], training_vector[j])
#         if vector_distance < sigma:
#             if training_label[i] == training_label[j]:
#                 G = G - 1
#                 delete_index.add(j)
# for index in delete_index:
#     training_vector[index] = 0
#     training_label[index] = 0
# # remove all 0 values from training_vector and training_label
# print "G:", G

"""
step3
"""
test_vector = list()
test_label = list()
f = open(testing_data_path, "rb")
for line in f:
    data_li = line.strip().split(',')
    test_vector.append(data_li[:-1])
    test_label.append(data_li[-1])
f.close()
print test_vector
print test_label
print len(test_vector)
print len(test_label)
predict_label = list()
counter = 0
for vector in test_vector:
    max_value = 0
    tmp_index = -1
    print "vector:", vector
    for k in range(0, G):
        # print "k:", k
        # print "gussian_centers[k]:", gussian_centers[k]
        # print "sigma:", sigma
        tmp_value = gaussian.gussian_function(vector, gussian_centers[k], sigma)
        # print "tmp_value:", tmp_value
        # print training_label[k]
        if tmp_value > max_value:
            max_value = tmp_value
            tmp_index = k
        # print "****************"
    predict_label.append(training_label[tmp_index])
print test_label
print predict_label

import csv
output = zip(test_label, predict_label)
with open(output_path, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output)
