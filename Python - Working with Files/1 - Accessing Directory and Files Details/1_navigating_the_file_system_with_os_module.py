# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

import os

def display_cwd():
    cwd = os.getcwd()
    print("Current Working Directory: " + cwd)
    print()
    
def up_one_directory_level():
    os.chdir("../")

def display_entries_in_directory(directory):
    with os.scandir(directory) as entrires:
        for entry in entrires:
            print(entry.name)

if __name__=='__main__':
    # display_cwd()
    # up_one_directory_level()
    # display_cwd()
    display_entries_in_directory('C:\\Users\\a248433\\Documents\\SB Mozambique\\EDO\\Robotics\\Bots\\Automatizacao do processo de extracao do fluxo')





