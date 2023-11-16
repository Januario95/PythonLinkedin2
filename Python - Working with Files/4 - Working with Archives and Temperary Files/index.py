# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:00:06 2022

@author: Januario Cipriano
"""


import shutil
import zipfile
from glob import glob

def create_zip(files):
    with zipfile.ZipFile('archiveTemp.zip', 'w') as arch:
        for file in files:
            arch.write(file)
            
    
if __name__=='__main__':
    files = glob('images/*.png')
    create_zip(files)