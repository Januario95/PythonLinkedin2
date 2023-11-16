# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:06:19 2022

@author: Januario Cipriano
"""

import os
import json
from glob import glob
from pathlib import Path
from datetime import datetime


def generate_creation_date(path):
    stat_result = path.stat()
    creation_date = stat_result.st_ctime
    utc = datetime.utcfromtimestamp(creation_date)
    return utc.strftime('%Y_%m_%d')

def organize_images(img_folder):
    file_types = ['.png', '.svg']
    for path in Path(img_folder).iterdir():
        if path.is_file() and path.suffix in file_types:
            print(f'Renaming file {path.stem!r}')
            date = generate_creation_date(path)
            new_path = Path(path.stem + '-' + date + path.suffix)
            path.rename(new_path)

if __name__=='__main__':
    organize_images('.')

    










































