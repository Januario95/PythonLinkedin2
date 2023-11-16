# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os
import shutil
from pathlib import Path

def delete_file_with_os():
    os.remove('Files/janu-renamed.txt')
    # os.unlink('Files/janu-renamed.txt')

def delete_with_pathlib():
    file = Path('Files/janu-2-renamed.txt')
    file.unlink()
    
def delete_directory_with_os():
    os.rmdir('To-Delete/')
    
def delete_directory_pathlib():
    directory = Path('To-Delete-2/')
    directory.rmdir()
    
def delete_directory_including_subdir():
    shutil.rmtree("New-Files")

if __name__=='__main__':
    # delete_file_with_os()
    # delete_with_pathlib()
    # delete_directory_with_os()
    # delete_directory_pathlib()
    delete_directory_including_subdir()
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




