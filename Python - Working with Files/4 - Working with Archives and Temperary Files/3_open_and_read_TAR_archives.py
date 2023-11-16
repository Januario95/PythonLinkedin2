# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

import tarfile


def read_tarfile():
    with tarfile.open('phayes-geoPHP-1.2-20-g6855624.tar.gz', 'r:gz') as tar:
        # Compression modes: r:gz, r:bz2, r:xz
        # print(tar.getnames())
        # file = tar.getmember('phayes-geoPHP-6855624/.travis.yml')
        # print(file.name)
        # print(file.size)
        # print(file.mode)
        for member in tar.getmembers():
            print(member.name)
            print(member.size)
            print(member.mode)
            print('')

def read_file_in_tar():
    with tarfile.open('phayes-geoPHP-1.2-20-g6855624.tar.gz', 'r:gz') as tar:
        with tar.extractfile('phayes-geoPHP-6855624/tests/input/simple_point.json') as file:
            print(file.read())


if __name__=='__main__':
    # read_tarfile()
    read_file_in_tar()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




