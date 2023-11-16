# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import json

def display_json():
    with open('Files/monster.json', 'r') as f:
        data = json.load(f)
    print(data)
    
def display_name_from_json():
    with open('Files/monster.json') as f:
        content_json = json.load(f)
        print("Welcome", content_json['monsterName'])

if __name__=='__main__':
    # display_json()
    display_name_from_json()



















