# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os
import shutil
from pathlib import Path


def rename_os():
    os.rename('Files/janu.txt', 'Files/janu-renamed.txt')
    
def rename_pathlib():
    file = Path('Files/janu-2.txt')
    file.rename('Files/janu-2-renamed.txt')

def move_files():
    os.mkdir('Files/Sub-Files')
    shutil.move('Files/janu-renamed.txt', 'Files/Sub-Files/janu-renamed.txt')

    os.mkdir('Files/Sub-Files-2')
    shutil.move('Files/janu-2-renamed.txt', 'Files/Sub-Files-2/janu-2-renamed.txt')

if __name__=='__main__':
    # rename_os()
    # rename_pathlib()
    move_files()
    
    
    
    




