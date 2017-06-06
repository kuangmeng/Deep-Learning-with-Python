#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:13:18 2017

@author: kuangmeng
"""

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../MNIST_data/",one_hot = True)

print(mnist.train.images.shape,mnist.train.labels.shape)

print(mnist.test.images.shape,mnist.test.labels.shape)

print(mnist.validation.images.shape,mnist.validation.labels.shape)

