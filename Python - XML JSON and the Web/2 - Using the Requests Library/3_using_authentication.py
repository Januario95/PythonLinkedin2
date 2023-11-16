# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:11:32 2022

@author: A248433
"""

import requests
from requests.auth import HTTPBasicAuth


def main():    
    # Access a URL that requires authentication - the format of htis
    # URL is that you provide the usernane/password to the auth
    # against
    url = 'https://httpbin.org/basic-auth/januario95/cipriano'
    
    # TODO: Create a credentials object using HTTPBasicAuth
    myCreds = HTTPBasicAuth('januario95', 'cipriano')
    
    # TODO: Issue the request with the authentication credentials
    result = requests.get(url, auth=myCreds)
    
    printResults(result)
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    