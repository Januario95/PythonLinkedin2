# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import shutil
import zipfile
from glob import glob


def create_zip(files):
    with zipfile.ZipFile('archive.zip', 'w') as archive:
        for file in files:
            archive.write(file)

def update_zip(files):
    with zipfile.ZipFile('archive.zip', 'a') as archive:
        for file in files:
            archive.write(file)


def create_zip_nested_dir(directory_path):
    shutil.make_archive('directory_archive', 'zip', directory_path)


if __name__=='__main__':
    # files = glob('images/*.png')
    files = glob('images/*.txt')
    # create_zip(files)
    # update_zip(files)
    create_zip_nested_dir('svg')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




