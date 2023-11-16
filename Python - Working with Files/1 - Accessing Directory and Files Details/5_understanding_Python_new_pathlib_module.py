# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

from pathlib import Path


def print_directory_contents():
    entries = Path.cwd()
    
    entries = Path('./First')
    # entries = Path.home()
    
    for entry in entries.iterdir():
        # print("Name:", entry.name)
        # print("Parent:", entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())


if __name__=='__main__':
    print_directory_contents()











