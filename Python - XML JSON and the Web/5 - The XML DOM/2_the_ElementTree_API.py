# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:05:34 2022

@author: Januario Cipriano
"""

import requests
from lxml import etree
from requests.auth import HTTPBasicAuth


def main():
    # retrieve the XML data using the requests library
    url = 'https://httpbin.org/xml'
    # url = 'http://localhost:8000/xml/collaborators/'
    auth = HTTPBasicAuth('januario95', 'Jaci1995')
    result = requests.get(url) # , auth=auth)
    # print(result.text)

    # TODO: build a doc structure using the ElementTree API
    doc = etree.fromstring(result.content)
    # print(result.content)
    
    # TODO: AAccess the vAlue of an attribute
    print(doc.tag)
    print(doc.attrib['title'])
    
    # TODO: Iterate over tags
    for elem in doc.findall('slide'):
        print(elem.tag)
        
    slideCount = len(doc.findall('slide'))
    print('There are {0} slides'.format(slideCount))
    
    # TODO: Create a new slide
    newSlide = etree.SubElement(doc, 'slide')
    newSlide.text = 'This is a new slide'
    
    # TODO: Count the number of slides
    slideCount = len(doc.findall('slide'))
    itemCount = len(doc.findall('.//item'))
    print('There are {0} slides'.format(slideCount))
    print('There are {0} items'.format(itemCount))
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    