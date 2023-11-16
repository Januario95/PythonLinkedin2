# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:11:32 2022

@author: A248433
"""

import urllib.request
import urllib.parse

def main():
    url = 'https://httpbin.org/get'
    
    # TODO: create some data to pass to the GET request
    args = {
        'name': 'Januario Cipriano',
        'is_author': True
    }
    
    # TODO: the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)
    
    # result = urllib.request.urlopen(url + "?" + data)
    
    # print('Result code: {0}'.format(result.status))
    # print('Returned data: ----------------------')
    # print(result.read().decode('utf-8'))
    
    
    # TODO: issue the request with a data parameter to use POST
    url = 'https://httpbin.org/post'
    data = data.encode()
    result = urllib.request.urlopen(url, data=data)
    
    
    print('Result code: {0}'.format(result.status))
    print('Returned data: ----------------------')
    print(result.read().decode('utf-8'))
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    