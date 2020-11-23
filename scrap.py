import bs4
import requests
import re
from filter import sep_upper
import json

extract = bs4.BeautifulSoup(requests.get('https://www.verywellfamily.com/the-secret-language-of-teens-100-social-media-acronyms-2609651').content, 'html.parser')
elems = extract.select('strong')

unfiltered=[]
for i in elems:
    unfiltered.append(i.getText())
un_string=" ".join(unfiltered)
un_string=un_string.replace(u'\xa0',u' ')
un_string=un_string.strip()
un_array=un_string.split('-')

""" 
uncomment following to see web scarpping part 
"""
# sep_upper(un_array)

def replace_acro(acro):
    with open("main_final.json", "r") as read_file:
        data = json.load(read_file)
    
    if acro in data:
        return data[acro]
    else:
        return -1


print(replace_acro('gal'))