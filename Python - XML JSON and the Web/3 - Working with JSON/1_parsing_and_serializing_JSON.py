# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:09:34 2022

@author: Januario Cipriano
"""


import json

# Parsing functions
#   obj = load(file)
#   obj = loads(string)

# Serializaiton functions
#   dump(obj, file)
#   str = dumps(obj)

def main():    
    # # define a string of JSON code
    # jsonStr = '''{
    #     "sandwich" : "Reuben",
    #     "toasted" : true,
    #     "toppings" : [
    #         "Thousand Island Dressing",
    #         "Sauerkraut",
    #         "Pickles"
    #     ],
    #     "price" : 0.99
    # }'''
    
    # TODO: parse the JSON data using loads
    # data = json.loads(jsonStr)
    
    # # TODO: print information from the data structure
    # print('Sandwich: ' + data['sandwich'])
    # if data['toasted']:
    #     print('And it is toasted!')
    # for topping in data['toppings']:
    #     print('Topping: ' + topping)
    
    
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price": 0.99
    }
    
    # TODO: serialize to JSON using dumps
    jsonStr = json.dumps(pythonData, indent=4)
    
    # TODO: print the resulting JSON string
    print("JSON data: -------------")
    print(jsonStr)
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    