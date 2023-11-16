# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:11:32 2022

@author: A248433
"""

import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError


def main():
    url = 'https://no-such-server.org'
    # url = 'https://httpbin.org/status/404'
    # url = 'https://httpbin.org/html'
    
    # TODO: use exception handling to attempt the URL access
    try:
        result = urllib.request.urlopen(url)
        print('Result code: {0}'.format(result.status))
        if result.getcode() == HTTPStatus.OK:
            print(result.read().decode('utf-8'))
    except HTTPError as err:
        print('Error: {0}'.format(err.code))
    except URLError as err:
        print('Yeah that server is bunk. {0}'.format(err.reason))
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    