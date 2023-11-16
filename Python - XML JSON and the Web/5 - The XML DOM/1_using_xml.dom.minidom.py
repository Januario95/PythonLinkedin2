# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:05:34 2022

@author: Januario Cipriano
"""

import requests
import xml.dom.minidom
from requests.auth import HTTPBasicAuth


def main():
    # retrieve the XML data using the requests library
    # url = 'https://httpbin.org/xml'
    url = 'http://localhost:8000/xml/collaborators/'
    auth = HTTPBasicAuth('januario95', 'Jaci1995')
    result = requests.get(url, auth=auth)
    # print(result.text)
    
    # TODO: parse the returned content into a DOM structure
    tree = xml.dom.minidom.parseString(result.text)
    root = tree.documentElement
    
    # TODO: display some information about the content
    print('The root element is {0}'.format(root.nodeName))
    print('Title: {0}'.format(root.getAttribute('title')))
    
    # manipulate the XML content in memory
    # TODO: create a new item tag
    # usernames = tree.getElementsByTagName('username')
    # first_names = tree.getElementsByTagName('first_name')
    # print('There are {0} usernames'.format(usernames.length))
    # print('There are {0} first_names'.format(first_names.length))
    
    # for username in usernames:
    #     print(username.toprettyxml())
    
    # TODO: add some text to the item
    newItem = tree.createElement('author')

    # TODO: now add the item to the first slide
    newItem.appendChild(tree.createTextNode('JANUARIO'))
    
    # TODO: Now count the item tags again
    firstSlide = tree.getElementsByTagName('collaborators')[0]
    firstSlide.appendChild(newItem)
    
    print(tree.toprettyxml())

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    