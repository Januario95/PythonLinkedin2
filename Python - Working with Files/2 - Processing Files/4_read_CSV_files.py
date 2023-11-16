# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import csv
import pandas as pd

def display_csv_reader():
    with open('Files/monsters.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row[0])

def display_csv_reader_dict():
    with open('Files/monsters.csv') as f:
        dictReader = csv.DictReader(f, delimiter=',')
        for row in dictReader:
            print(row['monsterName'] + ' is prices at $' + row['price'])


def display_csv_with_pandas():
    df = pd.read_csv('Files/monsters.csv')
    print(df)

if __name__=='__main__':
    # display_csv_reader()
    # display_csv_reader_dict()
    display_csv_with_pandas()



















