# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:11:32 2022

@author: A248433
"""

import requests


def main():
    # TODO: Use requests to issue a standard HTTP GET request
    # url = 'https://httpbin.org/xml'
    # result = requests.get(url)
    # printResults(result)
    
    # TODO: Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    # url = 'https://httpbin.org/get'
    # dataValues = {
    #     'key1': 'value1',
    #     'kay2': 'value2'
    # }
    # result = requests.get(url, params=dataValues)
    # printResults(result)
    
    
    # url = 'https://httpbin.org/post'
    # dataValues = {
    #     'key1': 'value1',
    #     'kay2': 'value2'
    # }
    # result = requests.post(url, data=dataValues)
    # printResults(result)
    
    
    url = 'https://httpbin.org/get'
    headers = {
        'User-Agent': 'Januario Cipriano App / 1.0.0',
    }
    result = requests.get(url, headers=headers)
    printResults(result)
    
    # TODO: Pass a custom header to the server
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    