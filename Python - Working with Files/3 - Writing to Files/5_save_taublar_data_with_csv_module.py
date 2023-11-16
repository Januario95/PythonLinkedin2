# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import csv
import pandas as pd


def writer_to_csv_list():
    with open('Files/products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Category', 'Name', 'Quantity', 'Price'])
        writer.writerow([41, 'Furnishings', 'Office Chair', 10, 85])
        writer.writerow([20, 'Office Supplies', 'Pens', 30, 10])
        writer.writerow([13, 'Housekeeping', 'Bed Sheet (Double)', 15, 20])


def writer_to_csv_dictionary():
    with open('Files/products-2.csv', 'w', newline='') as file:
        headers = ['id', 'name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        item = {'id':65, 'name':'ladder', 'quantity': 33, 'price':50}
        writer.writerow(item)
        
def append_to_csv_dictionary():
    with open('Files/products.csv', 'a', newline='') as file:
        headers = ['id', 'category', 'name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=headers)
        item = {'id':66, 'category':'clothes', 'name':'stairs', 'quantity': 98, 'price':24.99}
        writer.writerow(item)
        

if __name__=='__main__':
    # writer_to_csv_list()
    # writer_to_csv_dictionary()
    append_to_csv_dictionary()

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




