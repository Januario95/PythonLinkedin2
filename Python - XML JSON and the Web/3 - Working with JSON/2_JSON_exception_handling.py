# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:05:34 2022

@author: Januario Cipriano
"""


import json
from json import JSONDecodeError


def main():    
    # define a string of JSON code
    jsonStr = '''{
        "sandwich" : "Reuben",
        "toasted" : true,
        "toppings : [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price" : 0.99
    }'''
    
    #  TODO: parse the JSON data using loads
    try:
        data = json.loads(jsonStr)
    except JSONDecodeError as err:
        print("Whoops, JSON decoding error:")
        print(err.msg)
        print(err.lineno, err.colno)
    
    # TODO: print information from the data structure
    print('Sandwich: ' + data['sandwich'])
    if data['toasted']:
        print('And it is toasted!')
    for topping in data['toppings']:
        print('Topping: ' + topping)
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    