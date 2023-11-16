# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import zipfile

def read_zip():
    with zipfile.ZipFile('directory_archive.zip', 'r') as archive:
        print(archive.namelist())

def retireve_file_info_zip():
    with zipfile.ZipFile('directory_archive.zip', 'r') as archive:
        file_info = archive.getinfo('names.txt')
        print(file_info)

def read_file_in_zip():
    with zipfile.ZipFile('directory_archive.zip', 'r') as archive:
        with archive.open('names.txt') as file:
            print(file.read())


def extract_file(archive, file_to_extract):
    with zipfile.ZipFile(archive, 'r') as my_archive:
        print(my_archive.extract(file_to_extract))

def extract_all():
    with zipfile.ZipFile('directory_archive.zip', 'r') as archive:
        archive.extractall('extracted_files')

if __name__=='__main__':
    # read_zip()
    # retireve_file_info_zip()
    # read_file_in_zip()
    # extract_file('directory_archive.zip', 'names.txt')
    extract_all()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




