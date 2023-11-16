# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:40:33 2022

@author: Januario Cipriano
"""

import os
import PyPDF2
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt


def read_pdf():
    files = glob('Files/*.txt')
    tracker = {}
    
    for file in files:
        with open(file) as f:
            line = f.readline()
            while line != '':
                words = line.split()
                for word in words:
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1
                    else:
                        tracker[word] += 1
                line = f.readline()
    
    maxKey = max(tracker, key=tracker.get)
    print(maxKey)

if __name__=='__main__':
    read_pdf()































