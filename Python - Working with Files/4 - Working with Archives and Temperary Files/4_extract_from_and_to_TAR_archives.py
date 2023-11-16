# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import tarfile
from glob import glob


def create_tar_archive():
    files = glob('*.svg')
    with tarfile.open('archive.tar', 'w') as tar:
        for file in files:
            # overwrite any existing file in .tar
            tar.add(file)

def add_to_tar_archive():
    with tarfile.open('archive.tar', 'a') as tar:
        tar.add('Cadeia de valor.png')

def extract_tar():
    with tarfile.open('archive.tar') as tar:
        tar.extract('Cadeia de valor.png')

def extract_all():
    with tarfile.open('archive.tar') as tar:
        tar.extractall('extracted_archive')

if __name__=='__main__':
    # create_tar_archive()
    # add_to_tar_archive()
    # extract_tar()
    extract_all()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




