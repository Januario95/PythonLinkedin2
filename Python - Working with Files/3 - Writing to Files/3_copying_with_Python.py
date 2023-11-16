# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os
import shutil
from pathlib import Path


def copy_file():
    shutil.copy('Files/Sub-Files/janu-renamed.txt',
                'Files/')
    
def copy_file_with_metadata():
    shutil.copy2('Files/Sub-Files-2/janu-2-renamed.txt',
                 'Files')
    
def copy_directory():
    shutil.copytree('Files/', 'New-Files/')

if __name__=='__main__':
    # copy_file()
    # copy_file_with_metadata()
    copy_directory()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




