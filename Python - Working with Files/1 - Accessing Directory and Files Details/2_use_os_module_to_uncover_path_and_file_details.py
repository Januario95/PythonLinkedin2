# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:16 2022

@author: Januario Cipriano
"""

import os
import math
from datetime import datetime

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime('%d %b %Y %H:%M:%S')
    return formatted_date

def convert_size(size_bytes):
    if size_bytes == 0:
        return 'OB'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '%s %s' % (s, size_name[i])

def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print('File Name: ', entry.name)
            info = entry.stat()
            # print(info.st_uid)
            # print(info.st_file_attributes)
            # print(info.st_gid)
            print("Creation Time: ", format_datetime(info.st_ctime))
            print("Last Access Time:", format_datetime(info.st_atime))
            print('Size:', convert_size(info.st_size))
            print()
            

def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory Name:", entry.name)

def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File Name:", entry.name)
    
if __name__=='__main__':
    display_entries_in_directory("./")
    # display_directories("./")
    # display_files("./")


















