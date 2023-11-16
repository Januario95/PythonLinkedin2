# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:05:34 2022

@author: Januario Cipriano
"""


import json
import requests
from requests.auth import HTTPBasicAuth
from json import JSONDecodeError


def main():    
    # Use requests to issue a standard HTTP GET request
    url = 'http://localhost:8000/api/collaborators/'
    result = requests.get(url, auth=HTTPBasicAuth('januario95',
                                                  'Jaci1995'))
    
    # TODO: Use the build-in JSON function to return parsed daa
    dataObj = result.json()
    # print(json.dumps(dataObj, indent=4))
    
    # TODO: Access data in the python object
    print(dataObj[0].keys())
    print(dataObj[0]['department'])
    print('There are {0} collaborators'.format(len(dataObj)))

    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    