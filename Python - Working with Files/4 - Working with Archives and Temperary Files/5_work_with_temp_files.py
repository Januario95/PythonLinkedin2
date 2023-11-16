# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import tempfile

def work_with_temporaty_file():
    with tempfile.TemporaryFile('w+') as temp:
        temp.write('Order Id 93827, Account Id 286438173')
        temp.seek(0)
        print(temp.read())
        print(tempfile.gettempdir())



if __name__=='__main__':
    work_with_temporaty_file()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




