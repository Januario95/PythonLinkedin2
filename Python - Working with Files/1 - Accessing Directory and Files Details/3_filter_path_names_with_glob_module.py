# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

import os
import glob

def display_pngs():
    png_files = glob.glob('*.png')
    print(png_files)
    
def find_monster_one():
    filtered_items = glob.glob('*_os_*')
    print(filtered_items)
    

def find_monster_one_in_subdirs():
    for file in glob.glob('**.py', recursive=True):
        print(file)

if __name__=='__main__':
    # display_pngs()
    # find_monster_one()
    find_monster_one_in_subdirs()


