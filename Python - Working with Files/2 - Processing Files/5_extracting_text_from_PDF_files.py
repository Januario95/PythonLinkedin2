# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:47:30 2022

@author: A248433
"""

from glob import glob
try:
    import PyPDF2
except Exception as ex:
    import os
    os.system('pip install PyPDF2')
    import PyPDF2


def read_pdf():
    filename = 'Files/Edition Cnn Com 2022 10 13 Opinions Putin Far Right Fans West Europe Ghitis Inde.pdf'
    # filename = 'Files/recipe-book.pdf'
    with open(filename, 'r+b') as f:
        reader = PyPDF2.PdfFileReader(f)
        print(reader.numPages)
        
        #  print(reader.getDocumentInfo())
        # pageObj = reader.getPage(1)
        # print("\n", pageObj.extractText())
        
        for page in range(0, reader.numPages):
            pageObj = reader.getPage(page)
            print("\n", pageObj.extractText())
            
            
def find_most_common_word():
    text_files = glob('Files/*.txt')
    tracker = {}
    print(f'Number of files used: {text_files}')
    
    for txt in text_files:
        with open(txt) as f:
            line = f.readline()
            while line != '':
                words = line.split()
                for word in words:
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1
                    else:
                        tracker[word] += 1
                line = f.readline()
    
    maxKey = max(tracker, key=tracker.get)
    maxValue = max(tracker.values())
    print(f'Most common word: {maxKey}')
    print(f'How many times: {maxValue}')

if __name__=='__main__':
    # read_pdf()
    find_most_common_word()



















