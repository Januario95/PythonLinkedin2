# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os



def print_content():
    with open('Files/description-01.txt', 'r') as f:
        print(f.read(17))    

def print_file_content_readlines():
    with open('Files/description-01.txt', 'r') as f:
        lines = f.readlines()
        print(lines[0])
        print(lines[1])

def print_file_content_one_line_at_time():
    with open('Files/description-01.txt', 'r') as f:
        line = f.readline()
        while line != '':
            print(line, end='')
            line = f.readline()

if __name__=='__main__':
    # print_content()
    # print_file_content_readlines()
    print_file_content_one_line_at_time()



















