# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4 as bs
import urllib.request

# source page
#source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
source = urllib.request.urlopen('file:///C:/Users/user.T440_IT/Documents/Python%20Scripts/Dictionary.html').read()
soup = bs.BeautifulSoup(source, 'lxml')

my_dictionary = {
        "words": []}

## title of the page
#print(soup.title)
#
## get attributes:
#print(soup.title.name)
#
## get values:
#print(soup.title.string)
#
## beginning navigation:
#print(soup.title.parent.name)
#
## getting specific values:
#print(soup.p)
#
#print(soup.find_all('p'))

#for paragraph in soup.find_all('p'):
#    #print(paragraph.string)
#    print(str(paragraph.text))

# Another common task is to grab links. For example:
for idx, s in enumerate(soup.find_all('strong')):
    if idx > 1:
        word = s.string
        my_dictionary["words"].append(word)

# Finally, you may just want to grab text.
#print(soup.get_text())