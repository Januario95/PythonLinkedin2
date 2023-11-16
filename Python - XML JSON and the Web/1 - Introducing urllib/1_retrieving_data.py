# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:53:32 2022

@author: A248433
"""

import urllib.request

def main():
    url = 'https://httpbin.org/xml'
    
    # TODO: open the URL and retrieve some data
    result = urllib.request.urlopen(url)
    
    # TODO: Print the reuslt code from the request, should be 200
    print("Result code: {0}".format(result.status))
    
    # TODO: Print the returned data headers
    print("Headers:-------------------")
    print(result.getheaders())
    
    # TODO: Print the returned data
    print(result.read().decode('utf-8'))
    
    
if __name__=='__main__':
    main()