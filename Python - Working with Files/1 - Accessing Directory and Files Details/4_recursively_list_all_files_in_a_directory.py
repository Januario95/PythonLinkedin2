# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

import os


def top_down_walk():
    for dirpath, dirnames, files in os.walk('./'):
        print("Diretory:", dirpath)
        print("Includes these directories:")
        for dirname in dirnames:
            print(dirname)
        print("Includes these files:")
        for filename in files:
            print(filename)
        print()
        
def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('./', topdown=False):
        print("Diretory:", dirpath)
        print("Includes these directories:")
        for dirname in dirnames:
            print(dirname)
        print("Includes these files:")
        for filename in files:
            print(filename)
        print()


if __name__=='__main__':
    # top_down_walk()
    bottom_up_walk()











