# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:41:30 2022

@author: Januario Cipriano
"""

import os
from pathlib import Path


def count_files_with_scandir(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += 1
        else:
            total += count_files_with_scandir(entry)
    return total

def count_files_with_pathlib(path):
    total = 0
    for entry in Path(path).iterdir():
        if entry.is_file():
            total += 1
        else:
            total += count_files_with_pathlib(entry)
    return total
            
            
if __name__=='__main__':
    print(count_files_with_scandir('./'))
    print(count_files_with_pathlib('./'))






















