# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

import os
from pathlib import Path

def make_logs_dir():
    try:
        os.mkdir('logs/')
    except FileExistsError as ex:
        print(ex)
        print("Logs direcory already exists")

def make_output_dir():
    dir_path = Path('output/')
    dir_path.mkdir(exist_ok=True)


def count_files_with_os_walk(path):
    total = 0
    for base, subdirs, files in os.walk(path):
        for file in files:
            total += 1
    return total

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
    # make_logs_dir()
    # make_output_dir()
    print(count_files_with_os_walk('./'))
    print(count_files_with_scandir('./'))
    print(count_files_with_pathlib('./'))











