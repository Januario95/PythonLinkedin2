# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import json
from pathlib import Path
from datetime import datetime


def generate_creation_date(path):
    stat_result = path.stat()
    creation_date = stat_result.st_ctime
    utc_timestap = datetime.utcfromtimestamp(creation_date)
    return utc_timestap.strftime('%Y_%m_%d_')

def organize_images(image_folder):
    file_types = ['.png', '.svg']
    for path in Path(image_folder).iterdir():
        if path.is_file() and path.suffix in file_types:
            print(f'Renaming file {path.stem!r}')
            date = generate_creation_date(path)
            new_path = Path(image_folder + date + path.stem + 
                            path.suffix)
            path.rename(new_path)
            

if __name__=='__main__':
    organize_images('./images')
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




