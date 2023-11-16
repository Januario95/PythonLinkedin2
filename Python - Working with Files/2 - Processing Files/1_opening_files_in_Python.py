# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import os

original_text = '''Yodel grew up in a family of singers and 
loud talkers and could never get a word in edgewise
'''
new_text = '''Russian President Vladimir Putin’s so-far-disastrous invasion of Ukraine is
turning the former idol of the far right into a toxic figure among many who used to be
his greatest admirers.
'''

def print_content():
    # f = open('Files/description-01.txt', 'r')
    # content = f.read()
    # print(content)
    # f.close()
    
    with open('Files/description-01.txt', 'r') as f:
        content = f.read()
        print(content)
    
def writer_new_content():
        # f = open('Files/description-01.txt', 'w')
        # f.write(new_text)
        # f.close()
        
        with open('Files/description-01.txt', 'w') as f:
            f.write(new_text)

if __name__=='__main__':
    print_content()
    writer_new_content()
    print_content()




