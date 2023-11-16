# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:11:32 2022

@author: A248433
"""

import requests
from requests import HTTPError, Timeout


def main():    
    # url = 'https://httpbin.org/status/404'
    url = 'https://httpbin.org/delay/5'
    try:
        result = requests.get(url, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request timed out: {0}".format(err))
    
    
def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")
    
    print("Headers: ----------------------")
    print(resData.headers)
    print("\n")
    
    print("Returned data: ---------------------")
    # print(resData.content)
    print(resData.text)
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    