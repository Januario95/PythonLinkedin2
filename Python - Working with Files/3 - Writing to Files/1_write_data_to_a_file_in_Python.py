# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os

def write_content():
    with open('Files/num-series.txt', 'w') as writer:
        writer.write("hello")
        for x in range(50):
            content = f'{x}\n'
            writer.write(content)

def overwrite_content():
    with open('Files/num-series.txt', 'w') as f:
        for x in range(50, 100):
            content = f'{x}\n'
            f.write(content)

def append_content():
    with open('Files/num-series.txt', 'a') as f:
        for x in range(100, 150):
            content = f'{x}\n'
            f.write(content)



if __name__=='__main__':
    # write_content()
    # overwrite_content()
    append_content()
    
    
    
    




